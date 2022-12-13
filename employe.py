def employee(a,b):
    if a=="A":
       c=b*0.05
    elif a=="B":
       c=b*0.1
    else:
       print("Invalid")
    if b<10000:
       d=b*0.02
    else:
       d=0
       tot=b+c+d
    
    print("Bonus=",c)
    print("Total to be paid:",tot)
    return
x=str(input("Enter the grade of the employee:"))
y=int(input("Enter the employee salary:"))
print(employee(x,y))


