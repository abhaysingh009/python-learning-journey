# math = built-in module
# Provides mathematical functions
# Works with numbers only (no strings)
# Must use import math
# Faster (implemented in C)


# Basic Functions---------------------------------------------------------------------
# math.sqrt(x)        # square root
# math.pow(x, y)      # x^y (returns float)
# math.ceil(x)        # round up
# math.floor(x)       # round down
# math.trunc(x)       # remove decimal
# ----------------------------------------------------------------------------------------


# Constants -----------------------------------------------------------------------------
# math.pi             # 3.14159...
# math.e              # 2.718...
# ------------------------------------------------------------------------------------------


# Logarithmic Functions ------------------------------------------------------------------
# math.log(x)         # natural log
# math.log10(x)       # log base 10
# math.log2(x)        # log base 2
# ---------------------------------------------------------------------------------------


# Trigonometric Functions ----------------------------------------------------------------
# math.sin(x)         # sine
# math.cos(x)         # cosine
# math.tan(x)         # tangent
# math.degrees(x)     # rad → degree
# math.radians(x)     # degree → rad
# ----------------------------------------------------------------------------------------

# Other Functions-------------------------------------------------------------------------
# math.factorial(x)   # factorial
# math.gcd(a, b)      # greatest common divisor
# math.fabs(x)        # absolute value
# ==================================================================================================

import math as m
# print(m.fabs(3-5));#2.0

# print(m.ceil(10.2))#11
# print(m.floor(10.2))#10
# print(m.sqrt(5))#2.23606797749979
# print(m.pow(5,2))#25.0
# print(m.trunc(923.33))#removes decimal-->923
# print(m.factorial(4))#24
# print(m.factorial(50))#valid
# print(m.gcd(10,20,30))#10

print(m.log(10) )        # natural log
print(m.log10(10))       # log base 10
print(m.log2(8))           #log base 2





