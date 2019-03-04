# Splitting String
s = "Python,Perl,PHP,Ruby"
for item in s.split(','):
    print(item)

'''
Prototype:
S.split(sep=None, maxplit=-1 -> list of strings)
'''

# we can split the string below
s1 = "one two three four five"
print(s1.split())
print(s1.split(maxsplit=2))

# we can also implement split() for another character
list = "Java;C;C++;C#"
print(list.split(';'))
