h=int(input("enter your largest number:"))
s=int(input("enter your smallest number:"))
while(s):
    snew=s
    s=h%s
    h=snew
print("Hcf is:",h)
