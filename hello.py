print("hello venkatesh!")
person22 = {"name":"Jac", "surname":"Smith", "age":"22"}
#print(person22)///
"""print(person22.pop("name"))
print(person22)"""
person22["age"]= 25
print(person22)
person2= int(input("enter the number:"))
if person2 in person22.values():
    print("success")
else:
    print("not found")

venkat=int(input("enter number:"))
if venkat>10:
    print("good")
elif venkat==10:
    print("awesome")
else:
    print("bad")