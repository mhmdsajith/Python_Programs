import math
num=int(input("Enter the value:"))
sum=0
odd=1
for i in range(1,num+1):
    sum=sum+(pow(odd,2)/pow(odd,3))
    odd+=2
print("sum of the series is :",sum)
    
