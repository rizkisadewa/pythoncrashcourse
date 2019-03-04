# String without new line
data = ['Python', 'Perl', 'Ruby', 'PHP']

for s in data:
    print(s, end=' ') # end contain space

for s in data:
    print(s) # end contain space

'''
in default, print() has parameter end which is still the same with \n
'''

# or we can use another character new line with another character

for s in data:
    print(s, end=' | ')
