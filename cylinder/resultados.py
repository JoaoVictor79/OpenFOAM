import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos dados do OpenFOAM
df = pd.read_csv("dados_poiseuille.csv")

# Definição da solução numérica
r = df['arc_length'] - 0.01
U_numerico = df['U_Magnitude']

# Parâmetros relevantes do modelo
Vm = 0.1            # Velocidade média [m/s]
D = 7               # Diâmetro do tubo [mm]
R = 0.001 * D / 2   # Raio do tubo [m]

# Definição da função analítica
def U_analitica(r):
    U = 2*Vm
    return U * (1 - (r / R)**2)

# Cálculo da solução analítica para os mesmos pontos
U_teorico = U_analitica(r)

# Cálculo do erro absoluto e relativo
erro_abs = abs(U_numerico - U_teorico)
erro_rel = 100 * abs((U_numerico - U_teorico) / U_teorico)

# Plotagem dos dados numéricos e analíticos
plt.figure()
plt.plot(1000 * r, U_numerico, 'b-', label='Solução numérica')
plt.plot(1000 * r, U_teorico, 'r--', label='Solução analítica')
plt.xlabel('Raio (mm)', fontsize=14)
plt.ylabel('Velocidade (m/s)', fontsize=14)
plt.xlim([-5,5])
plt.ylim([0,0.22])
plt.xticks(np.arange(-5, 5, 0.5))
plt.title('Comparação entre Solução Numérica e Analítica', fontsize=20, pad=30)
plt.grid(True)
plt.legend()

# Plotagem dos erros absoluto e relativo
fig, ax1 = plt.subplots()
cor1 = 'tab:blue'
ax1.set_xlabel('Raio (mm)', fontsize=14)
ax1.set_ylabel('Erro absoluto (mm/s)', fontsize=14, color=cor1)
ax1.plot(1000 * r, 1000 * erro_abs, color=cor1, label='Erro absoluto')
ax1.tick_params(axis='y', labelcolor=cor1)
mask = (r > -0.0034) & (r < 0.0034) # Máscara aplicada para evitar divisão por zero no cálculo do erro relativo
ax2 = ax1.twinx()
cor2 = 'tab:red'
ax2.set_ylabel('Erro relativo (%)', fontsize=14, color=cor2)
ax2.plot(1000 * r[mask], erro_rel[mask], color=cor2, linestyle='--', label='Erro relativo')
ax2.tick_params(axis='y', labelcolor=cor2)
plt.title('Comparação entre Solução Numérica e Analítica', fontsize=20, pad=30)
plt.grid(True)
plt.show()
