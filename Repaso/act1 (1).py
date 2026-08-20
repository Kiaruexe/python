import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

np.random.seed(42)

# ── DATOS ──────────────────────────────────────────────────────────────────────
regiones = ['España', 'Francia', 'Italia', 'Alemania', 'Portugal', 'Países Bajos']
tasas    = np.random.randint(50, 400, size=len(regiones))

fechas  = [datetime(2020, 3, 1) + timedelta(days=i) for i in range(180)]
casos   = {'España':    np.cumsum(np.random.poisson(500,  180)),
           'Francia':   np.cumsum(np.random.poisson(600,  180)),
           'Italia':    np.cumsum(np.random.poisson(450,  180)),
           'Alemania':  np.cumsum(np.random.poisson(400,  180))}
muertes = {k: (v * np.random.uniform(0.01, 0.03, 180)).astype(int)
           for k, v in casos.items()}

colores = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Análisis de Datos de Salud', fontsize=16, fontweight='bold', y=1.01)

# ── GRÁFICO 1: Tasa de incidencia por región ───────────────────────────────────
ax1 = axes[0]
bars = ax1.bar(regiones, tasas, color=colores[:len(regiones)], width=0.6, edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, tasas):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.set_title('Tasa de incidencia por región\n(casos por 100 000 hab.)', fontsize=13)
ax1.set_ylabel('Tasa de incidencia')
ax1.set_ylim(0, max(tasas) * 1.2)
ax1.tick_params(axis='x', rotation=30)
ax1.grid(axis='y', linestyle='--', alpha=0.5)
ax1.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 2: Evolución de casos acumulados ───────────────────────────────────
ax2 = axes[1]
for (pais, vals), color in zip(casos.items(), colores):
    ax2.plot(fechas, vals, label=pais, color=color, linewidth=2)
    ax2.fill_between(fechas, vals, alpha=0.08, color=color)

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax2.xaxis.set_major_locator(mdates.MonthLocator())
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=30, ha='right')
ax2.set_title('Evolución de casos acumulados\n(COVID-19 simulado, 2020)', fontsize=13)
ax2.set_ylabel('Casos acumulados')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(linestyle='--', alpha=0.5)
ax2.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('ej1_salud.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico guardado como ej1_salud.png")
