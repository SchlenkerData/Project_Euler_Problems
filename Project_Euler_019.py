
# coding: utf-8

# # Project Euler Problem 19
# 
# You are given the following information, but you may prefer to do some research for yourself.
# 
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# 

# In[1]:


year = 1901
month = 1
dow = 2
# Let's number the months 1 to 12.
# Let's number the days of the week 0 to 6.
# 1 Jan 1901 was on a Tuesday.

sundaycounter = 0

while (year < 2001):
    # First check if the month starts with a Sunday.  Print year and month if so.
    if (dow == 0):
        sundaycounter += 1
        # print(year, month)
    
    # Add the appropriate number of days for the rest of the month.
    if (month == 2):
        if(year % 4 == 0):
            dow = (dow + 29) % 7
        else:
            dow = (dow + 28) % 7
    elif (month in (1, 3, 5, 7, 8, 10, 12)):
        dow = (dow + 31) % 7
    else:
        dow = (dow + 30) % 7
        
    # Now increment one month ahead.
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
        
print(f"There were {sundaycounter} sundays in the century.")

