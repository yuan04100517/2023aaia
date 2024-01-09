a = int(input())
if a%400==0: ans = 1
elif a%100==0: ans = 0
elif a%4==0: ans = 1
else: ans = 0
if ans==1: print(a, 'is a leap year.')
else: print(a, 'is not a leap year.')