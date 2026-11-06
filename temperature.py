def c_to_f(num):
    f = (num* 9/5) + 32
    return f
# print(c_to_f(40))

def f_to_c(num):
    c = (num - 32) * 5/9
    return c
# print(f_to_c(212))

def c_to_k(num):
    k = num + 273.15
    return k
# print(c_to_k(50))

def k_to_c(num):
    c = num - 273.15
    return c

def f_to_k(num):
    k = (num - 32)* 5/9 + 273.15
    return k
# print(f_to_k(40))

def k_to_f(num):
    f = (num - 273.15) * 9/5 + 32
    return f