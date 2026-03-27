# JSON = JavaScript Object Notation
# Used for data exchange (APIs, web)
# Human-readable format
# Python uses json module
# Similar to dictionary
# json.dump(obj, file)     # object → JSON file
# json.load(file)          # JSON file → object
# json.dumps(obj)          # object → JSON string
# json.loads(string)       # JSON string → object

# json supports mainly 6 datatypes
# string , number,boolean,null,object,array

import json

di={
    "Name":"Abhay",
    "Roll":245
}
f=json.dumps(di)
print(f);
print(type(f));
