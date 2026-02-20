# Resume Screening System (Simple Level 4 ATS)

This project is a simple Applicant Tracking System (ATS) built using Python.

It scans resumes in PDF format, checks must-have skills, estimates experience, scores candidates, and ranks them to support recruiter shortlisting.

## Features
- PDF resume parsing
- Must-have vs nice-to-have skill matching
- Simple experience estimation
- Candidate classification:
  - ELIGIBLE
  - REVIEW
  - REJECT
- Ranking of resumes based on final score

## Tech Stack
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" / <img src="https://img.shields.io/badge/PyPDF2-FF6F00?style=for-the-badge&logo=python&logoColor=white" />

## Folder Structure
resume-screening-level4/
├── simple_ats_level4.py
├── requirements.txt
├── README.md
└── resumes/ (Make sure you create a resumes folder and import resumes which you have in that(resumes) folder)

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Add resumes
Create a folder named `resumes` and add PDF resumes.

3. Run the script
python simple_ats_level4.py OR
python -m streamlit run resume_screening_level4.py

## Sample Output
Rank #1  
Resume: Resume 7.pdf  
Decision: REVIEW  
Final Score: 73.75  
Experience (approx): 4 years  
Found Skills: ['python', 'sql', 'machine learning']  
Missing MUST-HAVE: ['excel']

## Why This Project
Recruiters receive many resumes for a single job opening.  
This system helps automate resume screening and candidate ranking using simple rule-based logic.

## Future Improvements
- Export results to Excel
- Web UI using Streamlit
- Job description based skill input

## Author

Venkat Mandarapu







