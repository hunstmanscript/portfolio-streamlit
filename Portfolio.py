import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Mi Portfolio", page_icon="📊", layout="wide")

# Sidebar como índice de proyectos y CV
st.sidebar.title("📂 Índice")
seleccion = st.sidebar.radio(
    "Seleccione una sección:",
    [
        "CV",
        "Proyecto 1: Dashboard Finanzas Personales",
        "Proyecto 2: Grilla de Importaciones"
    ]
)

# Banner superior
st.image(
    "C:/Users/agrep1/Desktop/Data_Analyst/ISB-ABA-Product-Card-768x512.jpg.optimal.jpg",
    use_container_width=True
)

# Caption estilizado
st.markdown(
    """
    <p style="color:#4a568d; font-weight:bold; font-size:60px; text-align:center;">
        Data Analyst
    </p>
    """,
    unsafe_allow_html=True
)

# Encabezado
st.title("Hola!!! Soy Rossman Larez")
st.subheader("Contador Público | Experiencia en Logística, Finanzas, Control de Gestión y Análisis de Datos")

# Crear dos columnas: izquierda para foto/índice, derecha para contenido
col1, col2 = st.columns([1, 3])

with col1:
    st.image("C:/Users/agrep1/Documents/rl/doc/perf rl.jpeg", width=300)

