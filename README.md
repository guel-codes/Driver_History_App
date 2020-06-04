# Driver History Problem
## Instructions
This is a problem set to track driving history for people.

Two commands to enter information:
- Driver: to register new driver
- Trip: Driver, start_time, stop_time, miles_driven
- Discard any trips that average a speed < 5 mph or greater than 100 mph
- Generate a report containing each driver witht the total miles driven and the average speed. Sort the output by most miles driven to least. Round miles and miles per hour to the nearest integer.

### Assumptions
- 24 hour clock
- No driving past midnight (start time will always be before end time)


## First Thoughts
- Tests that can written:
    - test_driver_input
    - test_trip_input
    - test_time_driven()
    - test_calculate_mph()
    - test_store_driver_name()
    - test_store_driver_times_and_miles()
    - test_calculate_total_miles_traveled()
    - test_calculate_average_speed()
    - test_generate_report()
        - Generate a report containing each driver with total miles driven and average speed. Sort the output by most miles driven to least. Round miles and miles per hour to the nearest integer.

- Ways to store data:
    - list or dictionary

- Updating the data
    - if driver takes more than one trip, add each new trip to specific driver's total_mileage and total time_traveled in order to calculate_average_speed() for final report generation.


