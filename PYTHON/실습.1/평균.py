a = int(84)
b = int(50)
c = int(78)
d = int(60)
e = int(98)  

average = (a + b + c + d + e) / 5
average = int(average)

print("평균 = ", average)   

list = [a, b, c, d, e]
j = int(0)
for i in list:
    if i > average:
        j = j + 1
print("평균 이상인 수 = ", j)

for i in list:
    if i >= 90:
        print(f"{i} = A")
    elif i >= 80 and i < 90:
        print(f"{i} = B")
    elif i >= 70 and i < 80:
        print(f"{i} = C")
    elif i >= 60 and i < 70:
        print(f"{i} = D")
else:
    print(f"{i} = E")

    