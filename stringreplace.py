# String Replace Method

s = 'Python Perl Python PHP Ruby Ruby'
print('Before replaced : ', s)
s = s.replace('Ruby', 'Python')
print('After replaced : ', s)

'''
Formula :
s.replace(old, new[, count])
old is the paramenter word that will be replaced
new is the parameter the changer
count is the total word that will be replaced
'''

s = 'Ruby Ruby Ruby Ruby Ruby'
s = s.replace('Ruby', 'Python', 3)
print(s)
