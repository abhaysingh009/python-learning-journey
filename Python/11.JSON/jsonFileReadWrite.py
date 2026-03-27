import json
file=open("filej.json","r")
x=file.read();
li=json.loads(x);
# print(li)
# print(type(li));

# print(li["education"])
for a ,b in li.items():
    print(a,b)