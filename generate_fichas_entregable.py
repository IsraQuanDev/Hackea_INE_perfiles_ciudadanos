import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
DESKTOP_DIR = r"C:\Users\52477\Desktop"
ENTREGABLES_DIR = os.path.join(DESKTOP_DIR, "Entregables_HackeaINE_Reto1")
FICHAS_SUBDIR = os.path.join(ENTREGABLES_DIR, "03_Fichas_Individuales_PNG")
os.makedirs(ENTREGABLES_DIR, exist_ok=True)
os.makedirs(FICHAS_SUBDIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "processed_data", "dashboard_data_pro.json"), "r", encoding="utf-8") as f:
    DATA = json.load(f)

PERFILES = DATA["perfiles"]

def draw_profile_card_on_ax(ax, p):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Fondo general de la tarjeta
    bg = patches.FancyBboxPatch((1, 1), 98, 98, boxstyle="round,pad=0.8,rounding_size=3",
                                facecolor="#FFFFFF", edgecolor=p["color"], linewidth=2.5)
    ax.add_patch(bg)

    # Cabecera de color del perfil
    hdr = patches.FancyBboxPatch((1, 78), 98, 21, boxstyle="round,pad=0.4,rounding_size=2.5",
                                 facecolor=p["color"], edgecolor="none")
    ax.add_patch(hdr)

    ax.text(4, 93, f"PERFIL {p['id']}  |  {p['badge'].upper()}", color="#FDEBD0", fontsize=8.5, fontweight="bold")
    ax.text(4, 86, f"{p['name']}", color="white", fontsize=13.5, fontweight="bold")
    ax.text(4, 80.5, p["subtitle"][:75] + ("..." if len(p["subtitle"]) > 75 else ""), color="#F2F4F4", fontsize=8, style="italic")

    # Badge derecho de peso en Lista Nominal
    badge_bg = patches.FancyBboxPatch((75, 81), 21, 15, boxstyle="round,pad=0.3,rounding_size=2",
                                      facecolor="#17202A", edgecolor="white", linewidth=1, alpha=0.35)
    ax.add_patch(badge_bg)
    ax.text(85.5, 90, f"{p['pct_padron']}%", color="white", fontsize=14, fontweight="bold", ha="center")
    ax.text(85.5, 83.5, f"{p['ln_2024']/1e6:.2f}M Electores", color="#F9E79F", fontsize=7.5, fontweight="bold", ha="center")

    # Cinta de 6 KPIs Demográficos y Electorales
    kpis = [
        ("VOTO 2024", f"{p['tasa_2024']}%"),
        ("MEDIA PRES.", f"{p['tasa_pres']}%"),
        ("MEDIA INTER.", f"{p['tasa_inter']}%"),
        ("BRECHA", f"{p['brecha_pres_inter']} pp"),
        ("EDAD MEDIA", f"{p['edad_media']} años"),
        ("MUJERES / ESC.", f"{p['pct_mujer']}% | {p['escolaridad_est']}a")
    ]
    for i, (k_lbl, k_val) in enumerate(kpis):
        x0 = 3.5 + i * 15.6
        kbox = patches.FancyBboxPatch((x0, 64), 14.4, 11.5, boxstyle="round,pad=0.2,rounding_size=1.5",
                                      facecolor="#F8F9F9", edgecolor="#D5DBDB", linewidth=1)
        ax.add_patch(kbox)
        ax.text(x0 + 7.2, 71, k_val, color=p["color"], fontsize=9.5, fontweight="bold", ha="center")
        ax.text(x0 + 7.2, 66, k_lbl, color="#566573", fontsize=6.5, fontweight="bold", ha="center")

    # Bloque Narrativo
    ax.text(4, 59.5, "DIAGNÓSTICO SOCIODEMOGRÁFICO Y COMPORTAMIENTO CCPC (2009–2024):", color=p["color"], fontsize=8.5, fontweight="bold")
    
    # Wrap narrative text manually
    words = p["narrative"].split()
    lines, curr = [], ""
    for w in words:
        if len(curr + " " + w) <= 92:
            curr = (curr + " " + w).strip()
        else:
            lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)
    for idx_l, line in enumerate(lines[:4]):
        ax.text(4, 55.2 - idx_l * 3.8, line, color="#2C3E50", fontsize=8)

    # Mini barra visual de composición Urbana / Mixta / Rural y Género
    ax.text(4, 38.5, f"ENTORNO TERRITORIAL: Urbano {p['pct_urbano']}%  |  Mixto {p['pct_mixto']}%  |  Rural {p['pct_rural']}%     •     TENDENCIA 2009–2024: {p['tendencia_lp']:+.2f} pp",
            color="#34495E", fontsize=7.8, fontweight="bold")

    # Bloque de Estrategia Focalizada INE
    strat_box = patches.FancyBboxPatch((3.5, 4), 93, 31.5, boxstyle="round,pad=0.3,rounding_size=2",
                                       facecolor="#F5EEF8", edgecolor=p["color"], linewidth=1.5)
    ax.add_patch(strat_box)
    ax.text(5.5, 31.5, f"ESTRATEGIA INE / ENCIVICA: {p['ine_strategy'].upper()}", color=p["color"], fontsize=8.8, fontweight="bold")

    y_curr = 26.8
    for act in p["ine_actions"]:
        w_act = act.split()
        a_lines, c_l = [], ""
        for w in w_act:
            if len(c_l + " " + w) <= 90:
                c_l = (c_l + " " + w).strip()
            else:
                a_lines.append(c_l)
                c_l = w
        if c_l:
            a_lines.append(c_l)
        for il, al in enumerate(a_lines[:2]):
            prefix = "• " if il == 0 else "   "
            ax.text(5.5, y_curr, prefix + al, color="#1C2833", fontsize=7.8)
            y_curr -= 3.5
        y_curr -= 0.8

    ax.text(5.5, 6.2, f"Canales prioritarios: {p['channels'][:95]}", color="#566573", fontsize=7.5, fontweight="bold")


