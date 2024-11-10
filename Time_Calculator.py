def add_time (start_time, duration, week_day=None):
    # Split the string into time and period (AM/PM)
    time_part, period = start_time.split()

    # Further split the time part into hours and minutes
    hour, minute = map(int, time_part.split(":"))

    # making the hour at 24h format
    hours_to_add, minutes_to_add = map(int, duration.split(":")) 
    if period == 'PM':
        hour += 12
    
    # adding the hours of the start to the hours of the duration
    final_hours = hour + hours_to_add

    #adding the minutes of the start to the minutes of the duration
    final_minutes = minute + minutes_to_add

    #fixing hours and minutes if the final minutes surpaces an hour 
    if final_minutes > 59:
        final_hours += 1
        final_minutes -= 59

    # showing next days if there is and fixing final hours
    next_days = 0
    if final_hours > 23:
        next_days = int(final_hours/24)
        final_hours = final_hours%24

    final_period = 'PM'
    if final_hours > 12:
        final_hours -= 12
    elif final_hours == 0:
        final_hours = 12
    else:
        final_period = 'AM'

    next_day = ''
    if week_day:
        week_day = week_day.lower() # Convert to lowercase to handle case-insensitivity
        days_of_week = ['sunday', 'monday', 'tueSday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_index = days_of_week.index(week_day) # Get the index of the current day
        next_index = (day_index + next_days) % len(days_of_week) # Calculate the index of the next day, wrapping around if it's the last day
        next_day = days_of_week[next_index] # Get the next day

    return f'{final_hours}:{final_minutes} {final_period}, {next_day} ({next_days} days later)'

print(add_time('11:43 AM', '00:20'))






