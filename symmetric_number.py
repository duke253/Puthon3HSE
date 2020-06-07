a = int(input())
a1 = a % 10
a2 = a // 10 % 10
a3 = a // 100 % 10
a4 = a // 1000
k = 10**((a1 - a4) + (a2 - a3))
print(k)
