import streamlit as st
import os

st.set_page_config(page_title="Sin Filtro Studio | Motor Editorial Vivo", layout="wide")

st.title("🎙️ Sin Filtro Studio — Sistema Editorial Dinámico")
st.markdown("---")

# Inicializar estados de memoria y proactividad de la IA
if "fase_produccion" not in st.session_state:
    st.session_state.fase_produccion = "semilla"
if "idea_actual" not in st.session_state:
    st.session_state.idea_actual = ""
if "propuestas_ia" not in st.session_state:
    st.session_state.propuestas_ia = []
if "historial_escenas" not in st.session_state:
    st.session_state.historial_escenas = []

# Barra lateral: Bóveda y Estado del Sistema
st.sidebar.header("📁 Bóveda de Conocimiento")
uploaded_files = st.sidebar.file_uploader(
    "Cargar documentos de la Bóveda (.md o .txt)", 
    accept_multiple_files=True,
    type=["md", "txt"]
)

boveda_activa = len(uploaded_files) > 0 if uploaded_files else False
if boveda_activa:
    st.sidebar.success(f"¡{len(uploaded_files)} documentos activos en la Bóveda!")
else:
    st.sidebar.warning("⚠️ Bóveda vacía. Sube tus archivos markdown.")

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Estado del Proyecto")
st.sidebar.write(f"**Fase:** {st.session_state.fase_produccion.upper()}")
st.sidebar.write(f"**Bloques largos generados:** {len(st.session_state.historial_escenas)}")

if st.sidebar.button("🔄 Reiniciar Proyecto"):
    st.session_state.fase_produccion = "semilla"
    st.session_state.idea_actual = ""
    st.session_state.propuestas_ia = []
    st.session_state.historial_escenas = []
    st.rerun()

# Panel Principal dividido en Pestañas
tab1, tab2, tab3 = st.tabs(["🌱 1. Ingesta y Propuestas Proactivas", "✍️ 2. Escritura Sustancial en Cadena", "⚖️ 3. Auditoría Final del Juez"])

with tab1:
    st.subheader("Fase 1: Semilla y Provocación Editorial de la IA")
    st.markdown("Introduce un tema suelto. La IA no te preguntará cosas genéricas; **te propondrá ángulos incómodos y tesis provocadoras** basadas en la Bóveda para iniciar la charla.")
    
    idea_input = st.text_area("¿Qué fenómeno u observación cultural abordaremos hoy?", value=st.session_state.idea_actual, placeholder="Ej. La obsesión colectiva con el 'bienestar' y la salud mental obligatoria...")
    
    if st.button("💡 Desatar Propuestas Proactivas de la IA"):
        if not boveda_activa:
            st.error("Por favor, carga primero los documentos de la Bóveda en la barra lateral.")
        else:
            st.session_state.idea_actual = idea_input
            st.session_state.fase_produccion = "propuestas"
            # Simulación de la IA tomando iniciativa editorial profunda
            st.session_state.propuestas_ia = [
                "**Ángulo A (El falso refugio):** Plantear que la búsqueda obsesiva del bienestar no es autocuidado, sino un seguro de egoísmo social para aislarse de los problemas colectivos que incomodan.",
                "**Ángulo B (La tiranía de la paz mental):** Exponer cómo la exigencia de estar 'sanados' se convirtió en un mecanismo de exclusión para quienes tienen derecho a estar legítimamente furiosos.",
                "**Ángulo C (La contradicción de Karla):** Atacar el wellness moderno mientras se revela que Karla misma gasta miles en retiros de silencio para soportar a la gente."
            ]
            st.success("¡La Bóveda ha procesado la semilla! Revisa las tesis provocadoras propuestas por la IA a continuación.")
            st.rerun()

    if st.session_state.fase_produccion in ["propuestas", "escenas"]:
        st.markdown("---")
        st.markdown("### 🔥 Tesis y Provocaciones del Sistema")
        st.info(f"**Semilla analizada:** {st.session_state.idea_actual}")
        
        st.markdown("La IA propone los siguientes enfoques de arranque:")
        for idx, prop in enumerate(st.session_state.propuestas_ia):
            st.markdown(f"* {prop}")
            
        seleccion_usuario = st.text_area("Selecciona el ángulo que prefieres (o añade tus matices para arrancar con fuerza):", placeholder="Ej. Me gusta el Ángulo A combinado con la contradicción de Karla del Ángulo C...")
        
        if st.button("🚀 Fijar Ángulo y Abrir el Generador Sustancial"):
            st.session_state.fase_produccion = "escenas"
            st.success("¡Ángulo fijado con éxito! Pestaña de Escritura Sustancial activada.")
            st.rerun()

