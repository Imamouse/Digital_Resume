from pathlib import Path

import streamlit as st
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"


# GENERAL SETTINGS
PAGE_TITLE = "Digital CV | Jc Jeacanie Llido"
PAGE_ICON = "✋"
NAME = "Jc Jeacanie Llido"
DESCRIPTION = """
Experienced Customer Service VA and Escalation Specialist | 
Grit to become a Developer or Data Analyst
"""
EMAIL = "jcllido1@gmail.com"
SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube.com/@jc1263",
    "LinkedIn": "https://www.linkedin.com/in/jeacanie",
    "GitHub": "https://github.com/Imamouse",
    "Facebook": "https://www.facebook.com/jcjeacanie.llido"
}

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales accross the stores":"https://imamouse-salesdashboard-dashboard-j2tnvz.streamlit.app/",
    "🏆 TinDog - Front End: A Dog's Dating App": "https://imamouse.github.io/Tindog/",
    "🏆 Group Sales Dashboard: Excel Dashboards": "https://github.com/Imamouse/Group-Sales-Dashboard/blob/main/DashBoard%2010_09_2022.xlsx",
    "🏆 Project Management Dashboard: Excel Dashboards": "https://github.com/Imamouse/Project-Management-Dashboard/blob/main/Management%20Dashboard%2010_14_2022.xlsx"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# LOAD CSS, PDF, & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📜 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)


# SOCIAL LINKS
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# WORK HISTORY
st.write("#")
st.write("---")
st.subheader("Work History")
st.write("🛒", "ECommerce Customer Service Representative | Non-disclosure agreement")
st.write("January 2023 - Present (4 months)")
st.write(
    """Skilled Customer Service VA with expertise in handling German and English
stores, managing refunds, and coordinating supplier issues. Proficient in
providing exceptional customer support, resolving complex inquiries, and
ensuring timely and effective solutions. Adept at navigating challenging
situations with tact and diplomacy, and collaborating with cross-functional
teams to optimize service delivery. With a strong attention to detail and a
customer-centric focus, I am committed to providing the highest level of service
to customers and ensuring their satisfaction.
""")

st.write("#")
st.write("📞", "Escalations Specialist & Customer Service | Inspiro Relia, Inc")
st.write("December 2020 - January 2023 (2 years 2 months)")
st.write("""
As an experienced escalations specialist, I have a proven track record of
successfully resolving complex customer issues and ensuring a positive
experience for all parties involved. With strong communication and problemsolving skills, I am able to effectively navigate challenging situations and find
mutually beneficial solutions. I am highly organized and detail-oriented, and I
have a deep understanding of customer service best practices. I am confident
in my ability to handle escalated issues with tact and professionalism, and I am
dedicated to delivering exceptional results for my clients.
""")

st.write("#")
st.write("📱", "Digital Assistance Center Specialist | Concentrix")
st.write("September 2020 - November 2020 (3 months)")
st.write("""
As a customer-focused digital assistance center specialist, I have a passion
for helping others and a strong track record of providing exceptional service.
With extensive experience in technical support and troubleshooting, I am able
to quickly and accurately resolve customer issues and ensure a seamless
experience. I am a skilled communicator and able to effectively explain
technical concepts to non-technical audiences. I am also highly organized
and able to handle multiple tasks and priorities simultaneously. I am excited to
bring my skills and experience to a dynamic digital assistance center team and
help drive customer satisfaction and success.
""")

st.write("#")
st.write("📞", "Customer Service Representative | Human Resource Service Center | Transcom")
st.write("January 2019 - August 2020 (1 year 8 months)")
st.write("""
- Customer Service Representative and Billing- Voice and Live Chat:
- ► As a customer service representative with experience in voice support, billing,
and handling multiple chat channels, I am skilled at providing exceptional
service and resolving customer inquiries and issues in a timely and efficient
manner. With strong communication and problem-solving skills, I am able to
effectively navigate complex situations and find mutually beneficial solutions.
I am highly organized and able to efficiently manage multiple tasks and
priorities, including handling voice and chat channels simultaneously. I
am passionate about building long-term relationships with customers and
contributing to the success of a customer service team.

- Human Resource Service Center- Back Office :
- ► As a human resource service center back office specialist, I am skilled at
providing support and guidance to HR professionals and employees. With
extensive experience in HR processes and procedures, I am able to accurately
and efficiently handle a wide range of tasks, including employee onboarding,
benefits administration, and payroll. I am a strong communicator and able to
effectively explain HR policies and procedures to employees. I am also highly
organized and able to manage multiple tasks and priorities simultaneously. I
am dedicated to delivering exceptional service and contributing to the success
of the HR team.

- Customer Service Representative in Tracking and Shipping- Voice and Email:
- ► Experienced customer service representative with a strong track record
of providing exceptional support to customers in the tracking and shipping
industry. Skilled in handling both voice and email inquiries, with a focus on
accurately tracking orders and shipments and providing timely resolutions to
customer issues and concerns. Strong communication skills, ability to work
well under pressure, and exceptional problem-solving abilities.
""")

# SKILLS
st.write("#")
st.write("---")
st.subheader("Interests")
st.write("""
- 🐍Programming: Python
- 👨‍💻Front End Development: HTML, CSS, BootStrap
- 📊Data Visualization: MS Excel, Plotly
""")

# PERSONAL PROJECTS
st.write("#")
st.write("---")
st.subheader("Personal Projects")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



















