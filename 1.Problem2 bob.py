s = 'bobob' 
numBobs = 0
str = 0

for char in s:
    if char == 'b' :
        if str == 'bo':
            str += char
            numBobs += 1
            str = char
        else:
            str = char
    elif char == 'o':
        if str == 'b':
            str += char
        else:
            str = char
    else:
        str = char
print (numBobs) 