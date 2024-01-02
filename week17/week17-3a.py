a, c, b = input().split()
a = int(a)
b = int(b)
if c=='+': ans = a+b
if c=='-': ans = a-b
if c=='*': ans = a*b
if c=='/': ans = a//b
print(ans, end='')