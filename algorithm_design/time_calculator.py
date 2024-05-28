# Write a function named add_time that takes in two required parameters and one optional parameter:

# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# The function should add the duration time to the start time and return the result.

# If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

# If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

# Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

# add_time('3:00 PM', '3:10')
# # Returns: 6:10 PM

# add_time('11:30 AM', '2:32', 'Monday')
# # Returns: 2:02 PM, Monday

# add_time('11:43 AM', '00:20')
# # Returns: 12:03 PM

# add_time('10:10 PM', '3:30')
# # Returns: 1:40 AM (next day)

# add_time('11:43 PM', '24:20', 'tueSday')
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time('6:30 PM', '205:12')
# # Returns: 7:42 AM (9 days later)
# Do not import any Python libraries. Assume that the start times are valid times.
# The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
def add_time(start, duration, day_of_week=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # split the start time into hours and minutes
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    # split the duration time into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    # calculate the total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    if period == 'PM':
        total_minutes += 12 * 60
    # calculate the new time
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    # adjust the period (AM/PM)
    period = 'AM' if new_hour < 12 else 'PM'
    # calculate the number of days later
    days_later = total_minutes // (24 * 60)
    # adjust the new time if the hours exceed 12
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12
    # format the new time
    new_time = f'{new_hour}:{new_minute:02} {period}'
    if day_of_week:
        day_index = (days_of_week.index(day_of_week.capitalize()) + days_later) % 7
        new_time += f', {days_of_week[day_index]}'
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'
    return new_time

# print(add_time('11:30 AM', '2:32', 'Monday')) # Returns: 2:02 PM, Monday
# print(add_time('10:10 PM', '3:30')) # Returns: 1:40 AM (next day)
# print(add_time('8:16 PM', '466:02', 'tuesday')) # Returns: 7:42 AM (9 days later)
# print(add_time('2:59 AM', '24:00', 'saturDay'))
# print(add_time('11:30 AM', '2:32', 'Monday'))
# print(add_time('11:55 AM', '3:12'))

print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
