import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")
ART_DIR = r"C:\Users\52477\.gemini\antigravity\brain\60e0a364-5707-46f9-80a9-29e34ccdae7c"
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

import json
with open(os.path.join(OUT_DIR, "dashboard_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

def save_both(fig, filename):
    p1 = os.path.join(FIG_DIR, filename)
    p2 = os.path.join(ART_DIR, filename)
    fig.savefig(p1, dpi=180, bbox_inches='tight', facecolor='white')
    fig.savefig(p2, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

# 1. Gráfica de Ciclo de Vida Electoral por Edad Exacta y Sexo (2024 vs 2021)
df_age24 = pd.DataFrame(data['edad_exacta_2024'])
df_age21 = pd.DataFrame(data['edad_exacta_2021'])

fig, ax = plt.subplots(figsize=(11, 5.5))
h24 = df_age24[df_age24['SEXO'] == 0]
m24 = df_age24[df_age24['SEXO'] == 1]
h21 = df_age21[df_age21['SEXO'] == 0]
m21 = df_age21[df_age21['SEXO'] == 1]

ax.plot(m24['EDAD'], m24['TASA'], color='#6C3483', linewidth=2.8, label='Mujeres 2024 (Presidencial)')
ax.plot(h24['EDAD'], h24['TASA'], color='#1F618D', linewidth=2.8, label='Hombres 2024 (Presidencial)')
ax.plot(m21['EDAD'], m21['TASA'], color='#AF7AC5', linewidth=1.8, linestyle='--', label='Mujeres 2021 (Intermedia)')
ax.plot(h21['EDAD'], h21['TASA'], color='#5499C7', linewidth=1.8, linestyle='--', label='Hombres 2021 (Intermedia)')

ax.axvspan(20, 34, color='#FADBD8', alpha=0.35, label='Valle de Abstencionismo Joven (20-34 años)')
ax.annotate('Primer voto (18 años):\n55.1% Mujeres / 48.9% Hombres', xy=(18, 55.1), xytext=(21, 64),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.2), fontsize=9.5, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5EEF8', edgecolor='#6C3483'))
ax.annotate('Mínimo en Hombres (26 años): 37.8%\nBrecha de género llega a +12.5 pp', xy=(26, 37.8), xytext=(30, 29),
            arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.2), fontsize=9.5, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDEDEC', edgecolor='#C0392B'))
ax.annotate('Cúspide Cívica (65-72 años):\n>72% de participación', xy=(68, 73.5), xytext=(52, 78),
            arrowprops=dict(arrowstyle='->', color='#1E8449', lw=1.2), fontsize=9.5, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EAFAF1', edgecolor='#1E8449'))

ax.set_title('Curva del Ciclo de Vida Electoral en México (CCPC 2021 vs 2024 por Edad Exacta y Sexo)', fontsize=13, fontweight='bold', pad=12, color='#2C3E50')
ax.set_xlabel('Edad cumplida el día de la elección (años)', fontsize=11, fontweight='bold')
ax.set_ylabel('Tasa de Participación Ciudadana (%)', fontsize=11, fontweight='bold')
ax.set_xlim(18, 90)
ax.set_ylim(22, 85)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', frameon=True, facecolor='white', fontsize=9.5)
save_both(fig, "fig1_curva_edad_sexo.png")

# 2. Gráfica de los 6 Perfiles Ciudadanos (Mapa de Segmentación y Tamaño de Padrón)
perfiles = data['perfiles']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), gridspec_kw={'width_ratios': [1.2, 1.3]})

names = [f"{p['id']}: {p['name']}" for p in perfiles]
colors = [p['color'] for p in perfiles]
tasa_pres = [p['tasa_pres'] for p in perfiles]
tasa_inter = [p['tasa_inter'] for p in perfiles]
ln_mill = [p['ln_2024'] / 1e6 for p in perfiles]

y_pos = np.arange(len(perfiles))
bar_h = 0.36
ax1.barh(y_pos - bar_h/2, tasa_pres, height=bar_h, color='#5B2C6F', alpha=0.9, label='Elección Presidencial (Media 12-18-24)')
ax1.barh(y_pos + bar_h/2, tasa_inter, height=bar_h, color='#D4AC0D', alpha=0.85, label='Elección Intermedia (Media 09-15-21)')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(names, fontsize=9.5, fontweight='bold')
ax1.invert_yaxis()
ax1.set_xlabel('Tasa de Participación (%)', fontsize=10.5, fontweight='bold')
ax1.set_title('Participación Presidencial vs Intermedia por Perfil', fontsize=11.5, fontweight='bold', color='#2C3E50')
ax1.set_xlim(0, 82)
for i, (tp, ti) in enumerate(zip(tasa_pres, tasa_inter)):
    ax1.text(tp + 0.8, i - bar_h/2, f"{tp:.1f}%", va='center', fontsize=8.5, fontweight='bold', color='#5B2C6F')
    ax1.text(ti + 0.8, i + bar_h/2, f"{ti:.1f}%", va='center', fontsize=8.5, fontweight='bold', color='#9A7D0A')
ax1.grid(True, axis='x', linestyle=':', alpha=0.6)
ax1.legend(loc='lower right', fontsize=8.5)

# Scatter en ax2: Edad Media vs Brecha Presidencial-Intermedia (Tamaño = Lista Nominal 2024)
for p in perfiles:
    ax2.scatter(p['edad_media'], p['tasa_2024'], s=p['pct_padron']*42, color=p['color'], alpha=0.82, edgecolors='black', linewidth=1.5)
    ax2.annotate(f"{p['id']} ({p['pct_padron']}% LN)\n{p['tasa_2024']}% en 2024",
                 (p['edad_media'], p['tasa_2024']),
                 xytext=(0, 14 if p['id'] not in ['P5', 'P4'] else -26),
                 textcoords='offset points', ha='center', fontsize=8.5, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=p['color'], alpha=0.9))

ax2.set_title('Mapa Sociodemográfico: Edad Media vs Participación 2024\n(Tamaño de burbuja = Peso en Lista Nominal)', fontsize=11.5, fontweight='bold', color='#2C3E50')
ax2.set_xlabel('Edad Promedio del Perfil (años)', fontsize=10.5, fontweight='bold')
ax2.set_ylabel('Tasa de Participación 2024 (%)', fontsize=10.5, fontweight='bold')
ax2.set_xlim(22, 70)
ax2.set_ylim(35, 76)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
save_both(fig, "fig2_perfiles_clustering.png")

# 3. Evolución Longitudinal 2009-2024 de los 6 Perfiles Ciudadanos
fig, ax = plt.subplots(figsize=(11, 5.2))
years_str = ['2009', '2012', '2015', '2018', '2021', '2024']
for p in perfiles:
    vals = [p['evolucion_anual'][y] for y in years_str]
    ax.plot(years_str, vals, marker='o', linewidth=2.5, markersize=7, color=p['color'], label=f"{p['id']}: {p['name']} ({p['pct_padron']}%)")

ax.set_title('Trayectoria Longitudinal de Participación por Perfil Ciudadano (CCPC 2009–2024)', fontsize=12.5, fontweight='bold', color='#2C3E50', pad=12)
ax.set_xlabel('Año de Proceso Electoral Federal (Intermedias: 2009, 2015, 2021 | Presidenciales: 2012, 2018, 2024)', fontsize=10.5, fontweight='bold')
ax.set_ylabel('Tasa de Participación (%)', fontsize=10.5, fontweight='bold')
ax.set_ylim(28, 75)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), frameon=True, fontsize=9.5)
plt.tight_layout()
save_both(fig, "fig3_evolucion_perfiles_2009_2024.png")

print("Figuras generadas correctamente!")
