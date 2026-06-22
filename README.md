# 🚀 CareerBoost AI - Resume Analyzer & Job Matcher

CareerBoost AI is a modern, AI-powered Streamlit web application that analyzes resumes in PDF format using the **Google Gemini API** (`gemini-2.5-flash`). It computes an Applicant Tracking System (ATS) matching score, extracts technical and soft skills, uncovers critical skill gaps, identifies suitable job roles, and provides highly specific recommendations to tailor your resume for a job description.
APP LINK : https://careerboost-ai-resume-analyzer-yvvikannwf3emtebzaavzo.streamlit.app/

---

## ✨ Features

1. **ATS Score Calculator**: Provides a score out of 100 representing resume layout quality, structure, and keyword relevance.
2. **Text Extraction**: Uses `PyPDF2` to read uploaded PDF resume texts instantly.
3. **Gemini AI Integration**: Connects with Google Gemini API to analyze the resume layout and content.
4. **Skill Extractor**: Identifies technical/hard skills and soft/interpersonal skills separately.
5. **Skill Gap Analysis**: Compares the candidate's skills against industry demands and flags missing skills to focus on.
6. **Career Recommendations**: Recommends 3–5 job roles matching the candidate's career level and skills.
7. **Job Matching**: Paste a target Job Description (JD) to compute a dedicated Match Score, matching keywords, missing skills, and target alignment feedback.
8. **Actionable Suggestions**: Specific suggestions categorized by area (e.g., formatting, metrics, keywords) to help candidate's resume stand out.
9. **Interactive Dashboard**: Modern dark-themed dashboard using Plotly indicators and HTML badge elements.
10. **Sample Preview Mode**: Test all dashboard functionalities instantly with a single click using pre-loaded mock data (no API key or PDF required).

---

## 📂 Project Structure

```text
careerboost_ai/
│
├── .env.template          # Template for environment variables
├── app.py                 # Streamlit frontend, layouts, styles, and state logic
├── utils.py               # Core backend: PDF parsing and Gemini API interactions
├── requirements.txt       # Project python dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Installation & Setup

Follow these steps to set up and run CareerBoost AI locally:

### 1. Prerequisites
Make sure you have **Python 3.9+** installed on your system.

### 2. Clone/Copy Code
Ensure all files are placed in a single directory: `C:/Users/sri venkata praveen/.gemini/antigravity/scratch/careerboost_ai`.

### 3. Install Dependencies
Open your terminal in the directory and run:
```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables
1. Copy the `.env.template` file and rename it to `.env`:
   ```powershell
   copy .env.template .env
   ```
2. Open `.env` and fill in your Google Gemini API Key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```
   > 💡 **No API key?** You can get a free API Key from [Google AI Studio](https://aistudio.google.com/).
   > Alternatively, you can directly paste your API Key in the application's sidebar while running the app.

---

## 🚀 Running the Application

Launch the Streamlit server from your terminal:
```powershell
streamlit run app.py
```

The application will open automatically in your browser (usually at `http://localhost:8501`).

---

## 📖 Usage Guide

1. **Try Sample Data first**: If you want to check out the dashboard design immediately, check the **"Use Sample Resume Data"** checkbox in the sidebar and click **Analyze Resume**.
2. **Upload Your Resume**: Upload your own resume in PDF format.
3. **Optional Job Description**: Paste a target job description to match against it.
4. **Click Analyze**: Wait for Gemini AI to complete the evaluation.
5. **Analyze Tabs**:
   - Check **Dashboard** for overall ATS scores and skill badges.
   - Check **Job Matcher** (if JD is pasted) to see custom matching scores and alignments.
   - Check **Skill Analysis** to discover gaps.
   - Check **Improvement Tips** for specific action items.
