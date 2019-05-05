#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# getSchedule
# This function takes the current semester and pulls the appropriate course listing from web.stevens.edu/scheduler/core

import urllib
import wget
import os
from pathlib import Path

def getSchedule(semester):
    url = "https://web.stevens.edu/scheduler/core/" + str(semester) + "/sched_plus_crsemtg.txt"
    #print(url)
    destination = "../resources/" + str(semester) + ".txt"
    #print(destination)

    
    # We want the schedule to be as up to date as possible. In this case, everytime, the program is run the schedule should be redownloaded in case there are any changes. The schedule file isn't that big, and this program shouldn't be run that often, so this is an acceptable use of resources. But first we have to see if the schedule exists online before we overwrite the file.
    try:
        with urllib.request.urlopen(url) as f:
            output = open(destination, "w")
            output.write(f.read().decode('UTF-8'))
            f.close()
    except:
        # If an error is encountered, check to see if the file exists already and ignore updating (use "cached" version).
        # If the schedule is not downloaded, and it can not be retrieved, print error message and exit.
        if (not Path(destination).is_file()):
            print("The schedule for the current semester can not be found, and does not exist in the filesystem.")
            print("Possible causes include: ")
            print("\t-You are not connected to the internet to download schedule.")
            print("\t-You do not have access to the scheduler pages for some reason.")
            print("\t-The schedule for the current semester does not exist on the scheduler yet.")
            print("\t-The scheduler has been updated and no longer works with this program.")
            print("\nCheck your internet connection, and check the directory in web.stevens.edu/scheduler/core/ to see if the schedule you are looking for exists.")
            exit()
    #urllib.request.urlretrieve(url, destination)
