import os
import json

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")
ART_DIR = r"C:\Users\52477\.gemini\antigravity\brain\60e0a364-5707-46f9-80a9-29e34ccdae7c"

with open(os.path.join(OUT_DIR, "dashboard_data_pro.json"), "r", encoding="utf-8") as f:
    payload = json.load(f)

json_str = json.dumps(payload, ensure_ascii=False)

html_code = r"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HACKEA LA PARTICIPACIÓN — Plataforma de Inteligencia Cívica CCPC 2009–2024 (INE)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    * { box-sizing: border-box; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: transparent; }
    .custom-scroll::-webkit-scrollbar-thumb { background: rgba(142, 36, 170, 0.35); border-radius: 999px; }
    .glass-header {
      background: linear-gradient(135deg, #2A0838 0%, #5B1E6E 50%, #8E24AA 100%);
    }
    .ine-badge {
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.28);
      backdrop-filter: blur(8px);
    }
    .tab-pill {
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .tab-pill.active {
      background: #6B21A8;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(107, 33, 168, 0.35);
    }
    .card-hover {
      transition: transform 0.18s ease, box-shadow 0.18s ease;
    }
    .card-hover:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.12);
    }
    .svg-tooltip {
      position: fixed;
      pointer-events: none;
      z-index: 9999;
      opacity: 0;
      transition: opacity 0.12s ease;
    }
    input[type="range"] {
      accent-color: #8E24AA;
    }
    @media print {
      .no-print { display: none !important; }
    }
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased selection:bg-purple-600 selection:text-white">

  <!-- TOOLTIP FLOTANTE GLOBAL -->
  <div id="global-tooltip" class="svg-tooltip bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3.5 py-2.5 shadow-xl text-xs max-w-xs"></div>

  <!-- HERO HEADER INSTITUCIONAL INE / ENCIVICA -->
  <header class="glass-header text-white border-b border-purple-900/40">
    <div class="max-w-[1440px] mx-auto px-6 py-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="ine-badge px-3 py-1 rounded-full text-xs font-semibold tracking-wider uppercase">INE · DECEyEC · ENCÍVICA 2024–2026</span>
            <span class="ine-badge px-3 py-1 rounded-full text-xs font-semibold text-amber-300">Reto 1: Perfiles Ciudadanos de Participación</span>
            <span class="ine-badge px-3 py-1 rounded-full text-xs font-medium text-emerald-300">100% Datos Censales 2009–2024</span>
          </div>
          <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight">
            HACKEA LA PARTICIPACIÓN: <span class="text-amber-300">Datos que Construyen Democracia</span>
          </h1>
          <p class="text-sm text-purple-100/90 mt-1 max-w-3xl">
            Sistema de Inteligencia Sociodemográfica y Segmentación Electoral basado en <strong class="text-white">54,872,712 registros agregados</strong> de los Cuadernillos de la Lista Nominal (32 Entidades · 2,477 Municipios · 6 Elecciones Federales).
          </p>
        </div>

        <!-- ACCIONES RÁPIDAS Y PITCH MODE -->
        <div class="flex flex-wrap items-center gap-2.5 no-print">
          <button onclick="openPitchModal()" class="px-4 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-bold text-xs shadow-lg flex items-center gap-2 transition cursor-pointer">
            <span>🏆</span> Guía de Pitch para Jurado INE
          </button>
          <button onclick="exportFilteredMunicipalCSV()" class="px-3.5 py-2.5 rounded-xl ine-badge hover:bg-white/25 text-white font-semibold text-xs flex items-center gap-1.5 transition cursor-pointer">
            <span>⬇️</span> Exportar CSV Municipal
          </button>
        </div>
      </div>

      <!-- CINTA DE KPIs CENSALES GLOBALES -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mt-5">
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Registros Procesados</div>
          <div class="text-xl font-extrabold mt-0.5">54,872,712</div>
          <div class="text-xs text-emerald-300 font-medium mt-0.5">194 archivos CSV (2009–2024)</div>
        </div>
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Lista Nominal CCPC 2024</div>
          <div class="text-xl font-extrabold mt-0.5">98,330,348</div>
          <div class="text-xs text-amber-300 font-medium mt-0.5">54,899,228 sí votaron (55.83%)</div>
        </div>
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Brecha Pres. vs Interm.</div>
          <div class="text-xl font-extrabold mt-0.5">+13.03 pp</div>
          <div class="text-xs text-purple-100 mt-0.5">58.63% Pres. vs 45.60% Inter.</div>
        </div>
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Liderazgo Femenino 2024</div>
          <div class="text-xl font-extrabold mt-0.5">+7.68 pp</div>
          <div class="text-xs text-pink-200 font-medium mt-0.5">Mujeres 59.51% vs Hombres 51.83%</div>
        </div>
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Valle Abstención Joven</div>
          <div class="text-xl font-extrabold mt-0.5">37.8% Mín.</div>
          <div class="text-xs text-rose-300 font-medium mt-0.5">Hombres 25–27 años (Crítico)</div>
        </div>
        <div class="ine-badge rounded-xl p-3.5">
          <div class="text-xs text-purple-200 font-medium uppercase">Inclusión 2024 (VA·PP·NB)</div>
          <div class="text-xl font-extrabold mt-0.5">30,117</div>
          <div class="text-xs text-emerald-300 font-medium mt-0.5">No Binario: 75.24% (79/105)</div>
        </div>
      </div>
    </div>
  </header>

  <!-- BARRA DE NAVEGACIÓN MODULAR STICKY -->
  <nav class="sticky top-0 z-40 bg-[var(--card)]/95 backdrop-blur-md border-b border-[var(--border)] shadow-sm no-print">
    <div class="max-w-[1440px] mx-auto px-6 py-2.5 flex items-center justify-between gap-3 overflow-x-auto">
      <div class="flex items-center gap-2">
        <button onclick="switchView('view-perfiles', this)" class="tab-pill active px-4 py-2 rounded-xl text-xs sm:text-sm font-bold cursor-pointer whitespace-nowrap">
          🧩 1. Los 6 Perfiles Ciudadanos (Clustering)
        </button>
        <button onclick="switchView('view-ciclo', this)" class="tab-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-[var(--muted-foreground)] hover:text-[var(--foreground)] cursor-pointer whitespace-nowrap">
          📈 2. Ciclo de Vida Electoral y Brechas (2009–2024)
        </button>
        <button onclick="switchView('view-territorio', this)" class="tab-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-[var(--muted-foreground)] hover:text-[var(--foreground)] cursor-pointer whitespace-nowrap">
          🗺️ 3. Atlas Territorial (32 Estados y 2,477 Municipios)
        </button>
        <button onclick="switchView('view-simulador', this)" class="tab-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-[var(--muted-foreground)] hover:text-[var(--foreground)] cursor-pointer whitespace-nowrap">
          🎯 4. Laboratorio de Campañas INE & Simulador
        </button>
        <button onclick="switchView('view-inclusion', this)" class="tab-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-[var(--muted-foreground)] hover:text-[var(--foreground)] cursor-pointer whitespace-nowrap">
          ⚖️ 5. Inclusión 2024 (Voto Anticipado, Prisión Prev. y No Binario)
        </button>
      </div>
      <div class="hidden xl:flex items-center gap-2 text-xs text-[var(--muted-foreground)] font-medium">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span> Motor Vectorial Activo · Sin Dependencias Externas
      </div>
    </div>
  </nav>

  <!-- CONTENEDOR PRINCIPAL -->
  <main class="max-w-[1440px] mx-auto px-6 py-6 space-y-6">

    <!-- =====================================================================
         VISTA 1: LOS 6 PERFILES CIUDADANOS (CLUSTERING K-MEANS PONDERADO)
         ===================================================================== -->
    <section id="view-perfiles" class="view-section space-y-6">
      <!-- Explicación ejecutiva del método -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-md bg-purple-500/15 text-purple-600 dark:text-purple-300 text-xs font-bold uppercase">Metodología de Segmentación</span>
            <span class="text-xs text-[var(--muted-foreground)]">K-Means Ponderado por Lista Nominal (`sample_weight = LN_2024`) · Estandarización Z-Score</span>
          </div>
          <h2 class="text-lg font-bold mt-1">¿Qué tipos de ciudadanía existen en México según su comportamiento de participación (2009–2024)?</h2>
          <p class="text-xs sm:text-sm text-[var(--muted-foreground)] mt-0.5">
            Haz clic en cualquiera de los <strong>6 Perfiles Ciudadanos</strong> en el mapa de burbujas o en las tarjetas inferiores para inspeccionar su huella demográfica (radar), evolución en las 6 elecciones y estrategia focalizada de comunicación para el INE.
          </p>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <span class="text-xs font-semibold text-[var(--muted-foreground)]">Filtrar tarjetas:</span>
          <select id="filter-profile-badge" onchange="renderProfileCardsGrid()" class="bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
            <option value="ALL">Todos los Perfiles (6)</option>
            <option value="ALTA">Alta Participación Constante (P1, P2)</option>
            <option value="MEDIA">Participación Coyuntural / En Desgaste (P3, P4)</option>
            <option value="BAJA">Abstencionismo Joven Prioritario (P5, P6)</option>
          </select>
        </div>
      </div>

      <!-- Fila Interactiva: Mapa de Burbujas + Inspector Dinámico del Perfil Seleccionado (Radar + Evolución) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Mapa de Segmentación Sociodemográfica (7 cols) -->
        <div class="lg:col-span-7 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between gap-2 mb-1">
              <h3 class="font-bold text-base">Mapa Sociodemográfico de Clusters (Edad vs Participación 2024)</h3>
              <div class="flex items-center gap-1.5">
                <span class="text-xs text-[var(--muted-foreground)]">Eje Y:</span>
                <select id="cluster-y-metric" onchange="renderClusterBubbleSVG()" class="bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-lg px-2.5 py-1 text-xs font-semibold">
                  <option value="tasa_2024">Participación 2024 (%)</option>
                  <option value="tasa_inter">Participación Elección Intermedia (%)</option>
                  <option value="brecha_pres_inter">Brecha Presidencial vs Intermedia (pp)</option>
                  <option value="escolaridad_est">Escolaridad Estimada (Años)</option>
                </select>
              </div>
            </div>
            <p class="text-xs text-[var(--muted-foreground)] mb-3">
              El tamaño de cada burbuja representa su peso en la Lista Nominal 2024. <strong>Haz clic en una burbuja</strong> para actualizar el panel de diagnóstico derecho.
            </p>
          </div>
          <div id="svg-cluster-bubble" class="w-full h-[340px]"></div>
          <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 mt-3 pt-3 border-t border-[var(--border)]" id="cluster-quick-buttons"></div>
        </div>

        <!-- Inspector Profundo del Perfil Seleccionado (5 cols) -->
        <div class="lg:col-span-5 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col justify-between" id="profile-inspector-panel">
          <!-- Se llena dinámicamente con renderProfileInspector(selectedProfileId) -->
        </div>
      </div>

      <!-- Comparativa de Barras Horizontales Presidencial vs Intermedia + Trayectoria 2009-2024 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <h3 class="font-bold text-base">Contraste Electoral: Elección Presidencial vs Intermedia por Perfil</h3>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">
            El Perfil <strong>P3 (Votantes Coyunturales)</strong> sufre una caída de <strong>19.94 pp</strong> en intermedias, mientras que <strong>P5 (Juventud Urbana)</strong> cae hasta <strong>33.78%</strong>.
          </p>
          <div id="svg-cluster-bars" class="w-full h-[300px]"></div>
        </div>

        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <h3 class="font-bold text-base">Trayectoria Longitudinal de los 6 Perfiles (CCPC 2009–2024)</h3>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">
            Seguimiento a través de 6 elecciones federales: se observa el crecimiento de <strong>P1 (+3.67 pp)</strong> y el desgaste de <strong>P4 (-7.21 pp)</strong>.
          </p>
          <div id="svg-profiles-timeline" class="w-full h-[300px]"></div>
        </div>
      </div>

      <!-- Tarjetas Ejecutivas de los 6 Perfiles con Narrativa y Estrategias INE -->
      <div>
        <h3 class="font-bold text-lg mb-3">Catálogo Narrativo y Estrategias Diferenciadas de Fomento al Voto (INE / DECEyEC)</h3>
        <div id="profiles-cards-grid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5"></div>
      </div>
    </section>

    <!-- =====================================================================
         VISTA 2: CICLO DE VIDA ELECTORAL Y BRECHAS (2009–2024)
         ===================================================================== -->
    <section id="view-ciclo" class="view-section hidden space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Curva de Edad Exacta 18 a 90 años -->
        <div class="lg:col-span-8 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-1">
            <div>
              <h3 class="font-bold text-base">Curva del Ciclo de Vida Electoral por Edad Exacta (18 a 90 años) y Sexo</h3>
              <p class="text-xs text-[var(--muted-foreground)]">
                Pasa el cursor sobre cualquier edad exacta para comparar la participación de Mujeres y Hombres en 2024, 2021 y 2018.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <label class="text-xs font-semibold flex items-center gap-1 cursor-pointer">
                <input type="checkbox" id="chk-show-2021" checked onchange="renderAgeLifecycleSVG()"> Mostrar 2021 (Intermedia)
              </label>
              <label class="text-xs font-semibold flex items-center gap-1 cursor-pointer">
                <input type="checkbox" id="chk-show-2018" onchange="renderAgeLifecycleSVG()"> Mostrar 2018 (Pres.)
              </label>
            </div>
          </div>
          <div id="svg-age-lifecycle" class="w-full h-[370px] mt-2"></div>
        </div>

        <!-- Hallazgos Clave del Ciclo de Vida -->
        <div class="lg:col-span-4 space-y-4">
          <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
            <span class="px-2.5 py-1 rounded-full bg-rose-500/15 text-rose-500 text-xs font-bold uppercase">Hallazgo Crítico 1</span>
            <h4 class="font-bold text-base mt-2">La Paradoja del "Segundo Voto" (20–34 años)</h4>
            <p class="text-xs text-[var(--muted-foreground)] mt-1 leading-relaxed">
              A los <strong>18 años</strong>, la ciudadanía estrena su credencial con entusiasmo (<strong>55.1% Mujeres / 48.9% Hombres</strong> en 2024). Pero inmediatamente después se abre una fosa de abstención que toca fondo a los <strong>26 años en hombres (37.8%)</strong> y <strong>25 años en mujeres (48.5%)</strong>. En intermedias (2021), los hombres de 24 a 28 años caen hasta <strong>28.4%</strong>.
            </p>
            <div class="mt-3 p-3 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs">
              <strong>Causa raíz:</strong> Movilidad residencial por universidad o primer empleo sin actualizar el domicilio de la credencial INE, sumado a desconexión con partidos.
            </div>
          </div>

          <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
            <span class="px-2.5 py-1 rounded-full bg-purple-500/15 text-purple-500 text-xs font-bold uppercase">Hallazgo Crítico 2</span>
            <h4 class="font-bold text-base mt-2">Las Mujeres Sostienen la Democracia Mexicana</h4>
            <p class="text-xs text-[var(--muted-foreground)] mt-1 leading-relaxed">
              En todas las edades entre los <strong>18 y los 75 años</strong>, las mujeres superan a los hombres. La brecha máxima ocurre entre los <strong>25 y los 39 años (+11.8 pp a +12.5 pp a favor de las mujeres)</strong>. Solo a partir de los 76 años la tasa masculina supera a la femenina por brechas de movilidad física y viudez.
            </p>
          </div>
        </div>
      </div>

      <!-- Evolución Nacional 2009-2024 + Brecha Urbano/Mixto/Rural -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <h3 class="font-bold text-base">Evolución Censal Nacional (2009–2024): Lista Nominal vs Votantes Efectivos</h3>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">
            Crecimiento del padrón en cuadernillos de 77.48 millones (2009) a 98.33 millones (2024).
          </p>
          <div id="svg-national-history" class="w-full h-[310px]"></div>
        </div>

        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <h3 class="font-bold text-base">Participación por Tipo de Sección Electoral (Urbana, Mixta, Rural) y Sexo</h3>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">
            Las secciones <strong>Rurales (R)</strong> superan a las Urbanas en elecciones intermedias gracias a la cohesión comunitaria.
          </p>
          <div id="svg-tiposec-chart" class="w-full h-[310px]"></div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         VISTA 3: ATLAS TERRITORIAL (32 ENTIDADES Y 2,477 MUNICIPIOS)
         ===================================================================== -->
    <section id="view-territorio" class="view-section hidden space-y-6">
      <!-- Controles de Filtro Regional y Estatal -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-wrap items-center justify-between gap-4">
        <div class="flex flex-wrap items-center gap-3">
          <div>
            <label class="block text-xs font-bold text-[var(--muted-foreground)] uppercase">Región INE / Circunscripción:</label>
            <select id="terr-region-select" onchange="updateTerritorialView()" class="mt-1 bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
              <option value="ALL">Todas las Regiones (32 Entidades)</option>
              <option value="Centro">Región Centro (CDMX, Edomex, Hgo, Mor, Pue, Tlax)</option>
              <option value="Centro-Occidente">Región Centro-Occidente (Ags, Col, Gto, Jal, Mich, Nay, Qro)</option>
              <option value="Noreste">Región Noreste (Coah, NL, SLP, Tamps, Zac)</option>
              <option value="Noroeste">Región Noroeste (BC, BCS, Chih, Dgo, Sin, Son)</option>
              <option value="Sur-Sureste">Región Sur-Sureste (Camp, Chis, Gro, Oax, QRoo, Tab, Ver, Yuc)</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-[var(--muted-foreground)] uppercase">Entidad Federativa (Drill-Down Municipal):</label>
            <select id="terr-state-select" onchange="updateStateDrilldown()" class="mt-1 bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold"></select>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <div>
            <label class="block text-xs font-bold text-[var(--muted-foreground)] uppercase">Buscar Municipio (entre los 2,477):</label>
            <input type="text" id="mun-search-input" oninput="renderMunicipalTable()" placeholder="Ej. Ecatepec, Mérida, Benito Juárez..." class="mt-1 bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs w-64">
          </div>
        </div>
      </div>

      <!-- Gráficas Estatales: Composición de Perfiles + Serie Histórica de la Entidad Seleccionada -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-7 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <h3 class="font-bold text-base">Ranking y Mezcla de Perfiles Ciudadanos por Entidad Federativa</h3>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">
            Barras apiladas con el peso porcentual de cada perfil (`P1` a `P6`) en la Lista Nominal estatal. Haz clic en una entidad para filtrar sus municipios.
          </p>
          <div id="svg-states-stacked" class="w-full h-[460px] overflow-y-auto custom-scroll pr-2"></div>
        </div>

        <div class="lg:col-span-5 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between">
              <span class="px-2.5 py-0.5 rounded-md bg-purple-500/15 text-purple-500 text-xs font-bold uppercase" id="st-detail-region">Región</span>
              <span class="text-xs font-bold text-[var(--muted-foreground)]" id="st-detail-ln">LN 2024</span>
            </div>
            <h3 class="font-extrabold text-xl mt-1" id="st-detail-name">Selecciona una Entidad</h3>
            <div class="grid grid-cols-4 gap-2 my-3 p-3 rounded-xl bg-[var(--background)] border border-[var(--border)] text-center">
              <div>
                <div class="text-sm font-extrabold text-purple-600 dark:text-purple-400" id="st-kpi-24">--%</div>
                <div class="text-xs text-[var(--muted-foreground)]">Voto 2024</div>
              </div>
              <div>
                <div class="text-sm font-extrabold" id="st-kpi-pres">--%</div>
                <div class="text-xs text-[var(--muted-foreground)]">Media Pres.</div>
              </div>
              <div>
                <div class="text-sm font-extrabold" id="st-kpi-inter">--%</div>
                <div class="text-xs text-[var(--muted-foreground)]">Media Inter.</div>
              </div>
              <div>
                <div class="text-sm font-extrabold text-amber-600" id="st-kpi-esc">-- años</div>
                <div class="text-xs text-[var(--muted-foreground)]">Escolaridad</div>
              </div>
            </div>
          </div>

          <div>
            <h4 class="text-xs font-bold uppercase text-[var(--muted-foreground)] mb-1">Trayectoria Estatal vs Promedio Nacional (2009–2024)</h4>
            <div id="svg-single-state-ts" class="w-full h-[210px]"></div>
          </div>

          <div class="mt-3 pt-3 border-t border-[var(--border)]">
            <h4 class="text-xs font-bold uppercase text-[var(--muted-foreground)] mb-2">Distribución de los 6 Perfiles en la Entidad</h4>
            <div id="st-profiles-mini-bars" class="space-y-1.5"></div>
          </div>
        </div>
      </div>

      <!-- Tabla Interactiva de los Municipios de la Entidad (o Búsqueda Global) -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
          <div>
            <h3 class="font-bold text-base" id="mun-table-title">Explorador Municipal CCPC 2024 (2,477 Municipios)</h3>
            <p class="text-xs text-[var(--muted-foreground)]">
              Comparativa de participación general, voto joven (18–29 años), voto adulto mayor (60+), brecha de género y perfil prioritario de intervención INE.
            </p>
          </div>
          <div class="flex items-center gap-2">
            <label class="text-xs font-semibold text-[var(--muted-foreground)]">Ordenar por:</label>
            <select id="mun-sort-select" onchange="renderMunicipalTable()" class="bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-lg px-2.5 py-1.5 text-xs font-semibold">
              <option value="ln_desc">Mayor Lista Nominal (Padrón)</option>
              <option value="t24_desc">Mayor Participación 2024 (%)</option>
              <option value="t24_asc">Menor Participación 2024 (Prioridad INE)</option>
              <option value="tj_asc">Menor Voto Joven 18-29 años (Crítico)</option>
              <option value="br_desc">Mayor Brecha Presidencial-Intermedia</option>
            </select>
          </div>
        </div>

        <div class="overflow-x-auto max-h-[440px] custom-scroll border border-[var(--border)] rounded-xl">
          <table class="w-full text-left border-collapse text-xs">
            <thead class="bg-[var(--background)] sticky top-0 z-10 border-b border-[var(--border)]">
              <tr>
                <th class="py-3 px-3 font-bold">Municipio</th>
                <th class="py-3 px-3 font-bold">Entidad</th>
                <th class="py-3 px-3 font-bold text-right">Lista Nominal 2024</th>
                <th class="py-3 px-3 font-bold text-right">Part. 2024</th>
                <th class="py-3 px-3 font-bold text-right">Part. 2021</th>
                <th class="py-3 px-3 font-bold text-right">Jóvenes (18–29)</th>
                <th class="py-3 px-3 font-bold text-right">Mayores (60+)</th>
                <th class="py-3 px-3 font-bold text-right">Mujeres vs Hombres</th>
                <th class="py-3 px-3 font-bold text-right">% Rural</th>
                <th class="py-3 px-3 font-bold">Perfil Prioritario INE</th>
              </tr>
            </thead>
            <tbody id="mun-table-tbody" class="divide-y divide-[var(--border)]"></tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         VISTA 4: LABORATORIO DE CAMPAÑAS INE & SIMULADOR DE IMPACTO
         ===================================================================== -->
    <section id="view-simulador" class="view-section hidden space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Clasificador Ciudadano y Recomendador de Campaña (6 cols) -->
        <div class="lg:col-span-6 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col justify-between">
          <div>
            <span class="px-2.5 py-0.5 rounded-md bg-purple-500/15 text-purple-500 text-xs font-bold uppercase">Motor de Segmentación en Tiempo Real</span>
            <h3 class="font-bold text-lg mt-1">Clasificador de Perfil Ciudadano y Generador de Campaña</h3>
            <p class="text-xs text-[var(--muted-foreground)] mb-4">
              Configura un segmento objetivo para obtener su clasificación CCPC, probabilidad de voto y plan de medios diferenciados para las Juntas Locales y Distritales del INE.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              <div>
                <label class="block text-xs font-bold mb-1">1. Cohorte de Edad:</label>
                <select id="lab-edad" onchange="runCampaignLab()" class="w-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
                  <option value="18-19">18 a 19 años (Primer Voto)</option>
                  <option value="20-24" selected>20 a 24 años (Transición post-18)</option>
                  <option value="25-29">25 a 29 años (Adultez Joven)</option>
                  <option value="30-34">30 a 34 años</option>
                  <option value="35-39">35 a 39 años</option>
                  <option value="40-49">40 a 49 años</option>
                  <option value="50-59">50 a 59 años</option>
                  <option value="60-69">60 a 69 años (Adulto Mayor)</option>
                  <option value="70+">70 años o más</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold mb-1">2. Sexo / Identidad:</label>
                <select id="lab-sexo" onchange="runCampaignLab()" class="w-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
                  <option value="0" selected>Hombres (SEXO = 0)</option>
                  <option value="1">Mujeres (SEXO = 1)</option>
                  <option value="2">No Binario (SEXO = 2)</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold mb-1">3. Tipo de Sección Electoral:</label>
                <select id="lab-tiposec" onchange="runCampaignLab()" class="w-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
                  <option value="U" selected>Urbana (U)</option>
                  <option value="M">Mixta (M)</option>
                  <option value="R">Rural (R)</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold mb-1">4. Proceso Electoral Objetivo:</label>
                <select id="lab-eleccion" onchange="runCampaignLab()" class="w-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] rounded-xl px-3 py-2 text-xs font-semibold">
                  <option value="INTER" selected>Elección Intermedia (2027)</option>
                  <option value="PRES">Elección Presidencial (2030)</option>
                </select>
              </div>
            </div>
          </div>

          <div id="lab-output-card" class="mt-5"></div>
        </div>

        <!-- Simulador What-If de Movilización Nacional (6 cols) -->
        <div class="lg:col-span-6 bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm flex flex-col justify-between">
          <div>
            <span class="px-2.5 py-0.5 rounded-md bg-emerald-500/15 text-emerald-500 text-xs font-bold uppercase">Simulador Paramétrico de Política Pública</span>
            <h3 class="font-bold text-lg mt-1">Calculadora "What-If" de Movilización Nacional (Rumbo a 2027 / 2030)</h3>
            <p class="text-xs text-[var(--muted-foreground)] mb-4">
              Ajusta las metas de incremento en puntos porcentuales (pp) sobre los tres perfiles con déficit de participación para proyectar cuántos nuevos votantes sumaría el INE y cuál sería la nueva tasa nacional.
            </p>

            <div class="space-y-3 bg-[var(--background)] border border-[var(--border)] rounded-xl p-4">
              <div>
                <div class="flex justify-between text-xs font-bold mb-1">
                  <span>🏙️ Meta Incremento en P5: Juventud Urbana Escéptica (21.30M LN)</span>
                  <span id="lbl-slider-p5" class="text-purple-600 dark:text-purple-400">+6.0 pp</span>
                </div>
                <input type="range" id="slider-p5" min="0" max="20" step="0.5" value="6" oninput="updateWhatIfSimulator()" class="w-full">
              </div>

              <div>
                <div class="flex justify-between text-xs font-bold mb-1">
                  <span>⚡ Meta Incremento en P3: Votantes Coyunturales en Intermedia (16.14M LN)</span>
                  <span id="lbl-slider-p3" class="text-amber-600">+8.0 pp</span>
                </div>
                <input type="range" id="slider-p3" min="0" max="20" step="0.5" value="8" oninput="updateWhatIfSimulator()" class="w-full">
              </div>

              <div>
                <div class="flex justify-between text-xs font-bold mb-1">
                  <span>🚧 Meta Incremento en P6: Juventud Periférica y Rural (11.88M LN)</span>
                  <span id="lbl-slider-p6" class="text-orange-600">+5.0 pp</span>
                </div>
                <input type="range" id="slider-p6" min="0" max="20" step="0.5" value="5" oninput="updateWhatIfSimulator()" class="w-full">
              </div>

              <div>
                <div class="flex justify-between text-xs font-bold mb-1">
                  <span>📉 Meta Recuperación en P4: Adultos en Desencanto (13.12M LN)</span>
                  <span id="lbl-slider-p4" class="text-sky-600">+4.0 pp</span>
                </div>
                <input type="range" id="slider-p4" min="0" max="15" step="0.5" value="4" oninput="updateWhatIfSimulator()" class="w-full">
              </div>
            </div>
          </div>

          <div id="whatif-results-banner" class="my-4"></div>
          <div id="svg-whatif-bars" class="w-full h-[210px]"></div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         VISTA 5: INCLUSIÓN Y NUEVAS MODALIDADES 2024 (VA, PP Y NO BINARIO)
         ===================================================================== -->
    <section id="view-inclusion" class="view-section hidden space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Casilla No Binaria 2024 -->
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 rounded-full bg-purple-500/15 text-purple-500 text-xs font-bold uppercase">Identidad No Binaria (SEXO = 2)</span>
            <span class="text-2xl">🏳️‍🌈</span>
          </div>
          <h3 class="font-extrabold text-xl mt-2">75.24% de Participación</h3>
          <p class="text-xs text-[var(--muted-foreground)] mt-1">
            En 2024, por primera vez los Conteos Censales registraron el marcador `SEXO = 2` (Personas No Binarias). De <strong>105 personas en Lista Nominal</strong>, <strong>79 ejercieron su voto</strong>, superando en <strong>+19.41 pp</strong> el promedio nacional (55.83%).
          </p>
          <div class="mt-4 p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs space-y-1.5">
            <div class="flex justify-between"><span>Lista Nominal (`LN`):</span><strong>105 personas</strong></div>
            <div class="flex justify-between"><span>Con marca de voto (`SV`):</span><strong class="text-emerald-500">79 personas (75.24%)</strong></div>
            <div class="flex justify-between"><span>Sin marca de voto (`NV`):</span><strong>26 personas (24.76%)</strong></div>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] mt-3">
            <strong>Recomendación INE:</strong> Reconocer el efecto positivo del reconocimiento de identidad en la apropiación del derecho al voto y fortalecer protocolos contra discriminación en casilla.
          </p>
        </div>

        <!-- Voto Anticipado 2024 -->
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/15 text-emerald-500 text-xs font-bold uppercase">Voto Anticipado 2024</span>
            <span class="text-2xl">🏠</span>
          </div>
          <h3 class="font-extrabold text-xl mt-2">3,449 Votantes (62.1% Mujeres)</h3>
          <p class="text-xs text-[var(--muted-foreground)] mt-1">
            Modalidad garantizada para personas con discapacidad o limitación física (Art. 141 LGIPE). La mayoría femenina (<strong>2,141 mujeres vs 1,308 hombres</strong>) refleja la longevidad de las mujeres en el Perfil P1 (Guardianes Cívicos).
          </p>
          <div id="va-top-states" class="mt-4 space-y-2 text-xs"></div>
          <p class="text-xs text-[var(--muted-foreground)] mt-3">
            <strong>Recomendación INE:</strong> Ampliar el padrón de Voto Anticipado incluyendo a las personas cuidadoras primarias que no pueden abandonar el hogar el domingo electoral.
          </p>
        </div>

        <!-- Voto en Prisión Preventiva 2024 -->
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 rounded-full bg-amber-500/15 text-amber-500 text-xs font-bold uppercase">Prisión Preventiva 2024</span>
            <span class="text-2xl">⚖️</span>
          </div>
          <h3 class="font-extrabold text-xl mt-2">26,563 Votantes (91.2% Hombres)</h3>
          <p class="text-xs text-[var(--muted-foreground)] mt-1">
            Personas en prisión preventiva sin sentencia firme que ejercieron su derecho al sufragio (<strong>24,225 hombres y 2,338 mujeres</strong>). Demuestra que cuando el INE acerca la urna y elimina barreras físicas, los hombres jóvenes participan activamente.
          </p>
          <div id="pp-top-states" class="mt-4 space-y-2 text-xs"></div>
          <p class="text-xs text-[var(--muted-foreground)] mt-3">
            <strong>Recomendación INE:</strong> Fortalecer debates e información cívica impresa dentro de los centros penitenciarios previo a elecciones locales e intermedias.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- MODAL DE GUÍA DE PITCH PARA GANAR EL HACKATHON -->
  <div id="pitch-modal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-2xl max-w-3xl w-full p-6 shadow-2xl max-h-[88vh] overflow-y-auto custom-scroll">
      <div class="flex items-center justify-between border-b border-[var(--border)] pb-3">
        <div>
          <span class="text-xs font-bold uppercase text-purple-500">Estructura Ganadora para el Jurado del INE</span>
          <h3 class="text-xl font-extrabold">🏆 Guion Ejecutivo de Presentación (Pitch de 5 Minutos — Reto 1)</h3>
        </div>
        <button onclick="closePitchModal()" class="px-3 py-1.5 rounded-lg bg-[var(--background)] border border-[var(--border)] text-xs font-bold cursor-pointer">✕ Cerrar</button>
      </div>
      <div class="space-y-4 mt-4 text-xs sm:text-sm leading-relaxed">
        <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)]">
          <strong class="text-purple-500">1. El Gancho Censal (Minuto 0:00 – 1:00):</strong>
          "No hicimos un muestreo: procesamos los <strong>54,872,712 registros</strong> de los 194 archivos CSV de la Plataforma CCPC (2009–2024). Descubrimos que el abstencionismo en México no es uniforme: tiene edad exacta, género, territorio y coyuntura electoral."
        </div>
        <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)]">
          <strong class="text-rose-500">2. El Descubrimiento del 'Segundo Voto' y la Brecha Masculina (Minuto 1:00 – 2:15):</strong>
          "Muestren la pestaña 2 (Curva de Ciclo de Vida): A los 18 años votan el 55.1% de las mujeres y el 48.9% de los hombres, pero a los 20–29 años se desploman hasta el <strong>37.8% en hombres jóvenes</strong> (y 28.4% en intermedias). El problema no es el primer voto: es el <em>segundo voto</em> cuando el joven se muda por estudio o trabajo."
        </div>
        <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)]">
          <strong class="text-amber-500">3. Los 6 Perfiles Ciudadanos (Minuto 2:15 – 3:30):</strong>
          "Con K-Means ponderado por Lista Nominal segmentamos a los 98.3 millones de electores en 6 perfiles accionables: desde los <strong>Guardianes Cívicos Urbanos (P1, 67.96%)</strong> y la <strong>Comunidad Rural Comprometida (P2, 63.41%)</strong>, hasta los dos focos rojos: <strong>Votantes Coyunturales (P3, que caen 20 puntos en intermedias)</strong> y la <strong>Juventud Urbana Escéptica (P5, 21.3 millones con solo 33.78% en intermedias)</strong>."
        </div>
        <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)]">
          <strong class="text-emerald-500">4. Simulación de Política Pública en Vivo (Minuto 3:30 – 5:00):</strong>
          "Abran la pestaña 4 (Laboratorio INE): si el INE aplica nuestras campañas diferenciadas (<em>'Embajadores Intergeneracionales P1→P5'</em>, <em>'El Segundo Voto'</em> y <em>'Pedagogía Legislativa para P3'</em>) logrando subir apenas +6 pp en jóvenes y +8 pp en coyunturales, México sumaría <strong>más de 3.7 millones de votantes adicionales</strong> en la elección intermedia de 2027."
        </div>
      </div>
    </div>
  </div>

