# Keyword Argument Parameter
def fract(**kwargs):
    from fractions import Fraction
    a = kwargs['numerator']
    b = kwargs['denominator']
    c = Fraction(a, b)
    return float(c)

# implementation of the above function
x = fract(numerator=1, denominator=2)
print(x)


'''
** will return the dictionary object , which is means there is a pairing of key and value
kwargs :
{'numerator':1, 'denominator':2}
'''

# to proof the **kwargs will return the dictionary
def test(**kwargs):
    print(kwargs)

test(one=10, two=20, three=30, four=40)
test(name='Rizki', age=25, salarypermonth=130000000)

'''
The above function will always return a dictionary object
'''
