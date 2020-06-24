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
    for driver_details in driver_data:    
        if driver_details[0] == 'Driver':
            driver_trips_results['Drivers'].append(driver_details[1])
        else:
            driver_trips_results['Trips'].append(driver_details[1:])
    return driver_trips_results

def calculate_trip_times(driver_trip_results):
    for each_trip in driver_trip_results['Trips']:
        start_time = each_trip[1]
        end_time = each_trip[2]
        time_driven = calculate_trip_time(start_time,end_time)
    return time_driven

def calculate_avg_speed(driver_trip_results):
    for each_trip in driver_trip_results['Trips']:
        start_time = each_trip[1]
        end_time = each_trip[2]
        time_driven = calculate_trip_time(start_time,end_time)
        miles = float(each_trip[3])
        avg_speed = round(miles/(time_driven/60),0)
    return avg_speed

def calculate_avg_speed_for_all(driver_trip_results):
    trips_with_miles = []
    drivers = driver_trip_results['Drivers']
    trips = driver_trip_results['Trips']

    for trip in trips:
        trips_with_miles.append([trip[0], calculate_trip_time(trip[1],trip[2]), float(trip[-1])])
    trips_with_miles
    combined_trips = {}
    for x in trips_with_miles:
        name = x[0]
        if name not in combined_trips:
            combined_trips.update({
                name: {
                    'time_driven': x[1],
                    'miles': x[2]
                }})
        else:
            combined_trips[name]['time_driven'] = combined_trips[name]['time_driven'] + x[1]
            combined_trips[name]['miles'] = combined_trips[name]['miles'] + x[2] 
    return combined_trips

################################################################################
#put everything below into it's own file

def calculate_trip_time(start_time, end_time):
    FMT = '%H:%M'
    time_diff = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    time_driven = int(time_diff.total_seconds()/60)
    return time_driven
    

def calculate_mph(miles,hours):
    mph = miles/hours
    return mph


# with open('./driver_report.txt', 'w') as file_output:
#     for driver in drivers:
#         file_output.write(f'{driver}:\n')

    # for driver in drivers:
    #     if driver in combined_trips.keys():
    #         miles = int(y['miles'])
    #         time_driven = int(y['minutes'])
    #         avg_speed = round(miles/(time_driven/60))
    #         print(f'{driver}: {miles} miles @ {avg_speed} mph')
    #     else:
    #         print(f'{driver}: 0 miles')