n = int(input())
for i in range(n):
  x, y = input().split()
  x, y = int(x), int(y)
  if y == 0:
    print('divisao impossivel')
  else:
    val = (x / y)
    print(val)