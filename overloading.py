# Overloading

class aritmatika:
    def tambah(self, *daftarnilai):
        total = 0
        for i in daftarnilai:
            total += 1
        return total

# Make an object from class aritmatika
obj = aritmatika()

# call method addition with 2 parameter
print(obj.tambah(2, 3))

# call method addition with 3 parameter
print(obj.tambah(2, 3, 4))

# call method addition with 4 parameter
print(obj.tambah(2, 3, 4, 8))

# call method addition with 5 parameter
print(obj.tambah(2, 3, 4, 8, 9))

'''
Python does not allow to have two or more methods with the same name, therefore
we need to make the Overloading method for the alternative
'''
