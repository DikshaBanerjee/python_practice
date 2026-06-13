item = ["orange", "apple", "banana", "orange"]

print(type(item))
# print(len(item))
# print(item[-1])
# print(item[0:3])
# print(item[:2])
# print(item[1:])

item[1] = "grapes"
item.append("apple")
item.insert(0,"kiwi")

more_items = ["mango", "pear"]
item.extend(more_items)

# item.remove("orange")
# item.pop(1)
# item.clear()

position = item.index("orange")
print(position)
print(item.count("orange"))
new_items = item.copy()
item.reverse()
print(new_items)
print("apple" in item)

print(item)

number = [6, 3, 2, 9, 12, 99, 45]
# number.sort()
number.sort(reverse=True)

print(number)

