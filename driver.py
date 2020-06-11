from datetime import datetime
from collections import defaultdict

 
def read_file(input_file):
    with open(input_file, 'r') as file_input:
        driver_data = []
        for row in file_input:
            driver = row.split()
            driver_data.append(driver)
    return driver_data


def separate_drivers_and_trips(driver_data):
    driver_trips_results = defaultdict(list)
    for x in driver_data:    
        if x[0] == 'Driver':
            driver_trips_results['Drivers'].append(x[1])
    #         driver_trips_results['drivers'] = list(set(driver_trips_results['drivers']))
        else:
            driver_trips_results['Trips'].append(x[1:])
    print(dict(driver_trips_results))
    return driver_trips_results
    # with open('./driver_report.txt', 'w') as file_output:
    #     for driver in drivers:
    #         file_output.write(f'{driver}:\n')


def calculate_time(start_time, end_time):
    FMT = '%H:%M'
    time_diff = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    time_driven = int(time_diff.total_seconds()/60)
    return time_driven
    

def calculate_mph(miles,hours):
    mph = miles/hours
    return mph