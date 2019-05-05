#!/usr/bin/env python3

import getSchedule
import getSemester

semester = getSemester.getSemester()
getSchedule.getSchedule(semester)
getSchedule.getSchedule("2018F")
