s = 'abc'
i=0
currentStr = s[0]
longestStr= s[0]

for char in s:
    if s[i] <= s[i +1]:
        currentStr += s[i + 1]
        i += 1
        if i == len(s) - 1:
            if len(currentStr) >= len(longestStr):
                longestStr = currentStr
            break
    else:
        longestStr = currentStr
        currentStr = s[i +1]
        i += 1
        if i == len(s) - 1:
            if len(currentStr) >= len(longestStr):
                longestStr = currentStr
            break
print("longest string is:", longestStr)
