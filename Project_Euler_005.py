
# coding: utf-8

# # Project Euler Problem 5
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 

# In[1]:


# We can solve this by considering prime factorization.
# Take the prime factorization of every number from 2 to 20.
# If a number is divisible by every number from 1 to 20, it will
# have each of these factorizations as a subset.

from functools import reduce

# prime_factors(x) gives us the full list of prime factors of
# x, including multiples.  For instance, prime_factors(4) returns
# [2,2].

def prime_factors(x):
    i = 2
    factor_list = []
    while i <= x:
        if i == x:
            factor_list.append(i)
            return factor_list
        elif x % i == 0:
            factor_list.append(i)
            x = x/i
        elif x % i != 0:
            i += 1

full_factor_list = []

# In this for loop, we get the prime factorization of every number
# from 2 through 20.  If any of those prime factors aren't included
# in the same quantity as in full_factor_list, we append the factor
# to full_factor_list.

# For example, when j = 9, prime_factors(9) returns [3,3].  Since
# there is only one element in full_factor_list equal to 3 at that
# point, we append another 3 to full_factor_list.

for j in range(2, 21):
    factor_list = prime_factors(j)
    if len(full_factor_list) == 0:
        full_factor_list = full_factor_list + factor_list
    else:
        for k in factor_list:
            if full_factor_list.count(k) < factor_list.count(k):
                full_factor_list.append(k)

print("The full set of factors is {}."
      .format(full_factor_list))
print("The answer is {}."
      .format(reduce(lambda x, y: x*y, full_factor_list)))

