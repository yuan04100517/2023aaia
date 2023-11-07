a = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
N = len(a)
print(a)
for i in range(N-1):
  if a[i+1] < a[i]:
    a[i], a[i+1] = a[i+1], a[i]
print(a)