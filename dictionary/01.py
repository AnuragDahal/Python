# Dictionaries are ordered collection of data items
# They store multiple items in single variable
employee_id={
    111:"Anurag",
    146:"Swikriti",
    674:"Tyson",
    343:"Blaze"}
# throws error if key doesn't exist
print(employee_id[111])
# doesn't throws error if key doesn't exist
print(employee_id.get(111))
print(employee_id.keys())
for key in employee_id.keys():
 print(f"the value corresponding value to the key {key} is {employee_id[key]}") 
print(employee_id.values())
print(employee_id.items())
for key,values in employee_id.items():
    print(f"The corresponding value to the key{key} is {values}) ")