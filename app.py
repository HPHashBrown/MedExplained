import streamlit as st

# Configure the page settings
st.set_page_config(
    page_title="MedExplained",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to inject some medical-themed styling
st.markdown("""
<style>
    .blue-text { color: #2563eb; }
    .stDivider { margin-top: 3rem; margin-bottom: 3rem; }
    .article-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# Create Navigation Tabs
tab_home, tab_about, tab_services, tab_articles, tab_team, tab_involved, tab_contact = st.tabs(
    ["Home", "About", "Services", "Articles", "Team", "Get Involved", "Contact"]
)

# --- HOME TAB ---
with tab_home:
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("<h1 style='font-size: 3rem;'>Your Trusted Source for <span class='blue-text'>Simplified</span> Medical Knowledge</h1>", unsafe_allow_html=True)
        st.markdown("### Empower Your Health Literacy")
        st.write("Simplified medical knowledge at your fingertips - for free. We champion health literacy as a fundamental right, fostering a globally informed community concerning health and wellness.")
        st.info("💡 **Mission:** Making medical information accessible and understandable for everyone.")

    with col2:
        st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=1000", use_column_width=True)

# --- ABOUT TAB ---
with tab_about:
    st.header("About MedExplained")
    st.write("""
    At MedExplained, we are dedicated to making medical information accessible and understandable for everyone. Our platform provides simplified explanations of complex medical concepts, empowering individuals with the knowledge they need to make informed health-related decisions. 

    By delivering clear and actionable medical explanations for free, we champion health literacy as a fundamental right. We aim to foster a globally informed community concerning health and wellness.
    """)

# --- SERVICES TAB ---
with tab_services:
    st.header("Our Services")
    s_col1, s_col2, s_col3 = st.columns(3)

    with s_col1:
        st.subheader("🩺 Concept Simplification")
        st.write("We break down complex medical ideas into plain, digestible language for easy understanding.")
        
    with s_col2:
        st.subheader("🛡️ Accessible Resources")
        st.write("Our platform offers completely free, reliable health content to educate people around the world.")
        
    with s_col3:
        st.subheader("🌍 Community Empowerment")
        st.write("We provide tools and actionable knowledge aimed at global health literacy improvement.")

# --- ARTICLES TAB ---
with tab_articles:
    st.header("Latest Articles")
    a_col1, a_col2, a_col3 = st.columns(3, gap="medium")

    with a_col1:
        st.image("https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.subheader("The Importance of Anesthesiology")
        st.write("Anesthesia is a very important medical career aiming for patient safety during surgery.")
        with st.expander("Read the full article"):
            st.write("Anesthesiology is a critical medical specialty focused on the total perioperative care of patients before, during, and after surgery. It encompasses anesthesia, intensive care medicine, critical emergency medicine, and pain medicine. Anesthesiologists play a vital role in ensuring patient safety, managing pain, and monitoring vital life functions throughout surgical procedures, allowing complex and life-saving operations to take place safely.")

    with a_col2:
        st.image("https://images.unsplash.com/photo-1584308666744-24d5e45a05b3?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.subheader("Common Medical Hoaxes")
        st.write("No, sicknesses aren't caused by the cold, and cracking your knuckles doesn't cause arthritis.")
        with st.expander("Read the full article"):
            st.write("The medical field is surrounded by myths that have been passed down for generations. For example, going outside with wet hair does not give you a cold—viruses do. Similarly, cracking your knuckles does not lead to arthritis; the popping sound is simply gas bubbles bursting in your synovial fluid. In this article, we debunk these and other widespread medical hoaxes to help you distinguish fact from fiction.")

    with a_col3:
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.subheader("Do electronics emit radiation?")
        st.write("This article investigates whether devices emit harmful radiation like all of our parents say.")
        with st.expander("Read the full article"):
            st.write("It is a common concern that smartphones, laptops, and microwaves emit harmful radiation. While it is true that these devices emit electromagnetic radiation, it is 'non-ionizing' radiation. This means it lacks the energy required to break chemical bonds or cause DNA damage, unlike 'ionizing' radiation (such as X-rays). Current scientific consensus indicates that the low levels of non-ionizing radiation emitted by everyday electronics do not pose significant health risks to humans.")

# --- TEAM TAB ---
with tab_team:
    st.header("Meet the Team")
    t_col1, t_col2, t_col3 = st.columns([1, 2, 1])

    with t_col2:
        st.image("https://ui-avatars.com/api/?name=Harshith+Potluri&background=2563eb&color=fff&size=200", width=150)
        st.subheader("Harshith Potluri")
        st.markdown("**Founder and Leader**")
        st.write('"Hi! I\'m Harshith, the Founder and Leader of the youth-led initiative MedExplained! We hope to provide medical information across the world and increase health literacy!"')

# --- GET INVOLVED TAB ---
with tab_involved:
    st.header("Get Involved")
    st.write("Join us in our mission to impact global health literacy. By volunteering, you can earn volunteer hours and make a real difference.")

    g_col1, g_col2, g_col3 = st.columns(3)
    with g_col1:
        st.markdown("### 🌍 Impact")
        st.write("Help people across the world better understand the world of medicine!")
    with g_col2:
        st.markdown("### 🏆 Merit")
        st.write("Volunteering with us earns you honor and merit for universities and jobs.")
    with g_col3:
        st.markdown("### 🤝 Collaboration")
        st.write("Meet new like-minded individuals and form lasting connections.")

    st.success("Ready to make a difference? Reach out using the contact information below to join our team!")

# --- CONTACT TAB ---
with tab_contact:
    st.header("Contact Us")
    st.write("Feel free to reach out to us with any questions, partnership inquiries, or to volunteer!")

    c_col1, c_col2 = st.columns(2)
    with c_col1:
        st.write("📞 **Phone:** +1 (910) 434-5116")
        st.write("👤 **Contact Person:** Harshith Potluri")
    with c_col2:
        st.write("✉️ **Email:** harshuaz11@gmail.com")
        st.write("📸 **Instagram:** [@medical.explained_](https://instagram.com/medical.explained_)")

st.markdown("<br><br><center><small>© 2026 MedExplained. All rights reserved.</small></center>", unsafe_allow_html=True)
