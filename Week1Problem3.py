s = 'abcdefabcdefghz'
longestSubstring = s[0]
tempSubstring = ''
for i in range (len(s)-1):
    if s[i+1] >= s[i]:
        tempSubstring += s[i+1]
        i += 1
        if len(tempSubstring) > len(longestSubstring):
            longestSubstring = tempSubstring
        print (longestSubstring)
    else:
        tempSubstring = s[i+1]
        i += 1
        print (longestSubstring)
print (longestSubstring)
