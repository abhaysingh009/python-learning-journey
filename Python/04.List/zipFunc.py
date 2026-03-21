# zip() → combines multiple lists element-wise

# Loop unpacks values into a, b, c

# Iteration stops at shortest list
li=[10,20,30,60]
li2=[1,2,3,4]
li3=[72,92,2,82]

# for a,b,c in zip(li,li2,li3):
#     print(a,b,c);


# without zip function
for i in range(len(li)):
    print(li[i],li2[i],li3[i]);
   
