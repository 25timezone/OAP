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

# Перемещения
def per(q1, q2):
    print("0   ", approximation(0, [q1, q2], 1))
    print("0.25", approximation(0.25, [q1, q2], 1))
    print("0.5 ", approximation(0.5, [q1, q2], 1))
    print("0.75", approximation(0.75, [q1, q2], 1))
    print("1   ", approximation(1, [q1, q2], 1))

# Силы
def force(q1, q2, EF):
    print("0   ", force_approximation(0, [q1, q2], 1, EF))
    print("0.25", force_approximation(0.25, [q1, q2], 1, EF))
    print("0.5 ", force_approximation(0.5, [q1, q2], 1, EF))
    print("0.75", force_approximation(0.75, [q1, q2], 1, EF))
    print("1   ", force_approximation(1, [q1, q2], 1, EF))