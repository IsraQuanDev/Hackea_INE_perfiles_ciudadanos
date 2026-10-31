import os
import glob
import time
import json
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.csv as pv
import pyarrow.parquet as pq

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")
os.makedirs(OUT_DIR, exist_ok=True)

YEARS = ['2009', '2012', '2015', '2018', '2021', '2024']

# Regiones INE / ENCIVICA estándar (5 circunscripciones o regiones socio-geográficas)
REGION_MAP = {
    1: 'Centro-Occidente', 2: 'Noroeste', 3: 'Noroeste', 4: 'Sur-Sureste',
    5: 'Noreste', 6: 'Centro-Occidente', 7: 'Sur-Sureste', 8: 'Noroeste',
    9: 'Centro', 10: 'Noroeste', 11: 'Centro-Occidente', 12: 'Sur-Sureste',
    13: 'Centro', 14: 'Centro-Occidente', 15: 'Centro', 16: 'Centro-Occidente',
    17: 'Centro', 18: 'Centro-Occidente', 19: 'Noreste', 20: 'Sur-Sureste',
    21: 'Centro', 22: 'Centro-Occidente', 23: 'Sur-Sureste', 24: 'Noreste',
    25: 'Noroeste', 26: 'Noroeste', 27: 'Sur-Sureste', 28: 'Noreste',
    29: 'Centro', 30: 'Sur-Sureste', 31: 'Sur-Sureste', 32: 'Noreste'
}

CIRCUNSCRIPCION_MAP = {
    2: 1, 3: 1, 8: 1, 10: 1, 14: 1, 18: 1, 25: 1, 26: 1,
    1: 2, 5: 2, 11: 2, 19: 2, 22: 2, 24: 2, 28: 2, 32: 2,
    4: 3, 7: 3, 20: 3, 23: 3, 27: 3, 30: 3, 31: 3,
    9: 4, 12: 4, 17: 4, 21: 4, 29: 4,
    6: 5, 13: 5, 15: 5, 16: 5
}

STATE_NAMES = {
    1: 'Aguascalientes', 2: 'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
    5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua',
    9: 'Ciudad de México', 10: 'Durango', 11: 'Guanajuato', 12: 'Guerrero',
    13: 'Hidalgo', 14: 'Jalisco', 15: 'Estado de México', 16: 'Michoacán',
    17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
    21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
    25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas',
    29: 'Tlaxcala', 30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'
}

# Escolaridad promedio aproximada (años de estudio INEGI 2020) por entidad y ajuste por tipo de sección (U/M/R)
STATE_SCHOOLING_BASE = {
    1: 10.3, 2: 10.2, 3: 10.3, 4: 9.6, 5: 10.4, 6: 10.0, 7: 7.8, 8: 10.0,
    9: 11.5, 10: 9.7, 11: 9.0, 12: 8.4, 13: 9.4, 14: 9.9, 15: 10.1, 16: 8.6,
    17: 9.8, 18: 9.7, 19: 10.7, 20: 8.1, 21: 9.2, 22: 10.5, 23: 10.2, 24: 9.6,
    25: 10.2, 26: 10.4, 27: 9.7, 28: 10.1, 29: 9.8, 30: 8.7, 31: 9.6, 32: 9.2
}

def assign_age_group(edad_series):
    bins = [17, 19, 24, 29, 34, 39, 49, 59, 69, 200]
    labels = ['18-19', '20-24', '25-29', '30-34', '35-39', '40-49', '50-59', '60-69', '70+']
    return pd.cut(edad_series, bins=bins, labels=labels)

