# Searching String Part
'''
if would like to searching index number at some of word or senteces
'''
s = 'Python Language'
print(s.find('g'))
print(s.find('P'))

'''
formula : s.find(sub[, start[, end]])
sub is for the caracter or the part of text will be searching
start is for the index start range for searching
end is for the index end range for searching
'''

s1 = 'INFORMATIKA'
print(s1.find('I', 1, 10))

# Get the character from the index
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[-1]) # obtain the character from the right)
