import streamlit as st
import streamlit.components.v1 as components

# Configure the page settings
st.set_page_config(
    page_title="MedExplained | Simplified Medical Knowledge",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Blue/Turquoise Theme, animations, hover states, and responsive styling
st.markdown("""
<style>
    /* Gradient text effect and accent colors */
    .hero-title {
        font-size: 3.8rem;
        line-height: 1.15;
        font-weight: 800;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #38bdf8 0%, #2dd4bf 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .blue-text { color: #38bdf8; font-weight: 600; }
    .turquoise-text { color: #2dd4bf; font-weight: 600; }
    
    /* Interactive Card Zoom and Hover Effects */
    .custom-card {
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        background: rgba(255, 255, 255, 0.03);
        transition: all 0.3s ease;
    }
    .custom-card:hover {
        transform: translateY(-5px);
        border-color: #2dd4bf;
        box-shadow: 0 10px 20px rgba(45, 212, 191, 0.1);
    }
    
    /* Global Tab Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        padding-bottom: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 12px 20px;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        color: #38bdf8 !important; 
        border-bottom: 3px solid #2dd4bf !important;
    }

    /* Style enhancements for alert/success blocks */
    div[data-testid="stExpander"] {
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 10px;
    }
    div[data-testid="stInfo"] {
        background-color: rgba(56, 189, 248, 0.08);
        border-left: 5px solid #38bdf8;
        border-radius: 8px;
    }
    div[data-testid="stSuccess"] {
        background-color: rgba(45, 212, 191, 0.08);
        border-left: 5px solid #2dd4bf;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

def change_page(page_name):
    st.session_state.current_page = page_name

# ==========================================
# MAIN PAGE ROUTE (Contains all the tabs)
# ==========================================
if st.session_state.current_page == 'main':

    # Navigation Tabs
    tab_home, tab_about, tab_services, tab_articles, tab_team, tab_involved, tab_contact = st.tabs(
        ["🏠 Home", "📖 About", "⚙️ Services", "✍️ Articles", "👥 Team", "🌍 Get Involved", "✉️ Contact"]
    )

    # --- HOME TAB ---
    with tab_home:
        st.write("") 
        col1, col2 = st.columns([3, 2], gap="large")

        with col1:
            st.markdown("<h1 class='hero-title'>Your Trusted Source for Simplified Medical Knowledge</h1>", unsafe_allow_html=True)
            st.markdown("<h3 class='turquoise-text'>Empower Your Health Literacy</h3>", unsafe_allow_html=True)
            st.write(
                "Welcome to **MedExplained**, a youth-led initiative aiming to bridge the gap between "
                "complex medical jargon and everyday understanding. We believe health literacy is a "
                "fundamental human right, and we provide reliable, accessible information for free."
            )
            st.write("")
            st.info("💡 **Our Mission:** Demystifying the world of medicine, breaking down barriers, and fostering a globally informed community.")
            st.write("")

        with col2:
            st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=1000", use_column_width=True)

    # --- ABOUT TAB ---
    with tab_about:
        st.write("")
        st.markdown("<h2 class='turquoise-text'>About MedExplained</h2>", unsafe_allow_html=True)
        
        col_abt1, col_abt2 = st.columns([3, 2], gap="large")
        with col_abt1:
            st.write("""
            At **MedExplained**, we are passionate about making health literacy a universal reality. Today, the internet is flooded 
            with confusing medical websites and misleading rumors. We solve this issue by offering peer-reviewed, easily 
            digestible medical explanations without the complex gatekeeping jargon.
            
            We create structured write-ups on critical biological mechanisms, professional healthcare careers, healthcare history, 
            and global health topics. By breaking these down, we empower students, parents, and community members worldwide 
            to understand wellness and advocate for their own medical needs.
            """)
            st.markdown("#### Why Health Literacy Matters:")
            st.write("✔️ **Safe Self-Care:** Helps people spot and avoid dangerous medical hoaxes.")
            st.write("✔️ **Stronger Communities:** Encourages collaborative health education across demographic sectors.")
            st.write("✔️ **Confident Patient-Doctor Conversations:** Bridges communications during personal medical visits.")
        
        with col_abt2:
            st.image("https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&q=80&w=800", use_column_width=True)

    # --- SERVICES TAB ---
    with tab_services:
        st.write("")
        st.markdown("<h2 class='blue-text'>Our Essential Services</h2>", unsafe_allow_html=True)
        st.write("Providing dynamic tools, structured research, and global resources to empower communities.")
        st.write("")
        
        s_col1, s_col2, s_col3 = st.columns(3, gap="large")

        with s_col1:
            st.markdown("""
            <div class='custom-card'>
                <h3 class='blue-text'>🩺 Concept Simplification</h3>
                <p>We transform dense, multi-syllable anatomical topics and medical jargon into plain, easy-to-read guides that anybody can understand.</p>
            </div>
            """, unsafe_allow_html=True)
            
        with s_col2:
            st.markdown("""
            <div class='custom-card'>
                <h3 class='blue-text'>🛡️ Accessible Resources</h3>
                <p>Providing high-quality educational guides, illustrations, and structured write-ups to the global public completely free of charge.</p>
            </div>
            """, unsafe_allow_html=True)
            
        with s_col3:
            st.markdown("""
            <div class='custom-card'>
                <h3 class='blue-text'>🌍 Global Literacy Reach</h3>
                <p>Mobilizing youth leaders to run outreach initiatives, distribute resources, and speak in local schools regarding wellness topics.</p>
            </div>
            """, unsafe_allow_html=True)

    # --- ARTICLES TAB ---
    with tab_articles:
        st.write("")
        st.markdown("<h2 class='turquoise-text'>Featured Medical Articles</h2>", unsafe_allow_html=True)
        st.write("Dive deep into our simplified medical explanations below:")
        st.write("")
        
        a_col1, a_col2, a_col3 = st.columns(3, gap="large")

        with a_col1:
            st.image("https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=600", use_column_width=True)
            st.markdown("<h4 class='blue-text'>The Importance of Anesthesiology</h4>", unsafe_allow_html=True)
            st.write("Anesthesia is a crucial specialty aiming to make surgeries painless and keep patients completely safe.")
            st.button("Read full article", key="btn_art1", on_click=change_page, args=("article_1",), use_container_width=True)

        with a_col2:
            st.image("https://images.unsplash.com/photo-1579684385127-1ecd15d5bfbc?auto=format&fit=crop&q=80&w=600", use_column_width=True)
            st.markdown("<h4 class='blue-text'>Common Medical Hoaxes</h4>", unsafe_allow_html=True)
            st.write("Vaccines, knuckle-cracking, gum-swallowing, and shaving. Let's bust 5 major myths together.")
            st.button("Read full article", key="btn_art2", on_click=change_page, args=("article_2",), use_container_width=True)

        with a_col3:
            st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=600", use_column_width=True)
            st.markdown("<h4 class='blue-text'>Do electronics emit radiation?</h4>", unsafe_allow_html=True)
            st.write("Is your phone's radiation actually dangerous, or is it non-ionizing? Here is the scientific truth.")
            st.button("Read full article", key="btn_art3", on_click=change_page, args=("article_3",), use_container_width=True)

    # --- TEAM TAB ---
    with tab_team:
        st.write("")
        st.header("Meet the Team")
        st.write("The people behind the mission of MedExplained.")
        st.write("")
        
        t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
        with t_col2:
            st.markdown("""
            <div style='text-align: center; padding: 30px; border-radius: 16px; border: 1px solid rgba(56, 189, 248, 0.2); background: rgba(56, 189, 248, 0.05);'>
                <img src='https://ui-avatars.com/api/?name=Harshith+Potluri&background=0284c7&color=fff&size=200' style='border-radius: 50%; width: 140px; margin-bottom: 15px;' />
                <h3 style='margin: 0;'>Harshith Potluri</h3>
                <p class='turquoise-text' style='font-size: 1.1rem; margin-top: 5px; font-weight: 700;'>Founder & Leader</p>
                <p style='font-style: italic; opacity: 0.9;'>
                    "Hi! I'm Harshith, the Founder and Leader of the youth-led initiative MedExplained! 
                    We hope to provide medical information across the world and increase health literacy!"
                </p>
            </div>
            """, unsafe_allow_html=True)

    # --- GET INVOLVED TAB ---
    with tab_involved:
        st.write("")
        st.markdown("<h2 class='turquoise-text'>Join the MedExplained Family</h2>", unsafe_allow_html=True)
        st.write("Become a youth health advocate! Help draft medical articles, design resources, or launch school clubs.")
        st.write("")

        g_col1, g_col2, g_col3 = st.columns(3, gap="large")
        with g_col1:
            st.markdown("### 🌍 Global Impact")
            st.write("Directly contribute to boosting global health knowledge and earning verified volunteer hours while making medical facts accessible.")
        with g_col2:
            st.markdown("### 🏆 Leadership Merit")
            st.write("Gain incredible resume weight for college applications, summer programs, and medical field connections by leading your own local chapter.")
        with g_col3:
            st.markdown("### 🤝 Active Collaboration")
            st.write("Join a vibrant, globally connected network of high schoolers and undergraduates interested in bioscience, public health, and medicine.")

        st.markdown("---")
        
        # Embedded Google Form for Volunteer Signups
        st.markdown("<h4 style='text-align: center;'>Volunteer Interest Signup Form</h4>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; opacity: 0.8;'>Submit your application below. Your responses will be securely logged directly to our system.</p>", unsafe_allow_html=True)
        
        # Center the Google Form on the page
        col_form_1, col_form_2, col_form_3 = st.columns([1, 8, 1])
        with col_form_2:
            components.iframe(
                "https://docs.google.com/forms/d/1sIS_cLAnovmQHTWf-FrBvByQvhOB8-OHBHTKOzMLilk/viewform?embedded=true", 
                height=800, 
                scrolling=True
            )
            
            # Backup Link Button in case of iframe scaling on mobile devices
            st.markdown("<div style='text-align: center; margin-top: 15px;'>", unsafe_allow_html=True)
            st.link_button("👉 Having trouble? Click here to open the Form in a new window", "https://docs.google.com/forms/d/1sIS_cLAnovmQHTWf-FrBvByQvhOB8-OHBHTKOzMLilk/viewform", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- CONTACT TAB ---
    with tab_contact:
        st.write("")
        st.markdown("<h2 class='blue-text'>Get in Touch</h2>", unsafe_allow_html=True)
        st.write("Whether you have questions, feedback, or would like to partner with us, we'd love to hear from you!")
        st.write("")

        c_col1, c_col2 = st.columns(2, gap="large")
        with c_col1:
            st.markdown("### 📬 Contact Information")
            st.write("📞 **Phone Support:** +1 (910) 434-5116")
            st.write("👤 **Direct Representative:** Harshith Potluri")
            st.write("✉️ **Email Address:** [harshuaz11@gmail.com](mailto:harshuaz11@gmail.com)")
            st.write("📸 **Instagram Portal:** [@medical.explained_](https://instagram.com/medical.explained_)")
            
        with c_col2:
            st.markdown("### 📩 Quick Message Box")
            # Contact form
            with st.form("contact_form", clear_on_submit=True):
                c_name = st.text_input("Your Name")
                c_email = st.text_input("Your Email")
                c_subject = st.text_input("Subject")
                c_msg = st.text_area("Message Detail")
                contact_submitted = st.form_submit_button("Send Message")
                if contact_submitted:
                    if c_name and c_email and c_msg:
                        st.success(f"🎉 Thanks {c_name}! Your message about '{c_subject}' was received. We will respond within 48 hours.")
                    else:
                        st.error("⚠️ All fields are required to successfully send a message!")

# ==========================================
# UNLISTED ARTICLE PAGES
# ==========================================

elif st.session_state.current_page == 'article_1':
    st.write("")
    st.button("← Back to Articles Dashboard", on_click=change_page, args=("main",))
    st.write("")
    
    col1, col2, col3 = st.columns([1, 6, 1]) 
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
        st.write("")
        st.button("Back to Home", on_click=change_page, args=("main",), key="btm1")

elif st.session_state.current_page == 'article_2':
    st.write("")
    st.button("← Back to Articles Dashboard", on_click=change_page, args=("main",))
    st.write("")
    
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("<h1 class='turquoise-text'>Common Medical Hoaxes</h1>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1579684385127-1ecd15d5bfbc?auto=format&fit=crop&q=80&w=1200", use_column_width=True)
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
        st.write("")
        st.button("Back to Home", on_click=change_page, args=("main",), key="btm2")

elif st.session_state.current_page == 'article_3':
    st.write("")
    st.button("← Back to Articles Dashboard", on_click=change_page, args=("main",))
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
        st.write("")
        st.button("Back to Home", on_click=change_page, args=("main",), key="btm3")


# Universal Footer (Shows on all pages)
st.markdown("<hr style='margin-top: 50px; border-color: rgba(128, 128, 128, 0.2);'><center><small>© 2026 MedExplained. All rights reserved.</small></center>", unsafe_allow_html=True)
