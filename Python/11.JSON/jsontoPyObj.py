import json
js='{"Name":"Abhay", "Roll":245 }' 
print(type(js))
y=json.loads(js);
print(y)
print(type(y));#dictionary

#list
js='[{"Name":"Abhay", "Roll":245 }]' 
print(type(js))
y=json.loads(js);
print(y)
print(type(y));#dictionary
print(y[0])