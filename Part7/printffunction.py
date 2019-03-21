# Printf Function
import sys

# declaration function of printf()
def printf(format, *args):
    sys.stdout.write(format % args)

# instance
printf('Nama : %s, Usia : %d', 'Ahmad', 45)
print()
printf('%.2f', 123.456789)
print()

# option 2
def printf2(format, *args):
    print(format % args, end='')

printf2('Nama : %s, Usia : %d', 'Rizki', 25)
print()
printf2('%.2f', 123.456789)
