
# coding: utf-8

# # Project Euler Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

# In[1]:


# We'll go back to using our trusty prime sieve from problem 7.

from math import sqrt

prime_list = [True]*2000000
prime_list[0] = False
prime_list[1] = False

for i in range(2, int(sqrt(len(prime_list)))+1):
    for j in range(2*i, len(prime_list), i):
        prime_list[j] = False

prime_sum = 0
for k in range(len(prime_list)):
    if prime_list[k]:
        prime_sum += k
        
print("The sum of primes below 2,000,000 is {}."
     .format(prime_sum))

