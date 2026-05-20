num = int(input("Enter the number here: "));
fact = 1;

if num < 0:
    print("For nagetive value factorial doesn't exist");
elif num == 0:
    print("Factorial of zero is ",1);
else:
    for i in range(1, num+1):
        fact = fact * i;
print("Factorial of the number is", fact);


# using recursion-----

def factorial(a):
    if a == 0:
        return 1
    else: 
        return (a)*factorial(a-1);
    
num2 = int(input("Enter the number here: "));  
result = factorial(num2);
print("Factorial of the number is", result);  

