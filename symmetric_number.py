a = int(input())
a1 = a // 1000
a2 = a // 100 % 10
a3 = a // 10 % 10
a4 = a % 10
a12 = a1 * 10 + a2
a34 = a4 * 10 + a3
k = a12 - a34 + 1
print(a1, a2, a3, a4)
print(a12, a34)
print(k)
