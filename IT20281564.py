def recusive(n):
    if n==1:
        return 1
    else:
        return (n-1) + recusive(n - 1)

while True:#Run untill user input -1
    n=int(input("Enter number : "))
    if n==-1:
        break
    else:
        print (recusive(n))
