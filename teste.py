import matplotlib.pyplot as plt

# Dados de exemplo (substitua pelos seus próprios dados)
temperaturas = [25, 30, 35, 40, 45]  # Temperaturas em graus Celsius
correntes = [5.0, 4.8, 4.6, 4.4, 4.2]  # Correntes correspondentes em A (Amperes)
tensoes = [40.0, 39.5, 38.9, 38.3, 37.7]  # Tensões correspondentes em V (Volts)

# Crie um gráfico de tensão (V) versus corrente (I) para diferentes temperaturas
plt.figure(figsize=(8, 6))
plt.plot(correntes, tensoes, marker='o', linestyle='-', markersize=8, label='Curvas de IV')
plt.xlabel('Corrente (A)')
plt.ylabel('Tensão (V)')
plt.title('Curvas de Tensão-Corrente em Função da Temperatura')
plt.legend(title='Temperatura (°C)')
plt.xticks(correntes)
plt.grid(True)

# Adicione as temperaturas ao eixo x como rótulos
plt.gca().set_xticklabels(temperaturas)

# Mostrar o gráfico
plt.show()