a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    print(a)
elif c >= b and a <= c:
    print(c)
elif a <= b and b >= c:
    print(b)