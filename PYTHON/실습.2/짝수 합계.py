a = 1
sum = 0

while a != 0:
    a = int(input("짝수면 더해줌: "))
    if a % 2 == 0:
        sum = sum + a

print(sum)