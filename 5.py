import math
import numpy as np

pop = 123151
residuo = 264.6 # kg por habitante
mi = residuo / 1000.0 * pop # toneladas de residuo ano

pop = 69458
mi = 0.832 * pop * 365 / 1000

k = 0.6
l0 = 141.0

t = np.arange(0.0, 10.0, 1.0)
print(t)

q = k * l0 * mi * math.e **(-k * t)

print(q)