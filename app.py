import streamlit as st

# Configure the page settings
st.set_page_config(
    page_title="MedExplained",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Blue and Turquoise Theme (Adapts to Streamlit's Light/Dark mode)
st.markdown("""
<style>
    /* Text accents */
    .blue-text { color: #38bdf8; } /* Lightened slightly to work on both backgrounds */
    .turquoise-text { color: #2dd4bf; }
    
    /* Tab navigation styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 32px;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 0;
        font-weight: 600;
        padding-top: 15px;
        padding-bottom: 15px;
    }
    .stTabs [aria-selected="true"] {
        color: #0284c7 !important; /* Blue active text */
        border-bottom: 3px solid #0d9488 !important; /* Turquoise active underline */
    }

    /* Customizing info/success banners to fit the theme using rgba for both light/dark mode support */
    div[data-testid="stExpander"] {
        border: 1px solid rgba(2, 132, 199, 0.2);
        border-radius: 8px;
    }
    div[data-testid="stInfo"] {
        background-color: rgba(2, 132, 199, 0.1); /* Transparent blue */
        border: none;
    }
    div[data-testid="stSuccess"] {
        background-color: rgba(13, 148, 136, 0.1); /* Transparent turquoise */
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

def change_page(page_name):
    st.session_state.current_page = page_name

# ==========================================
# MAIN PAGE ROUTE (Contains all the tabs)
# ==========================================
if st.session_state.current_page == 'main':

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
            st.button("Read full article", key="btn_art1", on_click=change_page, args=("article_1",), use_container_width=True)

        with a_col2:
            st.image("https://images.unsplash.com/photo-1584308666744-24d5e45a05b3?auto=format&fit=crop&q=80&w=600", use_column_width=True)
            st.markdown("<h3 class='turquoise-text'>Common Medical Hoaxes</h3>", unsafe_allow_html=True)
            st.write("No, sicknesses aren't caused by the cold, and cracking your knuckles doesn't cause arthritis.")
            st.button("Read full article", key="btn_art2", on_click=change_page, args=("article_2",), use_container_width=True)

        with a_col3:
            st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=600", use_column_width=True)
            st.markdown("<h3 class='turquoise-text'>Do electronics emit radiation?</h3>", unsafe_allow_html=True)
            st.write("This article investigates whether devices emit harmful radiation like all of our parents say.")
            st.button("Read full article", key="btn_art3", on_click=change_page, args=("article_3",), use_container_width=True)

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

# ==========================================
# UNLISTED ARTICLE PAGES
# ==========================================

elif st.session_state.current_page == 'article_1':
    st.write("")
    st.button("← Back to Home", on_click=change_page, args=("main",))
    st.write("")
    
    col1, col2, col3 = st.columns([1, 6, 1]) # Centered layout
    with col2:
        st.markdown("<h1 class='turquoise-text'>The Importance of Anesthesiology</h1>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=1200", use_column_width=True)
        st.write("")
        
        st.markdown("""
        *Anesthesiology is the field of medicine which applies anesthesia to patients to keep them safe during surgery. But what exactly is anesthesia? Is it deadly? You will find out in this article!*
        
        Anesthesiology is the field of medicine which applies anesthesia to patients to keep them safe during surgery. But first, what is anesthesia?
        
        Anesthesia is the substance used to make surgery painless for patients. Without anesthesia, surgery would be highly impractical and unethical, and in some cases it may even be impossible! Anesthesia can come in two different states: **Gas (inhaled)** or **liquid/gel**.
        
        ### The Four Main Forms of Anesthesia
        
        1. **General Anesthesia:** This type of anesthesia renders the patient completely unconscious and motionless when used.
        2. **Regional Anesthesia:** This type of anesthesia numbs a large, specific part of the body.
        3. **Local Anesthesia:** This type of anesthesia numbs only a small specific area, usually for something such as stitches or a dental filling.
        4. **Sedation:** Also known as "twilight sleep," this type of anesthesia relaxes the patient, ranging from light relaxation to deep sleep. However, the patient still has to breathe on their own.
        
        ---
        
        ### Side Effects and Risks
        
        Now you may be asking, *"Why don't we just use general anesthesia for all types of surgeries, whether big or small?"*
        
        For most patients, anesthesia can cause temporary side effects such as:
        * Nausea and vomiting
        * Dizziness
        * Sore throat
        * Temporary confusion
        * Shivering
        
        These usually fade away within twenty-four hours, and are much less common when regional or local anesthesia is used. 
        
        In some rare cases, anesthesia can cause serious issues such as postoperative delirium, cognitive dysfunction, breathing problems, or allergic reactions. While these risks are less prominent with regional/local anesthesia, they can still happen.
        
        However, **the risk of an anesthetic accident is incredibly low**, being roughly 1 for every 100,000 to 200,000 cases. If the patient is healthy and is just getting a routine checkup, the chances of an anesthetic accident are even lower, often less than 1 in a million.
        
        ---
        
        ### Statistics of Anesthesiologists
        
        Let's look into what it takes to join this respected profession, from the education timeline to expected earnings:
        
        * **Education:** Anesthesiologists on average need to study about **12 to 14 years** to become qualified. They must spend four years earning their bachelor's degree, four years in medical school, and four years in an anesthesiology residency. They can also spend 1 to 2 optional years in a fellowship to gain a sub-specialization. Anesthesiologic medicine is highly competitive and requires incredible amounts of skill and passion.
        * **Earnings:** The starting salary for Anesthesiologists in the United States is approximately **$393,215**. If an anesthesiologist is more specialized and experienced, they can earn between **$400,000 to $600,000 annually**!
        
        ### Summary
        To summarize, Anesthesiology is a very well respected but competitive field. Anesthesia/Anesthetics are the substances used to numb patients or make them unconscious. It can have side effects, but serious complications are very rare. Anesthesiologists take 12-14 years to be certified, and can earn up to $400k - $600k annually.
        """)

elif st.session_state.current_page == 'article_2':
    st.write("")
    st.button("← Back to Home", on_click=change_page, args=("main",))
    st.write("")
    
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("<h1 class='turquoise-text'>Common Medical Hoaxes</h1>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1584308666744-24d5e45a05b3?auto=format&fit=crop&q=80&w=1200", use_column_width=True)
        st.write("")
        
        st.markdown("""
        *No, sicknesses aren't caused by the cold, and cracking your knuckles doesn't cause arthritis. Here are some common medical myths that we have busted over the years.*
        
        ---
        
        ### 1. Vaccines can cause autism.
        
        **Vaccines simply do not give you autism.** This myth originated from a fraudulent study published in 1998. It was falsely concluded by Andrew Wakefield, the leader of the study, who claimed that the MMR (Measles, Mumps, and Rubella) vaccine had a correlation to autism and intestinal inflammation. 
        
        However, it was later discovered that Andrew Wakefield was paid by lawyers who were suing vaccine manufacturers. Furthermore, Wakefield was trying to develop his own alternative MMR vaccine to rival the existing one. He was ultimately caught, and his medical license in the UK was revoked. Despite being fully debunked, the myth still persists today because many news stations and celebrities in the early 2000s fueled public fear, keeping the myth alive in public memory.
        
        ---
        
        ### 2. Cracking Knuckles can cause Arthritis.
        
        **This is simply not true.** This myth most likely came from an assumption that the popping noise heard when cracking knuckles causes physical damage to your joint cartilage. 
        
        This myth was famously disproven by the brave Dr. Donald Unger, who cracked the knuckles of only his left hand for fifty years while leaving his right hand alone. After those fifty years, he examined both hands and was proven to have no arthritis in either, earning him an Ig Nobel Prize for his dedication. What really happens when you crack your joints is that dissolved nitrogen bubbles in your synovial fluid are popping.
        
        ---
        
        ### 3. Swallowing Gum causes it to stay in your stomach for seven years.
        
        A myth we all used to believe as kids, **this myth has thankfully been disproven.** While the human body cannot digest the synthetic rubber base of modern chewing gum, the gum still moves regularly through the digestive tract in roughly the same amount of time as other foods. 
        
        The gum will not stick to the stomach walls or intestines, and is instead safely excreted within a few days. This myth likely started as an old wives' tale to scare children from swallowing their gum.
        
        ---
        
        ### 4. Cold weather causes the Common Cold
        
        Surprisingly, **cold weather doesn't actually cause the common cold.** The common cold is caused entirely by viruses. 
        
        This myth originated from the obvious observed pattern that we get sick more often during cold weather. However, there is no direct causation between cold temperatures and the virus infecting you. Instead, cold weather causes people to stay indoors close to one another, making it easier for viruses to spread, and the cool, dry air provides ideal conditions for certain cold viruses to survive and travel.
        
        ---
        
        ### 5. Shaving your hair makes it grow back thicker, darker, and/or faster.
        
        **Shaving your hair simply does not make it grow back thicker, darker, or faster.** This myth has been proven false multiple times through scientific studies dating as far back as 1928. 
        
        Many people believe this myth due to a physical illusion: hair naturally tapers at the end, but when you shave it, you cut it at its thickest point near the root. As the short hair grows back out, the blunt edge feels coarser and looks darker than the tapered tip did, but the overall hair structure has not changed at all.
        
        ---
        
        ### Conclusion
        Those were five of the most common medical myths and hoaxes debunked! We hope you learned something new!
        """)

elif st.session_state.current_page == 'article_3':
    st.write("")
    st.button("← Back to Home", on_click=change_page, args=("main",))
    st.write("")
    
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("<h1 class='turquoise-text'>Do electronics emit radiation?</h1>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=1200", use_column_width=True)
        st.write("")
        
        st.markdown("""
        We've all heard it from our parents before: *"Get off of your phone. It causes radiation."* But have we ever fact-checked our parents? This article aims to figure out the legitimacy of this claim. Spoiler alert: the results may shock you!
        
        According to the U.S. Environmental Protection Agency, devices such as our mobile phones, tablets, and TV screens do release radiation, specifically known as **radiofrequency radiation**.
        
        ### HOWEVER...
        
        **Radiofrequency radiation is not damaging.** It is a form of **non-ionizing radiation**, meaning that it lacks the energy required to break chemical bonds, damage your DNA, or cause cancer. Ionizing radiation (like X-rays or nuclear radiation) is dangerous, but the low-frequency non-ionizing waves from your electronic devices are perfectly safe.
        
        This proves that while devices emit radiation, the radiation is not harmful enough to cause any significant damage. 
        
        To put this into perspective, **a single banana is far more radioactive than electronic devices**, and bananas are eaten safely every single day!
        
        So now you can finally rest easy (or stay up scrolling), knowing that your phone does not emit harmful radiation. You can finally prove your parents wrong.
        """)


# Universal Footer (Shows on all pages)
st.markdown("<hr style='margin-top: 50px; border-color: rgba(128, 128, 128, 0.2);'><center><small>© 2026 MedExplained. All rights reserved.</small></center>", unsafe_allow_html=True)
