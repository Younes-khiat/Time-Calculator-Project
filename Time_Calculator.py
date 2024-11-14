def add_time (start_time, duration, week_day=None):
    # Split the string into time and period (AM/PM)
    time_part, period = start_time.split()

    # Further split the time part into hours and minutes
    phour, minute = map(int, time_part.split(":"))

    #split duration
    hours_to_add, minutes_to_add = map(int, duration.split(":")) 

    hour = phour
    # making the hour at 24h format
    am_to_pm = {1:13,2:14,3:15,4:16,5:17,6:18,7:19,8:20,9:21,10:22,11:23,12:0}
    if period == 'PM':
        hour = am_to_pm[phour]
            
    # adding the hours of the start to the hours of the duration
    final_hours = hour + hours_to_add

    #adding the minutes of the start to the minutes of the duration
    final_minutes = minute + minutes_to_add

    #fixing hours and minutes if the final minutes surpaces an hour 
    if final_minutes > 59:
        final_hours += 1
        final_minutes -= 60

    # showing next days if there is and fixing final hours
    next_days = 0
    if final_hours > 24:
        next_days = int(final_hours/24)
        final_hours = final_hours%24

    if final_hours > 11: 
        final_period ='PM'
    else:
        final_period = 'AM'  
    if final_hours == 12:
        if period =='AM':
            final_period = 'PM'
        else:
            final_period = 'AM'
    if final_hours == 0:
        final_hours = 12
         
    wiw = final_hours
    #returning to 12h format
    if final_period == 'PM':
        for key, value in am_to_pm.items():
            if final_hours == value:
                wiw = key
                break


    result = f'{wiw}:{str(final_minutes).zfill(2)} {final_period}'

    

    next_day = ''
    if week_day:
        week_day = week_day.lower() # Convert to lowercase to handle case-insensitivity
        days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_index = days_of_week.index(week_day) # Get the index of the current day
        next_index = (day_index + next_days) % len(days_of_week) # Calculate the index of the next day, wrapping around if it's the last day
        next_day = days_of_week[next_index] # Get the next day
        
        result += f', {next_day.capitalize()}'
    if next_days == 1:
        result += ' (next day)'
    elif next_days >1:
        result += f' ({next_days} days later)'

    return result

print(add_time('2:59 AM', '24:00', 'saturDay'))






