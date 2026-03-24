# random = built-in module
# Used to generate random values
# Works with:
# numbers
# lists
# ranges
# Commonly used in games, simulations

#Random Numbers ------------------------------------------------------------------------------------------
# random.random()        # float (0 to 1)
# random.randint(a, b)   # integer between a and b (inclusive)
# random.uniform(a, b)   # float between a and b
# -------------------------------------------------------------------------------------------------------------


# List Operations  ------------------------------------------------------------------------------------------
# random.choice(li)      # random element from list
# random.shuffle(li)     # shuffle list (modifies original)
# random.sample(li, k)   # k random elements (no repeat)
# --------------------------------------------------------------------------------------------------


# Range Selection   ------------------------------------------------------------------------------------------
# random.randrange(start, stop, step)   # like range but random

import random as r
# print(r.random());
# print(r.randint(1000,9999));
# print(r.uniform(1000,9999));

# li=[10,20,30,40,50]
# print(r.choice(li))
# r.shuffle(li)
# print(li)
# print(r.sample(li,3))

print(r.randrange(10,89));#same as randint but 89 excluded


