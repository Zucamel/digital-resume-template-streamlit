from pathlib import Path
import time
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_ZJ.pdf"
profile_pic = current_dir / "assets" / "IMG_9188.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zuzana Jerdonekova"
PAGE_ICON = ":wave:"
NAME = "Zuzana Jerdonekova"
DESCRIPTION = """
Junior Data Analyst
"""
EMAIL = "jerdonekovazuzana@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/zuzana-jrd/",
    "GitHub":
    "https://github.com/Zucamel?tab=repositories",
    "Medium": "https://medium.com/@jerdonekovazuzana",
}
PROJECTS = {
    "🏆 Becoming a junior data analyst: exploration of job postings in Ireland":
    "https://medium.com/@jerdonekovazuzana/analysis-and-visualizations-of-job-postings-from-ireland-5f46024f5c8e",
    "🏆 Bricks & Figures: Dive with Us into the LEGO World":
    "https://medium.com/@jerdonekova-baluch/bricks-figures-db9c64852fad",
}
SECTIONS = {
    "Experience": "Exp",
    "Tech stack": "Hard-skills",
    "Career history": "CV",
    "Portfolio": "Projects",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS - Trochu crazy, ale neni to uplne nutny, jen priklad, co jde delat.. ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- LOAD PDF
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- PROFIL PIC
profile_pic = Image.open(profile_pic)

with st.sidebar:
    my_radio = st.radio("Wow effect radio button", list(SECTIONS.keys()))
    awesomeness_level = st.slider("Awesomeness leves", 0, 10, 0)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

if my_radio == "Experience":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qalifications")
    st.write("""
    - ✔️ 6 Months data analyst internship
    - ✔️ 300 hours during Czechitas Data Accademy
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """)

if my_radio == "Tech stack":
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write("""
    - 👩‍💻 Programming: SQL, Python
    - 📊 Data Visulization: Tableau
    - 🗄️ Databases: Snowflake, MySQL
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - :speech_balloon: Team Tools: Slack, Jira, Confluence
    """)

if my_radio == "Career history":
    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Junior Data Analyst | GAMEE**")
    st.write("02/2024 - Present")
    st.write("""
    - ► #Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► #Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► #Redesigned data model through iterations that improved predictions by 12%
    """)

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write("""
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """)

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write("""
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """)

if my_radio == "Portfolio":
    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

for i in range(awesomeness_level + 1):
    awesomeness_level = i
    with st.sidebar:
        st.write("🎉" * i)
    time.sleep(0.2)