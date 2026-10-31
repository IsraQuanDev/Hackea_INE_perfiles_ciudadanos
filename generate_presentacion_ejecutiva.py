import os
import json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas as rl_canvas

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
DESKTOP_DIR = r"C:\Users\52477\Desktop"
ENTREGABLES_DIR = os.path.join(DESKTOP_DIR, "Entregables_HackeaINE_Reto1")
os.makedirs(ENTREGABLES_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "processed_data", "dashboard_data_pro.json"), "r", encoding="utf-8") as f:
    DATA = json.load(f)

PERFILES = DATA["perfiles"]

def add_slide_header(slide, title_text, subtitle_text, slide_num):
    # Banner superior institucional INE
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    banner.fill.solid()
    banner.fill.fore_color.rgb = RGBColor(0x3B, 0x0D, 0x4A)
    banner.line.fill.background()

    tf = banner.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.45)
    tf.margin_top = Inches(0.14)
    p0 = tf.paragraphs[0]
    p0.text = title_text
    p0.font.size = Pt(22)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p0.font.name = "Arial"

    p1 = tf.add_paragraph()
    p1.text = subtitle_text
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = RGBColor(0xF7, 0xDC, 0x6F)
    p1.font.name = "Arial"

    # Número de diapositiva (X / 10)
    badge = slide.shapes.add_textbox(Inches(11.6), Inches(0.22), Inches(1.4), Inches(0.5))
    btf = badge.text_frame
    bp = btf.paragraphs[0]
    bp.text = f"Diapositiva {slide_num} / 10"
    bp.alignment = PP_ALIGN.RIGHT
    bp.font.size = Pt(10.5)
    bp.font.bold = True
    bp.font.color.rgb = RGBColor(0xE8, 0xDA, 0xEF)

def add_card(slide, left, top, width, height, title, bullets, border_hex="#5B2C6F", bg_hex="#F9F6FC"):
    r_b = int(border_hex[1:3], 16)
    g_b = int(border_hex[3:5], 16)
    b_b = int(border_hex[5:7], 16)

    r_bg = int(bg_hex[1:3], 16)
    g_bg = int(bg_hex[3:5], 16)
    b_bg = int(bg_hex[5:7], 16)

    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(r_bg, g_bg, b_bg)
    box.line.color.rgb = RGBColor(r_b, g_b, b_b)
    box.line.width = Pt(2)

    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.15)

    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(13.5)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(r_b, g_b, b_b)
    p0.font.name = "Arial"

    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.8)
        p.font.color.rgb = RGBColor(0x1E, 0x1B, 0x24)
        p.font.name = "Arial"
        p.space_before = Pt(4)

