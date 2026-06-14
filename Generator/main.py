def getNumber():
    for i in range(5):
        yield i;

for x in getNumber():
    print(x);

num1 = [i*i for i in range(5)]
print(type(num1))

num2 = (i*i for i in range(5))
print(type(num2))
print(next(num2))
print(next(num2))
print(next(num2))
print(next(num2))

print(list(num2))     #Generators can be used only once----
print(list(num2))     #The second result will be empty----

# def read_lines(filepath):
#     with open(filepath) as file:
#         for line in file:
#             yield line.strip()

