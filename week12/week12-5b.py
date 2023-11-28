from binascii import b2a_base64
a = 1500000000
b = 2000000000
c = a%b
print(a, b, c)
while c!=0:
  a = b
  b = c
  c = a%b
  print(a, b, c)
print(b)