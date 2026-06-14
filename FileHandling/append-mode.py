
# file = open("FileHandling/data.txt", "a")
# file.write("\nNew line added")
# file.close()

lines = ["Line 1 \n", "Line 2 \n", "Line 3 \n"]

with open("FileHandling/data.txt", "a") as f:
    f.writelines(lines)