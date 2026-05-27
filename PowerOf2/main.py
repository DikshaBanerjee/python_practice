nrange = int(input("Enter the range here: "));

result = list(map(lambda x: 2**x, range(nrange+1)));
#print(result)

for i in range(nrange + 1):
    print("The value 2 raised to power", i, "is", result[i]);
