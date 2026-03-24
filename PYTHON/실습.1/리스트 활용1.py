steps = [8000, 12000, 5000, 9000, 11000, 3000, 15000]
j = int(0)
for i in steps:
    if i >= 10000:
        j = j + 1
        
per = (j / 7) * 100
print(j, per,"%")