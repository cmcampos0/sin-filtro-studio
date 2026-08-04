import streamlit as st

st.set_page_title("Sin Filtro Studio | Producción de Episodios", layout="wide")

st.title("🎙️ Sin Filtro Studio — Panel de Producción")
st.markdown("---")

# Barra lateral para la Bóveda
st.sidebar.header("📁 Bóveda de Conocimiento (Core & Motores)")
st.sidebar.markdown("Sube o verifica los documentos clave de la Biblia Editorial.")

uploaded_files = st.sidebar.file_uploader(
    "Cargar documentos de la Bóveda (.md o .txt)", 
    accept_multiple_files=True,
    type=["md", "txt"]
)

if uploaded_files:
    st.sidebar.success(f"¡{len(uploaded_files)} documentos cargados en la Bóveda!")
    boveda_activa = True
else:
    st.sidebar.warning("⚠️ Bóveda vacía. Sube tus archivos markdown para activar el motor.")
    boveda_activa = False

# Panel Principal
tab1, tab2, tab3 = st.tabs(["🌱 Semillas e Ideas", "✍️ Generador por Escenas", "⚖️ Juez Evaluador (20 Variables)"])

with tab1:
    st.subheader("Paso 1: Selección de Semillas")
    st.markdown("Introduce una idea de la vida real o selecciona una semilla para evaluar si pasa el filtro editorial del show.")
    
    idea_usuario = st.text_area("¿Cuál es la observación o fenómeno que quieres analizar hoy?", placeholder="Ej. La gente que presume su terapia en redes sociales...")
    
    if st.button("Evaluar Semilla con el Sistema de Ideas"):
        if not boveda_activa:
            st.error("Por favor, carga primero los documentos de la Bóveda en el menú lateral.")
        else:
            st.info("Analizando semilla bajo los criterios de Karla y Regina...")
            # Aquí conectaremos la lógica de IA en el siguiente paso

with tab2:
    st.subheader("Paso 2: Motor de Conversación por Escenas")
    st.markdown("Genera la conversación respetando que el episodio **ya había empezado** y aplicando el contraste entre Karla y Regina.")
    st.text("Esta sección se activará una vez aprobada la semilla.")

with tab3:
    st.subheader("Paso 3: Auditoría y Sistema de Evaluación")
    st.markdown("El juez evaluará el guion sobre 200 puntos (umbral mínimo de aprobación: 170).")
    st.text("Sin puntuación aprobatoria, el episodio no se emite.")
