from driver import *

def test_time_driven():
    assert calculate_time('7:15','7:45') == 30
    assert calculate_time('12:01','13:16') == 75

def test_calculate_mph():
    assert calculate_mph(42.0,1.25)


