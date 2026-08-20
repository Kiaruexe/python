import numpy as np
import matplotlib.pyplot as plt

np.random.seed(21)

# ── DATOS ──────────────────────────────────────────────────────────────────────
meses   = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
solar   = np.array([5,  8,  18, 28, 38, 45, 50, 47, 35, 22, 10,  4])
eolica  = np.array([30, 28, 25, 20, 18, 15, 12, 14, 18, 24, 28, 32])
fosil   = np.array([80, 75, 65, 55, 48, 42, 40, 43, 50, 58, 70, 78])
x       = np.arange(len(meses))

sectores  = ['Industrial', 'Residencial', 'Transporte', 'Comercial', 'Agricultura']
consumo   = np.array([420, 280, 310, 190, 95])
colores_s = ['#4C72B0','#DD8452','#55A868','#C44E52','#9467BD']

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Análisis de Consumo Energético', fontsize=16, fontweight='bold')

# ── GRÁFICO 1: Consumo por tipo de energía (área apilada) ─────────────────────
ax1 = axes[0]
ax1.stackplot(x, solar, eolica, fosil,
              labels=['Solar', 'Eólica', 'Fósil'],
              colors=['#FFD700', '#55A868', '#C44E52'],
              alpha=0.85)
ax1.set_xticks(x)
ax1.set_xticklabels(meses)
ax1.set_title('Consumo energético por tipo\n(TWh mensuales, 2024)', fontsize=13)
ax1.set_ylabel('Consumo (TWh)')
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.4)
ax1.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 2: Consumo por sector ─────────────────────────────────────────────
ax2 = axes[1]
bars = ax2.bar(sectores, consumo, color=colores_s, width=0.55,
               edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, consumo):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 6,
             f'{val} TWh', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.set_title('Consumo energético por sector\n(TWh anuales, 2024)', fontsize=13)
ax2.set_ylabel('Consumo (TWh)')
ax2.set_ylim(0, max(consumo) * 1.2)
ax2.grid(axis='y', linestyle='--', alpha=0.4)
ax2.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('ej3_energia.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico guardado como ej3_energia.png")
