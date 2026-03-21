import random as r

n=r.randint(0,1000);
count=0;
while True:
    x=int(input("Guess The Number: "));
    count+=1;
    if x==n:
        print("Congrats! You Guessed the Number in "+str(count)+" Guesses");
        break;
    elif x<n:
        print("Guess a Bigger Number ! ")
    else:
        print("Guess a Smaller Number ! ")

        