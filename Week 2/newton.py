while True:
    number = float(input ('Newton Enter number: '))
    ans = number
    iter = 1
    while abs(ans**2 - number) > 0.01:
        ans = ans - (((ans**2) - number)/(2*ans))
        iter += 1
    print (ans, ans**2, iter)
