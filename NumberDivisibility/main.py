#using for loop---------

num = 13

print("The numbers are divisible by",num);
for i in range(1,100+1):
    if i % num == 0:
        print(i);

# using lambda and filter-----
r = [26,87,91,49,52,67,39]

result = list(filter(lambda x : x % 13 == 0 ,r));
print("The numbers divisible by 13 are:", result);