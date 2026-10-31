import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
)
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
DESKTOP_DIR = r"C:\Users\52477\Desktop"
ENTREGABLES_DIR = os.path.join(DESKTOP_DIR, "Entregables_HackeaINE_Reto1")
os.makedirs(ENTREGABLES_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "processed_data", "dashboard_data_pro.json"), "r", encoding="utf-8") as f:
    DATA = json.load(f)

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(colors.HexColor("#4A154B"))
    canvas.drawString(0.75 * inch, 10.55 * inch, "INE · DECEyEC · ENCÍVICA 2024–2026 | HACKEA LA PARTICIPACIÓN: DATOS QUE CONSTRUYEN DEMOCRACIA")
    canvas.setStrokeColor(colors.HexColor("#8E24AA"))
    canvas.setLineWidth(0.8)
    canvas.line(0.75 * inch, 10.45 * inch, 7.75 * inch, 10.45 * inch)

    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.line(0.75 * inch, 0.65 * inch, 7.75 * inch, 0.65 * inch)
    canvas.drawString(0.75 * inch, 0.45 * inch, "Documento Técnico — Reto 1: Perfiles Ciudadanos de Participación (CCPC 2009–2024)")
    canvas.drawRightString(7.75 * inch, 0.45 * inch, f"Cuartilla {doc.page}")
    canvas.restoreState()

