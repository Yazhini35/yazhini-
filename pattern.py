def patt(a):
    for i in range(0,a):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=int(input("Enter the limit:"))
print(patt(n))
