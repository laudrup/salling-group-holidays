import unittest
from datetime import date, datetime
from json import dumps as json_dumps
from unittest import mock

import salling_group_holidays
from salling_group_holidays import SallingGroupHolidaysException

DECEMBER_HOLIDAYS = [
    {
        'date': '2018-12-24',
        'name': 'Juleaftensdag',
        'nationalHoliday': True
    },
    {
        'date': '2018-12-25',
        'name': '1. juledag',
        'nationalHoliday': True
    },
    {
        'date': '2018-12-26',
        'name': '2. juledag',
        'nationalHoliday': True
    },
    {
        'date': '2018-12-31',
        'name': 'Nytårsaftensdag',
        'nationalHoliday': True
    }
]


def mocked_requests_get(url, headers=None, params=None):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self._json_data = json_data
            self.status_code = status_code

        @property
        def text(self):
            return json_dumps(self._json_data)

        def json(self):
            return self._json_data

    auth = headers['Authorization']
    key = auth.split()[1]
    if key != 'valid_key':
        return MockResponse({'error': 'Invalid auth'}, 403)

    if url.endswith('is-holiday'):
        day = datetime.strptime(params['date'], '%Y-%m-%d').date().day
        if day == 24:
            return MockResponse('true', 200)
        return MockResponse('false', 200)

    return MockResponse(DECEMBER_HOLIDAYS, 200)


class TestHolidays(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_key(self, mock_class):
        v1 = salling_group_holidays.v1('invalid_key')

        self.assertRaises(SallingGroupHolidaysException, v1.is_holiday, date(2018, 12, 24))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_is_holiday(self, mock_class):
        v1 = salling_group_holidays.v1('valid_key')

        self.assertFalse(v1.is_holiday(date(2018, 12, 23)))
        self.assertTrue(v1.is_holiday(date(2018, 12, 24)))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_holidays(self, mock_class):
        v1 = salling_group_holidays.v1('valid_key')
        result = v1.holidays(date(2018, 12, 1), date(2018, 12, 31))
        days = [datetime.strptime(val['date'], '%Y-%m-%d').date() for val in DECEMBER_HOLIDAYS]

        self.assertEquals(len(result), 4)
        for day in days:
            self.assertTrue(day in result)
        self.assertEquals(result[date(2018, 12, 24)]['name'], 'Juleaftensdag')
        self.assertTrue(result[date(2018, 12, 24)]['holiday'])
        self.assertEquals(result[date(2018, 12, 25)]['name'], '1. juledag')
        self.assertTrue(result[date(2018, 12, 25)]['holiday'])
        self.assertEquals(result[date(2018, 12, 26)]['name'], '2. juledag')
        self.assertTrue(result[date(2018, 12, 26)]['holiday'])
        self.assertEquals(result[date(2018, 12, 31)]['name'], 'Nytårsaftensdag')
        self.assertTrue(result[date(2018, 12, 31)]['holiday'])
