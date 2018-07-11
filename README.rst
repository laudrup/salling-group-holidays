.. image:: https://travis-ci.org/laudrup/salling-group-holidays.svg?master
   :target: https://travis-ci.org/laudrup/salling-group-holidays
   :alt: Linux Build Status

Unofficial library for the Salling Group Holidays API
=====================================================

Unofficial Python 3 library for the `Salling Group Holidays API <https://developer.dansksupermarked.dk/v1/api/services/holidays/>`_.

The API supports fetching Danish holidays for a given date or range of
dates. This library simply provides an abstraction over that API.

.. note::
   This library is in no way supported by Salling Group A/S nor is the author in any way affiliated with Salling Groups A/S.

Installation
------------

To install this library, type the following into the command prompt:

::

   $ pip install salling-group-holidays

Usage
-----

First of all, an API key is needed to use the Salling Group Holidays
API. `Contact Salling Group to receive your API key
<https://developer.dansksupermarked.dk/v1/api/reference/overview/getting-your-api-key/>`_.

Once you have received your key, you can start using this library. Usage is fairly simple. Start by getting an API instance:

.. code-block:: python

    import salling_group_holidays

    API_KEY = 'your_api_key'
    v1 = salling_group_holidays.v1(API_KEY)

To see if a given date is a holiday, use a Python `datetime.date
object <https://docs.python.org/3/library/datetime.html#date-objects>`_. and
call the *is_holiday* method. For example, to see if today is a Danish
holiday:

.. code-block:: python

    from datetime import date
    import salling_group_holidays

    v1 = salling_group_holidays.v1(API_KEY)

    if v1.is_holiday(date.today()):
      print('Great news. No work today!')
    else:
      print('Get back to work. No holiday today.')

To get a list of holidays for a given period, call the *holidays*
method with a start and end date as a Python `datetime.date
object <https://docs.python.org/3/library/datetime.html#date-objects>`_. This
method returns a Python dictionary with the holiday dates as the key
and the name of the day as well as whether it is a holiday. For
example to get the list of Danish holidays in December 2018:

.. code-block:: python

    from datetime import date
    import salling_group_holidays

    v1 = salling_group_holidays.v1(API_KEY)
    holidays = v1.holidays(date(2018, 12, 1), date(2018, 12, 31))

    print('There are {} holidays in December 2018.'.format(len(holidays)))
    print('December 25th is {}'.format(holidays[date(2018, 12, 25)]['name']))

Will output:

::

   There are 4 holidays in December 2018
   December 25th is 1. juledag.
