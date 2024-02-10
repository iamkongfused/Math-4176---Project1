"""
Project #1:
This program computes x^b mod n using the Square and Multiply Algorithm.
x = input plaintext number

Authors: Caleb Kong, Harrison Bui, Tide Adewunmi, Bobby Whitehead
Date: February 10, 2024
Course: MATH 4176
"""

n = 31313
b = 4913
x1 = 2388  # cat
x2 = 1371  # dog


def sq_n_mul(x):
    """
    Convert exponent 'b' to a binary string
    minus the first 2 characters
    """
    binary_rep = bin(b)[2:]
    
    """
    Start z at 1
    """
    z = 1
    
    """
    Execute algorithm for as many characters in binary string
    of exponent
    """
    COL_LENGTH = 20
    print("i\t| b_i\t| %s| z" % ("".ljust(COL_LENGTH)))
    print("--------------------------------------------")
    print("\t|    \t| %s| 1" % ("".ljust(COL_LENGTH)))
    for i in range(len(binary_rep)):
        prev_z = z
        rowIndexDisplay = len(binary_rep) - 1 - i
        if binary_rep[i] == '1':
            """
            if there is a 1 do the following equation:
                z_(n+1) = z^2 * our number mod n
            """
            z = (z ** 2 * x) % n
            # prints result in a row for this step
            computation = (str(prev_z) + "^2 * " + str(x)).ljust(COL_LENGTH)
            print("%d\t| 1\t\t| %s| %d" % (rowIndexDisplay, computation, z))
        else:
            """
            otherwise there must be a zero by rules of
            binary strings and we do this formula:
                z_(n+1) = z^2
            """
            z = (z ** 2) % n
            # prints result in a row for this step
            computation = (str(prev_z) + "^2").ljust(COL_LENGTH)
            print("%d\t| 0\t\t| %s| %d" % (rowIndexDisplay, computation, z))
    return z


# prints result for 1st problem
print("x = 2388 (for DOG):")
ans = sq_n_mul(x1)
print("%d^%d mod %d = %d" % (x1, b, n, ans))

print()
print()

# prints results for 2nd problem
print("x = 1371 (for CAT):")
ans = sq_n_mul(x2)
print("%d^%d mod %d = %d" % (x2, b, n, ans))
