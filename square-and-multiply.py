



n = 31313
b = 4913

x1 = 2388 #cat
x2 = 1371 #dog

def sq_n_mul(num):
    binary_rep = bin(num)[2:]
    z = 1
    for i in len(binary_rep):
        if binary_rep[i] == '1':
            z = (z**2 * num) % n
        else:
            z = (z ** 2) % n
            
