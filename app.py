from pathlib import Path
import streamlit as st
from PIL import Image
from profile_dicts.profiles import Profiles


#  ---  PATH TO FILES  ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

#  ---  PROFILE PICTURE  ---
img = Image.open(current_dir / "assets" / "crop_hockey_pic.jpg")
img = img.rotate(angle=10, expand=True, fillcolor='maroon')

#  ---  RESUME FILE  ---
resume = current_dir / "assets" / "Resume James Christopher Mattingly May24.pdf"
with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#  ---  TRAINING FILE  ---
training = current_dir / "assets" / "Mattingly Training and Knowledge.pdf"
with open(training, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()

#  ---  GENERAL SETTINGS  ---
PAGE_TITLE = "Digital CV | James C. Mattingly"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
NAME = "James C. Mattingly"
DESCRIPTION = "Assimilating years of CPA experience, data analytics and web development."
EMAIL = "jchrismattingly@gmail.com"


####################################################################################################################
#  ---  RESUME DATABASE  ---
conn = st.connection('db_mattingly_profile', type='sql')
p_conn = Profiles(conn)

####################################################################################################################
#  ---  BANNER SECTION  ---
col1, col2 = st.columns(2, gap='small')
with col1:
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
st.write("#")
with st.container():
    st.markdown("<h3 style='text-align: center; '>Areas of Expertise</h3>",
                unsafe_allow_html=True)
    for index, row in p_conn.expertise.iterrows():
        st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)


####################################################################################################################
#  ---  HARD SKILLS  ---
st.write("#")
with st.container():
    st.markdown("<h3 style='text-align: center'>Hard Skills</h3>", unsafe_allow_html=True)
    for index, row in p_conn.skills.iterrows():
        st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)


####################################################################################################################
#  ---  WORK HISTORY  ---
st.write("#")
with st.container():
    st.markdown("<h3 style='text-align: center'>Work History</h3>", unsafe_allow_html=True)
    for index, row in p_conn.work_history.iterrows():
        st.markdown(f"<h6 style='text-align: center; padding-top:3px'>{row[0]}</h6>", unsafe_allow_html=True)


####################################################################################################################
# ---  PROJECTS & ACCOMPLISHMENTS  ---
st.write("#")
with st.container():
    st.markdown("<h3 style='text-align: center'>Web & Data Analytic Projects</h3>", unsafe_allow_html=True)
    st.write("")

    cols = st.columns((3, 2, 2))
    for index, row in p_conn.links.iterrows():
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
    st.write(" *** Website Projects are hosted on Render and initial loading may be slow")


####################################################################################################################
#  --- CAREER HIGHLIGHTS  ---
st.write("#")
with st.expander("CAREER HIGHLIGHTS"):
    st.markdown("<h3 style='text-align: center; '>Career Highlights</h3>",
                unsafe_allow_html=True)
    for index, row in p_conn.highlights.iterrows():
        st.markdown(f"<h6 style=' padding-bottom:2px'><ul><li>{row[0]}</li></ul></h6>",
                    unsafe_allow_html=True)


####################################################################################################################
#  ---  EDUCATION, TRAINING & KNOWLEDGE  ---
st.write("")
st.write("")
with st.expander("EDUCATION, TRAINING & KNOWLEDGE"):
    st.write("")
    st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Education</h6>",
                unsafe_allow_html=True)
    st.markdown(f"<h6 style='padding: 10px'>Bachelor of Business Administration - Accounting, Texas A&M University, "
                f"College Station, Texas</h6<", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Training & Knowledge "
                f"Areas</h6>",
                unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown(f"<h6 style='text-align: center; background-color:#2B56AD; padding:5px'>Python Library</h6>",
                unsafe_allow_html=True)

    cols = st.columns([2, 6])
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

    cols = st.columns([2, 6])
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
        row1 = st.columns((2, 6))
        with row1[0]:
            tile = st.container()
            tile.write(f"{index}")
        with row1[1]:
            tile = st.container()
            tile.write(f"{item[0]}")

    st.write("")
    st.write("")

    # --- DOWNLOAD BUTTON
    st.download_button(
        label="Download Training & Knowledge PDF",
        data=PDFbyte2,
        file_name=training.name,
        mime="application/octet-stream"
    )
