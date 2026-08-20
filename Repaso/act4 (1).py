import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

np.random.seed(33)

# ── DATOS ──────────────────────────────────────────────────────────────────────
fechas  = [datetime(2024, 1, 1) + timedelta(weeks=i) for i in range(26)]
visitas = np.random.randint(8000, 20000, 26)

fuentes    = ['Búsqueda', 'Directo', 'Redes\nSociales', 'Email', 'Referidos']
colores_f  = ['#4C72B0','#55A868','#DD8452','#C44E52','#9467BD']
proporciones = np.array([38, 25, 20, 10, 7])

categorias  = ['Blog', 'Producto', 'Landing', 'Soporte', 'Checkout']
rebote      = np.array([75, 45, 60, 55, 30]) + np.random.uniform(-5, 5, 5)
permanencia = np.array([3.5, 5.2, 2.8, 4.1, 6.3]) + np.random.uniform(-0.3, 0.3, 5)
tam_burbuja = np.array([5000, 8000, 4000, 3000, 6000])
colores_disp = ['#4C72B0','#DD8452','#55A868','#C44E52','#9467BD']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis de Tráfico Web', fontsize=16, fontweight='bold')

# ── GRÁFICO 1: Evolución de visitas ──────────────────────────────────────────
ax1 = axes[0, 0]
ax1.plot(fechas, visitas, color='#4C72B0', linewidth=2, marker='o', markersize=4)
ax1.fill_between(fechas, visitas, alpha=0.12, color='#4C72B0')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax1.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=3))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=30, ha='right')
ax1.set_title('Visitas semanales (H1 2024)', fontsize=13)
ax1.set_ylabel('Visitas')
ax1.grid(linestyle='--', alpha=0.4)
ax1.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 2: Desglose de fuentes (circular) ────────────────────────────────
ax2 = axes[0, 1]
wedges, texts, autotexts = ax2.pie(
    proporciones, labels=fuentes, colors=colores_f,
    autopct='%1.1f%%', startangle=140,
    wedgeprops=dict(edgecolor='white', linewidth=1.5))
for t in autotexts:
    t.set_fontsize(9)
    t.set_fontweight('bold')
ax2.set_title('Fuentes de tráfico (%)', fontsize=13)

# ── GRÁFICO 3: Barras apiladas por fuente ────────────────────────────────────
ax3 = axes[1, 0]
semanas   = [f'S{i+1}' for i in range(0, 26, 5)]
idx_sem   = list(range(0, 26, 5))
bottom    = np.zeros(len(idx_sem))
for fuente, color, prop in zip(fuentes, colores_f, proporciones):
    vals = visitas[idx_sem] * prop / 100
    ax3.bar(semanas, vals, bottom=bottom, label=fuente.replace('\n',' '),
            color=color, edgecolor='white', linewidth=0.6)
    bottom += vals
ax3.set_title('Visitas por fuente (muestra quincenal)', fontsize=13)
ax3.set_ylabel('Visitas')
ax3.legend(loc='upper right', fontsize=8, ncol=2)
ax3.grid(axis='y', linestyle='--', alpha=0.4)
ax3.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 4: Tasa de rebote vs. tiempo de permanencia ──────────────────────
ax4 = axes[1, 1]
scatter = ax4.scatter(permanencia, rebote, s=tam_burbuja/20,
                      c=colores_disp, alpha=0.8, edgecolors='white', linewidths=1.5)
for i, cat in enumerate(categorias):
    ax4.annotate(cat, (permanencia[i], rebote[i]),
                 textcoords='offset points', xytext=(8, 4), fontsize=10)
ax4.set_xlabel('Tiempo medio de permanencia (min)')
ax4.set_ylabel('Tasa de rebote (%)')
ax4.set_title('Rebote vs. permanencia por categoría', fontsize=13)
ax4.grid(linestyle='--', alpha=0.4)
ax4.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('ej4_trafico.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico guardado como ej4_trafico.png")
