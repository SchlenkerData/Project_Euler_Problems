
# coding: utf-8

# # Project Euler Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 

# In[1]:


# We use a nested for loop to check all possible products of 
# 3-digit numbers.  To check if the product is a palindrome, we
# convert the product to a string, reverse the string, convert
# back to an integer, then see if that's equal to the original product.

max_palin_prod = 0
max_x = 0
max_y = 0

for x in range(100, 1000):
    for y in range(x, 1000):
        palin_check = int(str(x*y)[::-1])
        if (palin_check == x*y) and (x*y > max_palin_prod):
            max_palin_prod = x*y
            max_x = x
            max_y = y
            
print("Largest palindrome product: {} x {} = {}"
      .format(max_x, max_y, max_palin_prod))

