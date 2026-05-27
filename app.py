import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="MedExplained | Next-Gen Platform",
    page_icon="⚕️",
    layout="wide"
)

# Initialize Session State
if 'current_step' not in st.session_state: st.session_state.current_step = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'language' not in st.session_state: st.session_state.language = 'English'

st.markdown("""
<style>
    .vetted-badge { background: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 20px; font-weight: bold; border: 1px solid #22c55e; display: inline-block; font-size: 0.8rem; }
    .hero-title { font-size: 3.5rem; font-weight: 800; background: linear-gradient(135deg, #38bdf8 0%, #2dd4bf 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .custom-card { padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; background: #ffffff; transition: 0.3s; }
    .custom-card:hover { border-color: #38bdf8; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .roadmap-container { padding: 20px; background: #f8fafc; border-radius: 10px; border-left: 5px solid #38bdf8; }
</style>
""", unsafe_allow_html=True)

def vetted_badge(name):
    st.markdown(f'<div class="vetted-badge">✓ Peer-Reviewed by {name}</div>', unsafe_allow_html=True)

st.sidebar.title("⚕️ MedExplained")
nav = st.sidebar.radio("Navigate", ["Home", "AI Tools", "Diagnostic Simulator", "Community & Chapters", "Career Roadmap", "Contact"])

if nav == "Home":
    st.markdown('<h1 class="hero-title">Simplified Medical Knowledge</h1>', unsafe_allow_html=True)
    st.info("Welcome to the next-gen platform for health literacy.")
    
    # Language Toggle (Feature 9)
    st.session_state.language = st.selectbox("🌐 Select Language Library:", ["English", "Spanish", "French", "Mandarin"])
    
    st.subheader("Latest MythBuster")
    with st.expander("Does cracking knuckles cause arthritis?"):
        st.write("Myth: False. It is just nitrogen gas bubbles popping in your joints.")
        vetted_badge("Dr. Smith, Rheumatology")

elif nav == "AI Tools":
    st.header("🤖 AI-Powered Tools")
    # Jargon Translator (Feature 1)
    st.subheader("1. Jargon Translator")
    user_text = st.text_area("Paste complex medical text here:")
    if st.button("Simplify"):
        st.success("AI Logic: Translating for a 12-year-old... 'This condition basically means your body's defense system is slightly confused...'")
    
    # Ask-A-Scientist (Feature 10)
    st.subheader("2. Ask-A-Scientist")
    with st.form("mailbox"):
        st.text_area("What is your anonymous question?")
        st.form_submit_button("Send Anonymously")

elif nav == "Diagnostic Simulator":
    st.header("🩺 Diagnose the Patient")
    # Case Study Simulator (Feature 3)
    if st.session_state.current_step == 0:
        st.write("Scenario: A 14-year-old athlete reports knee swelling after a pivot.")
        if st.button("Order MRI"):
            st.session_state.current_step = 1
            st.rerun()
    elif st.session_state.current_step == 1:
        st.write("Result: The MRI shows a ligament tear.")
        if st.button("Diagnose: ACL Tear"):
            st.success("Correct! You solved the case.")
            st.session_state.current_step = 0

elif nav == "Community & Chapters":
    st.header("🌍 Global Community")
    
    # Map (Feature 6)
    st.subheader("Active Chapters")
    m = folium.Map(location=[20, 0], zoom_start=2)
    folium.Marker([35.7, -78.8], popup="MedExplained NC").add_to(m)
    st_folium(m, width=700)
    
    # Leaderboard (Feature 5)
    st.subheader("Volunteer Leaderboard")
    st.table({"Volunteer": ["Alice", "Bob", "Charlie"], "Hours": [120, 95, 80]})
    
    # Toolkits (Feature 4)
    st.subheader("Downloadable Resources")
    st.download_button("Download Club Toolkit PDF", "PDF_DATA", "toolkit.pdf")

elif nav == "Career Roadmap":
    # Career Pathway Roadmap (Feature 8)
    st.header("Path to Medicine")
    stage = st.slider("Select Stage:", 0, 3, 0, format_func=lambda x: ["High School", "Undergrad", "Med School", "Residency"][x])
    
    roadmaps = {
        0: "Focus on Biology, Chemistry, and volunteer hours.",
        1: "Complete Pre-med requirements and MCAT.",
        2: "Clinical rotations and specialty matching.",
        3: "Residency and Board Certification."
    }
    st.markdown(f'<div class="roadmap-container">{roadmaps[stage]}</div>', unsafe_allow_html=True)

elif nav == "Contact":
    st.header("Get in Touch")
    st.write("MedExplained Inc. Rolesville, NC")
