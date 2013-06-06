"""
Created on Tue Jun  4 12:06:47 2013
@author: Mott
"""
# Following function accepts an integer x and tests whether it is prime, will retun False if less than 2.
def is_prime(x):
    return sum([x%i == 0 for i in range(1,x)]) == 1