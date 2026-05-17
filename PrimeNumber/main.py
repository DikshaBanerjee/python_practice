num = int(input("Enter a number here: "));

if num == 1:
    print("Not a prime number.");
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
           print("Not a prime number.");
           break;
    else:
        print("A prime number.");

