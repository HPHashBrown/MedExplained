import streamlit as st

# Configure the page settings
st.set_page_config(
    page_title="MedExplained",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for White, Blue, and Turquoise Theme (Flat design, no glassmorphism)
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #ffffff;
    }

    /* Text accents */
    .blue-text { color: #0284c7; }
    .turquoise-text { color: #0d9488; }
    
    /* Headers */
    h1, h2, h3 {
        color: #0f172a;
    }

    /* Tab navigation styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 32px;
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 0;
        color: #64748b;
        font-weight: 600;
        padding-top: 15px;
        padding-bottom: 15px;
    }
    .stTabs [aria-selected="true"] {
        color: #0284c7 !important; /* Blue active text */
        border-bottom: 3px solid #0d9488 !important; /* Turquoise active underline */
    }

    /* Customizing info/success banners to fit the theme */
    div[data-testid="stExpander"] {
        border: 1px solid #e0f2fe;
        border-radius: 8px;
    }
    div[data-testid="stInfo"] {
        background-color: #e0f2fe; /* Light blue */
        color: #0369a1;
        border: none;
    }
    div[data-testid="stSuccess"] {
        background-color: #f0fdfa; /* Light turquoise */
        color: #0f766e;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Create Navigation Tabs
tab_home, tab_about, tab_services, tab_articles, tab_team, tab_involved, tab_contact = st.tabs(
    ["Home", "About", "Services", "Articles", "Team", "Get Involved", "Contact"]
)

# --- HOME TAB ---
with tab_home:
    st.write("") # Spacer
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("<h1 style='font-size: 3.5rem; line-height: 1.2; margin-bottom: 0px;'>Your Trusted Source for <br><span class='blue-text'>Simplified</span> Medical Knowledge</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='turquoise-text' style='margin-top: 10px;'>Empower Your Health Literacy</h3>", unsafe_allow_html=True)
        st.write("Simplified medical knowledge at your fingertips - for free. We champion health literacy as a fundamental right, fostering a globally informed community concerning health and wellness.")
        st.write("")
        st.info("💡 **Mission:** Making medical information accessible and understandable for everyone.")

    with col2:
        st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=1000", use_column_width=True)

# --- ABOUT TAB ---
with tab_about:
    st.write("")
    st.header("About MedExplained")
    st.write("""
    At MedExplained, we are dedicated to making medical information accessible and understandable for everyone. Our platform provides simplified explanations of complex medical concepts, empowering individuals with the knowledge they need to make informed health-related decisions. 

    By delivering clear and actionable medical explanations for free, we champion health literacy as a fundamental right. We aim to foster a globally informed community concerning health and wellness.
    """)

# --- SERVICES TAB ---
with tab_services:
    st.write("")
    st.header("Our Services")
    st.write("Providing essential tools and resources to demystify medicine.")
    st.write("")
    s_col1, s_col2, s_col3 = st.columns(3, gap="large")

    with s_col1:
        st.markdown("<h3 class='blue-text'>🩺 Concept Simplification</h3>", unsafe_allow_html=True)
        st.write("We break down complex medical ideas into plain, digestible language for easy understanding.")
        
    with s_col2:
        st.markdown("<h3 class='blue-text'>🛡️ Accessible Resources</h3>", unsafe_allow_html=True)
        st.write("Our platform offers completely free, reliable health content to educate people around the world.")
        
    with s_col3:
        st.markdown("<h3 class='blue-text'>🌍 Community Empowerment</h3>", unsafe_allow_html=True)
        st.write("We provide tools and actionable knowledge aimed at global health literacy improvement.")

# --- ARTICLES TAB ---
with tab_articles:
    st.write("")
    st.header("Latest Articles")
    st.write("Dive into our simple explanations of medical topics.")
    st.write("")
    a_col1, a_col2, a_col3 = st.columns(3, gap="large")

    with a_col1:
        st.image("https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.markdown("<h3 class='turquoise-text'>The Importance of Anesthesiology</h3>", unsafe_allow_html=True)
        st.write("Anesthesia is a very important medical career aiming for patient safety during surgery.")
        with st.expander("Read the full article"):
            st.write("Anesthesiology is a critical medical specialty focused on the total perioperative care of patients before, during, and after surgery. It encompasses anesthesia, intensive care medicine, critical emergency medicine, and pain medicine. Anesthesiologists play a vital role in ensuring patient safety, managing pain, and monitoring vital life functions throughout surgical procedures, allowing complex and life-saving operations to take place safely.")

    with a_col2:
        st.image("https://images.unsplash.com/photo-1584308666744-24d5e45a05b3?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.markdown("<h3 class='turquoise-text'>Common Medical Hoaxes</h3>", unsafe_allow_html=True)
        st.write("No, sicknesses aren't caused by the cold, and cracking your knuckles doesn't cause arthritis.")
        with st.expander("Read the full article"):
            st.write("The medical field is surrounded by myths that have been passed down for generations. For example, going outside with wet hair does not give you a cold—viruses do. Similarly, cracking your knuckles does not lead to arthritis; the popping sound is simply gas bubbles bursting in your synovial fluid. In this article, we debunk these and other widespread medical hoaxes to help you distinguish fact from fiction.")

    with a_col3:
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=600", use_column_width=True)
        st.markdown("<h3 class='turquoise-text'>Do electronics emit radiation?</h3>", unsafe_allow_html=True)
        st.write("This article investigates whether devices emit harmful radiation like all of our parents say.")
        with st.expander("Read the full article"):
            st.write("It is a common concern that smartphones, laptops, and microwaves emit harmful radiation. While it is true that these devices emit electromagnetic radiation, it is 'non-ionizing' radiation. This means it lacks the energy required to break chemical bonds or cause DNA damage, unlike 'ionizing' radiation (such as X-rays). Current scientific consensus indicates that the low levels of non-ionizing radiation emitted by everyday electronics do not pose significant health risks to humans.")

# --- TEAM TAB ---
with tab_team:
    st.write("")
    st.header("Meet the Team")
    st.write("The people behind the mission of MedExplained.")
    st.write("")
    
    t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
    with t_col2:
        st.image("https://ui-avatars.com/api/?name=Harshith+Potluri&background=0284c7&color=fff&size=200", width=150)
        st.markdown("<h3 class='blue-text'>Harshith Potluri</h3>", unsafe_allow_html=True)
        st.markdown("**Founder and Leader**")
        st.write('"Hi! I\'m Harshith, the Founder and Leader of the youth-led initiative MedExplained! We hope to provide medical information across the world and increase health literacy!"')

# --- GET INVOLVED TAB ---
with tab_involved:
    st.write("")
    st.header("Get Involved")
    st.write("Join us in our mission to impact global health literacy. By volunteering, you can earn volunteer hours and make a real difference.")
    st.write("")

    g_col1, g_col2, g_col3 = st.columns(3, gap="large")
    with g_col1:
        st.markdown("<h3 class='blue-text'>🌍 Impact</h3>", unsafe_allow_html=True)
        st.write("Help people across the world better understand the world of medicine!")
    with g_col2:
        st.markdown("<h3 class='blue-text'>🏆 Merit</h3>", unsafe_allow_html=True)
        st.write("Volunteering with us earns you honor and merit for universities and jobs.")
    with g_col3:
        st.markdown("<h3 class='blue-text'>🤝 Collaboration</h3>", unsafe_allow_html=True)
        st.write("Meet new like-minded individuals and form lasting connections.")

    st.write("")
    st.success("✨ **Ready to make a difference?** Reach out using the contact information below to join our team!")

# --- CONTACT TAB ---
with tab_contact:
    st.write("")
    st.header("Contact Us")
    st.write("Feel free to reach out to us with any questions, partnership inquiries, or to volunteer!")
    st.write("")

    c_col1, c_col2 = st.columns(2, gap="large")
    with c_col1:
        st.markdown("<h3 class='turquoise-text'>Contact Info</h3>", unsafe_allow_html=True)
        st.write("📞 **Phone:** +1 (910) 434-5116")
        st.write("👤 **Contact Person:** Harshith Potluri")
    with c_col2:
        st.markdown("<h3 class='turquoise-text'>Digital</h3>", unsafe_allow_html=True)
        st.write("✉️ **Email:** harshuaz11@gmail.com")
        st.write("📸 **Instagram:** [@medical.explained_](https://instagram.com/medical.explained_)")

st.markdown("<hr style='margin-top: 50px; border-color: #e2e8f0;'><center><small style='color: #64748b;'>© 2026 MedExplained. All rights reserved.</small></center>", unsafe_allow_html=True)
