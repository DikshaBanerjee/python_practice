empty_set = set()

numbers = {1,3,6,3,9,4,7,2}
print(numbers)

items = {"apple", "orange", "banana", "banana"}
for i in items:
    print(i);

print("banana" in items)

items.add("mango")
# print(items)

items.update(["kiwi", "pear"])
# print(items)

items.remove("pear")
print(items)

items.discard("guava")
items.pop()     #remove any random item
# items.clear()
print(items)

a = {1,2,3,4,5}
b = {4,6,5,7}
result = a.union(b)
print(result)

common = a.intersection(b)
print(common)

diff = a.difference(b)     #Returns elements present in the first set but not in the second.
print(diff)

Sdiff = a.symmetric_difference(b) #Remove common elements
print(Sdiff)





