i = int(input())
a = (i /365)
rm = (i % 365)
m = (rm / 30)
d = (rm % 30)
print(int(a),'ano(s)')
print(int(m),'mes(es)')
print(int(d),'dia(s)')