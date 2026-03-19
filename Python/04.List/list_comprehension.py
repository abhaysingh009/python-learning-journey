# “List comprehension = loop + append in one line”
# Short way to create lists

# Replaces loop + append

# Syntax: [expression for item in iterable]

# Can include conditions

# l=[]

# normal formula
# for a in range(1,101):
#     l.append(a);
# print(l);

#list comprehension
# n=[m for m in range(1,101)]
a=0
n=[a for m in range(1,101) if m%2==0]
print(n);

s="abhay";
l=[x for x in s ]#stores characters one by one in x and makes a list of characters(string)
print(l,type(l))#list
print(type(l[0])) #str