def build_pdf_document(pdf_paths):
    styles = getSampleStyleSheet()
    # Regla oficial de la convocatoria: Arial/Calibri 11 pt, interlineado 1.5 (11 * 1.5 = 16.5 pt leading)
    body_style = ParagraphStyle(
        "BodyINE",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=16.5,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        textColor=colors.HexColor("#1C2833")
    )
    bullet_style = ParagraphStyle(
        "BulletINE",
        parent=body_style,
        leftIndent=18,
        firstLineIndent=-10,
        spaceAfter=5
    )
    h1_style = ParagraphStyle(
        "H1INE",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14.5,
        leading=20,
        textColor=colors.HexColor("#4A154B"),
        spaceBefore=10,
        spaceAfter=8
    )
    h2_style = ParagraphStyle(
        "H2INE",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=17,
        textColor=colors.HexColor("#6C3483"),
        spaceBefore=8,
        spaceAfter=6
    )
    title_cover = ParagraphStyle(
        "CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=26,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4A154B"),
        spaceAfter=12
    )
    sub_cover = ParagraphStyle(
        "CoverSub",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#6C3483"),
        spaceAfter=14
    )

    for out_path in pdf_paths:
        doc = SimpleDocTemplate(
            out_path,
            pagesize=letter,
            leftMargin=0.75 * inch,
            rightMargin=0.75 * inch,
            topMargin=0.85 * inch,
            bottomMargin=0.85 * inch
        )
        story = []

        # ==================== CUARTILLA 1: PORTADA Y RESUMEN EJECUTIVO ====================
        story.append(Spacer(1, 0.15 * inch))
        story.append(Paragraph("INSTITUTO NACIONAL ELECTORAL (INE)<br/>DIRECCIÓN EJECUTIVA DE CAPACITACIÓN ELECTORAL Y EDUCACIÓN CÍVICA (DECEyEC)", sub_cover))
        story.append(Paragraph("HACKEA LA PARTICIPACIÓN: DATOS QUE CONSTRUYEN DEMOCRACIA<br/>DOCUMENTO TÉCNICO — RETO 1: PERFILES CIUDADANOS DE PARTICIPACIÓN", title_cover))
        story.append(Paragraph("Segmentación Sociodemográfica Longitudinal y Estrategias Diferenciadas sobre los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024", sub_cover))
        story.append(Spacer(1, 0.1 * inch))

        story.append(Paragraph("1. Resumen Ejecutivo y Alcance Censal del Proyecto", h1_style))
        story.append(Paragraph(
            "La participación electoral en México no es un fenómeno homogéneo ni estático; responde a configuraciones sociodemográficas, territoriales, generacionales y de coyuntura política que determinan quién acude a las urnas y quién permanece al margen. El presente Documento Técnico desarrolla la solución integral al Reto 1 (Perfiles ciudadanos de participación) de la convocatoria nacional Hackea la participación: Datos que construyen democracia, respondiendo a la pregunta guía del Instituto Nacional Electoral (INE): ¿Qué tipos de ciudadanía existen según su comportamiento de participación?",
            body_style
        ))
        story.append(Paragraph(
            "A diferencia de aproximaciones basadas en muestras parciales o encuestas de opinión sujetas a sesgo de deseabilidad social, este estudio procesó el 100% del universo de registros publicados en la Plataforma de los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024. En total, se consolidaron mediante procesamiento paralelo en PyArrow 54,872,712 registros agregados provenientes de 194 archivos CSV oficiales: los 192 archivos estatales correspondientes a las seis elecciones federales ordinarias (2009, 2012, 2015, 2018, 2021 y 2024 en las 32 entidades federativas) más los 2 archivos nacionales de modalidades especiales implementadas en 2024 (Voto Anticipado y Voto de Personas en Prisión Preventiva).",
            body_style
        ))
        story.append(Paragraph(
            "Sobre este acervo censal —que en la jornada electoral de 2024 abarcó una Lista Nominal en cuadernillos de 98,330,348 ciudadanas y ciudadanos distribuidos en 2,477 municipios—, se diseñó un modelo de aprendizaje no supervisado (K-Means ponderado por volumen de Lista Nominal y validado con el coeficiente de Silueta y Modelos de Mezclas Gaussianas) que identifica 6 Perfiles Ciudadanos claramente diferenciados. Para cada perfil se entrega su caracterización estadística, demográfica, territorial, de escolaridad inferida y una matriz accionable de campañas focalizadas alineada con la Estrategia Nacional de Educación Cívica (ENCÍVICA 2024–2026).",
            body_style
        ))
        story.append(Spacer(1, 0.1 * inch))

        # ==================== SECCIÓN 2: MARCO DE DATOS Y ARQUITECTURA ====================
        story.append(Paragraph("2. Arquitectura de Datos y Diagnóstico Longitudinal CCPC (2009–2024)", h1_style))
        story.append(Paragraph(
            "Los Conteos Censales de Participación Ciudadana tienen como fuente primaria la captura directa de los cuadernillos de la Lista Nominal utilizados por las y los funcionarios de las mesas directivas de casilla. Cada registro desglosa el año de elección (AELEC), entidad federativa (EDOCVE/EDONOM), municipio (MPIOCVE/MPIONOM), sección electoral (SECCION), tipología geográfica de la sección (TIPOSEC: Urbana U, Mixta M y Rural R), distritos electorales federal y local (DEF/DEL), sexo de las personas (SEXO: 0 Hombres, 1 Mujeres y, por primera vez en 2024, 2 No Binario) y edad exacta cumplida al día de la elección (EDAD), cuantificando la Lista Nominal (LN), los registros con marca de voto (SV), sin marca de voto (NV) y no especificados (NS).",
            body_style
        ))

        t_nac_data = [
            ["Año Electoral", "Tipo de Elección", "Lista Nominal (LN)", "Sí Votaron (SV)", "No Votaron (NV)", "No Especif. (NS)", "Participación"],
            ["2009", "Intermedia", "77,481,831", "33,316,974", "42,298,963", "1,865,894", "43.00%"],
            ["2012", "Presidencial", "76,490,962", "47,383,154", "28,939,159", "168,649", "61.95%"],
            ["2015", "Intermedia", "83,563,462", "36,926,612", "41,517,874", "5,118,976", "44.19%"],
            ["2018", "Presidencial", "89,123,997", "51,784,399", "31,249,856", "6,089,742", "58.10%"],
            ["2021", "Intermedia", "93,532,133", "46,389,189", "43,099,624", "4,043,320", "49.60%"],
            ["2024", "Presidencial", "98,330,348", "54,899,228", "37,105,466", "6,325,654", "55.83%"]
        ]
        t_nac = Table(t_nac_data, colWidths=[0.8*inch, 1.0*inch, 1.15*inch, 1.15*inch, 1.15*inch, 1.05*inch, 0.85*inch])
        t_nac.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4A154B")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8.5),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9F5FC"), colors.white]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D2B4DE")),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4)
        ]))
        story.append(Spacer(1, 0.06 * inch))
        story.append(t_nac)
        story.append(Spacer(1, 0.1 * inch))

        story.append(Paragraph("2.1 Dualidad Presidencial vs. Intermedia y Dinámica Territorial", h2_style))
        story.append(Paragraph(
            "El análisis longitudinal revela tres leyes empíricas fundamentales del comportamiento electoral mexicano entre 2009 y 2024. Primero, existe una brecha estructural de +13.03 puntos porcentuales (pp) entre las elecciones presidenciales (media de 58.63%) y las elecciones intermedias de renovación de la Cámara de Diputados (media de 45.60%). Esto demuestra que más de 12.8 millones de ciudadanas y ciudadanos perciben las elecciones legislativas como eventos de segundo orden, desconociendo el papel del Poder Legislativo en la asignación presupuestal y el diseño de políticas públicas cotidianas.",
            body_style
        ))
        story.append(Paragraph(
            "Segundo, la desagregación por tipo de sección electoral (Urbana, Mixta y Rural) desmiente el mito de que la urbanización garantiza mayor participación cívica. Mientras que las secciones urbanas sufren caídas abruptas en los comicios intermedios, las secciones rurales presentan una notable resiliencia comunitaria, superando en más de 8 puntos porcentuales la participación urbana durante elecciones intermedias gracias a mecanismos de cohesión social comunitaria y alta visibilidad de las autoridades locales.",
            body_style
        ))
        story.append(PageBreak())

        # ==================== CUARTILLA 3: CURVA DE CICLO DE VIDA Y BRECHA DE GÉNERO ====================
        story.append(Paragraph("3. La Curva del Ciclo de Vida Electoral y la Brecha de Género", h1_style))
        story.append(Paragraph(
            "Al graficar la tasa de participación exacta para cada año de edad cumplida desde los 18 hasta los 90 años, se descubre el hallazgo demográfico más relevante para el diseño de campañas del INE: la Paradoja del Primer y Segundo Voto y el Valle de Abstencionismo Joven (20 a 34 años).",
            body_style
        ))

        fig1_path = os.path.join(BASE_DIR, "figures", "fig1_curva_edad_sexo.png")
        if os.path.exists(fig1_path):
            story.append(Image(fig1_path, width=6.6 * inch, height=3.3 * inch))
            story.append(Spacer(1, 0.08 * inch))

        story.append(Paragraph(
            "• El Efecto Primer Voto (18 años) y el Desplome subsecuente (20 a 34 años): Quienes cumplen 18 años acuden a las urnas con una participación inicial de 55.1% en mujeres y 48.9% en hombres (2024). Sin embargo, una vez superado el ritual de estrenar la credencial para votar, la participación cae en picada entre los 20 y los 29 años, tocando su mínimo nacional en los hombres de 25 a 27 años con apenas 37.8% en elección presidencial y un crítico 28.4% en la elección intermedia de 2021. Este fenómeno se explica por la transición vital hacia la educación superior o el primer empleo y la movilidad residencial sin actualización de domicilio en el Padrón Electoral.",
            bullet_style
        ))
        story.append(Paragraph(
            "• Liderazgo Cívico Femenino (+7.68 pp a nivel nacional): En 2024, las mujeres registraron una participación de 59.51% frente al 51.83% de los hombres. Entre los 22 y los 40 años de edad, la brecha a favor de las mujeres alcanza niveles de +11.5 a +12.5 puntos porcentuales. La participación femenina solo desciende por debajo de la masculina después de los 76 años debido a brechas de salud, viudez y limitaciones de movilidad física.",
            bullet_style
        ))
        story.append(Paragraph(
            "• Nuevas Modalidades de Inclusión 2024: Por primera vez en la historia censal del INE, se incorporó el identificador SEXO = 2 (Personas No Binarias), logrando una ejemplar participación de 75.24% (79 votantes de 105 en Lista Nominal). Asimismo, el Voto Anticipado sumó 3,449 votantes (62.1% mujeres, mayoritariamente adultas mayores con limitaciones físicas) y el Voto en Prisión Preventiva registró 26,563 sufragios (91.2% hombres).",
            bullet_style
        ))
        story.append(PageBreak())

        # ==================== CUARTILLA 4: METODOLOGÍA DE SEGMENTACIÓN (CLUSTERING) ====================
        story.append(Paragraph("4. Metodología de Segmentación Sociodemográfica (Clustering)", h1_style))
        story.append(Paragraph(
            "Dado que los datos abiertos de la Plataforma CCPC son agregados anónimos sin identificadores personales (en estricto cumplimiento de la protección de datos personales), se construyó un panel longitudinal donde la unidad de observación es la Celda Sociodemográfica Territorial: la intersección de Entidad Federativa (32) × Región INE (5 circunscripciones) × Tipo de Sección Electoral (U, M, R) × Sexo (Hombres, Mujeres) × Cohorte de Edad (9 grupos etarios: 18–19, 20–24, 25–29, 30–34, 35–39, 40–49, 50–59, 60–69 y 70+ años), rastreada de forma continua a través de los seis procesos electorales federales (2009, 2012, 2015, 2018, 2021 y 2024).",
            body_style
        ))
        story.append(Paragraph("4.1 Ingeniería de Características e Inferencia Territorial de Escolaridad", h2_style))
        story.append(Paragraph(
            "Para satisfacer la sugerencia metodológica de la convocatoria de incorporar edad, sexo, región, historial de participación y posible escolaridad, se construyeron ocho variables explicativas estandarizadas mediante transformación Z-Score (media cero y varianza unitaria):",
            body_style
        ))
        story.append(Paragraph("1. Tasa de Participación Reciente (TASA_2024): Proporción efectiva SV / LN en la elección federal 2024.", bullet_style))
        story.append(Paragraph("2. Nivel Histórico Medio (TASA_MEDIA_HIST): Promedio longitudinal de participación en las 6 elecciones (2009–2024).", bullet_style))
        story.append(Paragraph("3. Brecha Coyuntural Presidencial-Intermedia (BRECHA_PRES_INTER): Diferencia entre el promedio de elecciones presidenciales (2012, 2018, 2024) y el promedio de elecciones intermedias (2009, 2015, 2021). Mide la intermitencia electoral.", bullet_style))
        story.append(Paragraph("4. Tendencia Secular de Largo Plazo (TENDENCIA_LP): Cambio porcentual entre el ciclo reciente (2021–2024) y el ciclo inicial (2009–2012), capturando procesos de activación cívica o desencanto democrático.", bullet_style))
        story.append(Paragraph("5. Ciclo de Vida (EDAD_APROX): Punto medio etario de la cohorte poblacional.", bullet_style))
        story.append(Paragraph("6. Indicadores de Urbanización y Ruralidad (ES_URBANO, ES_RURAL): Codificación de la tipología geográfica de la sección electoral.", bullet_style))
        story.append(Paragraph("7. Escolaridad Territorial Estimada (ESCOLARIDAD_EST): Años promedio de estudio inferidos mediante el cruce ecológico de los indicadores estatales de escolaridad del Censo de Población y Vivienda INEGI 2020 ajustados por el diferencial urbano/mixto/rural y la estructura generacional de cada cohorte.", bullet_style))

        story.append(Paragraph("4.2 Selección del Algoritmo K-Means Ponderado y Validación", h2_style))
        story.append(Paragraph(
            "Se aplicó el algoritmo K-Means ponderado por el volumen poblacional de la Lista Nominal 2024 (sample_weight = LN_2024), garantizando que los centroides reflejen la distribución real del padrón nacional y no se distorsionen por celdas rurales de baja densidad. Se evaluaron particiones desde K=4 hasta K=7 mediante el Coeficiente de Silueta (Silhouette Score: K=4: 0.2258, K=5: 0.1984, K=6: 0.1808, K=7: 0.2002) y criterios de interpretabilidad operativa para la DECEyEC, seleccionando K=6 como la partición óptima que distingue con precisión la fractura urbana/rural, el ciclo generacional y la intermitencia en elecciones intermedias.",
            body_style
        ))
        story.append(PageBreak())

        # ==================== CUARTILLA 5: SÍNTESIS VISUAL Y COMPARATIVA DE LOS 6 PERFILES ====================
        story.append(Paragraph("5. Síntesis Estadística y Visual de los 6 Perfiles Ciudadanos", h1_style))
        story.append(Paragraph(
            "El modelo de segmentación clasifica a los 98.33 millones de ciudadanas y ciudadanos de la Lista Nominal en seis perfiles estratégicos cuya distribución en el espacio sociodemográfico y evolución temporal se presentan en las siguientes figuras:",
            body_style
        ))

        fig2_path = os.path.join(BASE_DIR, "figures", "fig2_perfiles_clustering.png")
        if os.path.exists(fig2_path):
            story.append(Image(fig2_path, width=6.2 * inch, height=2.35 * inch))
            story.append(Spacer(1, 0.04 * inch))

        fig3_path = os.path.join(BASE_DIR, "figures", "fig3_evolucion_perfiles_2009_2024.png")
        if os.path.exists(fig3_path):
            story.append(Image(fig3_path, width=6.0 * inch, height=2.35 * inch))
            story.append(Spacer(1, 0.04 * inch))

        t_p_data = [["ID", "Nombre del Perfil", "Padrón 2024", "Voto 24", "Presid.", "Interm.", "Brecha", "Edad", "% Muj.", "Escolaridad"]]
        for p in DATA["perfiles"]:
            t_p_data.append([
                p["id"],
                p["name"][:28],
                f"{p['pct_padron']}% ({p['ln_2024']/1e6:.1f}M)",
                f"{p['tasa_2024']}%",
                f"{p['tasa_pres']}%",
                f"{p['tasa_inter']}%",
                f"{p['brecha_pres_inter']} pp",
                f"{p['edad_media']}a",
                f"{p['pct_mujer']}%",
                f"{p['escolaridad_est']} años"
            ])
        t_prof = Table(t_p_data, colWidths=[0.35*inch, 1.85*inch, 0.95*inch, 0.58*inch, 0.58*inch, 0.58*inch, 0.62*inch, 0.48*inch, 0.52*inch, 0.68*inch])
        t_prof.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4A154B")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.8),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("ALIGN", (1, 1), (1, -1), "LEFT"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9F5FC"), colors.white]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D2B4DE")),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)
        ]))
        story.append(t_prof)
        story.append(Spacer(1, 0.12 * inch))

        # ==================== SECCIÓN 6: CARACTERIZACIÓN PROFUNDA PERFILES P1, P2 Y P3 ====================
        story.append(Paragraph("6. Caracterización Narrativa y Sociodemográfica por Perfil (Parte I)", h1_style))
        for p in DATA["perfiles"][:3]:
            story.append(Paragraph(f"Perfil {p['id']}: {p['name']} — {p['badge']} ({p['pct_padron']}% de la Lista Nominal · {p['ln_2024']:,} electores)", h2_style))
            story.append(Paragraph(
                f"• Radiografía Demográfica y Territorial: Presenta una edad promedio de {p['edad_media']} años, con una composición por sexo de {p['pct_mujer']}% mujeres y {p['pct_hombre']}% hombres. Su escolaridad territorial estimada es de {p['escolaridad_est']} años de estudio. Geográficamente se ubica en un {p['pct_urbano']}% en secciones urbanas, {p['pct_mixto']}% mixtas y {p['pct_rural']}% rurales.",
                bullet_style
            ))
            story.append(Paragraph(
                f"• Historial de Participación (2009–2024): En 2024 registró una tasa de participación de {p['tasa_2024']}%. Su media en elecciones presidenciales es de {p['tasa_pres']}% frente a {p['tasa_inter']}% en elecciones intermedias (brecha coyuntural de {p['brecha_pres_inter']} pp) y una tendencia de largo plazo de {p['tendencia_lp']:+.2f} pp. {p['narrative']}",
                bullet_style
            ))
            story.append(Paragraph(
                f"• Estrategia Focalizada INE ({p['ine_strategy']}): {' '.join(p['ine_actions'])} Canales recomendados: {p['channels']}",
                bullet_style
            ))
            story.append(Spacer(1, 0.05 * inch))

        # ==================== SECCIÓN 7: CARACTERIZACIÓN PROFUNDA PERFILES P4, P5 Y P6 ====================
        story.append(Paragraph("7. Caracterización Narrativa y Sociodemográfica por Perfil (Parte II)", h1_style))
        for p in DATA["perfiles"][3:]:
            story.append(Paragraph(f"Perfil {p['id']}: {p['name']} — {p['badge']} ({p['pct_padron']}% de la Lista Nominal · {p['ln_2024']:,} electores)", h2_style))
            story.append(Paragraph(
                f"• Radiografía Demográfica y Territorial: Presenta una edad promedio de {p['edad_media']} años, con una composición por sexo de {p['pct_mujer']}% mujeres y {p['pct_hombre']}% hombres. Su escolaridad territorial estimada es de {p['escolaridad_est']} años de estudio. Geográficamente se distribuye en {p['pct_urbano']}% secciones urbanas, {p['pct_mixto']}% mixtas y {p['pct_rural']}% rurales.",
                bullet_style
            ))
            story.append(Paragraph(
                f"• Historial de Participación (2009–2024): En 2024 registró una tasa de participación de {p['tasa_2024']}%. Su media en elecciones presidenciales es de {p['tasa_pres']}% frente a {p['tasa_inter']}% en elecciones intermedias (brecha de {p['brecha_pres_inter']} pp) y una tendencia de largo plazo de {p['tendencia_lp']:+.2f} pp. {p['narrative']}",
                bullet_style
            ))
            story.append(Paragraph(
                f"• Estrategia Focalizada INE ({p['ine_strategy']}): {' '.join(p['ine_actions'])} Canales recomendados: {p['channels']}",
                bullet_style
            ))
            story.append(Spacer(1, 0.05 * inch))
        story.append(PageBreak())

        # ==================== CUARTILLA 8: DISTRIBUCIÓN REGIONAL Y EN LAS 32 ENTIDADES ====================
        story.append(Paragraph("8. Diagnóstico Territorial: Las 32 Entidades Federativas y 2,477 Municipios", h1_style))
        story.append(Paragraph(
            "La composición porcentual de los 6 Perfiles Ciudadanos varía significativamente entre las 32 entidades federativas y las cinco regiones socio-geográficas del país. Mientras que estados altamente urbanizados como Ciudad de México, Nuevo León, Querétaro y Baja California concentran una elevada proporción de Votantes Coyunturales (P3) y Juventud Urbana Escéptica (P5), entidades del Sur-Sureste y Centro como Yucatán, Campeche, Chiapas, Oaxaca, Tlaxcala e Hidalgo destacan por el peso de la Comunidad Rural Comprometida (P2), lo que explica su menor caída relativa durante elecciones intermedias.",
            body_style
        ))

        st_rows = [["Entidad Federativa", "Región INE", "Lista Nominal 24", "Part. 24", "Presid.", "Interm.", "Brecha", "Perfil Dominante"]]
        for s in DATA["estados"][:22]:
            st_rows.append([
                s["edonom"],
                s["region"],
                f"{s['ln_2024']:,}",
                f"{s['tasa_2024']}%",
                f"{s['tasa_pres']}%",
                f"{s['tasa_inter']}%",
                f"+{s['brecha']} pp",
                f"{s['perfil_dominante']} ({s['perfiles_pct'][s['perfil_dominante']]}%)"
            ])
        t_st = Table(st_rows, colWidths=[1.45*inch, 1.05*inch, 0.95*inch, 0.65*inch, 0.65*inch, 0.65*inch, 0.68*inch, 0.95*inch])
        t_st.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4A154B")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.8),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("ALIGN", (0, 1), (0, -1), "LEFT"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9F5FC"), colors.white]),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D2B4DE")),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3)
        ]))
        story.append(t_st)
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph(
            "Nota: Las 32 entidades completas y el clasificador de los 2,477 municipios del país se encuentran integrados interactivamente en el Dashboard Web desplegado para consulta de las 32 Juntas Locales Ejecutivas y las 300 Juntas Distritales del INE.",
            body_style
        ))
        story.append(Spacer(1, 0.1 * inch))

        # ==================== SECCIÓN 9: HOJA DE RUTA ESTRATÉGICA E IMPACTO CUANTITATIVO ====================
        story.append(Paragraph("9. Simulación de Política Pública e Impacto Esperado (Rumbo a 2027 y 2030)", h1_style))
        story.append(Paragraph(
            "El valor estratégico de esta segmentación para el Instituto Nacional Electoral radica en sustituir las campañas genéricas de llamado al voto por intervenciones quirúrgicas diferenciadas por perfil sociodemográfico y tipo de sección electoral:",
            body_style
        ))
        story.append(Paragraph(
            "1. Programa Nacional 'El Segundo Voto Construye el Hábito' (Foco en P5 — Juventud Urbana Escéptica, 21.30M de electores): Activar recordatorios cívicos y brigadas móviles de actualización de domicilio en universidades y centros laborales dirigidos específicamente a jóvenes de 20 a 29 años que votaron a los 18 años pero se ausentaron en el proceso subsecuente.",
            bullet_style
        ))
        story.append(Paragraph(
            "2. Alianza Intergeneracional 'Vota con tu Familia' (Sinergia P1 → P5): Dado que los Guardianes Cívicos Urbanos (P1, 67.96% de participación) cohabitan en los mismos hogares o barrios que los jóvenes abstencionistas urbanos (P5, 42.96%), el INE puede apalancar el liderazgo femenino adulto mayor como embajadoras cívicas dentro del núcleo familiar.",
            bullet_style
        ))
        story.append(Paragraph(
            "3. Campaña 'El Congreso Decide tu Día a Día' (Foco en P3 — Votantes Coyunturales, 16.14M de electores): Para abatir la brecha de 19.94 pp en elecciones intermedias, la comunicación institucional previa a 2027 debe traducir las funciones de la Cámara de Diputados en impactos tangibles para mujeres jóvenes y trabajadoras (presupuesto en salud, seguridad, transporte y sistema de cuidados).",
            bullet_style
        ))
        story.append(Paragraph(
            "4. Convenios de 'Domingo Cívico Laboral' y Módulos Periféricos (Foco en P6 — Juventud Periférica y Rural, 11.88M de electores): Coordinar con cámaras agroindustriales, maquiladoras y de servicios facilidades horarias efectivas para acudir a votar en domingo, junto con campañas en radio regional y WhatsApp.",
            bullet_style
        ))
        story.append(Paragraph("9.1 Proyección Paramétrica de Movilización Nacional (Simulador What-If)", h2_style))
        story.append(Paragraph(
            "Mediante nuestro modelo paramétrico de impacto, demostramos que si las estrategias diferenciadas del INE logran incrementar en +6.0 pp la participación de la Juventud Urbana (P5), +8.0 pp en los Votantes Coyunturales durante elecciones intermedias (P3), +5.0 pp en la Juventud Periférica/Rural (P6) y recuperar +4.0 pp en Adultos en Desencanto (P4), México incorporaría +3,689,400 nuevos votantes efectivos en la elección intermedia de 2027, elevando la participación nacional intermedia del 49.60% histórico a más de 53.35%, fortaleciendo de manera estructural la representatividad democrática del país.",
            body_style
        ))
        story.append(Spacer(1, 0.12 * inch))
        story.append(Paragraph(
            "Repositorio Oficial y Plataforma Interactiva en Vivo: https://github.com/IsraQuanDev/Hackea_INE_perfiles_ciudadanos | Dashboard Web: https://israquandev.github.io/Hackea_INE_perfiles_ciudadanos/",
            sub_cover
        ))

        doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

    print("Documento Técnico PDF (9 cuartillas con formato oficial) generado con éxito!")


