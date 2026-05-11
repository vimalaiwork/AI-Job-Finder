# AI Job Finder & Company Recommender

## Overview

AI Job Finder & Company Recommender is an AI-powered web application that helps job seekers discover suitable companies and live job openings based on their resume, skills, and preferences.

The system extracts skills from uploaded resumes, stores user preferences, and fetches real-time companies and job opportunities using APIs.

---

## Features

* Resume Upload & Parsing
* Skill Extraction
* User Preference Collection
* Live Company Search
* Live Job Search
* SQLite Database Integration
* Streamlit Web Interface
* Real API Integration using Apify

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* PDFPlumber
* Apify API

---

## Project Workflow

1. User uploads resume PDF
2. Resume text is extracted
3. Skills are identified from resume
4. User enters preferences:

   * Preferred role
   * Location
   * Salary range
   * Experience level
   * Domain
5. System searches live companies
6. System fetches real-time job openings
7. Results displayed in web application

---

## Installation

Clone repository:

```bash
git clone https://github.com/vimalaiwork/AI-Job-Finder.git
```

Open project folder:

```bash
cd AI-Job-Finder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
streamlit run app.py
```

---

## Project Structure

```text
AI-Job-Finder/
│
├── app.py
├── company_finder.py
├── job_fetcher.py
├── resume_parser.py
├── skill_extractor.py
├── database.py
├── requirements.txt
├── .gitignore
```

---

## Future Improvements

* AI-based job ranking
* Resume ATS score analysis
* Skill gap recommendations
* LinkedIn integration
* Email notifications
* Authentication system

---

## Author

Vimal Raj

---
