s = 'azcbobobegghakl'
longestSubstring = s[0]
tempSubstring = s[0]
for i in range (len(s)-1):
    if s[i+1] >= s[i]:
        tempSubstring += s[i+1]
        i += 1
        if len(tempSubstring) > len(longestSubstring):
            longestSubstring = tempSubstring
    else:
        tempSubstring = s[i+1]
        i += 1
print ('Longest substring in alphabetical order is: ', longestSubstring)
