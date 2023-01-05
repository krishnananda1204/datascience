def perfect_number(n):
    sum = 0
    for x in range(1,n):
        if n % x == 0:
            sum = sum + x
    return sum == n
a= int(input("Enter a number: "))

print(perfect_number(a))
