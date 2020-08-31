number = int(input('Enter number: '))
ans = 0
while ans**3 < number:
    ans += 1
if ans ** 3 > number:
    print ('Not a perfect root')
elif ans ** 3 == number:
        print ('3 root =', ans)
