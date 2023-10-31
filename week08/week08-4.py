a= 1234
ans = 0 
while a>0:
  ans = ans *10 + a%10
  print('現在的a是', a, '撥出來的皮a%10是', a%10, '現在的 ans 就變成', ans)
  a = a // 10