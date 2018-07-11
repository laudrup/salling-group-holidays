import requests
import datetime
import json


class SallingGroupHolidaysException(BaseException):
    pass


class v1:
    def __init__(self, api_key):
        self._api_key = api_key
        self._url = 'https://api.dansksupermarked.dk/v1/holidays'

    def _make_request(self, params, path='/'):
        headers = {'Authorization': 'Bearer {}'.format(self._api_key)}
        response = requests.get('{}{}'.format(self._url, path),
                                headers=headers,
                                params=params)

        if 'error' in response.json():
            raise SallingGroupHolidaysException(response.json()['error'])

        return response

    def is_holiday(self, date):
        if not isinstance(date, datetime.date):
            raise SallingGroupHolidaysException("date must be a datetime.date instance")

        response = self._make_request({'date': date.isoformat()}, path='/is-holiday')

        # The API returns the boolean value as a string for some reason
        if not isinstance(response.json(), str):
            raise SallingGroupHolidaysException('Unexpected reply: {}'.format(response.text))

        # Convert the string to a boolean value
        bool_reply = json.loads(response.json())
        if not isinstance(bool_reply, bool):
            raise SallingGroupHolidaysException('Unexpected reply: {}'.format(response.text))
        return bool_reply

    def holidays(self, start_date, end_date):
        if not isinstance(start_date, datetime.date):
            raise SallingGroupHolidaysException("start_date must be a datetime.date instance")
        if not isinstance(end_date, datetime.date):
            raise SallingGroupHolidaysException("end_date must be a datetime.date instance")

        response = self._make_request({'startDate': start_date.isoformat(),
                                       'endDate': end_date.isoformat()})
        result = {datetime.datetime.strptime(val['date'], '%Y-%m-%d').date():
                  {'name': val['name'],
                   'holiday': val['nationalHoliday']}
                  for val in response.json()}
        return result
