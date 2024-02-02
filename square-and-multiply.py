





x1 = 2388 #cat
x2 = 1371 #dog

def sq_n_mul(num):
    n = 31313
    b = 4913
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
    Do algorithm for as many characters in binary string
    of exponent
    """
    for i in len(binary_rep):
        if binary_rep[i] == '1':
            """
            if there is a 1 do the following equation:
                z_(n+1) = z^2 * our number mod n
            """
            z = (z**2 * num) % n
        else:
            """
            otherwise there must be a zero by rules of
            binary strings and we do this formula:
                z_(n+1) = z^2
            """
            z = (z ** 2) % n
    return n
            
