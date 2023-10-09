'''
    https://semengo.furg.br/images/2006/06.pdf
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

# Importa CSV
# ignora as primeiras linhas com dados de informacao
# Importa somente as primeiras 4 colunas dos dados porque a quinta eh resultado do delimitador extra
df = pd.read_csv('dados_A834_H_2013-01-01_2023-01-01.csv', skiprows=10, delimiter=';', usecols=range(4), dtype=str)

# Renomeia campos para facilitar a analise de dados
df.columns = ['date', 'hour', 'direction', 'speed']

# Remove dados null no campo speed
df = df[~df['speed'].isnull()] 

# Dividi o texto de date em dados separados
df[['year', 'month', 'day']] = df['date'].str.split('-', expand=True) 
# df['date/hour'] = df['date'].str.replace('-', '') + df['hour']

# Trato os valores da coluna 'speed' e 'direction', tranformando em uma float
df['speed'] = df['speed'].str.replace(',', '.').astype(float)
df['direction'] = df['direction'].astype(float)

# Remover zeros
df = df[~(df['speed'] == 0.0)] 

# Dados do aerogerador AGW 147 / 4.2
# https://static.weg.net/medias/downloadcenter/h67/ha7/WEG-aerogeradores-agw-147-4.2-50077448-catalogo-portugues.pdf

df_pot = pd.DataFrame()
df_pot['ms'] = np.arange(0.0, 20.0, 0.1)

p = [0.0, 0.0, 0.0, 0.0, 250.0, 510.0, 1000.0, 1500.0, 2500.0, 3500.0, 4000.0, 4180.0, 4200.0, 4200.0, 4200.0, 4200.0, 4200.0, 4200.0, 4200.0, 4200.0]
p_serie = pd.Series([np.nan]*100)
for i, element in enumerate(p):
    p_serie[i * 5] = element

p_serie = p_serie.interpolate()

plt.figure('Curva de Potência')
plt.title('Curva de Potência (AGW 147 / 4.2) (kW/m/s)')
plt.plot(np.linspace(0.0, 20.0, len(p_serie)), p_serie)
plt.ylabel("Potência (kW)")
plt.xlabel("Velocidade do Vento (m/s)")
plt.xticks(ticks=np.arange(0.0, 20.0 + 0.1, 1.0))
plt.yticks(ticks=np.arange(0.0, 4500.0, 500.0))
plt.grid()
plt.savefig('./4/curva_potencia_aerogerador_agw147.png')

year_to_analize = df['year'].unique().tolist()
# year_to_analize.remove('2013')
# year_to_analize.remove('2019') # Ano com muitos 0
# year_to_analize.remove('2020') # Ano com muitos 0
# year_to_analize.remove('2023') # Ano incompleto
# year_to_analize = ['2022']
for year in year_to_analize:

    # Filtros adicionais
    YEAR = year
    MONTH = '03'
    df_analise = df
    # print(len(df_analise))
    df_analise = df_analise[df_analise['year'] == YEAR]
    # print(len(df_analise))
    # df_analise = df_analise[df_analise['month'] == MONTH]
    # print(len(df_analise))

    ############## Direcao ##############
    # plt.figure(f'Histograma de direção do vento (°) do ventos - {year}')

    # bins_number = 100
    # bins = np.linspace(0.0, 2 * np.pi, bins_number + 1)
    # n, _, _ = plt.hist(df_analise['direction'], bins_number, density=True)
    # plt.clf()

    # ax = plt.subplot(111, polar=True)
    # width = 2 * np.pi / bins_number
    # bars = ax.bar(bins[:bins_number], n, width=width, bottom=0.0)

    # for r, bar in zip(n, bars):
    #     bar.set_facecolor(plt.cm.jet(r / max(n)))
    #     bar.set_alpha(0.8)

    # plt.title(f'Histograma de direção do vento (°) do ventos - {year}')
    # plt.savefig(f'./4/{year}_direction')
    # plt.close()
    

    ############## Velocidade ##############
    y = df_analise['speed'].to_list()
    x = np.linspace(0.0, 20.0, 100)

    plt.figure(f'Histograma de vel.(m/s) dos ventos - {year}')
    plt.title(f'Histograma de vel.(m/s) dos ventos - {year}')
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Ocorrências')

    # Histograma em barras
    n, _, _ = plt.hist(y, bins=x, histtype='step', density=False,
                       label='Histograma em barras',
                       weights=np.ones(len(y)) / len(y))    
    
    # Histograme em linhas
    density = stats.gaussian_kde(y)
    d_x = density(x)
    d_x /= sum(d_x)
    plt.plot(x, d_x, scaley=False, label='Histograma em densidade')
    plt.xticks(ticks=np.arange(0.0, math.ceil(max(x)) + 0.1, 1.0))

    # Treinamento e aquisicao dos paramentros e Weibull
    shape, loc, scale = stats.weibull_min.fit(y, floc=0)

    # Criacao de curva a partir dos parametros de Weibull
    y_w = stats.weibull_min.pdf(x, c=shape, loc=loc, scale=scale)
    y_w /= sum(y_w)
    plt.plot(x, y_w, label=f'Distr. Weibull(forma={shape:1.3f}, escala={scale:1.3f})')

    # Finalizacao de plot
    plt.legend(loc='best')
    plt.grid()
    plt.savefig(f'./4/{year}_speed')

    # Resultados
    print(f"#### {year} ####")
    print(f"Param. Weibull: Shape: {shape:.3f}, Scale: {scale:.3f}")
    potencia_df = sum(d_x * p_serie)
    print(f"Pot. Dados:   {potencia_df:.3f}")
    # h = (math.e / scale) ** ((- x / scale) ** 2.0)
    print(f'Pot. Weibull: {sum(y_w * p_serie)}')
    print()
