#dictionary inside the dictionary

student={
    'Student 1':{'Name':"Abhay","Age":22,'Roll':245},
    'Student 2':{'Name':"Aman","Age":22,'Roll':355}
}
print(student['Student 1']);#{'Name': 'Abhay', 'Age': 22, 'Roll': 245}
print(student['Student 1']['Name']);#Abhay
print(student);

for a,b in student.items():
    print(a,b["Name"],b["Age"])
#o/p---
# Student 1 Abhay 22
# Student 2 Aman 22

#Update value
student['Student 1']["Age"]=23

print(student);