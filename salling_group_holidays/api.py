import requests
import datetime
import json


class SallingGroupHolidaysException(BaseException):
    pass


class v1:
    def __init__(self, api_key):
        self._api_key = api_key
        self._url = 'https://api.dansksupermarked.dk/v1/holidays'

    def is_holiday(self, date):
        if not isinstance(date, datetime.date):
            raise SallingGroupHolidaysException("date must be a datetime.date instance")

        headers = {'Authorization': 'Bearer {}'.format(self._api_key)}
        response = requests.get('{}/is-holiday'.format(self._url),
                                headers=headers,
                                params={'date': date.isoformat()})

        if response.status_code != 200:
            if 'error' in response.json():
                raise SallingGroupHolidaysException(response.json()['error'])
            else:
                raise SallingGroupHolidaysException(response.text)

        reply = response.json()

        # The API returns the boolean value as a string for some reason
        if not isinstance(reply, str):
            raise SallingGroupHolidaysException('Unexpected reply: {}'.format(response.text))

        # Convert the string to a boolean value
        bool_reply = json.loads(reply)
        if not isinstance(bool_reply, bool):
            raise SallingGroupHolidaysException('Unexpected reply: {}'.format(response.text))
        return bool_reply
