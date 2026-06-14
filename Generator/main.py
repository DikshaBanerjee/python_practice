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

# def read_lines(filepath):
#     with open(filepath) as file:
#         for line in file:
#             yield line.strip()

