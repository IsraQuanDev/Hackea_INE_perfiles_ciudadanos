import os
import json
import numpy as np
import pandas as pd

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")

PROFILE_META = {
    2: {
        "id": "P1",
        "order": 1,
        "name": "Guardianes Cívicos Urbanos",
        "subtitle": "Adultos mayores urbanos con lealtad democrática inquebrantable y liderazgo femenino",
        "color": "#5B2C6F",
        "badge": "Alta Participación Constante",
        "icon": "🏛️",
        "narrative": "Representan el pilar más sólido de la democracia mexicana en zonas urbanas (21.82% de la Lista Nominal). Con una edad media de 62.4 años y mayoría femenina (63.1%), registran la tasa de participación más alta en 2024 (67.96%) y una tendencia histórica creciente (+3.67 pp). Votan tanto en elecciones presidenciales como intermedias por sentido de deber cívico.",
        "ine_strategy": "Embajadores Intergeneracionales y Accesibilidad Universal",
        "ine_actions": [
            "Programa 'Vota con tu Abuela/o': incentivar que lleven a jóvenes de su hogar (18-29 años) a la casilla.",
            "Garantizar accesibilidad física total, plantillas braille, fila preferente y capacitación empática a funcionarios de casilla.",
            "Convocarles como observadores electorales, capacitadores comunitarios y promotores de memoria democrática."
        ],
        "channels": "Televisión abierta, radio local, perifoneo barrial, centros comunitarios, clínicas de salud e IMSS/ISSSTE."
    },
    4: {
        "id": "P2",
        "order": 2,
        "name": "Comunidad Rural Comprometida",
        "subtitle": "Ciudadanía de secciones rurales y mixtas con fuerte cohesión comunitaria",
        "color": "#1E8449",
        "badge": "Alta Participación Comunitaria",
        "icon": "🌾",
        "narrative": "Agrupa al 14.67% del padrón nacional en secciones rurales (77.6%) y mixtas, con edad media de 53.7 años, alta presencia femenina (62.1%) y escolaridad básica (6.7 años promedio). Pese a barreras geográficas y menor escolaridad, mantienen la participación más alta en elecciones intermedias (57.37%) y un sólido 63.41% en presidenciales, impulsados por el tejido comunitario.",
        "ine_strategy": "Educación Cívica Comunitaria, Lenguas Indígenas yVoto Libre",
        "ine_actions": [
            "Campañas en lenguas indígenas y formatos radiofónicos/visuales sin tecnicismos sobre el valor del voto libre y secreto.",
            "Talleres de liderazgo cívico para mujeres rurales y asambleas ejidales/comunitarias en coordinación con Juntas Distritales.",
            "Rutas móviles de capacitación y acercamiento de casillas para reducir costos de traslado en zonas dispersas."
        ],
        "channels": "Radio comunitaria e indigenista, asambleas locales, mercados semanales, promotorías rurales de ENCIVICA."
    },
    5: {
        "id": "P3",
        "order": 3,
        "name": "Votantes Coyunturales de AltaExpectativa",
        "subtitle": "Jóvenes-adultos urbanos (especialmente mujeres) que se movilizan en presidenciales pero se ausentan en intermedias",
        "color": "#D4AC0D",
        "badge": "Participación Intermitente (Alta Brecha)",
        "icon": "⚡",
        "narrative": "Conforman el 16.42% de la Lista Nominal: población urbana (97.1%), joven-adulta (edad media 34.7 años), con alta escolaridad (11.8 años) y fuerte predominio femenino (68.2%). Su rasgo distintivo es la mayor brecha electoral del país (19.94 pp): votan masivamente en presidenciales (60.99%) pero caen drásticamente en intermedias (41.05%).",
        "ine_strategy": "Pedagogía del Poder Legislativo y Relevancia de Elecciones Intermedias",
        "ine_actions": [
            "Campaña focalizada 'El Congreso decide tu día a día': conectar elecciones intermedias con presupuesto en cuidados, salud, seguridad y empleo.",
            "Herramientas digitales interactivas ('Conoce a tus candidatos a Diputaciones') con comparadores de propuestas en 60 segundos.",
            "Mensajes diferenciados para mujeres trabajadoras y madres jóvenes sobre el impacto legislativo local y federal."
        ],
        "channels": "Instagram, TikTok, WhatsApp, podcasts, transporte público urbano (Metro/Metrobús) y centros de trabajo."
    },
    0: {
        "id": "P4",
        "order": 4,
        "name": "Ciudadanía Activa en Desencanto",
        "subtitle": "Adultos de mediana edad en zonas urbanas y mixtas con fatiga electoral reciente",
        "color": "#2874A6",
        "badge": "Participación Media en Retroceso",
        "icon": "📉",
        "narrative": "Representan el 13.35% del padrón (edad media 46.2 años, escolaridad media-alta de 10.8 años, en secciones urbanas y mixtas). Históricamente eran votantes constantes (61.47% presidencial, 54.36% intermedia), pero muestran el mayor desgaste longitudinal (-7.21 pp de caída entre el bloque 2009-2012 y 2021-2024). Sufren fatiga o escepticismo sobre la eficacia de su voto.",
        "ine_strategy": "Reconexión Democrática, Rendición de Cuentas y Combate al Cinismo",
        "ine_actions": [
            "Campañas de eficacia política: evidenciar cómo el voto ciudadano y los organismos autónomos protegen derechos y servicios públicos.",
            "Foros ciudadanos distritales de seguimiento legislativo y exigencia de rendición de cuentas post-electoral.",
            "Simplificación de información sobre ubicación de casillas cuando hay reconfiguración o cambio de domicilio."
        ],
        "channels": "Noticieros matutinos, radio hablada, prensa digital, portales de noticias, asociaciones vecinales y gremiales."
    },
    1: {
        "id": "P5",
        "order": 5,
        "name": "Juventud Urbana Escéptica y Desconectada",
        "subtitle": "Jóvenes urbanos (predominantemente hombres de 20 a 34 años) con abstencionismo crónico",
        "color": "#CB4335",
        "badge": "Baja Participación Crítica",
        "icon": "🏙️",
        "narrative": "Es uno de los grupos más grandes y desafiantes para el INE: 21.66% de la Lista Nominal (21.3 millones de electores). Son 100% urbanos, edad media de 29.4 años, alta escolaridad (11.8 años) y mayoría masculina (69.4% hombres vs 30.6% mujeres). Apenas alcanzan 42.96% en 2024 y un crítico 33.78% en elecciones intermedias. Después de votar por primera vez a los 18 años, se desconectan entre los 20 y 34 años.",
        "ine_strategy": "Reconquista Digital, Gamificación y Transición post-Primer Voto",
        "ine_actions": [
            "Estrategia 'Tu segundo voto importa más': seguimiento cívico a jóvenes de 20 a 29 años que dejaron de votar tras cumplir 18.",
            "Alianzas con universidades, plataformas de streaming, creadores de contenido, ligas deportivas y gaming para desmitificar el proceso electoral.",
            "Campañas de actualización de credencial para jóvenes que mudaron de domicilio por estudio o primer empleo (evitar abstención por lejanía de casilla)."
        ],
        "channels": "YouTube, Twitch, TikTok, Spotify, universidades, eventos deportivos/culturales y empleadores del sector servicios/tecnología."
    },
    3: {
        "id": "P6",
        "order": 6,
        "name": "Juventud Periférica y Rural con Barreras",
        "subtitle": "Jóvenes de secciones rurales y mixtas afectados por movilidad laboral y barreras estructurales",
        "color": "#CA6F1E",
        "badge": "Baja Participación por Barreras",
        "icon": "🚧",
        "narrative": "Abarca el 12.09% de la Lista Nominal (11.88 millones): jóvenes (edad media 29.3 años, 67.4% hombres) en secciones rurales (50.7%) y mixtas (49.3%), con escolaridad media-baja (8.9 años). Tienen una tasa de participación de solo 43.10% en 2024 y 39.41% en intermedias, con tendencia negativa (-2.87 pp), explicada por migración temporal laboral, trabajo en domingo y distancia a casillas.",
        "ine_strategy": "Inclusión Territorial, Movilidad Laboral y Facilidades para Votar",
        "ine_actions": [
            "Campañas con empleadores agropecuarios, industriales y de construcción para garantizar permisos efectivos de acudir a votar el domingo electoral.",
            "Módulos itinerantes del INE para actualización ágil de domicilio en zonas periurbanas y corredores agrícolas/industriales.",
            "Educación cívica práctica en telebachilleratos, CONALEP, CBTAs y centros de trabajo sobre cómo ubicar casillas y ejercer el voto."
        ],
        "channels": "WhatsApp, Facebook local, radio regional, perifoneo, centros de trabajo agrícola/maquilador y planteles de educación media técnica."
    }
}

