#!/usr/bin/env python3




class Time:

    """Simple object type for time of the day.

       data attributes: hour, minute, second

    """

    def __init__(self, hour=12, minute=0, second=0):

        """constructor for time object""" 

        self.hour = hour

        self.minute = minute

        self.second = second



def format_time(t):

    """Return time object (t) as a formatted string"""

    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'



def change_time(time, seconds):

    time.second += seconds

    # Ensure seconds are valid

    while time.second >= 60:

        time.second -= 60

        time.minute += 1

    while time.minute >= 60:

        time.minute -= 60

        time.hour += 1



    # Handle negative seconds

    while time.second < 0:

        time.second += 60

        time.minute -= 1

    while time.minute < 0:

        time.minute += 60

        time.hour -= 1



    # Ensure hour stays within valid range

    time.hour %= 24

    return None




def valid_time(t):

    """check for the validity of the time object attributes:

       24 > hour > 0, 60 > minute > 0, 60 > second > 0 """

    if t.hour < 0 or t.minute < 0 or t.second < 0:

        return False

    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:

        return False

    return True


