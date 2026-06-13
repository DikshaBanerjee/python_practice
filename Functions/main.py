def greet(name = "user"):
    print("Hello", name);

greet()
greet("Diksha")

def add(a, b):
    return a + b;

print(add(4, 5))

def info(name, age):
    print("Name:",name, " Age:", age);

info("Diksha", 26)
info(age=27, name="Piku")

def total(*args):
    print(args);

total(1,4,7,2)

def user_details(**kwargs):
    print(kwargs);
user_details(name="Mohan", age=45, city="Delhi")

def add(a, b):
    """Returns the sum of two numbers"""  #Docstrings are used to describe what a function does.
    return a + b;
print(add(3,7))

add = lambda a, b : a + b
print(add(1,2))