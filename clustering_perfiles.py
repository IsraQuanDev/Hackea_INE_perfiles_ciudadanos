import os
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")

# Escolaridad promedio aproximada (años de estudio INEGI 2020) por entidad y ajuste por tipo de sección (U/M/R) y edad
STATE_SCHOOLING_BASE = {
    1: 10.3, 2: 10.2, 3: 10.3, 4: 9.6, 5: 10.4, 6: 10.0, 7: 7.8, 8: 10.0,
    9: 11.5, 10: 9.7, 11: 9.0, 12: 8.4, 13: 9.4, 14: 9.9, 15: 10.1, 16: 8.6,
    17: 9.8, 18: 9.7, 19: 10.7, 20: 8.1, 21: 9.2, 22: 10.5, 23: 10.2, 24: 9.6,
    25: 10.2, 26: 10.4, 27: 9.7, 28: 10.1, 29: 9.8, 30: 8.7, 31: 9.6, 32: 9.2
}

TIPOSEC_SCHOOLING_ADJ = {'U': 1.15, 'M': -0.45, 'R': -2.10}
AGE_SCHOOLING_ADJ = {
    '18-19': 0.8, '20-24': 1.2, '25-29': 1.1, '30-34': 0.8,
    '35-39': 0.5, '40-49': 0.1, '50-59': -0.6, '60-69': -1.5, '70+': -2.8
}

AGE_MIDPOINT = {
    '18-19': 18.5, '20-24': 22.0, '25-29': 27.0, '30-34': 32.0,
    '35-39': 37.0, '40-49': 44.5, '50-59': 54.5, '60-69': 64.5, '70+': 77.0
}

