while True:
    try:
        if a == 'done':
            break
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        print ('Div result: ', a/b)

    except:
        print ('Input error')
