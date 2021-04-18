def scalar_product(a, b):
    return a[0] * b[0] + a[1] * b[1]


def approximation(x, u, l):
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    return scalar_product(N, u)

# Для расчета сил

def force_approximation(x, u, l, EF):
    N1prime = -1 / l
    N2prime = 1 / l
    N = [N1prime, N2prime]
    return scalar_product(N, u) * EF