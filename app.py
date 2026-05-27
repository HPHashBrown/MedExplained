import streamlit as st

st.set_page_config(
    page_title="MedExplained | Health Literacy Platform",
    page_icon="⚕️",
    layout="wide"
)

# Initialize session state
if 'current_step' not in st.session_state: st.session_state.current_step = 0

# Custom CSS for styling
st.markdown("""
<style>
    .vetted-badge { background: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 20px; font-weight: bold; border: 1px solid #22c55e; display: inline-block; font-size: 0.8rem; margin-bottom: 10px; }
    .hero-title { font-size: 3rem; font-weight: 800; color: #1e293b; }
    .roadmap-container { padding: 20px; background: #f1f5f9; border-radius: 10px; border-left: 5px solid #3b82f6; }
</style>
""", unsafe_allow_html=True)

def vetted_badge(name):
    st.markdown(f'<div class="vetted-badge">✓ Peer-Reviewed by {name}</div>', unsafe_allow_html=True)

st.sidebar.title("⚕️ MedExplained")
nav = st.sidebar.radio("Navigate", ["Home", "Articles", "Diagnostic Simulator", "Community & Chapters", "Career Roadmap", "Contact"])

if nav == "Home":
    st.markdown('<h1 class="hero-title">Simplified Medical Knowledge</h1>', unsafe_allow_html=True)
    st.info("Welcome to the next-gen platform for health literacy.")
    
    st.subheader("Latest MythBuster")
    with st.expander("Does cracking knuckles cause arthritis?"):
        st.write("Myth: False. It is just nitrogen gas bubbles popping in your joints.")
        vetted_badge("Dr. Smith, Rheumatology")
    
    st.write("---")
    st.subheader("Have a Myth you want us to bust?")
    st.link_button("📩 Submit a Myth via Email", "mailto:harshuaz11@gmail.com?subject=Medical Myth Submission")

elif nav == "Articles":
    st.header("📚 Medical Articles")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Using a reliable Unsplash URL for the image
        st.image("https://images.unsplash.com/photo-1584308666744-24d5e45a05b3?auto=format&fit=crop&q=80&w=400", caption="Medical MythBusting")
        
    with col2:
        st.subheader("Common Medical Hoaxes")
        st.write("""
        There are many myths in the medical field. For example, 'wet hair causes colds' is false (viruses cause colds), 
        and cracking your knuckles does not cause arthritis. We aim to debunk these misconceptions with science-backed evidence.
        """)
        vetted_badge("Medical Research Team")

elif nav == "Diagnostic Simulator":
    st.header("🩺 Diagnose the Patient")
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
    
    try:
        import folium
        from streamlit_folium import st_folium
        m = folium.Map(location=[35.7, -78.8], zoom_start=10)
        folium.Marker([35.7, -78.8], popup="MedExplained HQ").add_to(m)
        st_folium(m, width=700, height=300)
    except ImportError:
        st.warning("Folium map requires installation. Run `pip install folium streamlit-folium`.")
    
    st.subheader("Volunteer Leaderboard")
    st.table({"Volunteer": ["Alice", "Bob", "Charlie"], "Hours": [120, 95, 80]})

elif nav == "Career Roadmap":
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
    st.write("Email us at: harshuaz11@gmail.com")
