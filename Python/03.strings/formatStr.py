# The format() method is used to insert values into a string in a formatted way.

# w="hi my name is {fname} {lname} ".format(fname="abhay",lname="singh");

# w="hi my name is {} {} ".format("abhay","singh");

w="hi my name is {0} {1} ".format("abhay","singh");

x="hi"
w="hi my name is {0:^10} {1} {2} ".format("abhay",x,10); #{0:10} total 10 space will be ouccified and
#provided value will be stored from the right side if string exceeds the limit then space will be auto increased
#{0:^10} value is in middle of spaces ,{0:>10}=>in right side (by def),{0:<10} in left side     


print(w);