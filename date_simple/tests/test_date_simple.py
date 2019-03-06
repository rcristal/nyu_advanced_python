"""
    test_date_simple.py - Test cases for date_simple wrapper module.

    Author: Rexford Cristal, rexford.cristal@gmail.com
    Last Modified: 03/06/2019
"""

import pytest
import date_simple as ds
import datetime

def test_get_date_object_no_argument():
    """ get_date_object() with no argument should return date object for today """

    assert ds.get_date_object() == datetime.date.today()

def test_get_date_object_string_date():
    """ get_date_object() with properly formatted date string should return date object for that date """

    assert ds.get_date_object(date='2018-02-26') == datetime.datetime.strptime('2018-02-26', '%Y-%m-%d').date()

def test_get_date_string_no_argument():
    """ get_date_string() with no argument should return date string for today """

    assert ds.get_date_string() == datetime.date.today().strftime('%Y-%m-%d')

def test_get_date_string_date_object():
    """ get_date_string() with date object should return date string for that date """

    test_date_object = datetime.date(2018, 2, 26)
    assert ds.get_date_string(date_object=test_date_object) == '2018-02-26'

def test_get_date_object_value_error():
    """ get_date_object() with improperly formatted string should raise ValueError exception """

    with pytest.raises(ValueError):
        dateobj2 = ds.get_date_object(date='bad date')

def test_get_date_object_type_error():
    """ get_date_object() with object that is not type str should raise TypeError exception """

    not_a_string = datetime.date(2018, 2, 26)
    with pytest.raises(TypeError):
        date_object = ds.get_date_object(date=not_a_string)

def test_get_date_string_type_error():
    """ get_date_string() with object that is not type datetime.date should raise TypeError exception """

    not_a_date_object = '2018-02-26'
    with pytest.raises(TypeError):
        datestr = ds.get_date_string(date_object=not_a_date_object)

def test_get_date_string_format_value_error():
    """ get_date_string() with unrecognized date format should raise ValueError exception """

    dateobj2 = ds.get_date_object(date='2018-02-26')
    with pytest.raises(ValueError):
        datestr = ds.get_date_string(date_object=dateobj2, format='unrecognized format')

def test_get_date_string_format_one():
    """ get_date_string() with format='MM/DD/YYYY' should return date string with that format """

    test_date_object = datetime.date(2018, 2, 26)
    assert ds.get_date_string(date_object=test_date_object, format='MM/DD/YYYY') == '02/26/2018'

def test_get_date_string_format_two():
    """ get_date_string() with format='DD-Mon-YY' should return date string with that format """

    test_date_object = datetime.date(2018, 2, 26)
    assert ds.get_date_string(date_object=test_date_object, format='DD-Mon-YY') == '26-Feb-18'
