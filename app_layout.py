import streamlit as st
from pathlib import Path
from PIL import Image
from profile_data.profiles import Profiles

#  ---  GENERAL SETTINGS  ---
PAGE_TITLE = "Digital CV | James C. Mattingly"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
NAME = "James C. Mattingly"
DESCRIPTION = "Assimilating years of CPA experience, data analytics and web development."
EMAIL = "jchrismattingly@gmail.com"


#  ---  RESUME DATABASE  ---
from db_connection import conn
p_conn = Profiles(conn)

#  ---  PATH TO FILES  ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

#  ---  PROFILE PICTURE  ---
img = Image.open(current_dir / "assets" / "cv_photo_Jun27_borderwhite.jpg")
img = img.rotate(angle=8, expand=False )

#  ---  RESUME FILE  ---
resume = current_dir / "assets" / "Resume Jul20 James Christopher Mattingly.pdf"
with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#  ---  TRAINING FILE  ---
training = current_dir / "assets" / "Mattingly Training and Knowledge.pdf"
with open(training, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()




########################################################################
##  APP LAYOUT
########################################################################

class ResumeApp:
    def __init__(self):
        pass

    ####################################################################################################################
    #  ---  BANNER SECTION  ---

    def banner_section(self):
        col1, col2 = st.columns(2, gap='small')
        with col1:
            st.markdown("")
            st.markdown("")
            st.image(img, width=250)
        with col2:
            st.title(NAME)
            st.write(DESCRIPTION)
            st.download_button(
                label=" Download Resume",
                data=PDFbyte,
                file_name=resume.name,
                mime="application/octet-stream"
            )
            st.write(EMAIL)


    ####################################################################################################################
    #  ---  AREAS OF EXPERTISE  ---

    def expertise_section(self):
        st.write("#")
        with st.container():
            st.markdown("<h3 style='text-align: center; '>Areas of Expertise</h3>",
                        unsafe_allow_html=True)
            for index, row in p_conn.expertise.iterrows():
                st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)

        col = st.columns((1,2,1))
        with col[1]:
            st.markdown("<hr style='margin-top:4'></hr>", unsafe_allow_html=True)


    ####################################################################################################################
    #  ---  HARD SKILLS  ---

    def hard_skills_section(self):
        with st.container():
            st.markdown("<h3 style='text-align: center'>Hard Skills</h3>", unsafe_allow_html=True)
            for index, row in p_conn.skills.iterrows():
                st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)
        col = st.columns((1, 2, 1))
        with col[1]:
            st.markdown("<hr style='margin-top:4'></hr>", unsafe_allow_html=True)

    ####################################################################################################################
    #  ---  WORK HISTORY  ---

    def work_history_section(self):
        with st.container():
            st.markdown("<h3 style='text-align: center'>Work History</h3>", unsafe_allow_html=True)
            for index, row in p_conn.work_history.iterrows():
                st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)
        col = st.columns((1, 2, 1))
        with col[1]:
            st.markdown("<hr style='margin-top:4'></hr>", unsafe_allow_html=True)

    ####################################################################################################################
    # ---  PROJECTS & ACCOMPLISHMENTS  ---

    def projects_section(self):
        with st.container():
            st.markdown("<h3 style='text-align: center'>Web & Data Analytic Projects</h3>", unsafe_allow_html=True)
            st.write("")
            cols = st.columns((3, 2, 2))
            for index, row in p_conn.project_links.iterrows():
                with cols[0]:
                    st.write(f"{row[0]}")
                with cols[1]:
                    if row[1] == "":
                        st.write(f"[NA]()")
                    else:
                        st.write(f"[Web Site]({row[1]})")
                with cols[2]:
                    st.write(f"[GitHub Code]({row[2]})")

            st.write("")
            st.markdown("<p style='text-align:center'>** Website Projects are hosted on Render and initial loading "
                        "may be slow</p>", unsafe_allow_html=True)
        col = st.columns((1, 2, 1))
        with col[1]:
            st.markdown("<hr style='margin-top:4'></hr>", unsafe_allow_html=True)

    ####################################################################################################################
    #  --- CAREER HIGHLIGHTS  ---

    def career_highlights(self):
        st.write("#")
        with st.expander("CAREER HIGHLIGHTS"):
            st.markdown("<h3 style='text-align: center; '>Career Highlights</h3>",
                        unsafe_allow_html=True)
            for index, row in p_conn.highlights.iterrows():
                st.markdown(f"<h6 style=' padding-bottom:2px'><ul><li>{row[0]}</li></ul></h6>",
                            unsafe_allow_html=True)


    ####################################################################################################################
    #  ---  EDUCATION, TRAINING & KNOWLEDGE  ---

    def education_section(self):
        st.write("")
        st.write("")
        with st.expander("EDUCATION, TRAINING & KNOWLEDGE"):
            st.write("")
            st.markdown(f"<h5 style='text-align: center; background-color:#2B56AD; padding:5px'>Education</h5>",
                        unsafe_allow_html=True)
            st.markdown(f"<p style='padding: 10px'>Bachelor of Business Administration - Accounting, Texas A&M University, "
                        f"College Station, Texas</p>", unsafe_allow_html=True)
            st.markdown(f"<p> </p>", unsafe_allow_html=True)
            st.markdown(f"<h5 style='text-align: center; background-color:#2B56AD; padding:5px'>Training & Knowledge "
                        f"Areas</h5>",
                        unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; "
                        f"padding:5px'>Python Library</h6>",
                        unsafe_allow_html=True)
            cols = st.columns([2.2, 6])
            for index, row in p_conn.python.iterrows():
                with cols[0]:
                    st.write(f"{index}")
                with cols[1]:
                    st.write(f"{row[0]}")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Database Management</h6>",
                        unsafe_allow_html=True)
            cols = st.columns([2.2, 6])
            for index, row in p_conn.database.iterrows():
                with cols[0]:
                    st.write(f"{index}")
                with cols[1]:
                    st.write(f"{row[0]}")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Finance and Accounting</h6>",
                        unsafe_allow_html=True)
            for index, item in p_conn.accounting.iterrows():
                row1 = st.columns((2.2, 6))
                with row1[0]:
                    tile = st.container()
                    tile.write(f"{index}")
                with row1[1]:
                    tile = st.container()
                    tile.write(f"{item[0]}")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Online_Courses</h6>",
                        unsafe_allow_html=True)
            for index, item in p_conn.online_courses.iterrows():
                row1 = st.columns((2.2, 6))
                with row1[0]:
                    tile = st.container()
                    tile.write(f"{item[0]}")
                with row1[1]:
                    tile = st.container()
                    tile.write(f"[{item[1]}]({item[2]})")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Online_Video_Training</h6>",
                        unsafe_allow_html=True)
            for index, item in p_conn.video_training.iterrows():
                row1 = st.columns((2.2, 6))
                with row1[0]:
                    tile = st.container()
                    tile.write(f"{item[0]}")
                with row1[1]:
                    tile = st.container()
                    tile.write(f"[{item[1]}]({item[2]})")
            st.write("")
            st.write("")

    def section_call(self):
        self.banner_section()
        self.expertise_section()
        self.hard_skills_section()
        self.work_history_section()
        self.projects_section()
        self.career_highlights()
        self.education_section()