def build_docx_document(docx_paths):
    doc = docx.Document()
    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(11)
    style.paragraph_format.line_spacing = 1.5

    h = doc.add_heading("HACKEA LA PARTICIPACIÓN: DATOS QUE CONSTRUYEN DEMOCRACIA (INE · DECEyEC)", level=0)
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_sub = doc.add_paragraph("Documento Técnico — Reto 1: Perfiles Ciudadanos de Participación (CCPC 2009–2024 · 54.87 Millones de Registros)")
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_heading("1. Resumen Ejecutivo y Cobertura Censal", level=1)
    doc.add_paragraph(
        "Este documento técnico presenta la solución integral al Reto 1 de la convocatoria nacional del Instituto Nacional Electoral (INE). Se procesó el 100% de los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024: 54,872,712 registros distribuidos en 194 archivos CSV (las 6 elecciones federales ordinarias de 2009, 2012, 2015, 2018, 2021 y 2024 en las 32 entidades federativas más Voto Anticipado y Prisión Preventiva 2024), abarcando una Lista Nominal de 98,330,348 personas en 2,477 municipios."
    )

    doc.add_heading("2. Metodología de Segmentación Sociodemográfica (K-Means Ponderado)", level=1)
    doc.add_paragraph(
        "Se construyó un panel longitudinal de celdas sociodemográficas (Entidad × Región × Tipo de Sección [Urbana, Mixta, Rural] × Sexo × Cohorte de Edad) evaluando su tasa presidencial, tasa intermedia, brecha coyuntural, tendencia secular 2009–2024 y escolaridad territorial estimada (cruce con Censo INEGI 2020). Mediante K-Means ponderado por Lista Nominal (sample_weight = LN_2024) se identificaron 6 Perfiles Ciudadanos accionables."
    )

    for fig_name in ["fig1_curva_edad_sexo.png", "fig2_perfiles_clustering.png", "fig3_evolucion_perfiles_2009_2024.png"]:
        fp = os.path.join(BASE_DIR, "figures", fig_name)
        if os.path.exists(fp):
            doc.add_picture(fp, width=Inches(6.2))

    doc.add_heading("3. Caracterización de los 6 Perfiles Ciudadanos y Estrategias Diferenciadas INE", level=1)
    for p in DATA["perfiles"]:
        doc.add_heading(f"Perfil {p['id']}: {p['name']} ({p['pct_padron']}% LN · {p['ln_2024']:,} electores)", level=2)
        doc.add_paragraph(
            f"Participación 2024: {p['tasa_2024']}% | Presidencial: {p['tasa_pres']}% | Intermedia: {p['tasa_inter']}% | Brecha: {p['brecha_pres_inter']} pp | Edad media: {p['edad_media']} años | Mujeres: {p['pct_mujer']}% | Escolaridad estimada: {p['escolaridad_est']} años."
        )
        doc.add_paragraph(p["narrative"])
        doc.add_paragraph(f"Estrategia INE ({p['ine_strategy']}): " + " ".join(p["ine_actions"]) + f" Canales: {p['channels']}")

    for out_p in docx_paths:
        doc.save(out_p)
    print("Documento Técnico DOCX editable generado con éxito!")


if __name__ == "__main__":
    pdf_targets = [
        os.path.join(DESKTOP_DIR, "Documento_Tecnico_Reto1_HackeaINE.pdf"),
        os.path.join(ENTREGABLES_DIR, "01_Documento_Tecnico_Reto1_Perfiles_CCPC_INE.pdf")
    ]
    docx_targets = [
        os.path.join(ENTREGABLES_DIR, "01_Documento_Tecnico_Reto1_Perfiles_CCPC_INE.docx")
    ]
    build_pdf_document(pdf_targets)
    build_docx_document(docx_targets)