def run_analysis():
    print("Cargando datos macro...")
    df_macro = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_macro_2009_2024.parquet"))
    
    # Filtrar edades válidas >= 18
    df_macro = df_macro[df_macro['EDAD'] >= 18].copy()
    
    # 1. Resumen Nacional por Año
    nac_year = df_macro.groupby('AELEC', as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
    nac_year['TASA_PART'] = (nac_year['SV'] / nac_year['LN'] * 100).round(2)
    nac_year['TIPO_ELECCION'] = nac_year['AELEC'].apply(lambda y: 'Presidencial' if y in [2012, 2018, 2024] else 'Intermedia')
    print("\n--- PARTICIPACIÓN NACIONAL 2009-2024 ---")
    print(nac_year.to_string(index=False))
    
    # 2. Resumen por Grupo de Edad y Sexo en 2024 vs Histórico
    age_sex_year = df_macro[df_macro['SEXO'].isin([0, 1])].groupby(['AELEC', 'GRUPO_EDAD', 'SEXO'], as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
    age_sex_year['TASA_PART'] = (age_sex_year['SV'] / age_sex_year['LN'] * 100).round(2)
    
    # 3. Construir Matriz de Segmentación de Perfiles Ciudadanos (Celdas Sociodemográficas Longitudinales 2009-2024)
    # Unidad de perfilamiento: (EDOCVE, EDONOM, REGION, TIPOSEC, SEXO, GRUPO_EDAD) para SEXO in (0, 1)
    df_cells = df_macro[df_macro['SEXO'].isin([0, 1])].groupby(
        ['AELEC', 'EDOCVE', 'EDONOM', 'REGION', 'TIPOSEC', 'SEXO', 'GRUPO_EDAD'], as_index=False
    )[['LN', 'SV', 'NV', 'NS']].sum()
    df_cells['TASA'] = df_cells['SV'] / df_cells['LN'].replace(0, np.nan)
    
    # Pivotar años para tener la serie de tiempo completa de cada segmento sociodemográfico
    piv_tasa = df_cells.pivot_table(
        index=['EDOCVE', 'EDONOM', 'REGION', 'TIPOSEC', 'SEXO', 'GRUPO_EDAD'],
        columns='AELEC',
        values='TASA'
    ).reset_index()
    
    piv_ln = df_cells[df_cells['AELEC'] == 2024].groupby(
        ['EDOCVE', 'EDONOM', 'REGION', 'TIPOSEC', 'SEXO', 'GRUPO_EDAD'], as_index=False
    )[['LN', 'SV', 'NV', 'NS']].sum().rename(columns={'LN': 'LN_2024', 'SV': 'SV_2024', 'NV': 'NV_2024', 'NS': 'NS_2024'})
    
    segments = piv_tasa.merge(piv_ln, on=['EDOCVE', 'EDONOM', 'REGION', 'TIPOSEC', 'SEXO', 'GRUPO_EDAD'], how='inner')
    
    # Renombrar columnas de años
    year_cols = [2009, 2012, 2015, 2018, 2021, 2024]
    for y in year_cols:
        segments[f'TASA_{y}'] = segments[y].fillna(segments[2024])
    segments.drop(columns=year_cols, inplace=True)
    
    # Ingeniería de variables (Features de comportamiento electoral y sociodemografía)
    segments['TASA_PRESIDENCIAL'] = segments[['TASA_2012', 'TASA_2018', 'TASA_2024']].mean(axis=1)
    segments['TASA_INTERMEDIA'] = segments[['TASA_2009', 'TASA_2015', 'TASA_2021']].mean(axis=1)
    segments['TASA_MEDIA_HIST'] = segments[[f'TASA_{y}' for y in year_cols]].mean(axis=1)
    
    # Brecha Presidencial vs Intermedia (Intermitencia electoral / Votante de coyuntura)
    segments['BRECHA_PRES_INTER'] = segments['TASA_PRESIDENCIAL'] - segments['TASA_INTERMEDIA']
    
    # Tendencia secular (cambio reciente 2018-2024 vs 2009-2015)
    segments['TENDENCIA_RECIENTE'] = segments['TASA_2024'] - segments['TASA_2018']
    segments['TENDENCIA_LARGO_PLAZO'] = ((segments['TASA_2021'] + segments['TASA_2024']) / 2) - ((segments['TASA_2009'] + segments['TASA_2012']) / 2)
    
    # Volatilidad
    segments['VOLATILIDAD'] = segments[[f'TASA_{y}' for y in year_cols]].std(axis=1)
    
    # Variables sociodemográficas numéricas e inferidas
    segments['EDAD_APROX'] = segments['GRUPO_EDAD'].map(AGE_MIDPOINT).astype(float)
    segments['ES_MUJER'] = (segments['SEXO'] == 1).astype(int)
    segments['ES_URBANO'] = (segments['TIPOSEC'] == 'U').astype(int)
    segments['ES_RURAL'] = (segments['TIPOSEC'] == 'R').astype(int)
    
    # Escolaridad estimada (años de estudio promedio según Estado + Tipo Sección + Cohorte Edad)
    segments['ESCOLARIDAD_EST'] = (
        segments['EDOCVE'].map(STATE_SCHOOLING_BASE) +
        segments['TIPOSEC'].map(TIPOSEC_SCHOOLING_ADJ) +
        segments['GRUPO_EDAD'].map(AGE_SCHOOLING_ADJ)
    ).clip(lower=4.5, upper=15.5).round(1)
    
    def classify_schooling(yrs):
        if yrs < 8.5:
            return 'Básica (Primaria/Secundaria trunca)'
        elif yrs < 10.5:
            return 'Media (Secundaria/Media Superior)'
        else:
            return 'Media Superior y Superior'
    segments['NIVEL_ESCOLARIDAD'] = segments['ESCOLARIDAD_EST'].apply(classify_schooling)
    
    # 4. Aplicar Clustering sobre el comportamiento electoral y ciclo de vida
    feature_cols = [
        'TASA_MEDIA_HIST',
        'TASA_2024',
        'BRECHA_PRES_INTER',
        'TENDENCIA_LARGO_PLAZO',
        'EDAD_APROX',
        'ES_URBANO',
        'ES_RURAL',
        'ESCOLARIDAD_EST'
    ]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(segments[feature_cols])
    
    # Evaluar K entre 4 y 7 con Silhouette Score
    sil_scores = {}
    for k in range(4, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=20)
        labels = km.fit_predict(X_scaled, sample_weight=segments['LN_2024'].values)
        sil = silhouette_score(X_scaled, labels)
        sil_scores[k] = round(sil, 4)
    print("\nSilhouette scores por K:", sil_scores)
    
    # Usaremos K=6 perfiles ciudadanos bien diferenciados y accionables para el INE
    K_OPT = 6
    kmeans = KMeans(n_clusters=K_OPT, random_state=42, n_init=30)
    segments['CLUSTER_RAW'] = kmeans.fit_predict(X_scaled, sample_weight=segments['LN_2024'].values)
    
    # Analizar estadísticas de cada cluster para asignar nombres narrativos coherentes
    cluster_summary = []
    for c in range(K_OPT):
        sub = segments[segments['CLUSTER_RAW'] == c]
        w = sub['LN_2024']
        w_sum = w.sum()
        
        tasa_2024 = (sub['SV_2024'].sum() / w_sum) * 100
        tasa_pres = np.average(sub['TASA_PRESIDENCIAL'], weights=w) * 100
        tasa_inter = np.average(sub['TASA_INTERMEDIA'], weights=w) * 100
        brecha = tasa_pres - tasa_inter
        edad_media = np.average(sub['EDAD_APROX'], weights=w)
        pct_mujer = np.average(sub['ES_MUJER'], weights=w) * 100
        pct_urbano = np.average(sub['ES_URBANO'], weights=w) * 100
        pct_rural = np.average(sub['ES_RURAL'], weights=w) * 100
        esc_media = np.average(sub['ESCOLARIDAD_EST'], weights=w)
        tend = np.average(sub['TENDENCIA_LARGO_PLAZO'], weights=w) * 100
        
        cluster_summary.append({
            'cluster_raw': c,
            'ln_2024': int(w_sum),
            'pct_padron': round(w_sum / segments['LN_2024'].sum() * 100, 2),
            'tasa_2024': round(tasa_2024, 2),
            'tasa_pres': round(tasa_pres, 2),
            'tasa_inter': round(tasa_inter, 2),
            'brecha_pres_inter': round(brecha, 2),
            'edad_media': round(edad_media, 1),
            'pct_mujer': round(pct_mujer, 1),
            'pct_urbano': round(pct_urbano, 1),
            'pct_rural': round(pct_rural, 1),
            'escolaridad_est': round(esc_media, 1),
            'tendencia_lp': round(tend, 2)
        })
        
    df_csum = pd.DataFrame(cluster_summary)
    print("\n--- RESUMEN DE CLUSTERS (RAW) ---")
    print(df_csum.to_string(index=False))
    
    segments.to_parquet(os.path.join(OUT_DIR, "ccpc_perfiles_segmentados.parquet"), index=False)
    df_csum.to_json(os.path.join(OUT_DIR, "cluster_raw_summary.json"), orient="records", indent=2)

if __name__ == "__main__":
    run_analysis()
