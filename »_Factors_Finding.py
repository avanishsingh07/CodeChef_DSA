n = int(input("Enter the number"))
l = []
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count +1
        l.append(i)

print(count)
for j in l:
    print(j, end = " ")