<script>
const DATA = __JSON_PAYLOAD__;
let SELECTED_PROFILE_ID = "P1";

const tt = document.getElementById("global-tooltip");
function showTooltip(evt, htmlContent) {
  tt.innerHTML = htmlContent;
  tt.style.opacity = "1";
  const x = Math.min(window.innerWidth - 290, evt.clientX + 14);
  const y = Math.max(12, evt.clientY - 28);
  tt.style.left = x + "px";
  tt.style.top = y + "px";
}
function hideTooltip() {
  tt.style.opacity = "0";
}

function switchView(viewId, btn) {
  document.querySelectorAll(".view-section").forEach(s => s.classList.add("hidden"));
  document.getElementById(viewId).classList.remove("hidden");
  document.querySelectorAll(".tab-pill").forEach(b => {
    b.classList.remove("active");
    b.classList.add("text-[var(--muted-foreground)]");
  });
  btn.classList.add("active");
  btn.classList.remove("text-[var(--muted-foreground)]");

  // Re-renderizar SVGs activos para ajustar dimensiones
  if (viewId === "view-perfiles") {
    renderClusterBubbleSVG();
    renderProfileInspector(SELECTED_PROFILE_ID);
    renderClusterBarsSVG();
    renderProfilesTimelineSVG();
  } else if (viewId === "view-ciclo") {
    renderAgeLifecycleSVG();
    renderNationalHistorySVG();
    renderTipoSecSVG();
  } else if (viewId === "view-territorio") {
    updateTerritorialView();
    updateStateDrilldown();
  } else if (viewId === "view-simulador") {
    runCampaignLab();
    updateWhatIfSimulator();
  }
}

