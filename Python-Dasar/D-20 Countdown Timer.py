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

event_date = datetime(2026, 7, 20)
current_date = datetime.now()
time_difference = event_date - current_date
print("Time Difference: ", time_difference)
