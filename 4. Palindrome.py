def pallindrome(j):
    return j==j[::1]
j="MALAYALAM"
ans=pallindrome(j)
if ans:
    print("yes")
else:
    print("no")
