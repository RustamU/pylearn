s = 'azcbobobegghaklbobob'
bobcounter = 0
for i in range(len(s)):
    if s[i:i+3] == "bob":
        bobcounter += 1

print ('Number of times bob occurs is: ', bobcounter)
