single = (6,) #Without the comma, Python will treat it as a normal value.
items = ("apple", "banana", "orange")

# print(items[0])
# print(items[2])

print(type(items))
print(len(items))
# print(items[1:3])

# items[1] = "grapes"     // Tuples cannot be modified after creation.
# items.append("grapes") # Tuples do not have an append method, as they are immutable.
print(items.count("orange"))
print(items.index("apple"))

for i in items:
    print(i);

tup = ("subham", "diksha", "mohan")
lis = list(tup)
print(type(lis))

new_tup = tuple(lis)
print(type(new_tup))

data = 10, 20, 30
print(type(data))

a, b, c = data
print(a)
print(b)
print(c)