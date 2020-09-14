myDict = {}
with open ('src.txt') as fhandle:
    for i in (fhandle.read()):
        myDict[i] = myDict.get (i,0) + 1
print (myDict)
fhandle.close()
