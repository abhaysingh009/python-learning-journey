from collections import deque
q=deque();
while True:
    user=int(input("Enter Your choice \n1.Push\n2.pop\n3.front\n4.display\n5.Exit..\n"));
    if user==1:
        n=int(input("Enter the Number:"))
        q.append(n)
        print(n,"Pushed in the Queue");
    elif user==2:
        if(len(q)==0):
            print("Queue underFlow!");
        else:
            print(q.popleft(),"poped fom the queue");
    elif user==3:
        if(len(q)==0):
            print("No element found");
        else:
            print("front Element",q[0]);
    elif user==4:
        for i in q:
            print(i, end=" ");
        print("\n");
    elif user==5:
        break;
    else:
        print("Enter a Valid choice!");