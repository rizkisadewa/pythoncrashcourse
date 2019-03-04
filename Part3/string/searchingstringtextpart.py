# Searching String in certain part
data = ['Akhmad Koysim', 'Akhmad Ilman', 'Anis Yuliana Phasya', 'Rizki Sadewa', 'Muhammad Ilman', 'Muhammad Rozak', 'Muhammad Yusuf']

# Searching the String which is contain the name startwith 'Muhammad'
for name in data:
    if name.startswith('Muhammad'):
        print(name)

print()

# Searching the String whcih is contain the name with endswith 'Ilmand'
for name in data:
    if name.endswith('Ilman'):
        print(name)

'''
Prototype:
s.startswith(prefix[, start[, end]]) -> bool
means the method will return True if the string s started substring prefix, otherwise return false.
start and end will spcify the start or end position of the prefix that will be checked
'''

nama = 'Muhammad Ilman'
print(nama.startswith('Muhammad'))
print(nama.startswith('Akmal'))

print(nama.startswith('uha', 1, 4)) # will return True due to uha still contained in string of nama variable from index number 1 until 4

'''
Prototype:
s.endswith(prefix[, start[, end]]) -> bool
means the method will return True if the string s started substring suffix, otherwise return false.
start and end will spcify the start or end position of the suffix that will be checked
'''

print(nama.endswith('Ilman')) # will return True
print(nama.endswith('n'))  # will return True
print(nama.endswith('mad', 0, 8)) # will return True
