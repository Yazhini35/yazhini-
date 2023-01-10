a=int(input("enter the value"))
b=int(input("enter the value"))
print("which method did you want")
print("1-addition")
print("2-subraction")
print("3-division")
print("4-multiplication")
method=int(input("enter the method number"))
if(method==1):
    add=a+b
    print("addition",add)
elif(method==2):
    sub=a-b
    print("subraction",sub)
elif(method==3):
    div=a//b
    print("division",div)
elif(method==4):
    multi=a*b
    print("multiplication",multi)
else:
    print("the default method")
