# ZeroDivisionError --> 10/0
# NameEror --->print(a)   (you did not declare 'a')
#TypeError -->print('10' +10)
#ValueError -->x = int("abc") 
# import math
# print(math.sqrt(-1))

#IndexError -->s="abhay" print(s[10])
#KeyError  
# d={
#     1:"abhay",
# }
# d[2]

#ModuleNotfound -->  let you created module 'cal.py' then using  'import calc.py'
#ImportError --> you are calling a function from a module but function does not exist in module

# Exception Handling

# try :
#     print(10/0)
# # except Exception:
# except ZeroDivisionError:
#     print("Error")

# # multiple exception
# try:
#     a = int("abc")
# except ValueError:
#     print("Invalid value")
# except TypeError:
#     print("Type error")

#finally block
# finally always executes 
# Even if:
# - Error occurs
# - Error not handled
try:
    print(10/0)

finally:
    print("Always runs")