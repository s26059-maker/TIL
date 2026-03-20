a = input()
a = int(a)
hundred = a // 100
ten = ((a - hundred * 100) // 10)
one = (a - hundred * 100 - ten * 10)
print(hundred, ten, one)