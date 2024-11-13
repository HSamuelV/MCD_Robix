import sympy as sp
import numpy as np

# Define variáveis simbólicas para os parâmetros DH

d1, d2, d3 = sp.symbols('d1 d2 d3')
a1, a2, a3 = sp.symbols('a1 a2 a3')
alpha1, alpha2, alpha3 = sp.symbols('alpha1 alpha2 alpha3')
# theta1, theta2, theta3 = sp.symbols('theta1 theta2 theta3')
# l1, l2, l3, l4, l5, l6 = sp.symbols('l₁ l₂ l₃ l₄ l₅ l₆')

# VALORES NUMERICOS
theta1 = np.radians(-45)
theta2 = np.radians(-60)
theta3 = np.radians(-30)
l1 = 125
l2 = 95
l3 = 85
l4 = 15
l5 = 100
l6 = 10

# Função para criar a matriz de transformação simbólica a partir dos parâmetros DH
def dh_transform(theta, d, a, alpha):
    return sp.Matrix([
        [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha), sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
        [sp.sin(theta), sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
        [0, sp.sin(alpha), sp.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Define a tabela DH simbolicamente para cada elo do robô
# (os parâmetros podem ser ajustados conforme necessário para o robô)
dh_params = [
    {"theta": theta1, "d": 0, "a": l2, "alpha": sp.pi},  # Usando pi para simplificar
    {"theta": theta2, "d": 0, "a": l3, "alpha": -sp.pi/2},
    {"theta": theta3, "d": -l4, "a": l5, "alpha": 0}
]

# Calcula as matrizes de transformação simbólicas para cada elo
A1 = dh_transform(**dh_params[0])
A2 = dh_transform(**dh_params[1])
A3 = dh_transform(**dh_params[2])

# TRANSFORMAÇÕES DE FRAMES BASE E TOOL POINT
A4 = sp.Matrix([[1,0,0,    0],
                [0,1,0,   l6],
                [0,0,1,    0],
                [0,0,0,    1]])

A0 = sp.Matrix([[1,0,0,    0],
                [0,-1,0,    0],
                [0,0,-1,   l1],
                [0,0,0,    1]])

# Multiplica as matrizes para obter a transformação de 3 para 0

T_0_3 = A0 * A1 * A2 * A3 * A4
T_0_3 = T_0_3.applyfunc(lambda x: x.evalf(3))
#T_0_3 = A1 * A2 * A3
sp.pprint(T_0_3, use_unicode=True)

# Simplifica e remove valores pequenos aproximando-os a zero
# T_0_3 = sp.trigsimp(sp.nsimplify(T_0_3, tolerance=1e-4, rational=True))
# sp.pprint(T_0_3, use_unicode=True)
# # print("Matriz de transformação simbólica de 3 para 0 (T_0^3):\n")
# sp.pprint(T_0_3, use_unicode=True)

# subs = {
#     sp.sin(theta1): sp.Symbol('s1'), sp.cos(theta1): sp.Symbol('c1'),
#     sp.sin(theta2): sp.Symbol('s2'), sp.cos(theta2): sp.Symbol('c2'),
#     sp.sin(theta3): sp.Symbol('s3'), sp.cos(theta3): sp.Symbol('c3'),
#     sp.cos(theta1 - theta2):sp.Symbol('c₁-₂'),
#     sp.sin(theta1 - theta2):sp.Symbol('s₁-₂'),

# }

# # Aplica as substituições
# T_0_3_substituted = T_0_3.subs(subs)

# print("Matriz de transformação simbólica de 3 para 0 :                                                                           \n")
# sp.pprint(T_0_3_substituted, use_unicode=True)




