tsec = int(input())
h = tsec // 3600 % 24
m1 = tsec // 60 % 60 // 10
m2 = tsec // 60 % 60 % 10
s1 = tsec % 60 // 10
s2 = tsec % 60 % 10
print(h, ":", m1, m2, ":", s1, s2, sep="")
