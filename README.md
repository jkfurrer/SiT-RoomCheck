# SiT-RoomCheck
Useful utility for Classroom Technology at Stevens Institute of Technology to check the next availability of a specified room.

To use this tool, simply run:
python getRoomAvailability.py

and when prompted, enter a valid room name. If an invalid room name is entered, a list of rooms is shown.

This tool uses schedules uploaded in web.stevens.edu/scheduler/core to get classroom schedules. This mimics the functionality of web.stevens.edu/roomsched, but does so a lot faster and more succinctly.

First, a schedule is downloaded based on the current month and year. This is stored in resources. If you have no internet connection, but the schedule is found in the resources folder, the program will still run.

From the schedule, a list of rooms found in that schedule. Classes marked as TBD, TBA, CANCELLED, WEB, OFF, etc. are removed from the results.

Then, the user is prompted to pick a room. Entries are not case sensitive, nor whitespace sensitive. If an invalid selection is made, the user is prompted again, showing a list of valid rooms. 

Once a selection is made, the schedule is sifted through matching the room selection with timeslots where classes occur based on day of the week, start time, and end time. These are shown as X's in the visual timetable.

Finally, an algorithm shows when the next available timeslot of specified length is coming up based on the current system time. The program shows the next 10m, 30m, 1h, 2h, and 3h timeslot availability. Short time slots would be geared towards small things like cable replacements, where longer timeslots are for more involved testing or equipment swapping.

To take this program further, it would be great if a database was created to show equipment that is used in the room, so the technician knows what to expect when going to the room. This database is not internet facing nor complete yet, so this may be a future extension of this project.
