s = "abcdabcd"
d = {} 
for c in s:
  if c in d:
    d[c] = d[c] + 1
  else:
    d[c] = 1
  print('現在讀到的字母', c, "字母變成", d)