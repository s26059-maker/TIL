n, cost = input().split()
n = int(n)
cost = int(cost)
Cost = n * cost

if Cost >= 100000: 
    Cost = Cost * 0.90
print(Cost)