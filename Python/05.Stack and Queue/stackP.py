# Stack = LIFO (Last In First Out)

# Last inserted element is removed first

# Operations:

# push → add element

# pop → remove last element

# Python has no built-in stack, but we use:

# list (most common)

# collections.deque (faster)

# Why deque is Faster
# 📌 Key Points (Easy to Remember)

# list = dynamic array

# deque = doubly linked blocks

# deque supports O(1) operations on both ends

# list is fast only at end, slow at front

# deque avoids shifting elements

# from collections import deque
# stack=deque()

# stack.append(1);
# stack.append(2);
# stack.append(13);

# print(stack);
# stack.pop();
# print(stack);
# print(stack[-1])

import time
li=[]


while True:
    op=int(input('''1.Push Element\n2.Pop Element\n3.Peek Element\n4.Display Element\n5.Exit...\n'''))
    if(op==1):
            n=int(input("Enter the number: "))
            li.append(n);
            print(str(n)+" Pushed into stack")
    elif(op==2):
        if len(li)==0:
             print("Stack underflow")
        else:
            print("Popped Element: ",li[-1]);
            li.pop();
    elif(op==3):
        if len(li)==0:
             print("Stack underflow")
        else:
            print("Peek Element: ",li[-1]);

    elif(op==4):
        print(li)

    elif(op==5):
        print("Exiting..........");
        break;
    else:
         print("Select a valid Operation!")

time.sleep(3);

print("Exited Successfully!");
    