def process_all_years():
    t0 = time.time()
    
    # Listas para acumular agregaciones por año
    agg_macro_list = []      # AELEC, EDOCVE, TIPOSEC, SEXO, EDAD -> LN, SV, NV, NS
    agg_mun_list = []        # AELEC, EDOCVE, MPIOCVE, MPIONOM, TIPOSEC, SEXO, GRUPO_EDAD -> LN, SV, NV, NS
    agg_sec_list = []        # AELEC, EDOCVE, MPIOCVE, SECCION, TIPOSEC -> LN, SV, NV, NS, LN_JOVEN, SV_JOVEN, LN_ADULTO, SV_ADULTO, LN_MAYOR, SV_MAYOR, LN_MUJER, SV_MUJER, LN_HOMBRE, SV_HOMBRE
    
    total_files = 0
    total_rows = 0
    
    for y in YEARS:
        ty = time.time()
        folder = os.path.join(BASE_DIR, f"DatosAbiertos_DECEyEC_ConteosCensales{y}")
        files = sorted(glob.glob(os.path.join(folder, "*.csv")))
        print(f"Procesando año {y} ({len(files)} archivos)...")
        
        for f in files:
            total_files += 1
            tbl = pv.read_csv(f, read_options=pv.ReadOptions(use_threads=True))
            total_rows += tbl.num_rows
            df = tbl.to_pandas()
            
            # Normalizar nombres de columnas por si acaso
            df.columns = [c.strip().upper() for c in df.columns]
            
            # Limpiar TIPOSEC
            df['TIPOSEC'] = df['TIPOSEC'].fillna('U').astype(str).str.strip().str.upper()
            df.loc[~df['TIPOSEC'].isin(['U', 'M', 'R']), 'TIPOSEC'] = 'U'
            
            # Asegurar tipos numéricos
            for col in ['LN', 'SV', 'NV', 'NS', 'EDAD', 'SEXO', 'EDOCVE', 'MPIOCVE', 'SECCION']:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(np.int64)
            
            df['AELEC'] = int(y)
            
            # 1. Agregación Macro: AELEC, EDOCVE, TIPOSEC, SEXO, EDAD
            g_macro = df.groupby(['AELEC', 'EDOCVE', 'TIPOSEC', 'SEXO', 'EDAD'], as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
            agg_macro_list.append(g_macro)
            
            # 2. Grupo de edad para municipio
            df['GRUPO_EDAD'] = assign_age_group(df['EDAD']).astype(str)
            mpio_names = df.groupby(['EDOCVE', 'MPIOCVE'])['MPIONOM'].first().reset_index()
            g_mun = df.groupby(['AELEC', 'EDOCVE', 'MPIOCVE', 'TIPOSEC', 'SEXO', 'GRUPO_EDAD'], as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
            g_mun = g_mun.merge(mpio_names, on=['EDOCVE', 'MPIOCVE'], how='left')
            agg_mun_list.append(g_mun)
            
            # 3. Resumen por Sección Electoral (para seguimiento longitudinal de secciones)
            df['IS_JOVEN'] = (df['EDAD'] <= 29).astype(np.int64)
            df['IS_ADULTO'] = ((df['EDAD'] >= 30) & (df['EDAD'] <= 59)).astype(np.int64)
            df['IS_MAYOR'] = (df['EDAD'] >= 60).astype(np.int64)
            df['IS_MUJER'] = (df['SEXO'] == 1).astype(np.int64)
            df['IS_HOMBRE'] = (df['SEXO'] == 0).astype(np.int64)
            
            df['LN_JOVEN'] = df['LN'] * df['IS_JOVEN']
            df['SV_JOVEN'] = df['SV'] * df['IS_JOVEN']
            df['LN_ADULTO'] = df['LN'] * df['IS_ADULTO']
            df['SV_ADULTO'] = df['SV'] * df['IS_ADULTO']
            df['LN_MAYOR'] = df['LN'] * df['IS_MAYOR']
            df['SV_MAYOR'] = df['SV'] * df['IS_MAYOR']
            df['LN_MUJER'] = df['LN'] * df['IS_MUJER']
            df['SV_MUJER'] = df['SV'] * df['IS_MUJER']
            df['LN_HOMBRE'] = df['LN'] * df['IS_HOMBRE']
            df['SV_HOMBRE'] = df['SV'] * df['IS_HOMBRE']
            
            sec_cols = ['LN', 'SV', 'NV', 'NS', 'LN_JOVEN', 'SV_JOVEN', 'LN_ADULTO', 'SV_ADULTO', 'LN_MAYOR', 'SV_MAYOR', 'LN_MUJER', 'SV_MUJER', 'LN_HOMBRE', 'SV_HOMBRE']
            g_sec = df.groupby(['AELEC', 'EDOCVE', 'MPIOCVE', 'SECCION', 'TIPOSEC'], as_index=False)[sec_cols].sum()
            agg_sec_list.append(g_sec)
            
        print(f"  Año {y} completado en {time.time()-ty:.2f}s")

    print(f"Consolidando tablas ({total_rows:,} filas leídas de {total_files} archivos)...")
    
    df_macro = pd.concat(agg_macro_list, ignore_index=True)
    df_macro = df_macro.groupby(['AELEC', 'EDOCVE', 'TIPOSEC', 'SEXO', 'EDAD'], as_index=False)[['LN', 'SV', 'NV', 'NS']].sum()
    df_macro['EDONOM'] = df_macro['EDOCVE'].map(STATE_NAMES)
    df_macro['REGION'] = df_macro['EDOCVE'].map(REGION_MAP)
    df_macro['CIRCUNSCRIPCION'] = df_macro['EDOCVE'].map(CIRCUNSCRIPCION_MAP)
    df_macro['GRUPO_EDAD'] = assign_age_group(df_macro['EDAD']).astype(str)
    
    df_mun = pd.concat(agg_mun_list, ignore_index=True)
    df_mun['EDONOM'] = df_mun['EDOCVE'].map(STATE_NAMES)
    df_mun['REGION'] = df_mun['EDOCVE'].map(REGION_MAP)
    
    df_sec = pd.concat(agg_sec_list, ignore_index=True)
    
    # Guardar en Parquet para acceso instantáneo
    df_macro.to_parquet(os.path.join(OUT_DIR, "ccpc_macro_2009_2024.parquet"), index=False)
    df_mun.to_parquet(os.path.join(OUT_DIR, "ccpc_municipio_2009_2024.parquet"), index=False)
    df_sec.to_parquet(os.path.join(OUT_DIR, "ccpc_seccion_2009_2024.parquet"), index=False)
    
    # Procesar Modalidades Especiales 2024
    va_file = os.path.join(BASE_DIR, "DatosAbiertos_DECEyEC_ConteosCensales_VotoAnticipado2024", "DatosAbiertos_DECEyEC_ConteosCensales_VotoAnticipado2024", "datosabiertos_deceyec_conteoscensales_votoanticipado2024.csv")
    pp_file = os.path.join(BASE_DIR, "DatosAbiertos_DECEyEC_ConteosCensales_PrisionPreventiva2024", "DatosAbiertos_DECEyEC_ConteosCensales_PrisionPreventiva2024", "datosabiertos_deceyec_conteoscensales_prisionpreventiva2024.csv")
    
    df_va = pd.read_csv(va_file)
    df_pp = pd.read_csv(pp_file)
    df_va.to_parquet(os.path.join(OUT_DIR, "ccpc_voto_anticipado_2024.parquet"), index=False)
    df_pp.to_parquet(os.path.join(OUT_DIR, "ccpc_prision_preventiva_2024.parquet"), index=False)
    
    print(f"Pipeline finalizado con éxito en {time.time()-t0:.2f}s!")
    print(f"  Macro rows: {len(df_macro):,}")
    print(f"  Municipio rows: {len(df_mun):,}")
    print(f"  Seccion rows: {len(df_sec):,}")

if __name__ == "__main__":
    process_all_years()
