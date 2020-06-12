from driver import read_file, separate_drivers_and_trips, calculate_trip_time, calculate_trip_times
from pathlib import Path


mock_test_file = Path('./mocked_data_input.txt')


def test_generate_driver_report_reads_data_from_file():
    driver_data = [
        ['Driver', 'Dan'],
        ['Driver', 'Lauren'],
        ['Driver', 'Kumi'],
        ['Trip', 'Dan', '07:15', '07:45', '17.3'],
        ['Trip', 'Dan', '06:12', '06:32', '21.8'],
        ['Trip', 'Lauren', '12:01', '13:16', '42.0']
    ]
    assert read_file(mock_test_file) == driver_data


def test_separate_drivers_and_trips():
    driver_data = [
        ['Driver', 'Dan'],
        ['Driver', 'Lauren'],
        ['Driver', 'Kumi'],
        ['Trip', 'Dan', '07:15', '07:45', '17.3'],
        ['Trip', 'Dan', '06:12', '06:32', '21.8'],
        ['Trip', 'Lauren', '12:01', '13:16', '42.0']
    ]
    
    driver_trip_results = {
        'Drivers': [
            'Dan', 'Lauren', 'Kumi'
        ], 
        'Trips': [
            ['Dan', '07:15', '07:45', '17.3'], 
            ['Dan', '06:12', '06:32', '21.8'], 
            ['Lauren', '12:01', '13:16', '42.0']
        ]
    }
    assert separate_drivers_and_trips(driver_data) == driver_trip_results


def test_calculate_trip_time():
    driver_trip_results = {
        'Drivers': [
            'Dan', 'Lauren', 'Kumi'
        ], 
        'Trips': [
            ['Dan', '07:15', '07:45', '17.3'], 
            ['Dan', '06:12', '06:32', '21.8'], 
            ['Lauren', '12:01', '13:16', '42.0']
        ]
    }
    
    assert calculate_trip_times(driver_trip_results) == 75
    

def test_time_driven():
    assert calculate_trip_time('7:15','7:45') == 30
    assert calculate_trip_time('12:01','13:16') == 75


# def test_calculate_mph():
#     assert calculate_mph(42.0,1.25)
