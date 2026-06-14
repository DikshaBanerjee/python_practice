# import os;

# if os.path.exists("FileHandling/data.txt"):  #Checking File Existence
#     print("File exists")

# file = open("FileHandling/robot.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("FileHandling/robot.txt", "r")
# content = file.readline()    # read one line at a time
# print(content)
# file.close()

file = open("FileHandling/robot.txt", "r")
content = file.readlines()    # Reads all lines and returns them as a list.
print(content)
file.close()


