# using  a third variable

x = 12;
y = 13;

temp = x;
x = y;
y = temp;
print("Swap value of x is:", x);
print("Swap value of y is:", y);

# without using a third variable

a = 12;
b = 13;

a,b = b,a;
print("Swap value of a is:", a);
print("Swap value of b is:", b);