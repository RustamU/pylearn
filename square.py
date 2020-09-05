number = float(input ('Enter number: '))
ans = number
iter = 1
while abs(ans**2 - number) > 0.0001:
    ans = (ans + number/ans)/2
    iter += 1
print (ans, ans**2, iter)
