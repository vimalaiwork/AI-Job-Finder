import streamlit as st
import pdfplumber
import pandas as pd
import sqlite3

from company_finder import find_companies
from job_fetcher import fetch_jobs

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="AI Job Finder",
    layout="wide"
)

# ----------------------------
# Custom UI
# ----------------------------
st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
        color: white;
    }

    h1, h2, h3 {
        color: #38bdf8;
    }

    .stButton > button {
        background-color: #38bdf8;
        color: black;
        border-radius: 10px;
        height: 50px;
        width: 220px;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Database Setup
# ----------------------------
conn = sqlite3.connect(
    "jobfinder.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        location TEXT,
        salary TEXT,
        experience TEXT,
        domain TEXT
    )
    '''
)

conn.commit()

# ----------------------------
# Title
# ----------------------------
st.title("AI Job Finder & Company Recommender")

# ----------------------------
# Skill Database
# ----------------------------
skills_db = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "react",
    "node.js",
    "html",
    "css",
    "javascript",
    "ui/ux",
    "figma",
    "cybersecurity",
    "aws",
    "docker",
    "power bi",
    "excel"
]


# ----------------------------
# Upload Resume
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

# ----------------------------
# Main Process
# ----------------------------
if uploaded_file is not None:

    st.success("Resume Uploaded Successfully")

    resume_text = ""

    # ----------------------------
    # Extract Resume Text
    # ----------------------------
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                resume_text += text

    # ----------------------------
    # Show Resume Text
    # ----------------------------
    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    # ----------------------------
    # Skill Extraction
    # ----------------------------
    detected_skills = []

    resume_text_lower = resume_text.lower()

    for skill in skills_db:

        if skill in resume_text_lower:
            detected_skills.append(skill)

    detected_skills = list(set(detected_skills))

    # ----------------------------
    # Show Skills
    # ----------------------------
    st.subheader("Detected Skills")

    if detected_skills:

        for skill in detected_skills:
            st.write(f"✅ {skill.title()}")

    else:
        st.warning("No skills detected")

    # ----------------------------
    # User Preferences
    # ----------------------------
    st.subheader("Job Preferences")

    preferred_role = st.text_input(
        "Preferred Role",
        placeholder="Example: AI Engineer"
    )

    preferred_location = st.text_input(
        "Preferred Location",
        placeholder="Example: Chennai"
    )

    salary_range = st.selectbox(
        "Expected Salary Range",
        [
            "0-3 LPA",
            "3-5 LPA",
            "5-8 LPA",
            "8-12 LPA",
            "12+ LPA"
        ],
        key="salary_select"
    )

    experience_level = st.selectbox(
        "Experience Level",
        [
            "Fresher",
            "0-1 Years",
            "1-3 Years",
            "3+ Years"
        ],
        key="experience_select"
    )

    work_type = st.selectbox(
        "Work Type",
        [
            "Remote",
            "Hybrid",
            "Onsite"
        ],
        key="worktype_select"
    )

    preferred_domain = st.selectbox(
        "Preferred Domain",
        [
            "AI/ML",
            "Web Development",
            "Data Science",
            "Cybersecurity",
            "UI/UX Design",
            "Cloud Computing"
        ],
        key="domain_select"
    )

    # ----------------------------
    # Save Preferences
    # ----------------------------
    save_button = st.button(
        "Save Preferences",
        key="save_preferences_button"
    )

    if save_button:

        cursor.execute(
            '''
            INSERT INTO users
            (role, location, salary, experience, domain)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                preferred_role,
                preferred_location,
                salary_range,
                experience_level,
                preferred_domain
            )
        )

        conn.commit()

        st.success("Preferences Saved Successfully")

  

    # ----------------------------
    # Real API Search
    # ----------------------------
    st.subheader("Live Company & Job Search")

    search_button = st.button(
        "Find Real Jobs",
        key="find_real_jobs_button"
    )

    if search_button:

        # ----------------------------
        # Company Search
        # ----------------------------
        try:

            companies = find_companies(
                preferred_location,
                preferred_domain
            )

            st.subheader("Top Companies")

            if companies:

                for company in companies[:5]:

                    st.write(
                        f"🏢 {company['name']}"
                    )

            else:
                st.warning("No companies found")

        except Exception as e:

            st.error(f"Company API Error: {e}")

        # ----------------------------
        # Job Search
        # ----------------------------
        try:

            jobs = fetch_jobs(
                preferred_role,
                preferred_location
            )

            st.subheader("Live Job Openings")

            if jobs:

                for job in jobs[:10]:

                    st.markdown("---")

                    st.write(
                        f"## {job['title']}"
                    )

                    st.write(
                        f"🏢 Company: {job['company']}"
                    )

                    st.write(
                        f"📍 Location: {job['location']}"
                    )

                    st.write(
                        f"💰 Salary: {job['salary']}"
                    )

            else:
                st.warning("No jobs found")

        except Exception as e:

            st.error(f"Job API Error: {e}")

else:
    st.info("Please upload your resume to continue")