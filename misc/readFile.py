fh = open ('test.txt', 'r')
data =[]

for new in fh:
    if new != '\n':
        addIt = new[:-1].split(',')
        data.append(addIt)

fh.close()

print (data)
