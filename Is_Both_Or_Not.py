a = int(input())
if (a%5==0 and a%11!=0) or (a%5!=0 and a%11==0):
    print("ONE")
elif (a%5==0 and a%11==0):
    print("BOTH")
else:
    print("NONE")
