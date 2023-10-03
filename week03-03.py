# print ('1x1=1 1x2=2 1x3=3 1x4=4 1x5=5 1x6=6')
# print ('2x1=2 2x2=4 2x3=6 2x4=8 2x5=10 2x6=12')
for i in range(1,10):
  for j in range(1,10):
    print(i, 'x', j, '=',i*j, sep='', end=' ')
  print()