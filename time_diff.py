h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
hts1 = h1 * 3600
mts1 = m1 * 60
tsec1 = hts1 + mts1 + s1
hts2 = h2 * 3600
mts2 = m2 * 60
tsec2 = hts2 + mts2 + s2
tdiff = tsec2 - tsec1
print(tdiff)
