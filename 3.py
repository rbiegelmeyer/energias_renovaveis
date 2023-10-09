import numpy as np
import matplotlib.pyplot as plt

# Eixo X - Temperaturas
t = np.arange(-10.0, 85.0, 0.1)
# T = 20.0 #  800 W/m2
T = 25.0 #  1000 W/m2

# Tensao
VOC = 49.0 # 1000 W/m2
# VOC = 46.3 #  800 W/m2
v = VOC * (1.0 - 0.0034*(t - T))

# Corrente
ISC = 13.85 # 1000 W/m2
# ISC = 11.17 #  800 W/m2
i = ISC * (1.0 + 0.0005*(t - T))

# Potencia
p = v * i


# Tensao X Tempo
plt.figure("Tensão (V) x Temperatura (°C)")
plt.title("Tensão (V) x Temperatura (°C)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Tensão (V)")
plt.plot(t, v, c='blue')
plt.xticks(ticks=np.arange(0.0, 85.0, 10.0))
plt.xlim(-5.0, 85.0)
# plt.yticks(ticks=np.arange(28.0, 43.0, 1.0))
# plt.ylim(27.0, 43.0)
plt.grid()

plt.savefig('./3/tensao')

# Corrente X Tempo
plt.figure("Corrente (A) x Temperatura (°C)")
plt.title("Corrente (A) x Temperatura (°C)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Corrente (A)")
plt.plot(t, i, c='gold')
plt.xticks(ticks=np.arange(0.0, 85.0, 10.0))
plt.xlim(-5.0, 85.0)
# plt.yticks(ticks=np.arange(13.0, 15.0, 0.1))
# plt.ylim(13.55, 14.48)
plt.grid()

plt.savefig('./3/corrente')

# Potencia x Temperatura
plt.figure("Potência (W) x Temperatura (°C)")
plt.title("Potência (W) x Temperatura (°C)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Potência (W)")
plt.plot(t, p, c='darkorange')
plt.xticks(ticks=np.arange(0.0, 85.0, 10.0))
plt.xlim(-5.0, 85.0)
# plt.yticks(ticks=np.arange(13.5, 15.0, 0.1))
# plt.ylim(13.5, 14.6)
plt.grid()

plt.savefig('./3/potencia')





# plt.show()