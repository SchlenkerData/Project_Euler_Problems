
# coding: utf-8

# # Project Euler Problem 16
# 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
# 

# In[2]:


# Very simple: take 2^1000, turn it into a string, then
# turn that string into a list.  You have a list of numbers
# as characters.  Map int() to the elements of that list, so
# you now have a list of digits as integers.  Finally, 
# sum the list of digits.

print("The sum of the digits of 2^1000 is {}."
     .format(sum(list(map(int, list(str(2**1000)))))))

