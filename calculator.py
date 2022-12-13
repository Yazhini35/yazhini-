def calculator(a,b,c):
    if c=="add":
        add=a+b
        print("Addition of given number:",add)
    elif c=="sub":
        sub=a-b
        print("Subtract of given number:",sub)
    elif c=="mul":
        mul=a*b
        print("Multiple of given number:",mul)
    elif c=="div":
        div=a/b
        print("Division of given number:",div)
    return
z=(input("Enter your option:"))
x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
print(calculator(x,y,z))

