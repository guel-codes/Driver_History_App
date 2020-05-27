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
    - test_time_driven()
    - calculate_miles_per_hour()
    - store_driver_name()
    - store_driver_times_and_miles()
    - calculate_total_miles_traveled()
    - calculate_average_speed()
    - generate_report()

- Ways to store data:
    - list or dictionary

- Updating the data
    - if driver takes more than one trip, add each new trip to specific driver's total_mileage and total time_traveled in order to calculate_average_speed() for final report generation.