
# coding: utf-8

# # Project Euler Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
# 

# In[1]:


# The simplest way to find the prime factors of a number n
# is to start by dividing n by 2 as many times as you can, 
# then by 3, etc.  This method does not require a prime
# sieve, since dividing by all powers of smaller primes
# will exclude any composite numbers you hit along the way.
# For instance, once we've checked 2 and 3, we don't need to 
# worry about 4 and 6 showing up in the list of prime factors.

bignum = 600851475143
i = 2

while bignum > 1:
    if bignum == i:
        print("The largest prime factor is {}.".format(i))
        bignum = 1
    elif bignum % i == 0:
        print("{} is a prime factor.".format(i))
        bignum = bignum / i
    elif bignum % i != 0:
        i += 1

