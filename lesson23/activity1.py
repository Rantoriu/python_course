n=int(input("how many elements in the array? "))
arr=[]
i=1
while i<=n:
    x=int(input("enter a number: "))
    arr.append(x)
    i+=1
res=0
for x in arr:
    res=res^x
print(res,"is odd occuring number in array",arr)