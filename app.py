import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="wide")

# Sidebar
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])

# Home
if page == "Home":
    st.title("🌟 My Portfolio Website")
    st.subheader("Welcome to my Portfolio!")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://lh3.googleusercontent.com/a/ACg8ocJddJq_Vp0isH6XJ_uDMUx_Imbq-VNzuO6zxhX--QOVv1Gs5swV=s360-c-no",
            width=250
        )

    with col2:
        st.write("Hello! I'm **Jose Raphael R. Lawas**.")
        st.write("Aspiring Full-Stack Developer and AI Enthusiast.")
        st.metric("Projects Completed", "5+")
        st.progress(80)

# About Me
elif page == "About Me":
    st.title("👋 About Me")

    tabs = st.tabs(["Biography", "Education", "Goals"])

    with tabs[0]:
        st.write("I am passionate about building software systems and solving real-world problems.")
    
    with tabs[1]:
        st.write("🎓 Cebu Institute of Technology - University")

    with tabs[2]:
        st.write("🚀 Become a professional full-stack developer.")
        st.write("🤖 Specialize in AI systems.")
        st.write("🌍 Build impactful tech solutions.")

# Skills
elif page == "Skills":
    st.title("💻 Skills")

    skills = {
        "Python": 90,
        "Java": 80,
        "Django": 60,
        "React": 70,
        "Spring Boot": 70
    }

    for skill, level in skills.items():
        st.write(f"### {skill}")
        st.progress(min(level, 100))  # safety limit

    df = pd.DataFrame({
        "Skill": list(skills.keys()),
        "Level": list(skills.values())
    })

    st.bar_chart(df.set_index("Skill"))

# Projects
elif page == "Projects":
    st.title("🚀 Projects")

    with st.expander("🌊 AquaSense"):
        st.write("AI-powered water monitoring system.")

    with st.expander("🚗 ParkNow"):
        st.write("Parking management system using Spring Boot and React.")
    
    with st.expander("🚌 BusMate - Online Ticketing System"):
        st.write("Online bus ticketing system using Spring Boot and React.")
    
    with st.expander("📊 SPMP Evaluator"):
        st.write("System for evaluating SPMP projects.")
    
    with st.expander("📝 BlockNotes - NotesApp"):
        st.write("Online notes application using Spring Boot and React with blockchain storage.")

# Contact
elif page == "Contact":
    import base64

    st.title("📫 Contact Me")

    st.write("📧 Email: joseraphaellawas@gmail.com")
    st.write("📍 Location: Carcar City, Cebu")

    st.markdown("---")

    st.subheader("📄 My Resume")

    try:
        with open("resume.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" height="800px" type="application/pdf"></iframe>
        """

        st.markdown(pdf_display, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("Resume file not found. Make sure resume.pdf is inside the project folder.")