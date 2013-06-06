"""
Created on 10 Sep 2012
@author: Mott
"""
# Following function returns all prime numbers within given range.
from is_prime import is_prime
def find_primes(a,b):
    return filter(lambda a: a!=0,[i*is_prime(i) for i in range(a,b+1)])