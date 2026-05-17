num1 = float(input("Enter 1st number here: "));
num2 = float(input("Enter 2nd number here: "));
num3 = float(input("Enter 3rd number here: "));

if (num1 > num2) and (num1 > num3):
    print("Largest number:",num1);
elif (num2 > num1) and (num2 > num3):
    print("Largest number:", num2);
else:
    print("Largest number:", num3);