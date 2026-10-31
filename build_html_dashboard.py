import os
import json

BASE_DIR = r"C:\Users\52477\Desktop\hackatonINE"
OUT_DIR = os.path.join(BASE_DIR, "processed_data")

with open(os.path.join(OUT_DIR, "dashboard_data.json"), "r", encoding="utf-8") as f:
    payload = json.load(f)

json_str = json.dumps(payload, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HACKEA LA PARTICIPACIÓN — Reto 1: Perfiles Ciudadanos CCPC 2009–2024 (INE)</title>
<script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --ine-purple: #4A154B;
    --ine-magenta: #8E24AA;
    --ine-pink: #D81B60;
    --ine-gold: #D4AC0D;
    --bg-light: #F7F5FA;
    --card-bg: #FFFFFF;
    --text-dark: #1E1B24;
    --text-muted: #5E5868;
    --border-color: #E6E0EC;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-light);
    color: var(--text-dark);
    line-height: 1.5;
  }
  header {
    background: linear-gradient(135deg, #2E0836 0%, #5B2C6F 55%, #8E24AA 100%);
    color: white;
    padding: 28px 40px;
    box-shadow: 0 4px 20px rgba(46, 8, 54, 0.25);
  }
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    max-width: 1440px;
    margin: 0 auto;
  }
  .badge-convocatoria {
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.3);
    padding: 5px 14px;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.5px;
  }
  .subtitle {
    color: rgba(255,255,255,0.88);
    font-size: 0.96rem;
    margin-top: 4px;
  }
  .nav-tabs {
    background: #FFFFFF;
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .nav-container {
    max-width: 1440px;
    margin: 0 auto;
    display: flex;
    gap: 8px;
    padding: 0 40px;
    overflow-x: auto;
  }
  .tab-btn {
    padding: 16px 22px;
    border: none;
    background: transparent;
    font-family: inherit;
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--text-muted);
    cursor: pointer;
    border-bottom: 3px solid transparent;
    transition: all 0.2s;
    white-space: nowrap;
  }
  .tab-btn:hover { color: var(--ine-purple); }
  .tab-btn.active {
    color: var(--ine-purple);
    border-bottom-color: var(--ine-magenta);
    background: rgba(142, 36, 170, 0.04);
  }
  .main-container {
    max-width: 1440px;
    margin: 28px auto;
    padding: 0 40px 60px;
  }
  .tab-content { display: none; }
  .tab-content.active { display: block; }
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 16px;
    margin-bottom: 26px;
  }
  .kpi-card {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 20px;
    border: 1px solid var(--border-color);
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  }
  .kpi-label {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.4px;
  }
  .kpi-val {
    font-size: 1.75rem;
    font-weight: 800;
    color: var(--ine-purple);
    margin: 6px 0 4px;
  }
  .kpi-sub {
    font-size: 0.8rem;
    color: #2E7D32;
    font-weight: 500;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-bottom: 24px;
  }
  @media (max-width: 1024px) {
    .grid-2 { grid-template-columns: 1fr; }
  }
  .card {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 24px;
    border: 1px solid var(--border-color);
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    margin-bottom: 22px;
  }
  .card-title {
    font-size: 1.12rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .card-desc {
    font-size: 0.86rem;
    color: var(--text-muted);
    margin-bottom: 16px;
  }
  .profiles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(410px, 1fr));
    gap: 22px;
  }
  .profile-card {
    background: var(--card-bg);
    border-radius: 16px;
    border: 1px solid var(--border-color);
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    display: flex;
    flex-direction: column;
  }
  .profile-header {
    padding: 18px 22px;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  .profile-body {
    padding: 20px 22px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .metrics-mini {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    background: #F9F8FC;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #ECE6F2;
    text-align: center;
  }
  .metrics-mini .m-val {
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text-dark);
  }
  .metrics-mini .m-lbl {
    font-size: 0.7rem;
    color: var(--text-muted);
    text-transform: uppercase;
    font-weight: 600;
  }
  .strategy-box {
    background: #F4ECF7;
    border-left: 4px solid var(--ine-purple);
    padding: 12px 14px;
    border-radius: 0 8px 8px 0;
    font-size: 0.85rem;
  }
  .strategy-box h4 {
    color: var(--ine-purple);
    font-size: 0.86rem;
    margin-bottom: 6px;
  }
  .strategy-box ul {
    padding-left: 18px;
    margin-bottom: 8px;
  }
  .strategy-box li { margin-bottom: 4px; }
  .filter-bar {
    display: flex;
    gap: 16px;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 20px;
    background: white;
    padding: 16px 22px;
    border-radius: 12px;
    border: 1px solid var(--border-color);
  }
  select, input {
    padding: 9px 14px;
    border-radius: 8px;
    border: 1px solid #C5B8D1;
    font-family: inherit;
    font-size: 0.9rem;
    background: white;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.86rem;
  }
  th, td {
    padding: 10px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
  }
  th {
    background: #F4EFF8;
    color: var(--ine-purple);
    font-weight: 700;
    position: sticky;
    top: 0;
  }
  tr:hover { background: #FAF8FC; }
  .pill {
    display: inline-block;
    padding: 3px 9px;
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 700;
    color: white;
  }
</style>
</head>
<body>

<header>
  <div class="header-top">
    <div>
      <span class="badge-convocatoria">INE · DECEyEC · ENCIVICA 2024–2026</span>
      <h1>HACKEA LA PARTICIPACIÓN: Datos que Construyen Democracia</h1>
      <p class="subtitle">Reto 1: Perfiles Ciudadanos de Participación (Segmentación Sociodemográfica CCPC 2009–2024 · 54.87 Millones de Registros)</p>
    </div>
    <div style="text-align:right">
      <div style="font-size:0.82rem;opacity:0.85;">Cobertura Censal Procesada</div>
      <div style="font-size:1.45rem;font-weight:800;">6 Elecciones Federales (192 CSVs + 2 Especiales)</div>
      <div style="font-size:0.8rem;color:#F7DC6F;">Lista Nominal 2024: 98,330,348 ciudadanas y ciudadanos</div>
    </div>
  </div>
</header>

<nav class="nav-tabs">
  <div class="nav-container">
    <button class="tab-btn active" onclick="switchTab('tab-resumen', this)">1. Panorama Nacional y Ciclo de Vida (2009–2024)</button>
    <button class="tab-btn" onclick="switchTab('tab-perfiles', this)">2. Los 6 Perfiles Ciudadanos (Clustering)</button>
    <button class="tab-btn" onclick="switchTab('tab-estados', this)">3. Explorador Territorial (32 Entidades y Regiones)</button>
    <button class="tab-btn" onclick="switchTab('tab-simulador', this)">4. Simulador de Perfiles y Estrategias INE</button>
  </div>
</nav>

<main class="main-container">

  <!-- TAB 1: PANORAMA NACIONAL -->
  <section id="tab-resumen" class="tab-content active">
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Registros CCPC Analizados</div>
        <div class="kpi-val">54,872,712</div>
        <div class="kpi-sub">100% de los cuadernillos 2009–2024</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Participación CCPC 2024</div>
        <div class="kpi-val">55.83%</div>
        <div class="kpi-sub">54.90M votaron de 98.33M en cuadernillos</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Brecha Presidencial vs Intermedia</div>
        <div class="kpi-val">+13.03 pp</div>
        <div class="kpi-sub">58.63% Presidencial vs 45.60% Intermedia</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Brecha de Género 2024</div>
        <div class="kpi-val">+7.68 pp</div>
        <div class="kpi-sub">Mujeres 59.51% vs Hombres 51.83%</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Inclusión 2024 (Nuevas Modalidades)</div>
        <div class="kpi-val">30,117</div>
        <div class="kpi-sub">3,449 Voto Anticipado · 26,563 Prisión Prev. · 105 No Binario (75.2% part.)</div>
      </div>
    </div>

    <div class="grid-2">
      <div class="card">
        <div class="card-title">Evolución Histórica de la Participación (CCPC 2009–2024)</div>
        <div class="card-desc">Comparativa entre elecciones Presidenciales (2012, 2018, 2024) e Intermedias (2009, 2015, 2021) y crecimiento de la Lista Nominal.</div>
        <div id="chart-hist-nac" style="height:370px;"></div>
      </div>
      <div class="card">
        <div class="card-title">Curva del Ciclo de Vida Electoral por Edad Exacta y Sexo (18 a 90 años)</div>
        <div class="card-desc">El "Valle de Abstencionismo Joven" (20 a 34 años) tras el primer voto a los 18 años y la brecha de género a favor de las mujeres.</div>
        <div id="chart-age-curve" style="height:370px;"></div>
      </div>
    </div>

    <div class="grid-2">
      <div class="card">
        <div class="card-title">Participación por Tipo de Sección Electoral (Urbana, Mixta, Rural) y Sexo</div>
        <div class="card-desc">Las secciones rurales mantienen mayor resiliencia en elecciones intermedias que las secciones urbanas.</div>
        <div id="chart-tiposec" style="height:350px;"></div>
      </div>
      <div class="card">
        <div class="card-title">Trayectoria Longitudinal de los 6 Perfiles Ciudadanos (2009–2024)</div>
        <div class="card-desc">Comportamiento de cada clúster a través de seis procesos electorales federales consecutivos.</div>
        <div id="chart-profiles-ts" style="height:350px;"></div>
      </div>
    </div>
  </section>

  <!-- TAB 2: LOS 6 PERFILES CIUDADANOS -->
  <section id="tab-perfiles" class="tab-content">
    <div class="grid-2">
      <div class="card">
        <div class="card-title">Mapa de Segmentación Sociodemográfica (K-Means Ponderado por Lista Nominal)</div>
        <div class="card-desc">Posición de los 6 perfiles según Edad Promedio, Tasa de Participación 2024 y Brecha Presidencial-Intermedia.</div>
        <div id="chart-cluster-bubble" style="height:380px;"></div>
      </div>
      <div class="card">
        <div class="card-title">Contraste de Comportamiento: Presidencial vs Intermedia por Perfil</div>
        <div class="card-desc">Identificación de votantes constantes, votantes coyunturales (alta brecha) y perfiles en abstencionismo crónico.</div>
        <div id="chart-cluster-bars" style="height:380px;"></div>
      </div>
    </div>

    <div class="profiles-grid" id="profiles-cards-container"></div>
  </section>

  <!-- TAB 3: EXPLORADOR TERRITORIAL -->
  <section id="tab-estados" class="tab-content">
    <div class="filter-bar">
      <label style="font-weight:700;color:var(--ine-purple);">Filtrar por Región INE:</label>
      <select id="sel-region" onchange="updateStateView()">
        <option value="ALL">Todas las Regiones (32 Entidades)</option>
        <option value="Centro">Región Centro</option>
        <option value="Centro-Occidente">Región Centro-Occidente</option>
        <option value="Noreste">Región Noreste</option>
        <option value="Noroeste">Región Noroeste</option>
        <option value="Sur-Sureste">Región Sur-Sureste</option>
      </select>
      <label style="font-weight:700;color:var(--ine-purple);">Seleccionar Entidad para Detalle:</label>
      <select id="sel-state" onchange="updateSingleStateDetail()"></select>
    </div>

    <div class="grid-2">
      <div class="card">
        <div class="card-title">Composición de Perfiles Ciudadanos por Entidad Federativa (% de Lista Nominal)</div>
        <div class="card-desc">Distribución proporcional de los 6 perfiles sociodemográficos en cada estado.</div>
        <div id="chart-states-stacked" style="height:460px;"></div>
      </div>
      <div class="card">
        <div class="card-title" id="single-state-title">Diagnóstico Estatal Detallado</div>
        <div class="card-desc" id="single-state-subtitle">Evolución 2009–2024 y mezcla de perfiles ciudadanos en la entidad seleccionada.</div>
        <div id="chart-single-state" style="height:460px;"></div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Tabla Comparativa de las 32 Entidades Federativas (CCPC 2009–2024)</div>
      <div style="overflow-x:auto; max-height:480px;">
        <table id="table-states">
          <thead>
            <tr>
              <th>Entidad</th>
              <th>Región</th>
              <th>Lista Nominal 2024</th>
              <th>Part. 2024 (%)</th>
              <th>Media Pres. (%)</th>
              <th>Media Inter. (%)</th>
              <th>Brecha (pp)</th>
              <th>Escolaridad Est.</th>
              <th>Perfil Dominante</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- TAB 4: SIMULADOR INTERACTIVO DE PERFILES Y CAMPAÑAS INE -->
  <section id="tab-simulador" class="tab-content">
    <div class="grid-2">
      <div class="card">
        <div class="card-title">Clasificador Interactivo de Perfil Ciudadano y Simulador de Impacto</div>
        <div class="card-desc">Selecciona las características sociodemográficas de un grupo objetivo para identificar su Perfil CCPC, su probabilidad histórica de voto y la estrategia recomendada para el INE.</div>
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:16px;">
          <div>
            <label style="font-size:0.82rem;font-weight:700;display:block;margin-bottom:6px;">Rango de Edad:</label>
            <select id="sim-edad" style="width:100%" onchange="runSimulator()">
              <option value="18-19">18 a 19 años (Primer Voto)</option>
              <option value="20-24" selected>20 a 24 años (Juventud Universitaria/Laboral)</option>
              <option value="25-29">25 a 29 años (Adultez Joven)</option>
              <option value="30-34">30 a 34 años</option>
              <option value="35-39">35 a 39 años</option>
              <option value="40-49">40 a 49 años</option>
              <option value="50-59">50 a 59 años</option>
              <option value="60-69">60 a 69 años (Adultos Mayores)</option>
              <option value="70+">70 años o más</option>
            </select>
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:700;display:block;margin-bottom:6px;">Sexo:</label>
            <select id="sim-sexo" style="width:100%" onchange="runSimulator()">
              <option value="0" selected>Hombres (0)</option>
              <option value="1">Mujeres (1)</option>
              <option value="2">No Binario (2)</option>
            </select>
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:700;display:block;margin-bottom:6px;">Tipo de Sección Electoral:</label>
            <select id="sim-tiposec" style="width:100%" onchange="runSimulator()">
              <option value="U" selected>Urbana (U)</option>
              <option value="M">Mixta (M)</option>
              <option value="R">Rural (R)</option>
            </select>
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:700;display:block;margin-bottom:6px;">Tipo de Elección Objetivo:</label>
            <select id="sim-eleccion" style="width:100%" onchange="runSimulator()">
              <option value="INTER" selected>Elección Intermedia (ej. 2027)</option>
              <option value="PRES">Elección Presidencial (ej. 2030)</option>
            </select>
          </div>
        </div>

        <div id="sim-result-box" style="margin-top:22px;"></div>
      </div>

      <div class="card">
        <div class="card-title">Potencial de Movilización Nacional (Votos Adicionales si se Cierra Brecha)</div>
        <div class="card-desc">Simulación de cuántos nuevos votantes sumaría el INE si se incrementa en +5 pp la participación de los perfiles jóvenes e intermitentes (P3, P5 y P6).</div>
        <div id="chart-sim-impact" style="height:400px;"></div>
      </div>
    </div>
  </section>

</main>

<script>
const DATA = __JSON_PAYLOAD__;

function switchTab(tabId, btn) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  btn.classList.add('active');
  window.dispatchEvent(new Event('resize'));
}

function initDashboard() {
  renderHistNac();
  renderAgeCurve();
  renderTipoSec();
  renderProfilesTS();
  renderClusterBubble();
  renderClusterBars();
  renderProfileCards();
  initStatesTab();
  runSimulator();
  renderSimImpact();
}

function renderHistNac() {
  const nac = DATA.nacional_anual;
  const years = nac.map(d => d.AELEC.toString());
  const tasa = nac.map(d => d.TASA_SV);
  const ln = nac.map(d => +(d.LN / 1e6).toFixed(2));
  const sv = nac.map(d => +(d.SV / 1e6).toFixed(2));

  const trace1 = {
    x: years, y: ln, name: 'Lista Nominal (Millones)', type: 'bar',
    marker: { color: '#D7BDE2' }, yaxis: 'y2', opacity: 0.65
  };
  const trace2 = {
    x: years, y: sv, name: 'Votantes SV (Millones)', type: 'bar',
    marker: { color: '#8E44AD' }, yaxis: 'y2', opacity: 0.85
  };
  const trace3 = {
    x: years, y: tasa, name: 'Tasa Participación (%)', type: 'scatter', mode: 'lines+markers+text',
    text: tasa.map(v => v + '%'), textposition: 'top center',
    line: { color: '#D4AC0D', width: 3.5 },
    marker: { size: 10, color: '#4A154B', line: { color: '#D4AC0D', width: 2 } }
  };

  Plotly.newPlot('chart-hist-nac', [trace1, trace2, trace3], {
    barmode: 'group',
    margin: { t: 20, r: 50, b: 40, l: 50 },
    legend: { orientation: 'h', y: -0.18 },
    yaxis: { title: 'Participación (%)', range: [30, 72] },
    yaxis2: { title: 'Millones de Personas', overlaying: 'y', side: 'right', range: [0, 115], showgrid: false }
  }, { responsive: true });
}

function renderAgeCurve() {
  const d24 = DATA.edad_exacta_2024;
  const d21 = DATA.edad_exacta_2021;
  const m24 = d24.filter(d => d.SEXO === 1);
  const h24 = d24.filter(d => d.SEXO === 0);
  const m21 = d21.filter(d => d.SEXO === 1);
  const h21 = d21.filter(d => d.SEXO === 0);

  Plotly.newPlot('chart-age-curve', [
    { x: m24.map(d => d.EDAD), y: m24.map(d => d.TASA), name: 'Mujeres 2024 (Pres.)', mode: 'lines', line: { color: '#8E24AA', width: 3 } },
    { x: h24.map(d => d.EDAD), y: h24.map(d => d.TASA), name: 'Hombres 2024 (Pres.)', mode: 'lines', line: { color: '#1F618D', width: 3 } },
    { x: m21.map(d => d.EDAD), y: m21.map(d => d.TASA), name: 'Mujeres 2021 (Inter.)', mode: 'lines', line: { color: '#CE93D8', width: 2, dash: 'dot' } },
    { x: h21.map(d => d.EDAD), y: h21.map(d => d.TASA), name: 'Hombres 2021 (Inter.)', mode: 'lines', line: { color: '#7FB3D5', width: 2, dash: 'dot' } }
  ], {
    margin: { t: 20, r: 20, b: 45, l: 50 },
    xaxis: { title: 'Edad Cumplida (18 a 90 años)' },
    yaxis: { title: 'Tasa de Participación (%)', range: [22, 82] },
    legend: { orientation: 'h', y: -0.22 },
    shapes: [{
      type: 'rect', x0: 20, x1: 34, y0: 22, y1: 82,
      fillcolor: '#FADBD8', opacity: 0.28, line: { width: 0 }
    }],
    annotations: [{
      x: 27, y: 31, text: 'Valle de Abstención Joven (20-34 años)', showarrow: false,
      font: { size: 11, color: '#C0392B', weight: 'bold' }
    }]
  }, { responsive: true });
}

function renderTipoSec() {
  const ts = DATA.tiposec_sexo.filter(d => d.AELEC === 2024 || d.AELEC === 2021);
  const cats = ['Urbana (U)', 'Mixta (M)', 'Rural (R)'];
  const codeMap = ['U', 'M', 'R'];

  const m24 = codeMap.map(c => (ts.find(d => d.AELEC===2024 && d.TIPOSEC===c && d.SEXO===1) || {}).TASA || 0);
  const h24 = codeMap.map(c => (ts.find(d => d.AELEC===2024 && d.TIPOSEC===c && d.SEXO===0) || {}).TASA || 0);
  const m21 = codeMap.map(c => (ts.find(d => d.AELEC===2021 && d.TIPOSEC===c && d.SEXO===1) || {}).TASA || 0);
  const h21 = codeMap.map(c => (ts.find(d => d.AELEC===2021 && d.TIPOSEC===c && d.SEXO===0) || {}).TASA || 0);

  Plotly.newPlot('chart-tiposec', [
    { x: cats, y: m24, name: 'Mujeres 2024', type: 'bar', marker: { color: '#6C3483' } },
    { x: cats, y: h24, name: 'Hombres 2024', type: 'bar', marker: { color: '#2874A6' } },
    { x: cats, y: m21, name: 'Mujeres 2021 (Inter.)', type: 'bar', marker: { color: '#BB8FCE' } },
    { x: cats, y: h21, name: 'Hombres 2021 (Inter.)', type: 'bar', marker: { color: '#85C1E9' } }
  ], {
    barmode: 'group',
    margin: { t: 20, r: 20, b: 40, l: 50 },
    yaxis: { title: 'Tasa de Participación (%)', range: [0, 72] },
    legend: { orientation: 'h', y: -0.2 }
  }, { responsive: true });
}

function renderProfilesTS() {
  const years = ['2009', '2012', '2015', '2018', '2021', '2024'];
  const traces = DATA.perfiles.map(p => ({
    x: years,
    y: years.map(y => p.evolucion_anual[y]),
    name: `${p.id}: ${p.name}`,
    mode: 'lines+markers',
    line: { color: p.color, width: 3 },
    marker: { size: 8 }
  }));

  Plotly.newPlot('chart-profiles-ts', traces, {
    margin: { t: 15, r: 20, b: 45, l: 50 },
    yaxis: { title: 'Participación (%)', range: [28, 74] },
    legend: { orientation: 'h', y: -0.24, font: { size: 10 } }
  }, { responsive: true });
}

function renderClusterBubble() {
  const p = DATA.perfiles;
  Plotly.newPlot('chart-cluster-bubble', [{
    x: p.map(d => d.edad_media),
    y: p.map(d => d.tasa_2024),
    text: p.map(d => `<b>${d.id}: ${d.name}</b><br>Lista Nominal: ${(d.ln_2024/1e6).toFixed(2)}M (${d.pct_padron}%)<br>Tasa 2024: ${d.tasa_2024}%<br>Brecha Pres-Inter: ${d.brecha_pres_inter} pp`),
    mode: 'markers+text',
    textposition: 'top center',
    textfont: { size: 10, weight: 'bold' },
    hovertemplate: '%{text}<extra></extra>',
    marker: {
      size: p.map(d => d.pct_padron * 2.6),
      color: p.map(d => d.color),
      opacity: 0.85,
      line: { color: '#1E1B24', width: 1.5 }
    }
  }], {
    margin: { t: 25, r: 25, b: 45, l: 55 },
    xaxis: { title: 'Edad Promedio del Perfil (años)', range: [22, 68] },
    yaxis: { title: 'Tasa de Participación 2024 (%)', range: [36, 75] }
  }, { responsive: true });
}

function renderClusterBars() {
  const p = DATA.perfiles;
  const labels = p.map(d => `${d.id}: ${d.name.split(' ').slice(0,3).join(' ')}`);
  Plotly.newPlot('chart-cluster-bars', [
    { x: labels, y: p.map(d => d.tasa_pres), name: 'Media Presidencial (12-18-24)', type: 'bar', marker: { color: '#5B2C6F' } },
    { x: labels, y: p.map(d => d.tasa_inter), name: 'Media Intermedia (09-15-21)', type: 'bar', marker: { color: '#D4AC0D' } },
    { x: labels, y: p.map(d => d.brecha_pres_inter), name: 'Brecha (pp)', type: 'scatter', mode: 'lines+markers', line: { color: '#C0392B', width: 2.5 } }
  ], {
    barmode: 'group',
    margin: { t: 20, r: 20, b: 65, l: 50 },
    yaxis: { title: 'Porcentaje (%) / Puntos (pp)' },
    legend: { orientation: 'h', y: -0.28 }
  }, { responsive: true });
}

function renderProfileCards() {
  const container = document.getElementById('profiles-cards-container');
  container.innerHTML = DATA.perfiles.map(p => `
    <div class="profile-card">
      <div class="profile-header" style="background:${p.color}">
        <div>
          <div style="font-size:0.76rem;text-transform:uppercase;letter-spacing:0.6px;opacity:0.9;">Perfil ${p.id} · ${p.badge}</div>
          <h3 style="font-size:1.22rem;margin-top:3px;">${p.icon} ${p.name}</h3>
          <div style="font-size:0.82rem;opacity:0.92;margin-top:2px;">${p.subtitle}</div>
        </div>
        <div style="text-align:right;background:rgba(0,0,0,0.22);padding:6px 12px;border-radius:10px;">
          <div style="font-size:1.25rem;font-weight:800;">${p.pct_padron}%</div>
          <div style="font-size:0.7rem;">${(p.ln_2024/1e6).toFixed(2)}M Electores</div>
        </div>
      </div>
      <div class="profile-body">
        <div class="metrics-mini">
          <div><div class="m-val">${p.tasa_2024}%</div><div class="m-lbl">Voto 2024</div></div>
          <div><div class="m-val">${p.tasa_inter}%</div><div class="m-lbl">Intermedia</div></div>
          <div><div class="m-val">${p.edad_media} años</div><div class="m-lbl">Edad Media</div></div>
          <div><div class="m-val">${p.pct_mujer}% M</div><div class="m-lbl">${p.escolaridad_est} años esc.</div></div>
        </div>
        <p style="font-size:0.87rem;color:#333;">${p.narrative}</p>
        <div class="strategy-box" style="border-left-color:${p.color}">
          <h4 style="color:${p.color}">🎯 Estrategia INE: ${p.ine_strategy}</h4>
          <ul>
            ${p.ine_actions.map(a => `<li>${a}</li>`).join('')}
          </ul>
          <div style="font-size:0.78rem;color:#555;"><strong>Canales clave:</strong> ${p.channels}</div>
        </div>
      </div>
    </div>
  `).join('');
}

function initStatesTab() {
  const selState = document.getElementById('sel-state');
  const sortedByName = [...DATA.estados].sort((a,b) => a.edonom.localeCompare(b.edonom));
  selState.innerHTML = sortedByName.map(s => `<option value="${s.edocve}">${s.edonom} (${s.tasa_2024}%)</option>`).join('');
  updateStateView();
  updateSingleStateDetail();
}

function updateStateView() {
  const reg = document.getElementById('sel-region').value;
  const filtered = reg === 'ALL' ? DATA.estados : DATA.estados.filter(s => s.region === reg);

  const statesNames = filtered.map(s => s.edonom);
  const traces = DATA.perfiles.map(p => ({
    y: statesNames,
    x: filtered.map(s => s.perfiles_pct[p.id] || 0),
    name: `${p.id}: ${p.name.split(' ').slice(0,2).join(' ')}`,
    type: 'bar',
    orientation: 'h',
    marker: { color: p.color }
  }));

  Plotly.newPlot('chart-states-stacked', traces, {
    barmode: 'stack',
    margin: { t: 10, r: 20, b: 40, l: 135 },
    xaxis: { title: '% de la Lista Nominal Estatal', range: [0, 100] },
    yaxis: { autorange: 'reversed', tickfont: { size: 10 } },
    legend: { orientation: 'h', y: -0.18, font: { size: 9.5 } }
  }, { responsive: true });

  const tbody = document.querySelector('#table-states tbody');
  tbody.innerHTML = filtered.map(s => {
    const pMeta = DATA.perfiles.find(p => p.id === s.perfil_dominante) || DATA.perfiles[0];
    return `<tr>
      <td><strong>${s.edonom}</strong></td>
      <td>${s.region}</td>
      <td>${s.ln_2024.toLocaleString('es-MX')}</td>
      <td><strong>${s.tasa_2024}%</strong></td>
      <td>${s.tasa_pres}%</td>
      <td>${s.tasa_inter}%</td>
      <td>+${s.brecha} pp</td>
      <td>${s.escolaridad} años</td>
      <td><span class="pill" style="background:${pMeta.color}">${s.perfil_dominante}: ${pMeta.name.split(' ').slice(0,2).join(' ')} (${s.perfiles_pct[s.perfil_dominante]}%)</span></td>
    </tr>`;
  }).join('');
}

function updateSingleStateDetail() {
  const cve = parseInt(document.getElementById('sel-state').value, 10);
  const st = DATA.estados.find(s => s.edocve === cve) || DATA.estados[0];
  document.getElementById('single-state-title').textContent = `${st.edonom} — Evolución 2009–2024 (${st.region})`;
  document.getElementById('single-state-subtitle').textContent = `Lista Nominal 2024: ${st.ln_2024.toLocaleString('es-MX')} · Participación 2024: ${st.tasa_2024}% · Brecha Pres-Inter: +${st.brecha} pp`;

  const years = ['2009', '2012', '2015', '2018', '2021', '2024'];
  const nacVals = years.map(y => (DATA.nacional_anual.find(n => n.AELEC.toString() === y) || {}).TASA_SV || 0);
  const stVals = years.map(y => st.evolucion[y]);

  Plotly.newPlot('chart-single-state', [
    { x: years, y: stVals, name: st.edonom, mode: 'lines+markers+text', text: stVals.map(v=>v+'%'), textposition: 'top center', line: { color: '#8E24AA', width: 3.5 }, marker: { size: 10 } },
    { x: years, y: nacVals, name: 'Promedio Nacional', mode: 'lines+markers', line: { color: '#7F8C8D', width: 2, dash: 'dash' } }
  ], {
    margin: { t: 25, r: 20, b: 40, l: 50 },
    yaxis: { title: 'Tasa de Participación (%)', range: [25, 80] },
    legend: { orientation: 'h', y: -0.18 }
  }, { responsive: true });
}

function runSimulator() {
  const edad = document.getElementById('sim-edad').value;
  const sexo = document.getElementById('sim-sexo').value;
  const tiposec = document.getElementById('sim-tiposec').value;
  const eleccion = document.getElementById('sim-eleccion').value;

  let pId = 'P5';
  if (['60-69', '70+'].includes(edad) && tiposec === 'U') pId = 'P1';
  else if (['50-59', '60-69', '70+'].includes(edad) && tiposec !== 'U') pId = 'P2';
  else if (['18-19', '20-24', '25-29', '30-34'].includes(edad) && tiposec !== 'U') pId = 'P6';
  else if (['20-24', '25-29', '30-34'].includes(edad) && sexo === '0' && tiposec === 'U') pId = 'P5';
  else if (['18-19', '25-29', '30-34', '35-39'].includes(edad) && sexo === '1' && tiposec === 'U') pId = 'P3';
  else pId = 'P4';

  const p = DATA.perfiles.find(x => x.id === pId);
  const tasaEsp = eleccion === 'PRES' ? p.tasa_pres : p.tasa_inter;
  const extraNote = sexo === '2' ? '<div style="margin-top:8px;padding:8px;background:#E8F8F5;border-radius:6px;font-size:0.82rem;"><strong>Nota Casilla No Binaria 2024:</strong> Las personas con credencial No Binaria (SEXO=2) registraron una participación ejemplar de <strong>75.24%</strong> en 2024 (79 de 105 registros).</div>' : '';

  document.getElementById('sim-result-box').innerHTML = `
    <div style="border:2px solid ${p.color};border-radius:12px;padding:18px;background:#FCFAFD;">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <span class="pill" style="background:${p.color};font-size:0.85rem;">Perfil Asignado: ${p.id} — ${p.name}</span>
        <span style="font-size:1.35rem;font-weight:800;color:${p.color}">Tasa Esperada: ${tasaEsp}%</span>
      </div>
      <p style="font-size:0.88rem;margin:10px 0;color:#333;">${p.narrative}</p>
      <div class="strategy-box" style="border-left-color:${p.color};margin-top:10px;">
        <h4 style="color:${p.color}">🚀 Intervención Focalizada Recomendada al INE: ${p.ine_strategy}</h4>
        <ul>${p.ine_actions.map(a => `<li>${a}</li>`).join('')}</ul>
        <div style="font-size:0.8rem;"><strong>Canales prioritarios:</strong> ${p.channels}</div>
      </div>
      ${extraNote}
    </div>
  `;
}

function renderSimImpact() {
  const targetProfiles = DATA.perfiles;
  const names = targetProfiles.map(p => `${p.id}: ${p.name.split(' ').slice(0,2).join(' ')}`);
  const currentVotesInter = targetProfiles.map(p => Math.round(p.ln_2024 * (p.tasa_inter / 100) / 1e6 * 100) / 100);
  const gain5pp = targetProfiles.map(p => Math.round(p.ln_2024 * 0.05 / 1e6 * 100) / 100);

  Plotly.newPlot('chart-sim-impact', [
    { x: names, y: currentVotesInter, name: 'Votantes Base en Intermedia (Millones)', type: 'bar', marker: { color: '#5B2C6F' } },
    { x: names, y: gain5pp, name: 'Nuevos Votantes con Meta +5 pp (Millones)', type: 'bar', marker: { color: '#27AE60' } }
  ], {
    barmode: 'stack',
    margin: { t: 20, r: 20, b: 60, l: 50 },
    yaxis: { title: 'Millones de Votantes' },
    legend: { orientation: 'h', y: -0.25 }
  }, { responsive: true });
}

window.addEventListener('DOMContentLoaded', initDashboard);
</script>
</body>
</html>
"""

html_out = html_template.replace("__JSON_PAYLOAD__", json_str)
with open(os.path.join(BASE_DIR, "dashboard_ccpc_ine.html"), "w", encoding="utf-8") as f:
    f.write(html_out)

print("Dashboard HTML standalone creado en C:\\Users\\52477\\Desktop\\hackatonINE\\dashboard_ccpc_ine.html")
