# #simple import
# import createModules;
# a=10;
# b=20;
# x=createModules.sum(a,b);
# y=createModules.mul(a,b);

# we can write M instead of createModules
# createModules =M
import createModules as M  #as M → gives alias (short name)
x=M.sum(10,29);
print(x);


#import custom 
# from createModules import sum;

#import all 
# from createModules import *;
# a=10;
# b=20;
# x=sum(a,b);
# y=mul(a,b);

# print(x,y);
