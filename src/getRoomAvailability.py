#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# getRoomAvailability

# This is the main program that is intended to be run by the user. When run, the user will simply be asked to type in the name of a registrar room they want to check the next availability for. This program is useful to classroom technology staff who get TeamDynamix tickets or end user calls about issues in a room that need to be looked at. The current system of checking the room schedule is looking at https://web.stevens.edu/roomsched/ . While this is very useful, this website is slow to load by modern standards, and the timetable formatting is inconsistent from one room to the next, often causing errors in reading the room schedule. Often times IT staff simply wants to know when the room is next open for an hour or so. Simply typing in the room number and getting the result right away is much faster.

# This program is intended to work with registrar controlled rooms to determine when a class not scheduled. This program does not handle rooms that are not on registrar's list, such as conference rooms - these do not have publicly available schedules in most cases. This room does not account for events like club meetings either - these would be pulled from Virtual EMS, but unfortunately I do not have access to this scheduler's data. This would be a great way to extend this project further.

# In addition to checking room availability, it would be great to return the equipment that is used in the room so that the technician can gather the appropriate tools for the job (and prepare themselves mentally for the chaos that may ensue). Some of this information would be pulled from a database that lists equipment by room. This does not exist. However, some useful information can be pulled by chekcing hostnames that exist on the AV network: some information can be pulled from the web interface of the AV equipment.

from getSemester import getSemester
from getSchedule import getSchedule
from getRoomList import getRoomList
from singleRoomSchedule import singleRoomSchedule
from getCurrentTime import currentTime
from availability import freeTime
from arrayPosToTime import arrayDay, arrayTime

def main():
    currentSemester = getSemester()
    getSchedule(currentSemester)
    allRooms = getRoomList(currentSemester)

    while True:
        room = input("Enter the room you want to check availability for (q to quit): ")
        room = room.replace(" ", "")
        room = room.upper()

        if (room == "Q"):
            print("Exiting...")
            exit()

        if (room in allRooms):
            break;
        else:
            print("Room " + room + "not found. Here is a list of all valid rooms:")
            for x in allRooms:
                print(x, end="\t")
            print("Please try again using one of these rooms.")

    availability = singleRoomSchedule(currentSemester, room)
    now = currentTime()

    free10min = freeTime(now, availability)
    print("Next 10min timeslot: ", end="")
    arrayDay(free10min[0])
    arrayTime(free10min[1])
    print(" to ", end="")
    arrayTime(free10min[2])
    print()
    
    free30min = freeTime(now, availability, 30)
    print("Next 30min timeslot: ", end="")
    arrayDay(free30min[0])
    arrayTime(free30min[1])
    print(" to ", end="")
    arrayTime(free30min[2])
    print()
    
    free1h = freeTime(now, availability, 60)
    print("Next 1h timeslot: ", end="")
    arrayDay(free1h[0])
    arrayTime(free1h[1])
    print(" to ", end="")
    arrayTime(free1h[2])
    print()
    
    free2h = freeTime(now, availability, 120)
    print("Next 2h timeslot: ", end="")
    arrayDay(free2h[0])
    arrayTime(free2h[1])
    print(" to ", end="")
    arrayTime(free2h[2])
    print()
    
    free3h = freeTime(now, availability, 180)
    print("Next 3h timeslot: ", end="")
    arrayDay(free3h[0])
    arrayTime(free3h[1])
    print(" to ", end="")
    arrayTime(free3h[2])
    print()
    
if __name__ == "__main__":
    main()
