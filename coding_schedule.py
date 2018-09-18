"""
coding_schedule.py 
Input: Current weekday, derived from the datetime package within Python (called on line 11). 
Output: A string that states the present day and declares whether that day is a programming day or a day off.

"""

import datetime as dt


todays_day = dt.datetime.weekday(dt.datetime.now())

def convert_to_pronoun(day):
	if day == 0:
		return "Monday"
	if day == 1:
		return "Tuesday"
	if day == 2:
		return "Wednesday"
	if day == 3:
		return "Thursday"
	if day == 4:
		return "Friday"
	if day == 5:
		return "Saturday"
	if day == 6:
		return "Sunday"

if todays_day == 0 or 1 or 2 or 3 or 4 or 5:
	print("Today is " + convert_to_pronoun(todays_day) + " and you should program!")
else:
	print("Today is Sunday and you have the day off!")


