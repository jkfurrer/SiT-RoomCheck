#!/usr/bin/env python3

# James K. Furrer
# Electrical Egnineering
# Stevens Institute of Technology
# E: jkfurrer@gmail.com

# timeToArrayPosition

# Take the time in format xxxxAM or xxxxPM and convert it into the position of the 144 timetable array.

import re # Use regular expressions to separate xxxx and AM/PM

def pos(time):
    # Split format into three regex groups: hh, mm, A/P
    regex = re.search("(\d{2})(\d{2})(.)M", time)
    
    pm = True if regex.group(3) == "P" else False
    hour = int(regex.group(1))
    minute = int(regex.group(2))
    index = 0
    
    #print("Hour: " + str(hour))
    #print("Mins: " + str(minute))
    #print("PM" if pm else "AM")

    if (not pm):
        # No AM/PM Offset
        # Since there are no classes starting earlier than 8am, 8am is the "zero" index
        hour = hour - 8
        index += hour * 12 + int(minute/5)
    else:
        #Offset PM
        index += 4*12
        if (hour != 12):
            index += hour * 12
        index += int(minute/5)

    if (index > 144):
        #Since IT isn't open past 8PM, there are some classes that end at 9pm that are past the array limits. Truncate this time to 8PM
        index = 144

    #print(index)
    return(index)

        
