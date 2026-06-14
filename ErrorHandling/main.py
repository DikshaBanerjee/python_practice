try:
    x = int(input("Enter a number here: "))
    y = 10/x;
except ValueError:
    print("Please Enter a valid number!");
except ZeroDivisionError:
    print("Division by Zero is not allowed.");
else:
    print(y);
finally:
    print("Thankyou....");

try:
    x = int("abc");
except:
    pass;     # The pass statement can be used when you want to ignore an error.

print("End....")

# age = -6
# if age < 0:
#     raise ValueError("Age can't be negative!");


