a = 120
ans = 0
for i in range(1, a+1):
  if a%i==0:
    print( i, end=' ')
    ans += 1
print('有幾個整除? ', ans)