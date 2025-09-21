'''
@ASSESSME.USERID: lj7829
@ASSESSME.AUTHOR: Lazar Jovovic
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''

import math

def fact(n):
    if isinstance(n, int) and n > 0:
        return math.factorial(n)
    return 0

def root(x):
    if x > 0:
        return math.sqrt(float(x))
    return 0

def trunk(a):
    return math.trunc(float(a))

def main():
   
   val = input("Enter a numeric valure: ")
   num = int(float(val))
   print(f"{num} factorial = {fact(num)}")

   val = input("Enter a numeric valure: ")
   num = float(val)
   print(f"The square root of {num} = {root(num)}")

   val = input("Enter a numeric valure: ")
   num = float(val)
   print(f"{num} truncated = {trunk(num)}")



if __name__ == "__main__":
    main()