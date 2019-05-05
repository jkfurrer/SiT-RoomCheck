#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# getSemester
# This function is used purely to determine the current semester based on current date according to system date/time

import datetime

def getSemester(userYear="", userMonth=""):
    currentDate = datetime.datetime.now()
    #print("Current date: ", currentDate.strftime("%Y-%m-%d"))
    #The year is easy, just get the current year. Duh.
    if (userYear==""):
        currentYear = currentDate.strftime("%Y")
    else:
        currentYear = userYear
    
    if (userMonth == ""):
        currentMonth = int(currentDate.strftime("%m"))
    else:
        currentMonth = int(userMonth)

    #To determine F, S, A, or B, look at the months
    if (currentMonth >= 1 and currentMonth <= 5):
        getSemester = currentYear + "S" #Spring
    elif (currentMonth == 7):
        getSemester = currentYear + "A" #Summer Session A
    elif (currentMonth == 8):
        getSemester = currentYear + "B" #Summer Session B
    else:
        getSemester = currentYear + "F" #Fall
    #print(getSemester)
    return getSemester
