''' Project Euler Problem 19 Counting Sundays ---
    1 Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import time

start=time.clock()

year = 1901
month = 1
day = 1
day_of_wk = 3               # 1 == Sunday, 7 == Saturday (1/1/1901 is a Tuesday)
counter = 0
test = True

while (test == True):
    day += 1
    day_of_wk += 1
    if(day_of_wk > 7):
        day_of_wk = 1

# Cases for the month of february
#=================================================================
    if(month == 2 and day == 28):
        if(year % 4 != 0):
            month += 1
            day = 1
            day_of_wk += 1
            if(day_of_wk > 7):
                day_of_wk = 1
    elif(month == 2 and day == 29):
        day = 1
        day_of_wk += 1
        if(day_of_wk > 7):
            day_of_wk = 1
        month += 1


# Cases for months of Sep Apr Jun Nov
#=================================================================
    elif(month == 9 or month == 4 or month == 6 or month == 11):
        if(day == 30):
            day = 1
            day_of_wk += 1
            if(day_of_wk > 7):
                day_of_wk = 1
            month += 1

# Cases for all other months
#=================================================================
    else:
        if(day == 31):
            day = 1
            day_of_wk += 1
            if(day_of_wk > 7):
                day_of_wk = 1
            if(month == 12):
                month = 1
                year += 1
            else:
                month += 1

        
    if(day == 1 and day_of_wk == 1):
        counter += 1


    if(year > 2000):
        test = False
    
runtime=time.clock()-start
print("The number of Sundays to fall on first of the month in 20th Century is ",counter)
print ("The calculation time was",runtime," seconds.")
