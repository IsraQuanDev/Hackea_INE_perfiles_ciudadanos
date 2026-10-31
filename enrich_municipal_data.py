import os
import json
import numpy as np
import pandas as pd

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")

with open(os.path.join(OUT_DIR, "dashboard_data.json"), "r", encoding="utf-8") as f:
    payload = json.load(f)

df_mun = pd.read_parquet(os.path.join(OUT_DIR, "ccpc_municipio_2009_2024.parquet"))
df_m24 = df_mun[df_mun["AELEC"] == 2024].copy()

# Agregación por Municipio Total en 2024 + Jóvenes (18-29) vs Adultos Mayores (60+) + Mujeres vs Hombres
df_m24["IS_JOVEN"] = df_m24["GRUPO_EDAD"].isin(["18-19", "20-24", "25-29"]).astype(int)
df_m24["IS_MAYOR"] = df_m24["GRUPO_EDAD"].isin(["60-69", "70+"]).astype(int)
df_m24["IS_MUJER"] = (df_m24["SEXO"] == 1).astype(int)
df_m24["IS_HOMBRE"] = (df_m24["SEXO"] == 0).astype(int)
df_m24["IS_RURAL"] = (df_m24["TIPOSEC"] == "R").astype(int)

df_m24["LN_JOVEN"] = df_m24["LN"] * df_m24["IS_JOVEN"]
df_m24["SV_JOVEN"] = df_m24["SV"] * df_m24["IS_JOVEN"]
df_m24["LN_MAYOR"] = df_m24["LN"] * df_m24["IS_MAYOR"]
df_m24["SV_MAYOR"] = df_m24["SV"] * df_m24["IS_MAYOR"]
df_m24["LN_MUJER"] = df_m24["LN"] * df_m24["IS_MUJER"]
df_m24["SV_MUJER"] = df_m24["SV"] * df_m24["IS_MUJER"]
df_m24["LN_HOMBRE"] = df_m24["LN"] * df_m24["IS_HOMBRE"]
df_m24["SV_HOMBRE"] = df_m24["SV"] * df_m24["IS_HOMBRE"]
df_m24["LN_RURAL"] = df_m24["LN"] * df_m24["IS_RURAL"]

mun_agg = df_m24.groupby(["EDOCVE", "EDONOM", "MPIOCVE", "MPIONOM"], as_index=False)[
    ["LN", "SV", "NV", "LN_JOVEN", "SV_JOVEN", "LN_MAYOR", "SV_MAYOR", "LN_MUJER", "SV_MUJER", "LN_HOMBRE", "SV_HOMBRE", "LN_RURAL"]
].sum()

# También traer tasa de 2021 por municipio para calcular brecha municipal
df_m21 = df_mun[df_mun["AELEC"] == 2021].groupby(["EDOCVE", "MPIOCVE"], as_index=False)[["LN", "SV"]].sum()
df_m21["TASA_2021"] = (df_m21["SV"] / df_m21["LN"].replace(0, np.nan) * 100).round(2)

mun_agg = mun_agg.merge(df_m21[["EDOCVE", "MPIOCVE", "TASA_2021"]], on=["EDOCVE", "MPIOCVE"], how="left")
mun_agg["TASA_2024"] = (mun_agg["SV"] / mun_agg["LN"].replace(0, np.nan) * 100).round(2)
mun_agg["TASA_2021"] = mun_agg["TASA_2021"].fillna(mun_agg["TASA_2024"] - 9.5).round(2)
mun_agg["BRECHA"] = (mun_agg["TASA_2024"] - mun_agg["TASA_2021"]).round(2)
mun_agg["TASA_JOVEN"] = (mun_agg["SV_JOVEN"] / mun_agg["LN_JOVEN"].replace(0, np.nan) * 100).fillna(0).round(1)
mun_agg["TASA_MAYOR"] = (mun_agg["SV_MAYOR"] / mun_agg["LN_MAYOR"].replace(0, np.nan) * 100).fillna(0).round(1)
mun_agg["TASA_MUJER"] = (mun_agg["SV_MUJER"] / mun_agg["LN_MUJER"].replace(0, np.nan) * 100).fillna(0).round(1)
mun_agg["TASA_HOMBRE"] = (mun_agg["SV_HOMBRE"] / mun_agg["LN_HOMBRE"].replace(0, np.nan) * 100).fillna(0).round(1)
mun_agg["PCT_RURAL"] = (mun_agg["LN_RURAL"] / mun_agg["LN"].replace(0, np.nan) * 100).fillna(0).round(1)

# Clasificar el perfil prioritario de intervención de cada municipio
def assign_mun_profile(row):
    if row["PCT_RURAL"] >= 50:
        if row["TASA_JOVEN"] < 46:
            return "P6"
        return "P2"
    else:
        if row["TASA_JOVEN"] < 42:
            return "P5"
        elif row["BRECHA"] > 14:
            return "P3"
        elif row["TASA_2024"] >= 62:
            return "P1"
        else:
            return "P4"

mun_agg["PERFIL_DOM"] = mun_agg.apply(assign_mun_profile, axis=1)

# Filtrar municipios válidos (MPIOCVE > 0)
mun_agg = mun_agg[mun_agg["MPIOCVE"] > 0].sort_values(["EDOCVE", "LN"], ascending=[True, False])

municipios_compact = []
for _, r in mun_agg.iterrows():
    municipios_compact.append({
        "e": int(r["EDOCVE"]),
        "m": int(r["MPIOCVE"]),
        "n": str(r["MPIONOM"]),
        "ln": int(r["LN"]),
        "sv": int(r["SV"]),
        "t24": float(r["TASA_2024"]),
        "t21": float(r["TASA_2021"]),
        "br": float(r["BRECHA"]),
        "tj": float(r["TASA_JOVEN"]),
        "tm": float(r["TASA_MAYOR"]),
        "tf": float(r["TASA_MUJER"]),
        "th": float(r["TASA_HOMBRE"]),
        "pr": float(r["PCT_RURAL"]),
        "p": str(r["PERFIL_DOM"])
    })

payload["municipios_2024"] = municipios_compact

with open(os.path.join(OUT_DIR, "dashboard_data_pro.json"), "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False)

print(f"Exportados {len(municipios_compact)} municipios en dashboard_data_pro.json ({os.path.getsize(os.path.join(OUT_DIR, 'dashboard_data_pro.json'))/1024:.1f} KB)")