def build_pptx(pptx_paths):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==================== SLIDE 1: PORTADA ====================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = RGBColor(0x2E, 0x08, 0x36)
    bg1.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(5.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "INSTITUTO NACIONAL ELECTORAL (INE) · DECEyEC · ENCÍVICA 2024–2026"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xF7, 0xDC, 0x6F)

    p2 = tf1.add_paragraph()
    p2.text = "HACKEA LA PARTICIPACIÓN:\nDATOS QUE CONSTRUYEN DEMOCRACIA"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2.space_before = Pt(14)

    p3 = tf1.add_paragraph()
    p3.text = "Reto 1: Perfiles Ciudadanos de Participación (Segmentación Sociodemográfica CCPC 2009–2024)"
    p3.font.size = Pt(20)
    p3.font.bold = True
    p3.font.color.rgb = RGBColor(0xD7, 0xBD, 0xE2)
    p3.space_before = Pt(12)

    p4 = tf1.add_paragraph()
    p4.text = "54,872,712 Registros Censales Procesados  |  194 Archivos CSV Oficiales  |  98.33M en Lista Nominal 2024  |  2,477 Municipios\nDashboard en Vivo: https://israquandev.github.io/Hackea_INE_perfiles_ciudadanos/  |  Diapositiva 1 / 10"
    p4.font.size = Pt(13)
    p4.font.color.rgb = RGBColor(0xA9, 0xDF, 0xBF)
    p4.space_before = Pt(28)

    # ==================== SLIDE 2: EL RETO Y COBERTURA CENSAL ====================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "1. El Problema Público y Nuestro Alcance Censal (2009–2024)",
                     "¿Qué tipos de ciudadanía existen en México según su comportamiento de participación electoral?", 2)
    add_card(s2, 0.5, 1.45, 6.0, 5.5, "Diagnóstico del Abstencionismo en México", [
        "El abstencionismo (44.17% en 2024 y >50% en elecciones intermedias) no es uniforme: tiene edad exacta, género, territorio y coyuntura.",
        "Las campañas genéricas de llamado al voto tienen rendimientos decrecientes porque tratan igual a un adulto mayor urbano que a un joven rural.",
        "Pregunta guía del INE: Identificar grupos con patrones similares para diseñar campañas focalizadas y mensajes diferenciados por perfil.",
        "Brecha estructural Presidencial (58.63%) vs Intermedia (45.60%): +13.03 puntos porcentuales (12.8 millones de votantes intermitentes)."
    ], "#4A154B")
    add_card(s2, 6.8, 1.45, 6.0, 5.5, "Procesamiento del 100% del Acervo CCPC", [
        "54,872,712 registros procesados en paralelo (PyArrow/Parquet) sin muestreo parcial.",
        "192 archivos CSV de 6 elecciones federales ordinarias (2009, 2012, 2015, 2018, 2021 y 2024) en las 32 entidades federativas.",
        "2 archivos nacionales de modalidades especiales 2024: Voto Anticipado (3,449) y Prisión Preventiva (26,563).",
        "Cobertura de 98,330,348 ciudadanas y ciudadanos en Lista Nominal 2024 a través de los 2,477 municipios del país."
    ], "#1E8449", "#EAFAF1")

    # ==================== SLIDE 3: CURVA DE CICLO DE VIDA Y PARADOJA DEL 2° VOTO ====================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "2. Hallazgo Demográfico Clave: La Paradoja del 'Segundo Voto'",
                     "Curva del Ciclo de Vida Electoral por Edad Exacta (18 a 90 años) y Liderazgo Femenino", 3)
    fig1 = os.path.join(BASE_DIR, "figures", "fig1_curva_edad_sexo.png")
    if os.path.exists(fig1):
        s3.shapes.add_picture(fig1, Inches(0.45), Inches(1.45), width=Inches(7.7))
    add_card(s3, 8.35, 1.45, 4.55, 5.5, "3 Leyes Demográficas CCPC", [
        "Entusiasmo a los 18 años: 55.1% Mujeres y 48.9% Hombres votan al estrenar su INE.",
        "El Valle de Abstención Joven (20–34 años): Desplome hasta 37.8% en hombres de 26 años (y 28.4% en intermedias) por movilidad estudiantil/laboral sin cambio de domicilio.",
        "Liderazgo Femenino (+7.68 pp): Mujeres votan 59.51% vs 51.83% Hombres (hasta +12.5 pp en adultez joven).",
        "Inclusión 2024: Personas No Binarias (SEXO=2) lograron 75.24% de participación (79 de 105)."
    ], "#C0392B", "#FDEDEC")

    # ==================== SLIDE 4: METODOLOGÍA DE SEGMENTACIÓN K-MEANS ====================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "3. Metodología de Segmentación Sociodemográfica (Clustering)",
                     "Modelo K-Means Ponderado por Lista Nominal sobre Panel Longitudinal 2009–2024", 4)
    fig2 = os.path.join(BASE_DIR, "figures", "fig2_perfiles_clustering.png")
    if os.path.exists(fig2):
        s4.shapes.add_picture(fig2, Inches(0.45), Inches(1.5), width=Inches(7.8))
    add_card(s4, 8.4, 1.5, 4.5, 5.45, "Ingeniería de Variables (Z-Score)", [
        "Unidad de análisis: Celda Sociodemográfica Territorial (Entidad × Región × Tipo Sección U/M/R × Sexo × Cohorte Edad) en 6 elecciones.",
        "Features: Tasa 2024, Media Presidencial, Media Intermedia, Brecha Coyuntural (pp), Tendencia Secular 2009–2024, Edad, Urbanización/Ruralidad.",
        "Escolaridad Territorial Estimada: Cruce con Censo INEGI 2020 ajustado por sección U/M/R y cohorte.",
        "Ponderación exacta por Lista Nominal (sample_weight = LN_2024) para representar a los 98.33M de electores."
    ], "#5B2C6F")

    # ==================== SLIDE 5: PERFILES DE ALTA PARTICIPACIÓN (P1 Y P2) ====================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "4. Perfiles de Alta Participación Constante: P1 y P2 (36.49% del Padrón)",
                     "El pilar intergeneracional urbano y la resiliencia comunitaria del México rural", 5)
    p1, p2_prof = PERFILES[0], PERFILES[1]
    add_card(s5, 0.5, 1.45, 6.0, 5.5, f"🏛️ {p1['id']}: {p1['name']} ({p1['pct_padron']}% LN · 21.46M)", [
        f"Indicadores: Voto 2024: {p1['tasa_2024']}% | Pres.: {p1['tasa_pres']}% | Interm.: {p1['tasa_inter']}% | Tendencia: +{p1['tendencia_lp']} pp.",
        f"Demografía: Edad media {p1['edad_media']} años | {p1['pct_mujer']}% Mujeres | 95.6% Urbano | Escolaridad: {p1['escolaridad_est']} años.",
        "Narrativa: Adultos mayores urbanos con lealtad democrática inquebrantable y liderazgo femenino.",
        f"Estrategia INE ({p1['ine_strategy']}): Programa 'Vota con tu Abuela/o' (embajadores ante P5), accesibilidad física, fila preferente y Voto Anticipado."
    ], p1["color"])
    add_card(s5, 6.8, 1.45, 6.0, 5.5, f"🌾 {p2_prof['id']}: {p2_prof['name']} ({p2_prof['pct_padron']}% LN · 14.42M)", [
        f"Indicadores: Voto 2024: {p2_prof['tasa_2024']}% | Pres.: {p2_prof['tasa_pres']}% | Interm.: {p2_prof['tasa_inter']}% (La más alta del país).",
        f"Demografía: Edad media {p2_prof['edad_media']} años | {p2_prof['pct_mujer']}% Mujeres | Rural/Mixto | Escolaridad: {p2_prof['escolaridad_est']} años.",
        "Narrativa: Comunidades rurales con fuerte cohesión vecinal que votan tanto en presidenciales como intermedias.",
        f"Estrategia INE ({p2_prof['ine_strategy']}): Radio comunitaria, lenguas indígenas, promotorías rurales de mujeres y defensa del voto libre."
    ], p2_prof["color"], "#EAFAF1")

    # ==================== SLIDE 6: PERFILES INTERMITENTES Y EN DESGASTE (P3 Y P4) ====================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "5. Perfiles Coyunturales y en Desencanto: P3 y P4 (29.77% del Padrón)",
                     "La brecha crítica en elecciones intermedias y la fatiga democrática en mediana edad", 6)
    p3_prof, p4_prof = PERFILES[2], PERFILES[3]
    add_card(s6, 0.5, 1.45, 6.0, 5.5, f"⚡ {p3_prof['id']}: {p3_prof['name']} ({p3_prof['pct_padron']}% LN · 16.14M)", [
        f"Indicadores: Voto 2024: {p3_prof['tasa_2024']}% | Pres.: {p3_prof['tasa_pres']}% vs Interm.: {p3_prof['tasa_inter']}% (Brecha récord de {p3_prof['brecha_pres_inter']} pp).",
        f"Demografía: Edad media {p3_prof['edad_media']} años | {p3_prof['pct_mujer']}% Mujeres | 97.1% Urbano | Escolaridad: {p3_prof['escolaridad_est']} años.",
        "Narrativa: Mujeres jóvenes y profesionistas urbanas que acuden masivamente en presidenciales pero se ausentan en intermedias.",
        f"Estrategia INE ({p3_prof['ine_strategy']}): Campaña 'El Congreso decide tu día a día' (salud, cuidados, seguridad) y comparadores digitales en 60s."
    ], "#B7950B", "#FEF9E7")
    add_card(s6, 6.8, 1.45, 6.0, 5.5, f"📉 {p4_prof['id']}: {p4_prof['name']} ({p4_prof['pct_padron']}% LN · 13.12M)", [
        f"Indicadores: Voto 2024: {p4_prof['tasa_2024']}% | Pres.: {p4_prof['tasa_pres']}% | Interm.: {p4_prof['tasa_inter']}% | Caída histórica: {p4_prof['tendencia_lp']} pp.",
        f"Demografía: Edad media {p4_prof['edad_media']} años | {p4_prof['pct_mujer']}% Mujeres | Urbano/Mixto | Escolaridad: {p4_prof['escolaridad_est']} años.",
        "Narrativa: Adultos de mediana edad históricamente cumplidos que muestran el mayor desgaste longitudinal entre 2009 y 2024.",
        f"Estrategia INE ({p4_prof['ine_strategy']}): Observatorios distritales de rendición de cuentas legislativa y comunicación sobre eficacia del voto."
    ], p4_prof["color"], "#EBF5FB")

    # ==================== SLIDE 7: PERFILES DE BAJA PARTICIPACIÓN JOVEN (P5 Y P6) ====================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "6. Prioridad Nacional INE: Juventudes en Abstención P5 y P6 (33.75% LN)",
                     "33.18 millones de jóvenes urbanos, periféricos y rurales con predominio masculino", 7)
    p5_prof, p6_prof = PERFILES[4], PERFILES[5]
    add_card(s7, 0.5, 1.45, 6.0, 5.5, f"🏙️ {p5_prof['id']}: {p5_prof['name']} ({p5_prof['pct_padron']}% LN · 21.30M)", [
        f"Indicadores: Voto 2024: {p5_prof['tasa_2024']}% | Intermedia: ¡Solo {p5_prof['tasa_inter']}%! | Tendencia: {p5_prof['tendencia_lp']} pp.",
        f"Demografía: Edad media {p5_prof['edad_media']} años | 69.4% Hombres | 100% Urbano | Escolaridad alta: {p5_prof['escolaridad_est']} años.",
        "Narrativa: Jóvenes urbanos de 20 a 34 años que se desconectan tras su primer voto por movilidad residencial o apatía.",
        f"Estrategia INE ({p5_prof['ine_strategy']}): Campaña 'Tu Segundo Voto Importa Más', módulos INE en universidades y alianzas en gaming/deportes/streaming."
    ], p5_prof["color"], "#FDEDEC")
    add_card(s7, 6.8, 1.45, 6.0, 5.5, f"🚧 {p6_prof['id']}: {p6_prof['name']} ({p6_prof['pct_padron']}% LN · 11.88M)", [
        f"Indicadores: Voto 2024: {p6_prof['tasa_2024']}% | Intermedia: {p6_prof['tasa_inter']}% | Tendencia: {p6_prof['tendencia_lp']} pp.",
        f"Demografía: Edad media {p6_prof['edad_media']} años | 67.4% Hombres | Rural/Mixto | Escolaridad: {p6_prof['escolaridad_est']} años.",
        "Narrativa: Jóvenes de periferias y zonas rurales afectados por trabajo dominical, migración laboral y lejanía de casillas.",
        f"Estrategia INE ({p6_prof['ine_strategy']}): Convenios 'Domingo Cívico Laboral' con empleadores agrícolas/industriales y módulos itinerantes."
    ], p6_prof["color"], "#FDF2E9")

    # ==================== SLIDE 8: ATLAS TERRITORIAL E INCLUSIÓN 2024 ====================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "7. Dinámica Territorial (32 Estados / 2,477 Municipios) e Inclusión 2024",
                     "Trayectoria longitudinal de los perfiles y nuevas modalidades censales 2024", 8)
    fig3 = os.path.join(BASE_DIR, "figures", "fig3_evolucion_perfiles_2009_2024.png")
    if os.path.exists(fig3):
        s8.shapes.add_picture(fig3, Inches(0.45), Inches(1.5), width=Inches(7.5))
    add_card(s8, 8.15, 1.5, 4.7, 5.45, "Inclusión Histórica y Territorio", [
        "Personas No Binarias (SEXO=2 en 2024): 75.24% de participación (79 votaron de 105 en LN). El reconocimiento de identidad impulsa la ciudadanía.",
        "Voto Anticipado 2024: 3,449 votantes (62.1% mujeres, principalmente adultas mayores de P1).",
        "Prisión Preventiva 2024: 26,563 votantes (91.2% hombres jóvenes). Cuando se acerca la urna, los hombres jóvenes sí votan.",
        "Clasificador Municipal: Identificamos el perfil prioritario en cada uno de los 2,477 municipios para las 300 Juntas Distritales."
    ], "#4A154B")

    # ==================== SLIDE 9: PLATAFORMA WEB INTERACTIVA Y SIMULADOR WHAT-IF ====================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "8. Plataforma Interactiva de Inteligencia Cívica y Simulador 'What-If'",
                     "Herramienta desplegada en vivo para las 32 Juntas Locales Ejecutivas y la ciudadanía", 9)
    add_card(s9, 0.5, 1.45, 6.0, 5.5, "Arquitectura Frontend Moderna (En Vivo)", [
        "URL Pública: https://israquandev.github.io/Hackea_INE_perfiles_ciudadanos/",
        "Repositorio CI/CD: https://github.com/IsraQuanDev/Hackea_INE_perfiles_ciudadanos",
        "5 Módulos Interactivos: (1) Inspector de Clusters y Radar 5D, (2) Curva de Edad Exacta 18-90, (3) Buscador de 2,477 Municipios con exportación CSV, (4) Clasificador de Campañas INE y (5) Inclusión 2024.",
        "Diseño accesible con soporte claro/oscuro y motor vectorial instantáneo."
    ], "#5B2C6F")
    add_card(s9, 6.8, 1.45, 6.0, 5.5, "Simulación Paramétrica de Impacto (Meta 2027)", [
        "¿Qué pasa si el INE aplica estas estrategias diferenciadas en la elección intermedia de 2027?",
        "Meta +6.0 pp en P5 (Juventud Urbana): +1,278,048 nuevos votantes.",
        "Meta +8.0 pp en P3 (Votantes Coyunturales): +1,291,284 nuevos votantes.",
        "Meta +5.0 pp en P6 (Juventud Rural) y +4.0 pp en P4: +1,119,121 nuevos votantes.",
        "IMPACTO TOTAL: +3,688,453 nuevos votantes efectivos (+3.75 pp en la tasa nacional)."
    ], "#1E8449", "#EAFAF1")

    # ==================== SLIDE 10: MATRIZ EJECUTIVA DE ACCIÓN INE ====================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_header(s10, "9. Hoja de Ruta Accionable para el INE y ENCÍVICA 2024–2026",
                     "Síntesis de intervenciones focalizadas por Perfil Ciudadano para construir democracia", 10)
    add_card(s10, 0.5, 1.45, 12.3, 5.5, "Decálogo de Implementación Institucional (DECEyEC + 32 Juntas Locales)", [
        "1. [P1 → P5] Embajadores Intergeneracionales: Activar a las y los 21.46M de Guardianes Cívicos Urbanos para llevar a votar a los jóvenes de su hogar.",
        "2. [P5] Campaña 'Tu Segundo Voto Construye el Hábito' + Módulos INE Universitarios: Atacar la fosa de abstención de 20 a 29 años actualizando domicilios.",
        "3. [P3] Pedagogía del Poder Legislativo ('El Congreso Decide tu Día a Día'): Reducir la brecha de 19.94 pp en elecciones intermedias con micro-contenidos.",
        "4. [P2] Educación Cívica Intercultural y Comunitaria: Fortalecer radio indigenista, promotorías de mujeres rurales y defensa del voto libre y secreto.",
        "5. [P6] Convenios de 'Domingo Cívico Laboral': Garantizar permisos horarios y transporte en corredores agroindustriales, maquiladores y periféricos.",
        "6. [P4] Observatorios Distritales Post-Electorales: Reconectar a los adultos desencantados vinculando el voto con exigencia y rendición de cuentas.",
        "7. Adopción del Atlas Municipal Interactivo CCPC: Focalizar recursos de capacitación de las 300 Juntas Distritales en las secciones de menor voto joven."
    ], "#4A154B")

    for out_p in pptx_paths:
        prs.save(out_p)
    print("Presentación Ejecutiva PPTX (exactamente 10 diapositivas) generada con éxito!")


