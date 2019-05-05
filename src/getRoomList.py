#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# getRoomList
# This pulls the list of unique rooms in the registrar list.
# The room names are pulled from the course schedule. If they are not in the course schedule, then it is not a registrar room (or it is not used by classes and may be used as a conference room)

def getRoomList(semester):
    with open("../resources/" + str(semester) + ".txt") as schedule:
        rooms = []
        for line in schedule:
            if (line.strip() != ""):
                room = line.strip().split(",")[6].strip()
                room += line.strip().split(",")[7].strip()
                if not(room in rooms):
                    if (room != "") and (room.upper() != "OFFWEB") and (room.upper() != "OFFCLOSED") and (room.upper() != "OFFTBA") and (room.upper() !="N/AN/A"):
                        #print(room)
                        rooms.append(room)

    schedule.close()
    rooms.sort()
    #print(rooms)
    with open("../resources/" + str(semester) + "_rooms.txt", "w") as roomList:
        for x in rooms:
            roomList.write(x + "\n")
    roomList.close()
    return rooms