function openPitchModal() {
  const m = document.getElementById("pitch-modal");
  m.classList.remove("hidden");
  m.classList.add("flex");
}
function closePitchModal() {
  const m = document.getElementById("pitch-modal");
  m.classList.add("hidden");
  m.classList.remove("flex");
}

/* ============================================================================
   1. VISTA PERFILES: MAPA DE BURBUJAS + INSPECTOR RADAR + BARRAS + TIMELINE
   ============================================================================ */
function renderClusterBubbleSVG() {
  const container = document.getElementById("svg-cluster-bubble");
  if (!container) return;
  const metricKey = document.getElementById("cluster-y-metric").value;
  const metricLabels = {
    tasa_2024: { label: "Tasa de Participación 2024 (%)", min: 35, max: 75, unit: "%" },
    tasa_inter: { label: "Participación Media Intermedia (%)", min: 28, max: 64, unit: "%" },
    brecha_pres_inter: { label: "Brecha Presidencial - Intermedia (pp)", min: 4, max: 24, unit: " pp" },
    escolaridad_est: { label: "Escolaridad Estimada (Años)", min: 5, max: 13.5, unit: " años" }
  };
  const mCfg = metricLabels[metricKey];

  const W = 640, H = 330;
  const pad = { l: 52, r: 28, t: 22, b: 42 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;

  const xMin = 22, xMax = 68;
  const xScale = v => pad.l + ((v - xMin) / (xMax - xMin)) * plotW;
  const yScale = v => pad.t + plotH - ((v - mCfg.min) / (mCfg.max - mCfg.min)) * plotH;

  let gridLines = "";
  for (let i = 0; i <= 4; i++) {
    const valY = mCfg.min + (i / 4) * (mCfg.max - mCfg.min);
    const py = yScale(valY);
    gridLines += `<line x1="${pad.l}" y1="${py}" x2="${W - pad.r}" y2="${py}" stroke="currentColor" stroke-opacity="0.1" stroke-dasharray="4 4"/>`;
    gridLines += `<text x="${pad.l - 8}" y="${py + 4}" text-anchor="end" font-size="12" fill="currentColor" fill-opacity="0.65">${valY.toFixed(0)}${mCfg.unit === '%' ? '%' : ''}</text>`;
  }
  for (let age = 25; age <= 65; age += 10) {
    const px = xScale(age);
    gridLines += `<line x1="${px}" y1="${pad.t}" x2="${px}" y2="${H - pad.b}" stroke="currentColor" stroke-opacity="0.08" stroke-dasharray="4 4"/>`;
    gridLines += `<text x="${px}" y="${H - pad.b + 18}" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.65">${age} años</text>`;
  }

  let bubbles = "";
  DATA.perfiles.forEach(p => {
    const cx = xScale(p.edad_media);
    const cy = yScale(p[metricKey]);
    const r = Math.sqrt(p.pct_padron) * 7.8;
    const isSel = p.id === SELECTED_PROFILE_ID;
    const strokeW = isSel ? 3.5 : 1.5;
    const strokeCol = isSel ? "#F59E0B" : "#FFFFFF";
    const tipHtml = `<strong>${p.icon} ${p.id}: ${p.name}</strong><br>Lista Nominal: ${(p.ln_2024/1e6).toFixed(2)}M (${p.pct_padron}%)<br>Participación 2024: <b>${p.tasa_2024}%</b><br>Intermedia: <b>${p.tasa_inter}%</b> | Brecha: <b>${p.brecha_pres_inter} pp</b><br>Edad media: ${p.edad_media} años | Mujeres: ${p.pct_mujer}%`;

    bubbles += `
      <g class="cursor-pointer" onclick="selectProfile('${p.id}')"
         onmousemove="showTooltip(event, \`${tipHtml}\`)" onmouseleave="hideTooltip()">
        ${isSel ? `<circle cx="${cx}" cy="${cy}" r="${r + 6}" fill="none" stroke="${p.color}" stroke-width="2" stroke-dasharray="4 3" opacity="0.9"/>` : ""}
        <circle cx="${cx}" cy="${cy}" r="${r}" fill="${p.color}" fill-opacity="${isSel ? '0.92' : '0.76'}" stroke="${strokeCol}" stroke-width="${strokeW}"/>
        <text x="${cx}" y="${cy - 2}" text-anchor="middle" font-size="12" font-weight="800" fill="#FFFFFF">${p.id}</text>
        <text x="${cx}" y="${cy + 12}" text-anchor="middle" font-size="12" font-weight="600" fill="#FFFFFF">${p[metricKey]}${mCfg.unit}</text>
      </g>
    `;
  });

  container.innerHTML = `
    <svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">
      ${gridLines}
      <text x="${pad.l + plotW / 2}" y="${H - 4}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor" fill-opacity="0.8">Edad Promedio del Perfil Ciudadano (años)</text>
      ${bubbles}
    </svg>
  `;

  // Botones rápidos debajo del gráfico
  const qBtns = document.getElementById("cluster-quick-buttons");
  qBtns.innerHTML = DATA.perfiles.map(p => {
    const active = p.id === SELECTED_PROFILE_ID;
    return `
      <button onclick="selectProfile('${p.id}')" class="px-2.5 py-1.5 rounded-xl text-xs font-bold border transition cursor-pointer flex items-center justify-center gap-1 ${active ? 'ring-2 ring-amber-400 shadow-sm' : 'opacity-80 hover:opacity-100'}" style="background:${ active ? p.color : 'transparent'}; color:${active ? '#FFF' : 'inherit'}; border-color:${p.color}">
        <span>${p.icon}</span> <span>${p.id} (${p.pct_padron}%)</span>
      </button>
    `;
  }).join("");
}

function selectProfile(profileId) {
  SELECTED_PROFILE_ID = profileId;
  renderClusterBubbleSVG();
  renderProfileInspector(profileId);
}

function renderProfileInspector(profileId) {
  const p = DATA.perfiles.find(x => x.id === profileId) || DATA.perfiles[0];
  const panel = document.getElementById("profile-inspector-panel");
  if (!panel) return;

  // Construir Radar SVG de 5 ejes normalizados (0 a 100)
  const axes = [
    { name: "Voto 2024", val: Math.min(100, (p.tasa_2024 / 75) * 100), raw: p.tasa_2024 + "%" },
    { name: "Lealtad Interm.", val: Math.min(100, (p.tasa_inter / 65) * 100), raw: p.tasa_inter + "%" },
    { name: "% Mujeres", val: p.pct_mujer, raw: p.pct_mujer + "%" },
    { name: "Escolaridad", val: Math.min(100, (p.escolaridad_est / 13) * 100), raw: p.escolaridad_est + " años" },
    { name: "Urbanización", val: p.pct_urbano, raw: p.pct_urbano + "%" }
  ];

  const cx = 115, cy = 98, maxR = 68;
  let radarGrid = "";
  [0.33, 0.66, 1.0].forEach(level => {
    const pts = axes.map((_, idx) => {
      const ang = -Math.PI / 2 + (idx * 2 * Math.PI) / axes.length;
      return `${cx + Math.cos(ang) * maxR * level},${cy + Math.sin(ang) * maxR * level}`;
    }).join(" ");
    radarGrid += `<polygon points="${pts}" fill="none" stroke="currentColor" stroke-opacity="0.15" stroke-width="1"/>`;
  });

  let axisLines = "";
  let polyPts = [];
  axes.forEach((ax, idx) => {
    const ang = -Math.PI / 2 + (idx * 2 * Math.PI) / axes.length;
    const x2 = cx + Math.cos(ang) * maxR;
    const y2 = cy + Math.sin(ang) * maxR;
    const lx = cx + Math.cos(ang) * (maxR + 22);
    const ly = cy + Math.sin(ang) * (maxR + 16);
    axisLines += `<line x1="${cx}" y1="${cy}" x2="${x2}" y2="${y2}" stroke="currentColor" stroke-opacity="0.2"/>`;
    axisLines += `<text x="${lx}" y="${ly + 4}" text-anchor="middle" font-size="12" font-weight="600" fill="currentColor" fill-opacity="0.85">${ax.name}</text>`;
    const vx = cx + Math.cos(ang) * maxR * (ax.val / 100);
    const vy = cy + Math.sin(ang) * maxR * (ax.val / 100);
    polyPts.push(`${vx},${vy}`);
  });

  panel.innerHTML = `
    <div>
      <div class="flex items-start justify-between gap-2 pb-3 border-b border-[var(--border)]">
        <div>
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold text-white" style="background:${p.color}">Perfil Seleccionado · ${p.id}</span>
          <h3 class="text-lg font-extrabold mt-1">${p.icon} ${p.name}</h3>
          <p class="text-xs text-[var(--muted-foreground)]">${p.subtitle}</p>
        </div>
        <div class="text-right shrink-0">
          <div class="text-xl font-extrabold" style="color:${p.color}">${p.tasa_2024}%</div>
          <div class="text-xs text-[var(--muted-foreground)]">${(p.ln_2024/1e6).toFixed(2)}M Electores</div>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 items-center my-2">
        <svg viewBox="0 0 230 195" class="w-full h-[175px]">
          ${radarGrid}
          ${axisLines}
          <polygon points="${polyPts.join(' ')}" fill="${p.color}" fill-opacity="0.35" stroke="${p.color}" stroke-width="2.5"/>
        </svg>
        <div class="space-y-1.5 text-xs">
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Peso en Padrón:</span><strong>${p.pct_padron}% (${(p.ln_2024/1e6).toFixed(2)}M)</strong></div>
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Media Presidencial:</span><strong>${p.tasa_pres}%</strong></div>
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Media Intermedia:</span><strong>${p.tasa_inter}%</strong></div>
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Brecha Coyuntural:</span><strong class="text-amber-500">${p.brecha_pres_inter} pp</strong></div>
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Edad / Escolaridad:</span><strong>${p.edad_media} años · ${p.escolaridad_est} esc.</strong></div>
          <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]"><span>Composición Sexo:</span><strong>${p.pct_mujer}% M / ${p.pct_hombre}% H</strong></div>
        </div>
      </div>
    </div>

    <div class="p-3.5 rounded-xl border-l-4 bg-[var(--background)] text-xs space-y-1.5" style="border-left-color:${p.color}">
      <div class="font-bold uppercase tracking-wide" style="color:${p.color}">🎯 Estrategia INE: ${p.ine_strategy}</div>
      <ul class="list-disc pl-4 space-y-1 text-[var(--foreground)]">
        ${p.ine_actions.map(a => `<li>${a}</li>`).join("")}
      </ul>
      <div class="pt-1 text-[var(--muted-foreground)]"><strong>Canales clave:</strong> ${p.channels}</div>
    </div>
  `;
}

function renderClusterBarsSVG() {
  const container = document.getElementById("svg-cluster-bars");
  if (!container) return;
  const W = 580, H = 290;
  const pad = { l: 155, r: 45, t: 15, b: 30 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const rowH = plotH / DATA.perfiles.length;

  let rows = "";
  DATA.perfiles.forEach((p, idx) => {
    const y0 = pad.t + idx * rowH;
    const wPres = (p.tasa_pres / 80) * plotW;
    const wInter = (p.tasa_inter / 80) * plotW;
    const shortName = `${p.id}: ${p.name.split(" ").slice(0, 3).join(" ")}`;

    rows += `
      <g class="cursor-pointer" onclick="selectProfile('${p.id}')">
        <text x="${pad.l - 8}" y="${y0 + rowH / 2 + 4}" text-anchor="end" font-size="12" font-weight="700" fill="currentColor">${shortName}</text>
        <rect x="${pad.l}" y="${y0 + 6}" width="${wPres}" height="${rowH / 2 - 6}" rx="4" fill="${p.color}" fill-opacity="0.9"/>
        <text x="${pad.l + wPres + 5}" y="${y0 + rowH / 4 + 7}" font-size="12" font-weight="700" fill="currentColor">${p.tasa_pres}%</text>
        <rect x="${pad.l}" y="${y0 + rowH / 2 + 1}" width="${wInter}" height="${rowH / 2 - 6}" rx="4" fill="#D97706" fill-opacity="0.75"/>
        <text x="${pad.l + wInter + 5}" y="${y0 + (3 * rowH) / 4 + 2}" font-size="12" font-weight="600" fill="#D97706">${p.tasa_inter}%</text>
      </g>
    `;
  });

  container.innerHTML = `
    <svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">
      ${rows}
      <text x="${pad.l}" y="${H - 4}" font-size="12" fill="currentColor" fill-opacity="0.7">■ Barra superior: Media Presidencial (2012, 2018, 2024) · ■ Barra ámbar: Media Intermedia (2009, 2015, 2021)</text>
    </svg>
  `;
}

function renderProfilesTimelineSVG() {
  const container = document.getElementById("svg-profiles-timeline");
  if (!container) return;
  const W = 580, H = 290;
  const pad = { l: 44, r: 48, t: 18, b: 36 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const years = ["2009", "2012", "2015", "2018", "2021", "2024"];
  const yMin = 28, yMax = 74;

  const xScale = idx => pad.l + (idx / (years.length - 1)) * plotW;
  const yScale = v => pad.t + plotH - ((v - yMin) / (yMax - yMin)) * plotH;

  let grid = "";
  for (let v = 30; v <= 70; v += 10) {
    const py = yScale(v);
    grid += `<line x1="${pad.l}" y1="${py}" x2="${W - pad.r}" y2="${py}" stroke="currentColor" stroke-opacity="0.1" stroke-dasharray="3 3"/>`;
    grid += `<text x="${pad.l - 6}" y="${py + 4}" text-anchor="end" font-size="12" fill="currentColor" fill-opacity="0.65">${v}%</text>`;
  }
  years.forEach((yr, idx) => {
    const px = xScale(idx);
    grid += `<text x="${px}" y="${H - 10}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor" fill-opacity="0.8">${yr}</text>`;
  });

  let lines = "";
  DATA.perfiles.forEach(p => {
    const pts = years.map((yr, idx) => `${xScale(idx)},${yScale(p.evolucion_anual[yr])}`).join(" ");
    const lastY = yScale(p.evolucion_anual["2024"]);
    lines += `<polyline points="${pts}" fill="none" stroke="${p.color}" stroke-width="2.6"/>`;
    years.forEach((yr, idx) => {
      const cx = xScale(idx), cy = yScale(p.evolucion_anual[yr]);
      lines += `<circle cx="${cx}" cy="${cy}" r="4" fill="${p.color}" class="cursor-pointer"
        onmousemove="showTooltip(event, '<b>${p.id}: ${p.name}</b><br>Año ${yr}: <b>${p.evolucion_anual[yr]}%</b>')" onmouseleave="hideTooltip()"/>`;
    });
    lines += `<text x="${W - pad.r + 6}" y="${lastY + 4}" font-size="12" font-weight="800" fill="${p.color}">${p.id}</text>`;
  });

  container.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">${grid}${lines}</svg>`;
}

function renderProfileCardsGrid() {
  const filter = document.getElementById("filter-profile-badge").value;
  const grid = document.getElementById("profiles-cards-grid");
  if (!grid) return;

  const filtered = DATA.perfiles.filter(p => {
    if (filter === "ALTA") return ["P1", "P2"].includes(p.id);
    if (filter === "MEDIA") return ["P3", "P4"].includes(p.id);
    if (filter === "BAJA") return ["P5", "P6"].includes(p.id);
    return true;
  });

  grid.innerHTML = filtered.map(p => `
    <div onclick="selectProfile('${p.id}')" class="card-hover bg-[var(--card)] border border-[var(--border)] rounded-2xl overflow-hidden shadow-sm flex flex-col justify-between cursor-pointer">
      <div>
        <div class="p-4 text-white flex items-start justify-between gap-2" style="background:${p.color}">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider opacity-90">${p.id} · ${p.badge}</span>
            <h4 class="text-base font-extrabold mt-0.5">${p.icon} ${p.name}</h4>
            <p class="text-xs opacity-90 mt-0.5">${p.subtitle}</p>
          </div>
          <div class="bg-black/25 rounded-xl px-2.5 py-1.5 text-right shrink-0">
            <div class="text-base font-extrabold">${p.pct_padron}%</div>
            <div class="text-xs opacity-90">${(p.ln_2024/1e6).toFixed(2)}M LN</div>
          </div>
        </div>

        <div class="p-4 space-y-3">
          <div class="grid grid-cols-4 gap-1.5 text-center bg-[var(--background)] p-2.5 rounded-xl border border-[var(--border)] text-xs">
            <div><div class="font-extrabold text-sm">${p.tasa_2024}%</div><div class="text-[var(--muted-foreground)]">2024</div></div>
            <div><div class="font-extrabold text-sm">${p.tasa_inter}%</div><div class="text-[var(--muted-foreground)]">Interm.</div></div>
            <div><div class="font-extrabold text-sm">${p.edad_media}a</div><div class="text-[var(--muted-foreground)]">Edad</div></div>
            <div><div class="font-extrabold text-sm">${p.pct_mujer}%</div><div class="text-[var(--muted-foreground)]">Mujeres</div></div>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">${p.narrative}</p>
        </div>
      </div>

      <div class="px-4 pb-4">
        <div class="p-3 rounded-xl bg-[var(--background)] border-l-4 text-xs space-y-1" style="border-left-color:${p.color}">
          <div class="font-bold" style="color:${p.color}">🎯 ${p.ine_strategy}</div>
          <ul class="list-disc pl-4 space-y-0.5 text-[var(--foreground)]">
            ${p.ine_actions.map(a => `<li>${a}</li>`).join("")}
          </ul>
        </div>
      </div>
    </div>
  `).join("");
}

/* ============================================================================
   2. VISTA CICLO DE VIDA ELECTORAL Y EVOLUCIÓN NACIONAL
   ============================================================================ */
function renderAgeLifecycleSVG() {
  const container = document.getElementById("svg-age-lifecycle");
  if (!container) return;
  const show21 = document.getElementById("chk-show-2021").checked;
  const show18 = document.getElementById("chk-show-2018").checked;

  const W = 760, H = 355;
  const pad = { l: 48, r: 24, t: 22, b: 42 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;

  const xMin = 18, xMax = 90, yMin = 22, yMax = 82;
  const xScale = e => pad.l + ((e - xMin) / (xMax - xMin)) * plotW;
  const yScale = v => pad.t + plotH - ((v - yMin) / (yMax - yMin)) * plotH;

  let grid = "";
  for (let v = 30; v <= 80; v += 10) {
    const py = yScale(v);
    grid += `<line x1="${pad.l}" y1="${py}" x2="${W - pad.r}" y2="${py}" stroke="currentColor" stroke-opacity="0.1" stroke-dasharray="3 3"/>`;
    grid += `<text x="${pad.l - 8}" y="${py + 4}" text-anchor="end" font-size="12" fill="currentColor" fill-opacity="0.65">${v}%</text>`;
  }
  for (let e = 20; e <= 90; e += 10) {
    const px = xScale(e);
    grid += `<line x1="${px}" y1="${pad.t}" x2="${px}" y2="${H - pad.b}" stroke="currentColor" stroke-opacity="0.08" stroke-dasharray="3 3"/>`;
    grid += `<text x="${px}" y="${H - pad.b + 18}" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.7">${e} años</text>`;
  }

  // Banda sombreada del Valle de Abstencionismo Joven (20 a 34 años)
  const vx1 = xScale(20), vx2 = xScale(34);
  const valleyRect = `
    <rect x="${vx1}" y="${pad.t}" width="${vx2 - vx1}" height="${plotH}" fill="#F43F5E" fill-opacity="0.09"/>
    <text x="${(vx1 + vx2) / 2}" y="${pad.t + 16}" text-anchor="middle" font-size="12" font-weight="700" fill="#E11D48">Valle de Abstención Joven (20–34 años)</text>
  `;

  function buildPath(arr, sexo, color, dash = "") {
    const sub = arr.filter(d => d.SEXO === sexo).sort((a, b) => a.EDAD - b.EDAD);
    const pts = sub.map(d => `${xScale(d.EDAD)},${yScale(d.TASA)}`).join(" ");
    return `<polyline points="${pts}" fill="none" stroke="${color}" stroke-width="${dash ? '2' : '3'}" ${dash ? `stroke-dasharray="${dash}"` : ""}/>`;
  }

  let curves = "";
  if (show18) {
    curves += buildPath(DATA.edad_exacta_2018, 1, "#10B981", "3 3");
    curves += buildPath(DATA.edad_exacta_2018, 0, "#059669", "6 4");
  }
  if (show21) {
    curves += buildPath(DATA.edad_exacta_2021, 1, "#C084FC", "5 4");
    curves += buildPath(DATA.edad_exacta_2021, 0, "#60A5FA", "5 4");
  }
  curves += buildPath(DATA.edad_exacta_2024, 1, "#9333EA");
  curves += buildPath(DATA.edad_exacta_2024, 0, "#2563EB");

  // Puntos interactivos para 2024
  let dots = "";
  for (let age = 18; age <= 90; age += 2) {
    const m = DATA.edad_exacta_2024.find(d => d.EDAD === age && d.SEXO === 1);
    const h = DATA.edad_exacta_2024.find(d => d.EDAD === age && d.SEXO === 0);
    if (m && h) {
      const gap = (m.TASA - h.TASA).toFixed(1);
      const tip = `<strong>Edad cumplida: ${age} años (2024)</strong><br>Mujeres: <b>${m.TASA}%</b><br>Hombres: <b>${h.TASA}%</b><br>Brecha género: <b>+${gap} pp</b>`;
      dots += `<circle cx="${xScale(age)}" cy="${yScale(m.TASA)}" r="4" fill="#9333EA" class="cursor-pointer" onmousemove="showTooltip(event, \`${tip}\`)" onmouseleave="hideTooltip()"/>`;
      dots += `<circle cx="${xScale(age)}" cy="${yScale(h.TASA)}" r="4" fill="#2563EB" class="cursor-pointer" onmousemove="showTooltip(event, \`${tip}\`)" onmouseleave="hideTooltip()"/>`;
    }
  }

  container.innerHTML = `
    <svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">
      ${valleyRect}
      ${grid}
      ${curves}
      ${dots}
      <text x="${pad.l + 10}" y="${H - 6}" font-size="12" font-weight="600" fill="#9333EA">● Mujeres 2024</text>
      <text x="${pad.l + 125}" y="${H - 6}" font-size="12" font-weight="600" fill="#2563EB">● Hombres 2024</text>
      <text x="${pad.l + 245}" y="${H - 6}" font-size="12" fill="currentColor" fill-opacity="0.75">--- Punteadas: Intermedia 2021 / Presidencial 2018</text>
    </svg>
  `;
}

function renderNationalHistorySVG() {
  const container = document.getElementById("svg-national-history");
  if (!container) return;
  const W = 580, H = 295;
  const pad = { l: 46, r: 42, t: 24, b: 38 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const nac = DATA.nacional_anual;
  const colW = plotW / nac.length;

  let bars = "";
  let linePts = [];
  nac.forEach((d, idx) => {
    const cx = pad.l + idx * colW + colW / 2;
    const hLN = (d.LN / 105e6) * plotH;
    const hSV = (d.SV / 105e6) * plotH;
    const yTasa = pad.t + plotH - ((d.TASA_SV - 30) / 40) * plotH;
    linePts.push(`${cx},${yTasa}`);

    bars += `
      <g class="cursor-pointer" onmousemove="showTooltip(event, '<b>Elección ${d.AELEC} (${d.TIPO})</b><br>Lista Nominal: ${d.LN.toLocaleString()}<br>Sí Votaron: ${d.SV.toLocaleString()}<br>Participación: <b>${d.TASA_SV}%</b>')" onmouseleave="hideTooltip()">
        <rect x="${cx - 22}" y="${pad.t + plotH - hLN}" width="20" height="${hLN}" rx="4" fill="#A855F7" fill-opacity="0.32"/>
        <rect x="${cx + 2}" y="${pad.t + plotH - hSV}" width="20" height="${hSV}" rx="4" fill="#7E22CE"/>
        <text x="${cx}" y="${H - 12}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${d.AELEC}</text>
      </g>
    `;
  });

  let tasaNodes = "";
  nac.forEach((d, idx) => {
    const cx = pad.l + idx * colW + colW / 2;
    const yTasa = pad.t + plotH - ((d.TASA_SV - 30) / 40) * plotH;
    tasaNodes += `<circle cx="${cx}" cy="${yTasa}" r="5" fill="#F59E0B" stroke="#1E1B24" stroke-width="1.5"/>`;
    tasaNodes += `<text x="${cx}" y="${yTasa - 9}" text-anchor="middle" font-size="12" font-weight="800" fill="#D97706">${d.TASA_SV}%</text>`;
  });

  container.innerHTML = `
    <svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">
      ${bars}
      <polyline points="${linePts.join(' ')}" fill="none" stroke="#F59E0B" stroke-width="3"/>
      ${tasaNodes}
    </svg>
  `;
}

function renderTipoSecSVG() {
  const container = document.getElementById("svg-tiposec-chart");
  if (!container) return;
  const W = 580, H = 295;
  const pad = { l: 48, r: 24, t: 22, b: 40 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const cats = [
    { code: "U", name: "Sección Urbana (U)" },
    { code: "M", name: "Sección Mixta (M)" },
    { code: "R", name: "Sección Rural (R)" }
  ];
  const groupW = plotW / cats.length;

  let content = "";
  cats.forEach((c, idx) => {
    const gx = pad.l + idx * groupW + 24;
    const m24 = (DATA.tiposec_sexo.find(d => d.AELEC === 2024 && d.TIPOSEC === c.code && d.SEXO === 1) || {}).TASA || 0;
    const h24 = (DATA.tiposec_sexo.find(d => d.AELEC === 2024 && d.TIPOSEC === c.code && d.SEXO === 0) || {}).TASA || 0;
    const m21 = (DATA.tiposec_sexo.find(d => d.AELEC === 2021 && d.TIPOSEC === c.code && d.SEXO === 1) || {}).TASA || 0;
    const h21 = (DATA.tiposec_sexo.find(d => d.AELEC === 2021 && d.TIPOSEC === c.code && d.SEXO === 0) || {}).TASA || 0;

    const vals = [
      { l: "M 24", v: m24, col: "#7E22CE" },
      { l: "H 24", v: h24, col: "#2563EB" },
      { l: "M 21", v: m21, col: "#C084FC" },
      { l: "H 21", v: h21, col: "#93C5FD" }
    ];

    vals.forEach((item, bIdx) => {
      const bx = gx + bIdx * 32;
      const bh = (item.v / 75) * plotH;
      const by = pad.t + plotH - bh;
      content += `
        <rect x="${bx}" y="${by}" width="26" height="${bh}" rx="4" fill="${item.col}"/>
        <text x="${bx + 13}" y="${by - 5}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${item.v.toFixed(0)}%</text>
      `;
    });

    content += `<text x="${gx + 60}" y="${H - 12}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${c.name}</text>`;
  });

  container.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">${content}</svg>`;
}

/* ============================================================================
   3. VISTA ATLAS TERRITORIAL (32 ENTIDADES Y 2,477 MUNICIPIOS)
   ============================================================================ */
function initTerritorialSelectors() {
  const selState = document.getElementById("terr-state-select");
  if (!selState) return;
  const sortedStates = [...DATA.estados].sort((a, b) => a.edonom.localeCompare(b.edonom));
  selState.innerHTML = `<option value="ALL">Todas las Entidades (Top Municipios Nacionales)</option>` +
    sortedStates.map(s => `<option value="${s.edocve}">${s.edonom} — ${s.tasa_2024}% part.</option>`).join("");
  selState.value = "9"; // Ciudad de México por defecto para mostrar drilldown inmediato
}

function updateTerritorialView() {
  const reg = document.getElementById("terr-region-select").value;
  const container = document.getElementById("svg-states-stacked");
  if (!container) return;

  const filtered = reg === "ALL" ? DATA.estados : DATA.estados.filter(s => s.region === reg);

  container.innerHTML = filtered.map(st => {
    let acc = 0;
    const segmentsHtml = DATA.perfiles.map(p => {
      const pct = st.perfiles_pct[p.id] || 0;
      const seg = `<div style="width:${pct}%; background:${p.color}" class="h-full" title="${p.id}: ${pct}%"></div>`;
      acc += pct;
      return seg;
    }).join("");

    return `
      <div onclick="selectStateFromBar(${st.edocve})" class="py-1.5 px-2 rounded-lg hover:bg-[var(--background)] cursor-pointer transition flex items-center gap-3 text-xs">
        <div class="w-36 font-bold truncate shrink-0">${st.edonom}</div>
        <div class="flex-1 h-4 rounded-full overflow-hidden flex bg-slate-200 dark:bg-slate-800">${segmentsHtml}</div>
        <div class="w-14 text-right font-extrabold shrink-0">${st.tasa_2024}%</div>
      </div>
    `;
  }).join("");
}

function selectStateFromBar(edocve) {
  document.getElementById("terr-state-select").value = String(edocve);
  updateStateDrilldown();
}

function updateStateDrilldown() {
  const val = document.getElementById("terr-state-select").value;
  const st = val === "ALL" ? DATA.estados[0] : (DATA.estados.find(s => String(s.edocve) === String(val)) || DATA.estados[0]);

  document.getElementById("st-detail-region").textContent = `Región ${st.region}`;
  document.getElementById("st-detail-ln").textContent = `Lista Nominal: ${st.ln_2024.toLocaleString("es-MX")}`;
  document.getElementById("st-detail-name").textContent = st.edonom;
  document.getElementById("st-kpi-24").textContent = st.tasa_2024 + "%";
  document.getElementById("st-kpi-pres").textContent = st.tasa_pres + "%";
  document.getElementById("st-kpi-inter").textContent = st.tasa_inter + "%";
  document.getElementById("st-kpi-esc").textContent = st.escolaridad + " años";

  // Serie histórica SVG de la entidad vs nacional
  const years = ["2009", "2012", "2015", "2018", "2021", "2024"];
  const W = 440, H = 195;
  const pad = { l: 38, r: 22, t: 22, b: 28 };
  const plotW = W - pad.l - pad.r, plotH = H - pad.t - pad.b;
  const xScale = i => pad.l + (i / 5) * plotW;
  const yScale = v => pad.t + plotH - ((v - 25) / 52) * plotH;

  const stPts = years.map((y, i) => `${xScale(i)},${yScale(st.evolucion[y])}`).join(" ");
  const nacPts = years.map((y, i) => {
    const nv = (DATA.nacional_anual.find(n => String(n.AELEC) === y) || {}).TASA_SV || 50;
    return `${xScale(i)},${yScale(nv)}`;
  }).join(" ");

  let nodes = "";
  years.forEach((y, i) => {
    const cx = xScale(i), cy = yScale(st.evolucion[y]);
    nodes += `<circle cx="${cx}" cy="${cy}" r="4.5" fill="#9333EA"/>`;
    nodes += `<text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${st.evolucion[y]}%</text>`;
    nodes += `<text x="${cx}" y="${H - 6}" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.7">${y}</text>`;
  });

  document.getElementById("svg-single-state-ts").innerHTML = `
    <svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">
      <polyline points="${nacPts}" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="4 4"/>
      <polyline points="${stPts}" fill="none" stroke="#9333EA" stroke-width="3"/>
      ${nodes}
    </svg>
  `;

  // Mini barras de perfiles en el estado
  const miniBars = document.getElementById("st-profiles-mini-bars");
  miniBars.innerHTML = DATA.perfiles.map(p => {
    const pct = st.perfiles_pct[p.id] || 0;
    return `
      <div class="flex items-center gap-2 text-xs">
        <span class="w-28 truncate font-semibold">${p.icon} ${p.id}: ${p.name.split(" ")[0]}</span>
        <div class="flex-1 h-2.5 rounded-full bg-[var(--background)] overflow-hidden">
          <div style="width:${pct}%; background:${p.color}" class="h-full rounded-full"></div>
        </div>
        <span class="w-12 text-right font-bold">${pct}%</span>
      </div>
    `;
  }).join("");

  renderMunicipalTable();
}

function renderMunicipalTable() {
  const stateVal = document.getElementById("terr-state-select").value;
  const query = (document.getElementById("mun-search-input").value || "").trim().toLowerCase();
  const sortMode = document.getElementById("mun-sort-select").value;

  let list = DATA.municipios_2024;
  if (query.length > 0) {
    list = list.filter(m => m.n.toLowerCase().includes(query));
  } else if (stateVal !== "ALL") {
    list = list.filter(m => String(m.e) === String(stateVal));
  }

  list = [...list].sort((a, b) => {
    if (sortMode === "ln_desc") return b.ln - a.ln;
    if (sortMode === "t24_desc") return b.t24 - a.t24;
    if (sortMode === "t24_asc") return a.t24 - b.t24;
    if (sortMode === "tj_asc") return a.tj - b.tj;
    if (sortMode === "br_desc") return b.br - a.br;
    return b.ln - a.ln;
  });

  const stateMap = {};
  DATA.estados.forEach(s => { stateMap[s.edocve] = s.edonom; });

  const displayList = list.slice(0, 120);
  document.getElementById("mun-table-title").textContent =
    `Explorador Municipal CCPC 2024 (${list.length} municipios encontrados · Mostrando top ${displayList.length})`;

  const tbody = document.getElementById("mun-table-tbody");
  tbody.innerHTML = displayList.map(m => {
    const pMeta = DATA.perfiles.find(p => p.id === m.p) || DATA.perfiles[0];
    return `
      <tr class="hover:bg-[var(--background)] transition">
        <td class="py-2.5 px-3 font-bold">${m.n}</td>
        <td class="py-2.5 px-3 text-[var(--muted-foreground)]">${stateMap[m.e] || ""}</td>
        <td class="py-2.5 px-3 text-right font-medium">${m.ln.toLocaleString("es-MX")}</td>
        <td class="py-2.5 px-3 text-right font-extrabold">${m.t24}%</td>
        <td class="py-2.5 px-3 text-right">${m.t21}%</td>
        <td class="py-2.5 px-3 text-right font-semibold ${m.tj < 42 ? 'text-rose-500' : 'text-emerald-500'}">${m.tj}%</td>
        <td class="py-2.5 px-3 text-right font-semibold">${m.tm}%</td>
        <td class="py-2.5 px-3 text-right">${m.tf}% M / ${m.th}% H</td>
        <td class="py-2.5 px-3 text-right">${m.pr}%</td>
        <td class="py-2.5 px-3">
          <span class="px-2.5 py-0.5 rounded-full text-white font-bold text-xs inline-block" style="background:${pMeta.color}">
            ${m.p}: ${pMeta.name.split(" ").slice(0, 2).join(" ")}
          </span>
        </td>
      </tr>
    `;
  }).join("");
}

function exportFilteredMunicipalCSV() {
  const stateVal = document.getElementById("terr-state-select").value;
  let list = stateVal === "ALL" ? DATA.municipios_2024 : DATA.municipios_2024.filter(m => String(m.e) === String(stateVal));
  const headers = ["EDOCVE,MPIOCVE,MUNICIPIO,LN_2024,SV_2024,TASA_2024,TASA_2021,TASA_JOVEN_18_29,TASA_MAYOR_60,TASA_MUJER,TASA_HOMBRE,PCT_RURAL,PERFIL_PRIORITARIO"];
  const rows = list.map(m => `${m.e},${m.m},"${m.n}",${m.ln},${m.sv},${m.t24},${m.t21},${m.tj},${m.tm},${m.tf},${m.th},${m.pr},${m.p}`);
  const blob = new Blob([headers.concat(rows).join("\n")], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `perfiles_municipales_ccpc2024_${stateVal}.csv`;
  a.click();
}

/* ============================================================================
   4. VISTA LABORATORIO DE CAMPAÑAS & SIMULADOR WHAT-IF
   ============================================================================ */
function runCampaignLab() {
  const edad = document.getElementById("lab-edad").value;
  const sexo = document.getElementById("lab-sexo").value;
  const tiposec = document.getElementById("lab-tiposec").value;
  const eleccion = document.getElementById("lab-eleccion").value;

  let pId = "P5";
  if (["60-69", "70+"].includes(edad) && tiposec === "U") pId = "P1";
  else if (["50-59", "60-69", "70+"].includes(edad) && tiposec !== "U") pId = "P2";
  else if (["18-19", "20-24", "25-29", "30-34"].includes(edad) && tiposec !== "U") pId = "P6";
  else if (["20-24", "25-29", "30-34"].includes(edad) && sexo === "0" && tiposec === "U") pId = "P5";
  else if (["18-19", "25-29", "30-34", "35-39"].includes(edad) && sexo === "1" && tiposec === "U") pId = "P3";
  else pId = "P4";

  const p = DATA.perfiles.find(x => x.id === pId) || DATA.perfiles[0];
  const baseRate = eleccion === "PRES" ? p.tasa_pres : p.tasa_inter;
  const sexAdj = sexo === "1" ? 2.4 : (sexo === "0" ? -2.4 : 14.5);
  const estRate = Math.min(85, Math.max(24, baseRate + sexAdj)).toFixed(1);

  const nbBanner = sexo === "2" ? `
    <div class="mt-2.5 p-2.5 rounded-xl bg-purple-500/15 border border-purple-500/30 text-xs">
      <strong>🏳️‍🌈 Dato Censal No Binario 2024:</strong> Las personas con credencial No Binaria registraron una participación de <strong>75.24%</strong> (79 de 105 en Lista Nominal).
    </div>
  ` : "";

  document.getElementById("lab-output-card").innerHTML = `
    <div class="p-4 rounded-2xl border-2 bg-[var(--background)] space-y-3" style="border-color:${p.color}">
      <div class="flex items-center justify-between gap-2">
        <div>
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold text-white" style="background:${p.color}">
            ${p.icon} Clasificación: ${p.id} — ${p.name}
          </span>
          <div class="text-xs text-[var(--muted-foreground)] mt-1">${p.subtitle}</div>
        </div>
        <div class="text-right">
          <div class="text-2xl font-extrabold" style="color:${p.color}">${estRate}%</div>
          <div class="text-xs text-[var(--muted-foreground)]">Prob. Voto Estimada</div>
        </div>
      </div>

      <div class="p-3 rounded-xl bg-[var(--card)] border border-[var(--border)] text-xs space-y-1.5">
        <div class="font-bold" style="color:${p.color}">🚀 Intervención INE Recomendada: ${p.ine_strategy}</div>
        <ul class="list-disc pl-4 space-y-1">
          ${p.ine_actions.map(a => `<li>${a}</li>`).join("")}
        </ul>
        <div class="pt-1 text-[var(--muted-foreground)]"><strong>Mix de Medios:</strong> ${p.channels}</div>
      </div>
      ${nbBanner}
    </div>
  `;
}

function updateWhatIfSimulator() {
  const gP5 = parseFloat(document.getElementById("slider-p5").value);
  const gP3 = parseFloat(document.getElementById("slider-p3").value);
  const gP6 = parseFloat(document.getElementById("slider-p6").value);
  const gP4 = parseFloat(document.getElementById("slider-p4").value);

  document.getElementById("lbl-slider-p5").textContent = `+${gP5.toFixed(1)} pp`;
  document.getElementById("lbl-slider-p3").textContent = `+${gP3.toFixed(1)} pp`;
  document.getElementById("lbl-slider-p6").textContent = `+${gP6.toFixed(1)} pp`;
  document.getElementById("lbl-slider-p4").textContent = `+${gP4.toFixed(1)} pp`;

  const gainsMap = { P1: 0, P2: 0, P3: gP3, P4: gP4, P5: gP5, P6: gP6 };
  let totalLN = 0;
  let baseVotesInter = 0;
  let newVotesAdded = 0;

  DATA.perfiles.forEach(p => {
    totalLN += p.ln_2024;
    baseVotesInter += p.ln_2024 * (p.tasa_inter / 100);
    newVotesAdded += p.ln_2024 * (gainsMap[p.id] / 100);
  });

  const baseRateInter = (baseVotesInter / totalLN) * 100;
  const newRateInter = ((baseVotesInter + newVotesAdded) / totalLN) * 100;

  document.getElementById("whatif-results-banner").innerHTML = `
    <div class="grid grid-cols-3 gap-3 p-3.5 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-center">
      <div>
        <div class="text-xs text-[var(--muted-foreground)] font-semibold">Nuevos Votantes Movilizados</div>
        <div class="text-xl font-extrabold text-emerald-500">+${Math.round(newVotesAdded).toLocaleString("es-MX")}</div>
      </div>
      <div>
        <div class="text-xs text-[var(--muted-foreground)] font-semibold">Tasa Base Intermedia</div>
        <div class="text-xl font-extrabold">${baseRateInter.toFixed(2)}%</div>
      </div>
      <div>
        <div class="text-xs text-[var(--muted-foreground)] font-semibold">Nueva Participación Nacional</div>
        <div class="text-xl font-extrabold text-purple-500">${newRateInter.toFixed(2)}% (+${(newRateInter - baseRateInter).toFixed(2)} pp)</div>
      </div>
    </div>
  `;

  // Gráfico SVG de impacto por perfil
  const W = 540, H = 200;
  const pad = { l: 42, r: 20, t: 18, b: 32 };
  const plotW = W - pad.l - pad.r, plotH = H - pad.t - pad.b;
  const colW = plotW / DATA.perfiles.length;

  let bars = "";
  DATA.perfiles.forEach((p, idx) => {
    const cx = pad.l + idx * colW + colW / 2;
    const baseM = (p.ln_2024 * (p.tasa_inter / 100)) / 1e6;
    const addM = (p.ln_2024 * (gainsMap[p.id] / 100)) / 1e6;
    const hBase = (baseM / 16) * plotH;
    const hAdd = (addM / 16) * plotH;

    bars += `
      <rect x="${cx - 18}" y="${pad.t + plotH - hBase}" width="36" height="${hBase}" rx="3" fill="${p.color}" fill-opacity="0.82"/>
      ${addM > 0 ? `<rect x="${cx - 18}" y="${pad.t + plotH - hBase - hAdd}" width="36" height="${hAdd}" rx="3" fill="#10B981"/>` : ""}
      <text x="${cx}" y="${pad.t + plotH - hBase - hAdd - 5}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${(baseM + addM).toFixed(1)}M</text>
      <text x="${cx}" y="${H - 10}" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">${p.id}</text>
    `;
  });

  document.getElementById("svg-whatif-bars").innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="w-full h-full select-none">${bars}</svg>`;
}

/* ============================================================================
   5. VISTA INCLUSIÓN 2024
   ============================================================================ */
function renderInclusionPanels() {
  const va = DATA.kpis_globales.voto_anticipado_2024;
  const pp = DATA.kpis_globales.prision_preventiva_2024;

  const vaContainer = document.getElementById("va-top-states");
  if (vaContainer) {
    vaContainer.innerHTML = `<div class="font-bold text-[var(--muted-foreground)] uppercase">Top 5 Entidades en Voto Anticipado:</div>` +
      Object.entries(va.top_estados).map(([edo, cnt]) => `
        <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]">
          <span>${edo}</span><strong>${cnt.toLocaleString("es-MX")} votantes</strong>
        </div>
      `).join("");
  }

  const ppContainer = document.getElementById("pp-top-states");
  if (ppContainer) {
    ppContainer.innerHTML = `<div class="font-bold text-[var(--muted-foreground)] uppercase">Top 5 Entidades en Prisión Preventiva:</div>` +
      Object.entries(pp.top_estados).map(([edo, cnt]) => `
        <div class="flex justify-between p-1.5 rounded-lg bg-[var(--background)]">
          <span>${edo}</span><strong>${cnt.toLocaleString("es-MX")} votantes</strong>
        </div>
      `).join("");
  }
}

window.addEventListener("DOMContentLoaded", () => {
  initTerritorialSelectors();
  renderClusterBubbleSVG();
  renderProfileInspector("P1");
  renderClusterBarsSVG();
  renderProfilesTimelineSVG();
  renderProfileCardsGrid();
  renderInclusionPanels();
});
</script>
</body>
</html>
"""

final_html = html_code.replace("__JSON_PAYLOAD__", json_str)

# Guardar en Artifact Directory y en Workspace Directory
art_path = os.path.join(ART_DIR, "dashboard_hackea_ine_pro.html")
ws_path = os.path.join(BASE_DIR, "dashboard_ccpc_ine.html")

with open(art_path, "w", encoding="utf-8") as f:
    f.write(final_html)

with open(ws_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Dashboard PRO generado con éxito en:")
print("  1)", art_path)
print("  2)", ws_path)