def build_slides_pdf(pdf_paths):
    # También generar versión PDF apaisada de las 10 diapositivas para lectura universal sin PowerPoint
    slides_data = [
        ("Diapositiva 1 / 10 — Portada Oficial", "HACKEA LA PARTICIPACIÓN: DATOS QUE CONSTRUYEN DEMOCRACIA (INE · DECEyEC)", [
            "Reto 1: Perfiles Ciudadanos de Participación (Segmentación Sociodemográfica CCPC 2009–2024)",
            "54,872,712 registros censales procesados | 194 archivos CSV oficiales | 98,330,348 en Lista Nominal 2024 | 2,477 Municipios",
            "Dashboard Interactivo en Vivo: https://israquandev.github.io/Hackea_INE_perfiles_ciudadanos/",
            "Repositorio GitHub con CI/CD: https://github.com/IsraQuanDev/Hackea_INE_perfiles_ciudadanos"
        ]),
        ("Diapositiva 2 / 10 — Problema y Alcance Censal", "1. El Problema Público y Procesamiento del 100% del Acervo CCPC (2009–2024)", [
            "El abstencionismo (44.17% en 2024 y >50% en intermedias) tiene edad exacta, género, territorio y coyuntura electoral.",
            "Procesamos los 54.87 millones de registros de las 6 elecciones federales (2009, 2012, 2015, 2018, 2021 y 2024) + Voto Anticipado y Prisión Preventiva.",
            "Brecha estructural entre elecciones Presidenciales (58.63%) e Intermedias (45.60%): +13.03 puntos porcentuales (12.8 millones de votantes)."
        ]),
        ("Diapositiva 3 / 10 — Ciclo de Vida Electoral", "2. Hallazgo Demográfico Clave: La Paradoja del 'Segundo Voto' y Liderazgo Femenino", [
            "A los 18 años votan el 55.1% de las mujeres y 48.9% de los hombres, pero entre los 20 y 34 años caen al 'Valle de Abstencionismo Joven' (37.8% en hombres de 26 años).",
            "Las mujeres superan a los hombres en +7.68 pp a nivel nacional (59.51% vs 51.83%) y hasta en +12.5 pp entre los 25 y 39 años.",
            "En 2024, las personas con credencial No Binaria (SEXO=2) registraron 75.24% de participación (79 de 105)."
        ]),
        ("Diapositiva 4 / 10 — Metodología de Clustering", "3. Modelo de Segmentación Sociodemográfica (K-Means Ponderado por Lista Nominal)", [
            "Panel longitudinal de celdas sociodemográficas (Entidad × Región × Tipo de Sección U/M/R × Sexo × Cohorte de Edad) en las 6 elecciones.",
            "Variables Z-Score: Tasa 2024, Media Presidencial, Media Intermedia, Brecha Coyuntural, Tendencia 2009–2024, Edad, Urbanización y Escolaridad INEGI.",
            "K-Means ponderado por Lista Nominal (sample_weight = LN_2024) que divide el padrón en 6 Perfiles Ciudadanos accionables."
        ]),
        ("Diapositiva 5 / 10 — Perfiles de Alta Participación", "4. Perfiles Constantes: P1 Guardianes Cívicos Urbanos y P2 Comunidad Rural Comprometida", [
            "P1 Guardianes Cívicos Urbanos (21.82% LN, 21.46M): Edad media 62.4 años, 63.1% mujeres, 67.96% voto en 2024. Estrategia: Embajadores Intergeneracionales.",
            "P2 Comunidad Rural Comprometida (14.67% LN, 14.42M): Edad media 53.7 años, 63.41% voto en 2024 y 57.37% en intermedias. Estrategia: Radio comunitaria y lenguas indígenas."
        ]),
        ("Diapositiva 6 / 10 — Perfiles Intermitentes y en Desgaste", "5. Perfiles Coyunturales y en Desencanto: P3 y P4 (29.77% de la Lista Nominal)", [
            "P3 Votantes Coyunturales de Alta Expectativa (16.42% LN, 16.14M): 68.2% mujeres urbanas (34.7 años), caen 19.94 pp en intermedias. Estrategia: Pedagogía Legislativa.",
            "P4 Ciudadanía Activa en Desencanto (13.35% LN, 13.12M): Adultos de 46.2 años con caída histórica de -7.21 pp. Estrategia: Rendición de cuentas post-electoral."
        ]),
        ("Diapositiva 7 / 10 — Prioridad Juventudes (P5 y P6)", "6. Foco Rojo Nacional: P5 Juventud Urbana Escéptica y P6 Juventud Periférica/Rural", [
            "P5 Juventud Urbana Escéptica (21.66% LN, 21.30M): 69.4% hombres (29.4 años), 42.96% en 2024 y 33.78% en intermedias. Estrategia: Campaña 'Segundo Voto' y módulos en universidades.",
            "P6 Juventud Periférica y Rural con Barreras (12.09% LN, 11.88M): 67.4% hombres (29.3 años), 43.10% en 2024. Estrategia: Convenios de 'Domingo Cívico Laboral'."
        ]),
        ("Diapositiva 8 / 10 — Atlas Territorial e Inclusión", "7. Explorador de las 32 Entidades, 2,477 Municipios y Modalidades Especiales 2024", [
            "Diagnóstico completo por región INE y clasificador del perfil prioritario en cada uno de los 2,477 municipios de México.",
            "Voto Anticipado 2024: 3,449 participantes (62.1% mujeres). Prisión Preventiva 2024: 26,563 participantes (91.2% hombres)."
        ]),
        ("Diapositiva 9 / 10 — Simulador de Política Pública", "8. Plataforma Interactiva en Vivo y Simulador Paramétrico 'What-If' (Meta 2027)", [
            "Al incrementar +6 pp en P5, +8 pp en P3, +5 pp en P6 y +4 pp en P4 mediante campañas diferenciadas, el INE movilizaría +3,688,453 nuevos votantes.",
            "La participación nacional en elecciones intermedias subiría de 49.60% a más de 53.35%."
        ]),
        ("Diapositiva 10 / 10 — Hoja de Ruta INE / ENCÍVICA", "9. Síntesis de Estrategias Diferenciadas por Perfil para la DECEyEC", [
            "1. Embajadores Intergeneracionales (P1→P5) | 2. Módulos Universitarios y Hábito del Segundo Voto (P5) | 3. Relevancia del Congreso en Intermedias (P3).",
            "4. Promotorías Interculturales Rurales (P2) | 5. Domingo Cívico Laboral (P6) | 6. Observatorios Distritales de Rendición de Cuentas (P4)."
        ])
    ]

    for out_pdf in pdf_paths:
        c = rl_canvas.Canvas(out_pdf, pagesize=landscape(letter))
        W, H = landscape(letter)
        for idx, (tag, title, bullets) in enumerate(slides_data):
            c.setFillColor(colors.HexColor("#F8F5FA"))
            c.rect(0, 0, W, H, fill=1, stroke=0)

            c.setFillColor(colors.HexColor("#3B0D4A"))
            c.rect(0, H - 72, W, 72, fill=1, stroke=0)

            c.setFillColor(colors.HexColor("#F7DC6F"))
            c.setFont("Helvetica-Bold", 10)
            c.drawString(36, H - 24, tag + "   |   INE · DECEyEC · ENCÍVICA 2024–2026")

            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 15.5)
            c.drawString(36, H - 50, title)

            y = H - 115
            c.setFillColor(colors.HexColor("#1E1B24"))
            c.setFont("Helvetica", 12)
            for b in bullets:
                c.drawString(44, y, "• " + b[:105])
                if len(b) > 105:
                    y -= 18
                    c.drawString(58, y, b[105:])
                y -= 32

            # Insertar figuras clave en las diapositivas 3, 4 y 8
            if idx == 2 and os.path.exists(os.path.join(BASE_DIR, "figures", "fig1_curva_edad_sexo.png")):
                c.drawImage(os.path.join(BASE_DIR, "figures", "fig1_curva_edad_sexo.png"), 44, 36, width=520, height=250, preserveAspectRatio=True)
            elif idx == 3 and os.path.exists(os.path.join(BASE_DIR, "figures", "fig2_perfiles_clustering.png")):
                c.drawImage(os.path.join(BASE_DIR, "figures", "fig2_perfiles_clustering.png"), 44, 36, width=560, height=250, preserveAspectRatio=True)
            elif idx == 7 and os.path.exists(os.path.join(BASE_DIR, "figures", "fig3_evolucion_perfiles_2009_2024.png")):
                c.drawImage(os.path.join(BASE_DIR, "figures", "fig3_evolucion_perfiles_2009_2024.png"), 44, 36, width=540, height=250, preserveAspectRatio=True)

            c.showPage()
        c.save()
    print("Presentación Ejecutiva PDF (10 diapositivas) generada con éxito!")


if __name__ == "__main__":
    pptx_targets = [
        os.path.join(DESKTOP_DIR, "Presentacion_Ejecutiva_Reto1_HackeaINE.pptx"),
        os.path.join(ENTREGABLES_DIR, "02_Presentacion_Ejecutiva_10_Diapositivas_INE.pptx")
    ]
    pdf_slides_targets = [
        os.path.join(ENTREGABLES_DIR, "02_Presentacion_Ejecutiva_10_Diapositivas_INE.pdf")
    ]
    build_pptx(pptx_targets)
    build_slides_pdf(pdf_slides_targets)
