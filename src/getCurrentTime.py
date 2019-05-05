#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# getCurrentTime

# Most modern machines have their time automatically set based on ntp time settings. Rather than getting the current time from ntp ourselves, rely on the system time (assume it is set correct) since this is easier and faster.

import datetime

class currentTime:
    def __init__(self):
        self.dt = datetime.datetime.now()
        self.day = self.dt.weekday()
        self.hour = self.dt.hour
        self.minute = self.dt.minute
        self.generateArrayPos()
    def getDay(self):
        #print(self.day)
        return self.day
    def getHour(self):
        #print(self.hour)
        return self.hour
    def getMinute(self):
        #print(self.minute)
        return self.minute
    def generateArrayPos(self):
        if (self.day > 4):
            # Jump to beginning of week
            self.indexDay = 0
            self.indexTime = 0
        elif (self.hour < 8):
            # Jump to beginning of classes
            self.indexDay = self.day
            self.indexTime = 0
        elif (self.hour > 20):
            # Jump to beginning of classes the next day
            self.indexDay = self.day + 1
            self.indexTime = 0
        else:
            self.indexDay = self.day
            self.indexTime = (self.hour - 8) * 12
            self.indexTime += int(self.minute/5)
    def getDayIndex(self):
        #print(self.indexDay)
        return self.indexDay
    def getTimeIndex(self):
        #print(self.indexTime)
        return self.indexTime