# Contenido según selección
with col2:
    if seleccion == "CV":
        st.subheader("📄 Curriculum Vitae - Rossman A. Larez Carrero")
           
        st.markdown("**Perfil Profesional:**")
        st.markdown("Profesional proactivo, comprometido y adaptable, con sólida experiencia en análisis y gestión de operaciones, finanzas y logística. Orientado a optimizar procesos y mejorar la eficiencia operativa mediante el análisis de datos y controles financieros")

        st.markdown("**Habilidades:**")
        st.markdown("""
        - **Software:** SAP, WMS, Excel avanzado, Power BI, VBA, Saint, A2, Valery, ERP Manager.  
        - **Finanzas:** Análisis de costos, conciliación bancaria, presupuestos.  
        - **Logística:** Gestión marítima y terrestre, control de contenedores, despachos e inventarios.  
        - **Competencias:** Liderazgo, proactividad, comunicación, resolución de problemas, adaptabilidad.
        """)

        st.markdown("**Experiencia Profesional:**")
        st.markdown("""
        - **Implant IMPO - Departamento de Importaciones CCU (Mar. 2022–Actualidad)**  
          Gestión de operaciones marítimas, control de contenedores, costos logísticos y riesgos (demurrage, free time).  
          Elaboración de reportes logísticos y financieros para toma de decisiones.  

        - **Sitrans Ltda. – Encargado de Agendamiento (Dic. 2021–Mar. 2022)**  
          Responsable del agendamiento y gestión de proveedores para el proyecto Walmart.  

        - **Sociedad Clínica Comercial S.A. – Encargado de Compras (Ene. 2021–Ago. 2021)**  
          Gestión estratégica de compras y coordinación con Finanzas para cumplimiento de pagos.  

        - **Talleres Lucas S.A. – Administrativo de Logística y Compras (Oct. 2017–Jun. 2020)**  
          Planificación de compras, control de inventario y digitalización de procesos logísticos (WMS, ERP).  

        - **Inversiones Looard, C.A – Administrador de Tienda (Dic. 2015–Mar. 2017)**  
          Gestión administrativa y operativa de tienda, supervisión de personal y control de inventarios.  

        - **Maderas del Orinoco C.A – Analista de Costos (Sep. 2011–Ago. 2015)**  
          Elaboración de análisis de costos, control presupuestario y reportes financieros.
        """)

        st.markdown("**Formación Académica:**")
        st.markdown("""
        - Licenciado en Contaduría Pública (UCV 2010)  
        - Técnico Superior Universitario en Administración, mención Contabilidad y Finanzas (La Salle 2007)
        """)

    elif seleccion == "Proyecto 1: Dashboard Finanzas Personales":
        st.subheader("1- 📊 Dashboard de Finanzas Personales en Google Sheets")
        st.write("Visualización y análisis interactivo de ingresos y egresos en Google Sheets📊, integrado con la app móvil MyFinance para una gestión confiable y seguimiento en tiempo real.")

        st.markdown("**Resumen del análisis:**")
        st.markdown("""
        - Se analizaron los ingresos y egresos de manera mensual.  
        - Se identificaron patrones de gasto y oportunidades de ahorro.  
        - Se generaron gráficos 📈 dinámicos para facilitar la interpretación de los datos.  
        - Integración con la app móvil MyFinance para asegurar datos confiables y actualizados.
        """)

        st.markdown("**Objetivos del proyecto:**")
        st.markdown("""
        - Brindar una herramienta visual para el seguimiento financiero personal.  
        - Facilitar la toma de decisiones basadas en datos históricos y en tiempo real.  
        - Detectar tendencias y comportamientos financieros a lo largo del tiempo.  
        - Garantizar la confiabilidad y disponibilidad de los datos.
        """)

        st.markdown("**Soluciones implementadas:**")
        st.markdown("""
        - 📈 Dashboard interactivo en Google Sheets con filtros por categoría y mes.  
        - 📊 Gráficos de barras y líneas para visualizar ingresos, egresos y balances.  
        - 🚦 Alertas visuales para gastos que exceden presupuestos establecidos.  
        - 🚀 Sincronización con la app MyFinance para seguimiento en tiempo real.
        """)

        st.image("C:/Users/agrep1/Desktop/Data_Analyst/dashboard.jpg", width=600)
        st.markdown("[Abrir Google Sheets](https://docs.google.com/spreadsheets/d/1FayawMLjrhKKlfUTh0oTJM2O0q_dwFcw/edit?rtpof=true)")
        st.subheader("📱 App Móvil: MyFinance")
        st.write("Aplicación para control de ingresos y egresos, con Dashboard Interactivo integrado con Google Sheets.")
        st.image("C:/Users/agrep1/Desktop/Data_Analyst/app Myfinance.jpg", width=600)
        st.markdown("[Abrir AppSheet](https://www.appsheet.com/newshortcut/4b240338-7e90-4e8b-9d17-b838216ba9d2)")

    elif seleccion == "Proyecto 2: Grilla de Importaciones":
        st.subheader("2- ✈️🚚🚢 Grilla de Importaciones en Procesos")
        st.write("Dashboard Interactivo en Excel")

        st.markdown("**Objetivo General:**")
        st.markdown("Controlar y visualizar las operaciones de importación en todas sus etapas, integrando KPI de desempeño y eficiencia.")

        st.markdown("**Planteamiento del Problema:**")
        st.markdown("""
        En las operaciones de importación, es fundamental mantener un control preciso de cada etapa: operaciones por aceptar 📋, pagadas 💰 y por retirar 📦.  
        La falta de visibilidad sobre el estado de despachos e impuestos puede generar retrasos y errores financieros.
        """)

        st.markdown("**Análisis Realizado:**")
        st.markdown("""
        - Recopilación de datos de operaciones, estado de despachos y contenedores.  
        - Análisis de pagos pendientes y plazos de demurrage.  
        - Establecimiento de KPI: eficiencia de provisión vs saldo pagado.  
        - Dashboard visual con filtros por cliente, aduana y comprador.
        """)

        st.markdown("**Resultados Obtenidos:**")
        st.markdown("""
        - Visualización clara y en tiempo real de operaciones en curso.  
        - Identificación de contenedores y operaciones con riesgo de retraso o costos adicionales.  
        - Monitoreo efectivo de provisión e impuestos, permitiendo ajustes financieros.  
        - Dashboard interactivo que mejora la toma de decisiones y la planificación logística.
        """)

        st.image("C:/Users/agrep1/Desktop/Data_Analyst/GRILLA.jpg", width=600)
        st.markdown("[Abrir Dashboard de Importaciones](https://docs.google.com/spreadsheets/d/1TU_ID_DE_TU_PROYECTO/edit?usp=sharing)")
