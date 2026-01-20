def iseven(n):
    if(n ^ 1==n+1):
        return True
    else:
        return False
n=int(input("Enter your number: "))
if iseven(n):
    print("even number")
else:
    print("odd number")