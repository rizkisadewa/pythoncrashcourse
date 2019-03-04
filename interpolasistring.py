# Interpolasi String

# Mengimpor modil string
import string

# membuat string yang mengandung nama variable
s = string.Template("$x and $y")

# show the string
print(s.substitute({'x': 10, 'y':20}))
