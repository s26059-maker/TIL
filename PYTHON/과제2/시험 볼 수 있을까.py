a, b = input().split()

a = int(a)

b = int(b)

if a == 1 and b >= 80:
    print("시험 응시 가능")

elif a == 0 and b >= 80:
    print("과제 미제출")

else:
    print("시험 응시 불가")
    
    
