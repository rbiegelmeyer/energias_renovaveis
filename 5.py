import math
import numpy as np

t = np.arange(0.0, 20.0, 1.0)
# print(t)


# pop_ini = 123151.0
# pop = pop_ini * (1.0 + 0.01 * (t))
# residuo = 264.6 # kg por habitante
# mi = residuo / 1000.0 * pop # toneladas de residuo ano

pop_ini = 90000.0
pop = pop_ini * (1.0 + 0.01) ** t

# Producao de RSU por dia em toneladas por toda populacao
mi = 0.75 * pop / 1000 * (33.75/67.5)
mi_ano = mi * 365
print(mi_ano)

k = 0.8
l0 = 170.0


q = k * l0 * mi_ano * math.e **(-k * t)

for x_0, x_1, x_2, x_3 in zip(t, pop, mi, q):
    print(f'{int(x_0 + 1):2} - {round(x_1):6} - {round(x_2, 3): .3f} - {round(x_3,3):11.3f}')


