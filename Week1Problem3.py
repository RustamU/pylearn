s = 'azcbobobegghakl'
longestSubstring = s[0]
for i in range (len(s)-1):
    while s[i+1] > s[i]:
        if i == len(s):
            break
        longestSubstring += s[i+1]
        print (longestSubstring)
