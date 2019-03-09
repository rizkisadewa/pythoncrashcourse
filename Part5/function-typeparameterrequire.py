# function which is requiring a certain parameter which is delcared
# => parameter function with int type
def addition(a: int, b: int) -> int:
    return a + b

# ** call function addition() with parameter int
print(addition(2,3))

# ** call function addition() with parameter float
print(addition(2.00, 3.00))

# => parameter function with float type
def multiple(a: float, b:float) -> float:
    return a * b

# ** call function multiple() with parameter float
print(multiple(2.00,3.00))

# ** call function multiple() with parameter int
print(multiple(5,4))
