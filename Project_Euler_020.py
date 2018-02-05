
# coding: utf-8

# # Project Euler Problem 20
# 
# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!
# 

# In[2]:


from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x*y, list(range(1, n+1)))

print("The sum of the digits in 100! is {}."
     .format(sum(list(map(int, list(str(factorial(100))))))))