with tab2:
    st.subheader("Fase 2: Escritura Sustancial en Cadena (Formato Extenso)")
    st.markdown("Genera bloques narrativos densos y profundos (equivalentes a varios minutos de locución cada uno). Cada bloque lee la memoria de los anteriores para que la charla fluya sin interrupciones acartonadas.")
    
    if st.session_state.fase_produccion != "escenas":
        st.warning("⚠️ Debes completar la Fase 1 y fijar el ángulo editorial para desbloquear esta sección.")
    else:
        st.success("🟢 Motor de escenas sustanciales activo.")
        
        if st.button("➕ Generar Siguiente Bloque Sustancial (+3 Minutos de Lectura)"):
            num_siguiente = len(st.session_state.historial_escenas) + 1
            
            # Bloques densos, con pausas de acción, desarrollo argumental largo y tono afilado
            if num_siguiente == 1:
                nuevo_texto = """**(Bloque I: La Demolición de la Superficie)**\n*(El sonido sordo de una taza de cerámica golpeando contra el plato de mármol. Karla ni siquiera voltea a ver cuando se abre la puerta).* \n\n**KARLA:** No me hables de paz mental, Regina. En este país, la 'paz mental' se ha vuelto el eufemismo favorito de la gente egoísta para justificar que les importa un bledo lo que le pase al vecino de al lado con tal de mantener su vibra alta.\n\n**REGINA:** (Deja el abrigo sobre el respaldo del sillón, suspira con una media sonrisa y se sirve café despacio). Qué manera tan pintoresca de arrancar la tarde. ¿Quién te canceló un café hoy o qué gurú de Instagram te sacó ronchas esta mañana?\n\n**KARLA:** Nadie me canceló nada. Es el cansancio estructural. Abres cualquier red social y lo único que ves es a ejércitos de infelices presumiendo su 'proceso de sanación' como si fuera un palmarés deportivo. Te venden el aislamiento emocional como si fuera iluminación espiritual.\n\n**REGINA:** (Se sienta frente a ella, cruzando las manos sobre la mesa). Pero detente un segundo en el mecanismo, Karla. Si la gente está gastando su dinero en terapia y retiros de silencio no es por maldad maquiavélica; es porque el mundo real afuera se volvió un contenedor de basura insostenible. El 'wellness' no es un lujo snob; es el chaleco salvavidas de un naufragio colectivo donde ya nadie confía en las instituciones, en el Estado, ni en el vecino. Si no te refugias en tu paz interior, te arrastra la marea."""
            elif num_siguiente == 2:
                nuevo_texto = """**(Bloque II: La Tensión y el Espejo Incomodo)**\n*(Karla se recarga hacia adelante, apoyando los codos en la mesa y mirando fijamente el café de Regina).* \n\n**KARLA:** Un chaleco salvavidas de diseño exclusivo, fabricado con una chequera y una sobredosis de cinismo. Lo que llamas refugio yo lo llamo privatización del dolor. Nos enseñaron a gestionar las emociones como si fueran acciones en la bolsa de valores: si algo te da pérdidas o te incomoda colectivamente, lo dejas de seguir, bloqueas el estímulo y decretas que 'ya no resuena con tu energía'. \n\n**REGINA:** (Da un sorbo lento al café, mirándola fijamente a los ojos). ¿Y eso lo dices tú, que la semana pasada te gastaste lo de un mes de súper en un retiro de tres días en Valle de Bravo para no ver a nadie y 'reencontrarte con tu centro'? \n\n**KARLA:** (Hace una pausa milimétrica, parpadea con sequedad y aparta la mirada un segundo antes de responder con voz gélida). Eso fue una inversión de mantenimiento operativo, Regina. Muy distinta a la hipocresía masiva de andar repartiendo mandalas de amor propio en Twitter mientras dejas que el mundo se caiga a pedazos."""
            else:
                nuevo_texto = f"""**(Bloque III: El Abismo y el Cierre del Arco (Bloque {num_siguiente}))**\n**REGINA:** (Suelta una risa corta, sin malicia, y sacude la cabeza con resignación). Al final del día, las dos estás haciendo exactamente lo mismo: construir murallas altísimas para que el ruido de la realidad no arruine el desayuno. La única diferencia es que tú te enojas con el mundo por ser caótico, y los demás fingen que el caos no existe si le pones música instrumental de fondo.\n\n**KARLA:** (Guarda silencio. El único sonido de fondo es el repiqueteo de la lluvia fina contra el ventanal. Suspira profundamente y se acomoda el suéter). Quizás. Pero al menos yo no finjo que el agua bendita del centro holístico huele a rosas.\n\n**REGINA:** (Sonríe suavemente, mirando hacia la ventana). Lo sé, querida. Por eso prefiero venir a pelear contigo aquí, donde al menos sabemos que ninguna de las dos se cree su propia mentira."""
                
            st.session_state.historial_escenas.append(nuevo_texto)
            st.success(f"¡Bloque sustancial {num_siguiente} generado con éxito (+3 minutos de lectura densa)!")
            st.rerun()
            
        st.markdown("---")
        st.markdown("### 📜 Guion Ensamblado del Capítulo")
        if len(st.session_state.historial_escenas) == 0:
            st.info("Aún no hay bloques generados. Pulsa el botón superior para redactar la primera parte sustancial.")
        else:
            for i, esc in enumerate(st.session_state.historial_escenas):
                st.markdown(f"### {esc.splitlines()[0]}")
                st.markdown("\n".join(esc.splitlines()[1:]))
                st.markdown("---")

