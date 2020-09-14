myDict = {}
with open ('c:\\project\\6.00.1x\Week 3\\src.txt') as fhandle:
    for i in (fhandle.read()):
        myDict[i] = myDict.get (i,0) + 1
print (myDict)
fhandle.close()
