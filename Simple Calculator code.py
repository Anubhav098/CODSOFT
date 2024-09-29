#python program to make a simple calculator for two numbers
print("Enter the two numbers below:")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
ch=0
while ch<5:
    print("Calculator Menu:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    ch=int(input("Enter your Choice:"))
    if ch==1:
        c=a+b
        print("Sum:",c)
    elif ch==2:
        c=a-b
        print("Difference:",c)
    elif ch==3:
        c=a*b
        print("Product:",c)
    elif ch==4:
        c=a/b
        print("Quotient:",c)
    elif ch==5:
        break
    else:
        print("Invalid Choice")
