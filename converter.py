def c_to_f(c):
    return c * 9 / 5 + 32

if __name__ == "__main__":
    print(c_to_f(25))  # expect 77.0

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_k(c):
    return c + 273.15
