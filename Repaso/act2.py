import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

np.random.seed(7)

# ── DATOS ──────────────────────────────────────────────────────────────────────
fechas = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(90)]
base   = np.random.poisson(200, 90)

# Picos de actividad en eventos concretos
eventos = {20: ('Lanzamiento\nproducto', 600),
           45: ('Viral\nChallenge',      900),
           70: ('Controversia',          750)}
for dia, (_, extra) in eventos.items():
    base[dia - 2 : dia + 3] += np.linspace(50, extra, 5).astype(int)

temas  = ['IA y tecnología', 'Política', 'Deportes', 'Entretenimiento',
          'Ciencia', 'Economía', 'Cultura', 'Salud']
conteos = np.array([3800, 3200, 2900, 2600, 1800, 1600, 1200, 900])
colores_bar = ['#4C72B0','#DD8452','#55A868','#C44E52',
               '#9467BD','#8C564B','#E377C2','#7F7F7F']

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Análisis de Datos de Redes Sociales', fontsize=16, fontweight='bold')

# ── GRÁFICO 1: Actividad de publicaciones ─────────────────────────────────────
ax1 = axes[0]
ax1.plot(fechas, base, color='#4C72B0', linewidth=1.8, zorder=2)
ax1.fill_between(fechas, base, alpha=0.15, color='#4C72B0')

for dia, (label, _) in eventos.items():
    ax1.axvline(fechas[dia], color='#C44E52', linestyle='--', linewidth=1.2, alpha=0.8)
    ax1.text(fechas[dia], base[dia] + 30, label, ha='center', fontsize=8,
             color='#C44E52', fontweight='bold')

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax1.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=30, ha='right')
ax1.set_title('Actividad de publicaciones\n(Q1 2024)', fontsize=13)
ax1.set_ylabel('Publicaciones / día')
ax1.grid(linestyle='--', alpha=0.4)
ax1.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 2: Distribución de temas ─────────────────────────────────────────
ax2 = axes[1]
idx   = np.argsort(conteos)
bars  = ax2.barh([temas[i] for i in idx], [conteos[i] for i in idx],
                  color=[colores_bar[i] for i in idx], edgecolor='white', linewidth=0.6)
for bar, val in zip(bars, [conteos[i] for i in idx]):
    ax2.text(bar.get_width() + 40, bar.get_y() + bar.get_height()/2,
             f'{val:,}', va='center', fontsize=9, fontweight='bold')
ax2.set_title('Temas más discutidos\n(menciones en Q1 2024)', fontsize=13)
ax2.set_xlabel('Número de menciones')
ax2.set_xlim(0, max(conteos) * 1.2)
ax2.grid(axis='x', linestyle='--', alpha=0.4)
ax2.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('ej2_redes.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico guardado como ej2_redes.png")
