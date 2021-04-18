# K - матрица жесткости системы, 3*3
# q - вектор-столбец наеизвестных узловых перемещений
# f - вектор-столбец известных внешних нагрузок

# Зададим жёсткости элементов и внешнее усилие
EF1 = 1
EF2 = 2
EF3 = 3
С1 = 2
F = 10

# Определим вектор усилий
f=[0, 0,0,0,F]

# Составим матрицы жесткости
K1 = [[EF1,-EF1],
      [-EF1, EF1]]
K2 = [[EF2,-EF2],
      [-EF2, EF2]]
K3 = [[EF3,-EF3],
      [-EF3, EF3]]
K4 = [[С1,-С1],
      [-С1, С1]]

# Определим общую матрицу

K = [[K4[0][0], K4[0][1], 0, 0, 0],
     [K4[1][0], K4[1][1] + K1[0][0], K1[0][1], 0, 0],
     [0, K1[1][0], K1[1][1] + K2[0][0], K2[0][1], 0],
     [0,0, K2[1][0], K2[1][1]+K3[0][0], K3[0][1]],
     [0,0,0, K3[1][0], K3[1][1]]
]

print('Матрица жёсткости системы: ', K)

# Введем граничные условия (левый конец балки закреплён)

K[0][0] = 1
for i in range (1,len(K)):
    K[0][i] = 0
for i in range(1, len(K)):
    K[i][0]=0

print('Матрица жёсткости системы c ГУ: ', K)


from matan import inverse_matrix

invK = inverse_matrix(K)

print('Матрица инвертированная: ', invK)

q = []
for i in range(len(f)):
    u = 0
    for j in range(len(f)):
        u += invK[i][j] * f[j]
    q.append(u)
print('u', q)

# Апроксимации

from Aproximation import approximation

def per(q1, q2):
    print("0   ", approximation(0, [q1, q2], 1))
    print("0.25", approximation(0.25, [q1, q2], 1))
    print("0.5 ", approximation(0.5, [q1, q2], 1))
    print("0.75", approximation(0.75, [q1, q2], 1))
    print("1   ", approximation(1, [q1, q2], 1))

from Aproximation import force_approximation

def force(q1, q2, EF):
    print("0   ", force_approximation(0, [q1, q2], 1, EF))
    print("0.25", force_approximation(0.25, [q1, q2], 1, EF))
    print("0.5 ", force_approximation(0.5, [q1, q2], 1, EF))
    print("0.75", force_approximation(0.75, [q1, q2], 1, EF))
    print("1   ", force_approximation(1, [q1, q2], 1, EF))

# Перемещения элементов и усилия

for i in range(0,4):
    print('Перемещения элемента', i)
    per(q[i],q[i+1])

EF_all = [С1, EF1, EF2, EF3]

for i in range(0,4):
    print('Усилия для элемента', i)
    force(q[i],q[i+1],EF_all[i])