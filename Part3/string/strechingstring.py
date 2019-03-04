# Streching The String

'''
we would like to show the data in table which is contain column and line
'''
data = [
('P01','Spidol',7500,10),
('P02','Papan Tulis',8500,20),
('P03','Pencil',1500,8)
]

for line in data:
    print('%s %s %s %s' %
            (line[0].ljust(5),
             line[1].ljust(15),
             str(line[2]).ljust(9),
             str(line[3]).ljust(30))
            )

# Ljust / left justify
print('Python'.ljust(10))

# using a character
print('Python'.ljust(10, '$'))

# Rjust / right justify
print('Python'.rjust(10))

# using a character
print('Python'.rjust(10, '$'))

# Center
print('Python'.center(10))
