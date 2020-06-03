from datetime import datetime

def calculate_time(start_time, end_time):
    FMT = '%H:%M'
    time_diff = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    time_driven = int(time_diff.total_seconds()/60)
    return time_driven
    
def calculate_mph(miles,hours):
    mph = miles/hours
    return mph
