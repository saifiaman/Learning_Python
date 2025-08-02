# Countdown Timer in Python
# This script implements a simple countdown timer that takes user input for the number of seconds.

import time

# take the input for countdown time in seconds
time_seconds = int(input("Enter the time in seconds for the countdown: "))

# Initialize the timer
while time_seconds > 0:
    hrs = (int(time_seconds / 3600))
    minutes = (int(time_seconds / 60)) % 60
    seconds = time_seconds % 60
    print(f"{hrs:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)  # wait for 1 second
    time_seconds -= 1
print("Time's up!")
