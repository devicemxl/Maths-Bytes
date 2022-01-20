
# Set Theory: Cartesian Product Routine
def CartesianProduct(a,b,c):
    for C in range(len(b)):
        for D in range(len(a)):
            c.append(tuple(b[C]+a[D]))
    return c
