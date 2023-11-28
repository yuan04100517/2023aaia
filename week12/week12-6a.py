def gcd(a, b):
  print(a, b)
  if a==0: return b
  if b==0: return a
  return ged(b, a%b)

a = 1500000000
b = 2000000000
print( gcd(a, b) )