student = {
    "name" : "Diksha",
    "age" : 27,
    "city" : "delhi"
}

print(type(student))
print("Hello",student["name"])
print(student.get("age"))
print(student.get("email"))

student["email"] = "abc@example.com"
student["age"] = 26

student.pop("email")
student.popitem()
del student["age"]
student.clear()
print(student)

student.update({
    "name" : "Diksha",
    "age" : 27,
    "city" : "delhi"
})

print(student.keys())
print(student.values())
print(student.items())

for i in student:
    print(i);

for i in student.values():
    print(i);

for i in student.items():
    print(i);

print("class" in student)
print(student)

copy_student = student.copy()
copy_student["name"] = "Piku"
print(copy_student)

user = {
    "id" : 1,
    "profile" :{
        "name" : "Diksha",
        "age" : 26
    }
}
print(user)
print(user["profile"]["name"])





