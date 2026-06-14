numbers = [1,2,3,4,5,6]

squared = []
for i in numbers:
    squared.append(i*i);
print(squared)

SquaredComp = [i*i for i in numbers]
print(SquaredComp)

EvenNumber = [i for i in numbers if i % 2 == 0]  #Filtering data----
print(EvenNumber)

names = [" Diksha ", " Sita", "Ram  "]

CleanNames = [i.strip().lower() for i in names]   #Transforming data----
print(CleanNames)

items = ["mobile", "TV", "computer"]
prices = [10000, 15000, 45000]

ItemsDict = {item : price for item, price in zip(items, prices)}
print(ItemsDict)

scores = {"maths" : 80, "english" : 45, "hindi" : 76, "science" : 69}
passed = {k : v for k, v in scores.items() if v >= 70}
print(passed) 

values = [ 1, 2, 2, 3, 3, 3, 4, 5, 5]
squr = {i*i for i in values}    #Set comprehensions remove duplicates automatically.
print(squr)

pairs = [(x, y) for x in [1,2] for y in [3,4]]
print(pairs)   #Nested Comprehensions

PairsLoop = []
for x in [1,2]:   #Normal nested loop
    for y in [3,4]:
        PairsLoop.append((x, y));

print(PairsLoop)


