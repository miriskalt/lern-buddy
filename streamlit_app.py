import streamlit as st

st.set_page_config(page_title="Leni's Lernpflanze", page_icon="🌱")

if "minutes" not in st.session_state:
    st.session_state.minutes = 0

st.title("🌱 Leni's Lernpflanze")
st.write("Lass deine Pflanze wachsen, indem du lernst!")

minutes_added = st.number_input(
    "Wie viele Minuten hast du gelernt?",
    min_value=1,
    max_value=300,
    value=25,
)

if st.button("Ich habe gelernt!"):
    st.session_state.minutes += minutes_added

total = st.session_state.minutes

st.subheader(f"Gesamte Lernzeit: {total} Minuten")

if total < 30:
    plant = "🌱"
    stage = "Keimling"
elif total < 60:
    plant = "🌿"
    stage = "Junge Pflanze"
elif total < 120:
    plant = "🪴"
    stage = "Kräftig am Wachsen"
elif total < 300:
    plant = "🌷"
    stage = "Blühende Pflanze"
else:
    plant = "🌳"
    stage = "Lernbaum"

st.markdown(
    f"""
    <div style="text-align:center;font-size:120px;">
        {plant}
    </div>
    """,
    unsafe_allow_html=True,
)

st.success(f"Stufe: {stage}")

if total < 30:
    progress = total / 30
    target = 30
elif total < 60:
    progress = (total - 30) / 30
    target = 60
elif total < 120:
    progress = (total - 60) / 60
    target = 120
elif total < 300:
    progress = (total - 120) / 180
    target = 300
else:
    progress = 1.0
    target = None

if target:
    st.write(f"Nächste Wachstumsstufe bei {target} Minuten!")
    st.progress(progress)
else:
    st.balloons()
    st.write("🎉 Deine Pflanze ist zu einem mächtigen Lernbaum geworden!")

if st.button("Neue Pflanze starten"):
    st.session_state.minutes = 0
    st.rerun()