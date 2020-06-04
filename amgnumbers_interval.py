N=int(input("Enter the limit:"))
if N<0:
    print("Invalid input")
else:
    print("Armstrong number between 0 and",N,"are:")
    for N in range(1,N+1):
        sum=0
        i=N
        l=len(str(N))
        while i>0:
            sum=sum+((i%10)**l)
            i//=10
        if N==sum:
            print(N,end=" ")
