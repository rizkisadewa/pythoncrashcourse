# from Chararacter to ASCII using ord()
print(ord('A'))

# from ASCII to Character using chr()
print(chr(65))

# all the ASCII code
for i in range(0, 256):
    print('%d => %c'%(i, chr(i)))
