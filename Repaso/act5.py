import numpy as np
import matplotlib.pyplot as plt

np.random.seed(15)

# ── DATOS ──────────────────────────────────────────────────────────────────────
meses      = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
categorias = ['Electrónica', 'Ropa', 'Hogar', 'Alimentación']
colores_c  = ['#4C72B0','#DD8452','#55A868','#C44E52']

ventas = {
    'Electrónica':  np.array([45, 42, 50, 55, 60, 58, 62, 65, 70, 75, 95, 120]),
    'Ropa':         np.array([30, 28, 35, 40, 50, 55, 45, 42, 48, 52, 65, 80]),
    'Hogar':        np.array([25, 22, 30, 35, 38, 40, 35, 33, 38, 42, 55, 70]),
    'Alimentación': np.array([60, 58, 62, 60, 65, 63, 68, 66, 64, 67, 72, 85]),
}

campañas = ['SEO', 'SEM', 'Email\nMktg', 'Instagram', 'Facebook', 'TV', 'Prensa', 'Afiliados']
inversion = np.array([15, 25, 10, 20, 18, 40, 30, 12])
ingresos  = np.array([45, 60, 35, 55, 40, 70, 45, 38])
roi       = ((ingresos - inversion) / inversion * 100).astype(int)
colores_r = ['#55A868' if r >= 100 else '#DD8452' if r >= 50 else '#C44E52' for r in roi]

x = np.arange(len(meses))

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Análisis de Ventas y Marketing', fontsize=16, fontweight='bold')

# ── GRÁFICO 1: Evolución de ventas por categoría ─────────────────────────────
ax1 = axes[0]
for (cat, vals), color in zip(ventas.items(), colores_c):
    ax1.plot(x, vals, label=cat, color=color, linewidth=2, marker='o', markersize=4)

# Marcar mes pico de cada categoría
for (cat, vals), color in zip(ventas.items(), colores_c):
    pico = np.argmax(vals)
    ax1.annotate(f'{vals[pico]}k', xy=(pico, vals[pico]),
                 xytext=(0, 10), textcoords='offset points',
                 ha='center', fontsize=8, color=color, fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels(meses)
ax1.set_title('Ventas mensuales por categoría\n(miles €, 2024)', fontsize=13)
ax1.set_ylabel('Ventas (miles €)')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(linestyle='--', alpha=0.4)
ax1.spines[['top', 'right']].set_visible(False)

# ── GRÁFICO 2: ROI de campañas de marketing ───────────────────────────────────
ax2 = axes[1]
idx  = np.argsort(roi)
bars = ax2.barh([campañas[i].replace('\n',' ') for i in idx],
                [roi[i] for i in idx],
                color=[colores_r[i] for i in idx],
                edgecolor='white', linewidth=0.6)
for bar, val in zip(bars, [roi[i] for i in idx]):
    ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
             f'{val}%', va='center', fontsize=9, fontweight='bold')

ax2.axvline(100, color='gray', linestyle='--', linewidth=1, label='ROI 100%')
ax2.set_title('ROI por campaña de marketing\n(% retorno sobre inversión)', fontsize=13)
ax2.set_xlabel('ROI (%)')
ax2.set_xlim(0, max(roi) * 1.25)
ax2.legend(fontsize=9)
ax2.grid(axis='x', linestyle='--', alpha=0.4)
ax2.spines[['top', 'right']].set_visible(False)

# Leyenda de colores ROI
from matplotlib.patches import Patch
leyenda = [Patch(color='#55A868', label='ROI ≥ 100%'),
           Patch(color='#DD8452', label='ROI 50-99%'),
           Patch(color='#C44E52', label='ROI < 50%')]
ax2.legend(handles=leyenda, loc='lower right', fontsize=8)

plt.tight_layout()
plt.savefig('ej5_ventas.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico guardado como ej5_ventas.png")
