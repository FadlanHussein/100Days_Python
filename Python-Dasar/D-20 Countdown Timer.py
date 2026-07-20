# %% Kasus working data times

from datetime import datetime

current_time = datetime.now()
print("Current Date and Time: ", current_time)

# %% Date Formatting

from datetime import datetime

event_date = datetime(2026, 7, 20, 14, 30, 0)
print("Event Date: ", event_date)
formatted_date = event_date.strftime("%A, %B %d, %Y %H:%M:%S")
print("Formatted Date: ", formatted_date)


# %% Count Down Timer Function
from datetime import datetime

event_date = datetime(2026, 11, 20)
current_date = datetime.now()
time_difference = event_date - current_date
print("Time Difference: ", time_difference)

# %% Project : Event Countdown Timer
from datetime import datetime, timedelta
import time

# Step 1: Get Event Date and Timer from User
def get_event_datetime():
    try:
        date_input = input("Enter the event date (YYYY-MM-DD HH:MM:SS): ")
        event_datetime = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        return event_datetime
    except ValueError:
        print("Invalid date and time format. Please try again.")
        return None

# Step 2: Calculate Time Remaining
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

# Step 3: Display Cuntdown Timer
def display_countdown(time_left):
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    print(f"Time Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Step 4: Main Countdown loop
def start_countdown(event_datetime):
    while True:
        time_left = calculate_time_remaining(event_datetime)
        if time_left.total_seconds() <= 0:
            print("\n---- Countdown Complete!! ----")
            break
        display_countdown(time_left)
        time.sleep(1)

# Step 5: Main Program loop
event_datetime = get_event_datetime()
if event_datetime:
    print(f"Event set for: {event_datetime}")
    start_countdown(event_datetime)
        
