print ("Armstrong numbers upto 1000 ")

for x in range(100,1000):
    sum=0
    temp=x
    while temp > 0:
        d=temp%10
        sum=sum+d**3
        temp=temp//10
        if x == sum:
            print(x)