def generate_fichas():
    # 1. Poster Maestro (Grid 3x2 con los 6 Perfiles en ultra alta resolución)
    fig = plt.figure(figsize=(20, 24), facecolor="#F4ECF7")
    fig.suptitle("HACKEA LA PARTICIPACIÓN: DATOS QUE CONSTRUYEN DEMOCRACIA (INE · DECEyEC · ENCÍVICA)\nReto 1: Infografía y Fichas Narrativas de los 6 Perfiles Ciudadanos de Participación (CCPC 2009–2024 · 54.87 Millones de Registros)",
                 fontsize=18, fontweight="bold", color="#4A154B", y=0.985)

    for idx, p in enumerate(PERFILES):
        ax = fig.add_subplot(3, 2, idx + 1)
        draw_profile_card_on_ax(ax, p)

    plt.tight_layout(rect=[0.01, 0.01, 0.99, 0.955])

    poster_png_desktop = os.path.join(DESKTOP_DIR, "Fichas_Perfiles_Reto1_HackeaINE.png")
    poster_png_folder = os.path.join(ENTREGABLES_DIR, "03_Fichas_Perfiles_Infografia_Reto1_INE.png")
    fig.savefig(poster_png_desktop, dpi=220, facecolor=fig.get_facecolor())
    fig.savefig(poster_png_folder, dpi=220, facecolor=fig.get_facecolor())
    plt.close(fig)

    # 2. PDF multipágina de alta resolución (Página 1 = Poster Maestro + Páginas 2 a 7 = Fichas Individuales + Gráfica Ciclo)
    pdf_desktop = os.path.join(DESKTOP_DIR, "Fichas_Perfiles_Reto1_HackeaINE.pdf")
    pdf_folder = os.path.join(ENTREGABLES_DIR, "03_Fichas_Perfiles_Infografia_Reto1_INE.pdf")

    for pdf_path in [pdf_desktop, pdf_folder]:
        with PdfPages(pdf_path) as pdf:
            # Página 1: Poster de los 6 perfiles
            fig_p = plt.figure(figsize=(16, 20), facecolor="#F4ECF7")
            fig_p.suptitle("HACKEA LA PARTICIPACIÓN (INE) — FICHAS DE PERFILES CIUDADANOS CCPC 2009–2024",
                           fontsize=15, fontweight="bold", color="#4A154B", y=0.98)
            for idx, p in enumerate(PERFILES):
                ax = fig_p.add_subplot(3, 2, idx + 1)
                draw_profile_card_on_ax(ax, p)
            plt.tight_layout(rect=[0.01, 0.01, 0.99, 0.95])
            pdf.savefig(fig_p, facecolor=fig_p.get_facecolor())
            plt.close(fig_p)

            # Páginas individuales por cada perfil y guardar PNG individual
            for p in PERFILES:
                fig_ind = plt.figure(figsize=(11, 7.5), facecolor="white")
                ax_ind = fig_ind.add_subplot(111)
                draw_profile_card_on_ax(ax_ind, p)
                plt.tight_layout()
                pdf.savefig(fig_ind, facecolor="white")
                if pdf_path == pdf_folder:
                    ind_png = os.path.join(FICHAS_SUBDIR, f"Ficha_{p['id']}_{p['name'].replace(' ', '_')}.png")
                    fig_ind.savefig(ind_png, dpi=220, facecolor="white")
                plt.close(fig_ind)

    print("Fichas de Perfil (PNG y PDF de alta resolución) generadas con éxito en Desktop!")

if __name__ == "__main__":
    generate_fichas()
