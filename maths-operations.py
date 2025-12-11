a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c = a + b
d = a - b
e = a * b

if b != 0:
    f = a / b
else:
    print("Undefined")

print("\nAddition: ",c)
print("Substraction: ",d)
print("Multiplication: ",e)
print("Division: ",f)
