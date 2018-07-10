import unittest
from datetime import date, datetime
from json import dumps as json_dumps
from unittest import mock

import salling_group_holidays
from salling_group_holidays import SallingGroupHolidaysException


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

    return MockResponse(None, 404)


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
