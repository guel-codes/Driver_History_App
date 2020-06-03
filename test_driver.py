from driver import *

def test_time_driven():
    start_time = '7:15'
    end_time = '7:45'
    assert calculate_time(start_time,end_time) == 30.0