def generate_all_exports():
    df_macro = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_macro_2009_2024.parquet"))
    df_macro = df_macro[df_macro['EDAD'] >= 18].copy()
    
    segments = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_perfiles_segmentados.parquet"))
    
    # Mapear metadata a segments
    segments['PERFIL_ID'] = segments['CLUSTER_RAW'].map(lambda c: PROFILE_META[c]['id'])
    segments['PERFIL_ORDEN'] = segments['CLUSTER_RAW'].map(lambda c: PROFILE_META[c]['order'])
    segments['PERFIL_NOMBRE'] = segments['CLUSTER_RAW'].map(lambda c: PROFILE_META[c]['name'])
    segments['PERFIL_COLOR'] = segments['CLUSTER_RAW'].map(lambda c: PROFILE_META[c]['color'])
    segments['PERFIL_BADGE'] = segments['CLUSTER_RAW'].map(lambda c: PROFILE_META[c]['badge'])
    
    segments.to_parquet(os.path.join(OUT_DIR, "ccpc_perfiles_final.parquet"), index=False)
    
    # 1. Evolución Nacional 2009-2024
    nac_ts = df_macro.groupby('AELEC', as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
    nac_ts['TASA_SV'] = (nac_ts['SV'] / nac_ts['LN'] * 100).round(2)
    nac_ts['TASA_NV'] = (nac_ts['NV'] / nac_ts['LN'] * 100).round(2)
    nac_ts['TASA_NS'] = (nac_ts['NS'] / nac_ts['LN'] * 100).round(2)
    nac_ts['TIPO'] = nac_ts['AELEC'].apply(lambda y: 'Presidencial' if y in [2012, 2018, 2024] else 'Intermedia')
    
    # 2. Curva de Ciclo de Vida por Edad Exacta (18 a 90 años) y Sexo en 2024 vs 2018 vs 2021
    df_age_exact = df_macro[(df_macro['EDAD'] >= 18) & (df_macro['EDAD'] <= 90) & (df_macro['SEXO'].isin([0, 1]))].groupby(
        ['AELEC', 'EDAD', 'SEXO'], as_index=False
    )[['LN', 'SV']].sum()
    df_age_exact['TASA'] = (df_age_exact['SV'] / df_age_exact['LN'] * 100).round(2)
    
    # También personas no binarias en 2024
    df_nb_2024 = df_macro[(df_macro['AELEC'] == 2024) & (df_macro['SEXO'] == 2)]
    nb_ln = int(df_nb_2024['LN'].sum())
    nb_sv = int(df_nb_2024['SV'].sum())
    nb_tasa = round(nb_sv / nb_ln * 100, 2) if nb_ln > 0 else 0.0
    
    # 3.Modalidades Especiales 2024
    df_va = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_voto_anticipado_2024.parquet"))
    df_pp = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_prision_preventiva_2024.parquet"))
    
    va_summary = {
        "total": int(len(df_va)),
        "mujeres": int((df_va['SEXO'] == 1).sum()),
        "hombres": int((df_va['SEXO'] == 0).sum()),
        "pct_mujeres": round((df_va['SEXO'] == 1).mean() * 100, 1),
        "top_estados": df_va['EDONOM'].value_counts().head(5).to_dict()
    }
    pp_summary = {
        "total": int(len(df_pp)),
        "mujeres": int((df_pp['SEXO'] == 1).sum()),
        "hombres": int((df_pp['SEXO'] == 0).sum()),
        "pct_hombres": round((df_pp['SEXO'] == 0).mean() * 100, 1),
        "top_estados": df_pp['EDONOM'].value_counts().head(5).to_dict()
    }
    
    # 4. Resumen detallado de los 6 Perfiles Ciudadanos
    profiles_list = []
    for c_raw, meta in sorted(PROFILE_META.items(), key=lambda x: x[1]['order']):
        sub = segments[segments['CLUSTER_RAW'] == c_raw]
        w = sub['LN_2024']
        w_sum = w.sum()
        
        ts_years = {}
        for y in [2009, 2012, 2015, 2018, 2021, 2024]:
            ts_years[str(y)] = round(float(np.average(sub[f'TASA_{y}'], weights=w) * 100), 2)
            
        # Distribución por región
        reg_dist = sub.groupby('REGION')['LN_2024'].sum() / w_sum * 100
        # Distribución por grupo de edad
        age_dist = sub.groupby('GRUPO_EDAD')['LN_2024'].sum() / w_sum * 100
        # Distribución por tipo de sección
        sec_dist = sub.groupby('TIPOSEC')['LN_2024'].sum() / w_sum * 100
        
        profiles_list.append({
            **meta,
            "cluster_raw": int(c_raw),
            "ln_2024": int(w_sum),
            "sv_2024": int(sub['SV_2024'].sum()),
            "nv_2024": int(sub['NV_2024'].sum()),
            "pct_padron": round(float(w_sum / segments['LN_2024'].sum() * 100), 2),
            "tasa_2024": round(float(sub['SV_2024'].sum() / w_sum * 100), 2),
            "tasa_pres": round(float(np.average(sub['TASA_PRESIDENCIAL'], weights=w) * 100), 2),
            "tasa_inter": round(float(np.average(sub['TASA_INTERMEDIA'], weights=w) * 100), 2),
            "brecha_pres_inter": round(float(np.average(sub['BRECHA_PRES_INTER'], weights=w) * 100), 2),
            "edad_media": round(float(np.average(sub['EDAD_APROX'], weights=w)), 1),
            "pct_mujer": round(float(np.average(sub['ES_MUJER'], weights=w) * 100), 1),
            "pct_hombre": round(100.0 - float(np.average(sub['ES_MUJER'], weights=w) * 100), 1),
            "pct_urbano": round(float(np.average(sub['ES_URBANO'], weights=w) * 100), 1),
            "pct_rural": round(float(np.average(sub['ES_RURAL'], weights=w) * 100), 1),
            "pct_mixto": round(max(0.0, 100.0 - float(np.average(sub['ES_URBANO'], weights=w) * 100) - float(np.average(sub['ES_RURAL'], weights=w) * 100)), 1),
            "escolaridad_est": round(float(np.average(sub['ESCOLARIDAD_EST'], weights=w)), 1),
            "tendencia_lp": round(float(np.average(sub['TENDENCIA_LARGO_PLAZO'], weights=w) * 100), 2),
            "evolucion_anual": ts_years,
            "regiones": {k: round(float(v), 1) for k, v in reg_dist.to_dict().items()},
            "grupos_edad": {k: round(float(v), 1) for k, v in age_dist.to_dict().items()},
            "tipo_seccion": {k: round(float(v), 1) for k, v in sec_dist.to_dict().items()}
        })
        
    # 5. Resumen por Entidad Federativa (32 Estados) con distribución de perfiles y tasas históricas
    state_list = []
    for edocve, grp in segments.groupby('EDOCVE'):
        edonom = grp['EDONOM'].iloc[0]
        region = grp['REGION'].iloc[0]
        ln_tot = grp['LN_2024'].sum()
        sv_tot = grp['SV_2024'].sum()
        tasa_24 = round(float(sv_tot / ln_tot * 100), 2)
        tasa_pres = round(float(np.average(grp['TASA_PRESIDENCIAL'], weights=grp['LN_2024']) * 100), 2)
        tasa_inter = round(float(np.average(grp['TASA_INTERMEDIA'], weights=grp['LN_2024']) * 100), 2)
        
        p_dist = grp.groupby('PERFIL_ID')['LN_2024'].sum() / ln_tot * 100
        p_dict = {f"P{i}": round(float(p_dist.get(f"P{i}", 0.0)), 1) for i in range(1, 7)}
        dom_perfil = max(p_dict.items(), key=lambda x: x[1])[0]
        
        # Tasas por año del estado
        st_years = {}
        for y in [2009, 2012, 2015, 2018, 2021, 2024]:
            st_years[str(y)] = round(float(np.average(grp[f'TASA_{y}'], weights=grp['LN_2024']) * 100), 2)
            
        state_list.append({
            "edocve": int(edocve),
            "edonom": edonom,
            "region": region,
            "ln_2024": int(ln_tot),
            "sv_2024": int(sv_tot),
            "tasa_2024": tasa_24,
            "tasa_pres": tasa_pres,
            "tasa_inter": tasa_inter,
            "brecha": round(tasa_pres - tasa_inter, 2),
            "escolaridad": round(float(np.average(grp['ESCOLARIDAD_EST'], weights=grp['LN_2024'])), 1),
            "perfiles_pct": p_dict,
            "perfil_dominante": dom_perfil,
            "evolucion": st_years
        })
        
    # 6. Resumen por Tipo de Sección y Sexo
    tiposec_sex = df_macro[df_macro['SEXO'].isin([0, 1])].groupby(['AELEC', 'TIPOSEC', 'SEXO'], as_index=False)[['LN', 'SV']].sum()
    tiposec_sex['TASA'] = (tiposec_sex['SV'] / tiposec_sex['LN'] * 100).round(2)
    
    dashboard_payload = {
        "kpis_globales": {
            "total_registros_procesados": 54872712,
            "total_archivos_csv": 194,
            "elecciones_analizadas": [2009, 2012, 2015, 2018, 2021, 2024],
            "ln_2024": int(nac_ts[nac_ts['AELEC'] == 2024]['LN'].iloc[0]),
            "sv_2024": int(nac_ts[nac_ts['AELEC'] == 2024]['SV'].iloc[0]),
            "tasa_2024": float(nac_ts[nac_ts['AELEC'] == 2024]['TASA_SV'].iloc[0]),
            "tasa_media_presidencial": round(float(nac_ts[nac_ts['TIPO'] == 'Presidencial']['TASA_SV'].mean()), 2),
            "tasa_media_intermedia": round(float(nac_ts[nac_ts['TIPO'] == 'Intermedia']['TASA_SV'].mean()), 2),
            "no_binario_2024": {"ln": nb_ln, "sv": nb_sv, "tasa": nb_tasa},
            "voto_anticipado_2024": va_summary,
            "prision_preventiva_2024": pp_summary
        },
        "nacional_anual": nac_ts.to_dict(orient="records"),
        "perfiles": profiles_list,
        "estados": sorted(state_list, key=lambda x: x['tasa_2024'], reverse=True),
        "edad_exacta_2024": df_age_exact[df_age_exact['AELEC'] == 2024].to_dict(orient="records"),
        "edad_exacta_2021": df_age_exact[df_age_exact['AELEC'] == 2021].to_dict(orient="records"),
        "edad_exacta_2018": df_age_exact[df_age_exact['AELEC'] == 2018].to_dict(orient="records"),
        "tiposec_sexo": tiposec_sex.to_dict(orient="records")
    }
    
    with open(os.path.join(OUT_DIR, "dashboard_data.json"), "w", encoding="utf-8") as f:
        json.dump(dashboard_payload, f, ensure_ascii=False, indent=2)
        
    print("Exportación de dashboard_data.json completada exitosamente!")
    print(f"No binario 2024: LN={nb_ln}, SV={nb_sv}, Tasa={nb_tasa}%")
    print(f"Voto anticipado 2024: {va_summary['total']} registros ({va_summary['pct_mujeres']}% mujeres)")
    print(f"Prisión preventiva 2024: {pp_summary['total']} registros ({pp_summary['pct_hombres']}% hombres)")

if __name__ == "__main__":
    generate_all_exports()