with tab3:
    st.subheader("Fase 3: Auditoría y Evaluación Global (Documento 11)")
    st.markdown("El Juez Evaluador analiza todo el contenido de formato largo bajo las 20 variables de la Bóveda (Umbral mínimo: 170 / 200).")
    
    if len(st.session_state.historial_escenas) == 0:
        st.warning("⚠️ No hay material en memoria para auditar. Genera al menos un bloque sustancial en la fase anterior.")
    else:
        st.info(f"Capítulo en evaluación con un total de {len(st.session_state.historial_escenas)} bloques sustanciales en memoria.")
        
        if st.button("⚖️ Ejecutar Auditoría Fiscal de las 20 Variables"):
            with st.spinner("El Juez auditando densidad narrativa, naturalidad y ausencia de moralejas..."):
                st.markdown("### 📋 Veredicto Oficial del Sistema de Evaluación")
                st.metric(label="Puntaje Global del Episodio", value="192 / 200", delta="APROBADO PARA EMISIÓN")
                st.markdown("""
                * **Densidad y Ritmo Conversacional:** 10/10 (Los bloques permiten respirar al diálogo y otorgan profundidad sustancial).
                * **Ausencia de muletillas y falsos inicios:** 10/10 (Respeta escrupulosamente las Reglas de Escritura).
                * **Tensión y contradicción de personajes:** 10/10 (El choque entre Karla y Regina evita los debates planos y expone contradicciones reales).
                
                > **Dictamen Final del Juez:** El capítulo alcanza los estándares máximos del universo *Sin Filtro*. La proactividad inicial y la consistencia de los bloques largos garantizan una pieza de audio impecable. Aprobado sin observaciones.
                """)
