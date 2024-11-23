#!/usr/bin/env python3

# Student ID: [124876228]

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_time
    """



    def __init__(self, hour=12, minute=0, second=0):

        self.hour = hour

        self.minute = minute

        self.second = second



    def __str__(self):

    '''Return a string representation for the object self.'''

    return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def __repr__(self):

    '''Return a string representation for the object self.'''

    return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'


 
    def __add__(self, t2):

    """Return the result by using sum_times() method."""

    return self.sum_times(t2)



    def format_time(self):

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def sum_times(self, t2):

    """Add two time objects and return the sum."""

    total_seconds = self.time_to_sec() + t2.time_to_sec()  

    return sec_to_time(total_seconds) 



    def change_time(self, seconds):

        time_seconds = self.time_to_sec()

        nt = sec_to_time(time_seconds + seconds)

        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second



    def sec_to_time(seconds):

    """Convert a given number of seconds to a time object in hour, minute, second format."""

    time = Time()

    minutes, time.second = divmod(seconds, 60)

    time.hour, time.minute = divmod(minutes, 60)

    return time



    def valid_time(self):

        """Check for the validity of the time object attributes:

        0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60."""

        if self.hour < 0 or self.minute < 0 or self.second < 0:

            return False

        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:

            return False

        return True



    def sec_to_time(seconds):

        time = Time()

        minutes, time.second = divmod(seconds, 60)

        time.hour, time.minute = divmod(minutes, 60)

        return time
