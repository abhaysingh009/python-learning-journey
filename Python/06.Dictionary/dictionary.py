# Dictionary in Python
# 📌 Key Points (Easy to Remember)

# Dictionary = key-value pair collection

# Written using {}

# Keys must be unique

# Keys must be immutable (int, string, tuple)

# Values can be anything

# Fast lookup → O(1) (hashing)

d={
    1:"Abhay",
    2:"Pratap",
    3:"Singh",
    'roll':9202
}

# d[1]="Rahul"
# print(d[1]);
# print(d.keys());#prints keys
# print(d.items());#dict_items([(1, 'Abhay'), (2, 'Pratap'), (3, 'Singh'), ('roll', 9202)])
# print(d)

# print(type(d['roll']))#int


#iterate on dictionary
# for i in d:
#     print(i,":",d[i]);

# functions
# print(d.get('roll')); # returns the value of provided key
# print(d.keys())#prints keys dict_keys([1, 2, 3, 'roll'])
# print(d.pop(1));#deletes and returns  key value of provide key
# print(d.clear())#clear dict..
# print(d.popitem());#removes last item  like pop_back
# del(d[1]); #deletes item of key
# print(d);
# del(d);# delete dictionary

# dic=dict(name="Ayush", age=22);#dict()=> creates new dictionary;
# print(dic);


# fromkeys() → creates a new dictionary

# Takes keys from iterable

# Default value = None

# Original values are ignored

# Works on keys only
new_dict={}
new_dict=dict.fromkeys(d)
print(new_dict.keys());

# new_dict = {}
# for key in d:
#     new_dict[key] = None
# print(new_dict);# copied d in new_dict

# print(d.items());#dict_items([(1, 'Abhay'), (2, 'Pratap'), (3, 'Singh'), ('roll', 9202)])
# print(d.keys());#dict_keys([1, 2, 3, 'roll'])
# print(d.values())#dict_values(['Abhay', 'Pratap', 'Singh', 9202])



# setdefault(key, default=None)
# If key exists → return its value
# If key does NOT exist →
# add key with default value
# return default value
# It modifies dictionary
# print(d.setdefault(1))
d={
    1:"Abhay",
    2:"Pratap",
    3:"Singh",
    'roll':9202
}
d2={
    'x':"sd"
}
print(d.setdefault(10))
print(d.keys());

# print(d.update(d2))#merger d2 in d1
d.update({1:"Happy"}) # or d[1]="Happy"  #updates value 
d.update({9:"Happy"})#adds new value if key not present
print(d);


for a,b in d.items():
    print(a,b);
# output
# 1 Abhay
# 2 Pratap
# 3 Singh
# roll 9202
# x sd
