import os
import streamlit as st
import plotly.graph_objects as go
from dotenv import load_dotenv
import sample_data
from utils import (
    extract_text_from_pdf,
    analyze_resume_general,
    analyze_resume_match,
    generate_html_report
)

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="CareerBoost AI - SaaS Resume Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- SESSION STATE & INITIALIZATION -----------------
session_keys = {
    "last_analyzed_resume": None,
    "analysis_result": None,
    "analysis_results": None,
    "uploaded_file": None,
    "selected_resume": None,
    "job_matches": None,
    "skill_analysis": None,
    "match_results": None,
    "resume_text": "",
    "last_analyzed_jd": None,
    "use_mock": False
}

for key, default_val in session_keys.items():
    if key not in st.session_state:
        st.session_state[key] = default_val


# ----------------- SIDEBAR CONTROLS -----------------

st.sidebar.markdown("<h2 style='text-align: center; color: #6366f1; margin-bottom: 0px;'>🚀 CareerBoost AI</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>Enterprise Resume Suite</p>", unsafe_allow_html=True)
st.sidebar.write("---")

# API Key Configuration Check
api_key_configured = os.getenv("GEMINI_API_KEY") is not None
if not api_key_configured:
    st.sidebar.error("🚨 Admin Error: GEMINI_API_KEY is not set in `.env` file!")
    st.sidebar.info("💡 Please set GEMINI_API_KEY in your local environment `.env` to enable PDF processing.")

st.sidebar.write("---")

# Theme Switcher Control
st.sidebar.subheader("🎨 Visual Theme")
theme_choice = st.sidebar.selectbox(
    "Select App Theme",
    ["SaaS Dark Mode", "SaaS Light Mode", "Streamlit Adaptive"],
    help="Force a specific styling layout or adapt automatically to your browser theme."
)

st.sidebar.write("---")

# 10 Built-in Sample Resumes Loader
st.sidebar.subheader("📚 Built-in Demo Resumes")
selected_demo = st.sidebar.selectbox(
    "Choose a Demo Profile",
    ["None - Use Uploaded PDF"] + list(sample_data.DOMAINS.keys()),
    help="Select a preloaded profile to instantly test the system."
)

# PDF upload control (always visible)
st.sidebar.subheader("📄 Upload Resume")
uploaded_file = st.sidebar.file_uploader(
    "Choose a Resume (PDF Format)",
    type=["pdf"],
    help="Upload your resume in PDF format to start the analysis."
)

use_mock_data = (uploaded_file is None) and (selected_demo != "None - Use Uploaded PDF")

st.sidebar.write("---")

# Target Job Description
st.sidebar.subheader("🎯 Job Matcher (Optional)")
job_desc_input = st.sidebar.text_area(
    "Target Job Description",
    height=150,
    placeholder="Paste the job description you want to match your resume against here..."
)

# Analyze trigger button
st.sidebar.write("")
analyze_button = st.sidebar.button(
    "Analyze Resume",
    type="primary",
    width="stretch",
    disabled=not (uploaded_file or selected_demo != "None - Use Uploaded PDF")
)

# ----------------- LOGIC TRIGGERS -----------------

if analyze_button:
    if use_mock_data:
        # Load sample values
        demo_payload = sample_data.DOMAINS[selected_demo]
        st.session_state.use_mock = True
        
        # If API key is available, run live analysis for maximum AI authenticity
        if api_key_configured:
            try:
                with st.spinner(f"Running live AI audit on {selected_demo} profile..."):
                    st.session_state.resume_text = demo_payload["resume_text"]
                    st.session_state.analysis_results = analyze_resume_general(st.session_state.resume_text)
                    st.session_state.analysis_result = st.session_state.analysis_results
                    st.session_state.skill_analysis = st.session_state.analysis_results.get("missing_skills", [])
                    st.session_state.selected_resume = selected_demo
                    st.session_state.last_analyzed_resume = selected_demo
                    if job_desc_input.strip():
                        st.session_state.match_results = analyze_resume_match(st.session_state.resume_text, job_desc_input)
                        st.session_state.job_matches = st.session_state.match_results
                        st.session_state.last_analyzed_jd = job_desc_input
                    else:
                        st.session_state.match_results = None
                        st.session_state.job_matches = None
                        st.session_state.last_analyzed_jd = None
                st.success("Live AI analysis complete!")
            except Exception as e:
                st.warning(f"Live API call failed: {str(e)}. Loading cached pre-computed report instead.")
                st.session_state.resume_text = demo_payload["resume_text"]
                st.session_state.analysis_results = demo_payload["analysis"]
                st.session_state.analysis_result = demo_payload["analysis"]
                st.session_state.skill_analysis = demo_payload["analysis"].get("missing_skills", [])
                st.session_state.selected_resume = selected_demo
                st.session_state.last_analyzed_resume = selected_demo
                st.session_state.match_results = demo_payload["match"] if job_desc_input.strip() else None
                st.session_state.job_matches = demo_payload["match"] if job_desc_input.strip() else None
                st.session_state.last_analyzed_jd = job_desc_input if job_desc_input.strip() else None
        else:
            # Offline mock data load
            st.session_state.resume_text = demo_payload["resume_text"]
            st.session_state.analysis_results = demo_payload["analysis"]
            st.session_state.analysis_result = demo_payload["analysis"]
            st.session_state.skill_analysis = demo_payload["analysis"].get("missing_skills", [])
            st.session_state.selected_resume = selected_demo
            st.session_state.last_analyzed_resume = selected_demo
            st.session_state.match_results = demo_payload["match"] if job_desc_input.strip() else None
            st.session_state.job_matches = demo_payload["match"] if job_desc_input.strip() else None
            st.session_state.last_analyzed_jd = job_desc_input if job_desc_input.strip() else None
            st.success(f"Successfully loaded pre-computed {selected_demo} report!")
    else:
        # Real PDF audit
        st.session_state.use_mock = False
        try:
            with st.spinner("Extracting text from PDF resume..."):
                st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
                st.session_state.last_analyzed_resume = uploaded_file.name
                st.session_state.uploaded_file = uploaded_file.name
            
            # Perform general analysis
            with st.spinner("Analyzing resume..."):
                st.session_state.analysis_results = analyze_resume_general(
                    st.session_state.resume_text
                )
                st.session_state.analysis_result = st.session_state.analysis_results
                st.session_state.skill_analysis = st.session_state.analysis_results.get("missing_skills", [])
            
            # Perform JD match if present
            if job_desc_input.strip():
                with st.spinner("Calculating matching alignment with job description..."):
                    st.session_state.match_results = analyze_resume_match(
                        st.session_state.resume_text,
                        job_desc_input
                    )
                    st.session_state.job_matches = st.session_state.match_results
                    st.session_state.last_analyzed_jd = job_desc_input
            else:
                st.session_state.match_results = None
                st.session_state.job_matches = None
                st.session_state.last_analyzed_jd = None
                
            if not api_key_configured:
                st.info("💡 Analysis complete via Local Heuristic Mode (Gemini key not set).")
            else:
                st.success("AI analysis complete!")
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")

# Determine active file label
source_label = selected_demo if use_mock_data else (st.session_state.last_analyzed_resume or "No File Loaded")

# ----------------- EXPORT REPORT SIDEBAR LINK -----------------
if st.session_state.analysis_results:
    st.sidebar.write("---")
    st.sidebar.subheader("📥 Export Audit Report")
    
    # Generate HTML report structure
    report_html = generate_html_report(
        st.session_state.analysis_results,
        st.session_state.match_results
    )
    
    st.sidebar.download_button(
        label="📥 Download HTML Report",
        data=report_html,
        file_name=f"careerboost_ai_audit_{source_label.replace(' ', '_').lower()}.html",
        mime="text/html",
        use_container_width=True
    )

# ----------------- THEME INJECTOR -----------------
if theme_choice == "SaaS Dark Mode":
    theme_css = """
    <style>
        .stApp { background-color: #0b0f19; color: #f1f5f9; }
        .header-container { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-color: #1e293b; }
        .header-title { color: #ffffff; }
        .header-subtitle { color: #94a3b8; }
        .saas-kpi-card { background-color: #111827; border-color: #1f2937; }
        .saas-kpi-value { color: #f3f4f6; }
        .saas-kpi-title { color: #9ca3af; }
        .saas-panel { background-color: #111827; border-color: #1f2937; }
        .saas-panel-title { color: #f3f4f6; border-bottom-color: #1f2937; }
        .roadmap-item { background-color: #111827; border-color: #1f2937; }
        .roadmap-area { color: #f9fafb; }
        .roadmap-desc { color: #d1d5db; }
        .custom-alert { background-color: rgba(30, 41, 59, 0.3); border-color: #334155; color: #94a3b8; }
        .badge-tech { background-color: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
        .badge-soft { background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
        .badge-missing { background-color: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
        .badge-role { background-color: rgba(139, 92, 246, 0.15); color: #c084fc; border: 1px solid rgba(139, 92, 246, 0.3); }
    </style>
    """
elif theme_choice == "SaaS Light Mode":
    theme_css = """
    <style>
        .stApp { background-color: #f8fafc; color: #0f172a; }
        .header-container { background: linear-gradient(135deg, #e2e8f0 0%, #dbeafe 100%); border-color: #cbd5e1; }
        .header-title { color: #1e3a8a; }
        .header-subtitle { color: #475569; }
        .saas-kpi-card { background-color: #ffffff; border-color: #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
        .saas-kpi-value { color: #0f172a; }
        .saas-kpi-title { color: #64748b; }
        .saas-panel { background-color: #ffffff; border-color: #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
        .saas-panel-title { color: #1e3a8a; border-bottom-color: #e2e8f0; }
        .roadmap-item { background-color: #ffffff; border-color: #e2e8f0; }
        .roadmap-area { color: #1e293b; }
        .roadmap-desc { color: #4b5563; }
        .custom-alert { background-color: rgba(219, 234, 254, 0.5); border-color: #bfdbfe; color: #1e40af; }
        .badge-tech { background-color: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
        .badge-soft { background-color: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }
        .badge-missing { background-color: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
        .badge-role { background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; }
    </style>
    """
else:
    theme_css = """
    <style>
        /* Streamlit Adaptive Mode */
        .saas-kpi-card {
            background-color: var(--secondary-background-color);
            border: 1px solid var(--border-color);
        }
        .saas-panel {
            background-color: var(--secondary-background-color);
            border: 1px solid var(--border-color);
        }
        .roadmap-item {
            background-color: var(--secondary-background-color);
            border: 1px solid var(--border-color);
        }
        .custom-alert {
            background-color: var(--secondary-background-color);
            border: 1px dashed var(--border-color);
        }
        .badge-tech { background-color: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
        .badge-soft { background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
        .badge-missing { background-color: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
        .badge-role { background-color: rgba(139, 92, 246, 0.15); color: #c084fc; border: 1px solid rgba(139, 92, 246, 0.3); }
    </style>
    """

# Custom Premium CSS Layout Core
st.markdown(theme_css, unsafe_allow_html=True)
st.markdown("""
<style>
    /* SaaS KPI Card core dimensions */
    .saas-kpi-card {
        border-radius: 10px;
        padding: 1.25rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }
    .saas-kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
    }
    .saas-kpi-title {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    .saas-kpi-value {
        font-size: 2.25rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1;
    }
    .saas-kpi-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    /* SaaS Card Panel core */
    .saas-panel {
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .saas-panel-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom-style: solid;
        border-bottom-width: 1px;
    }
    
    /* Roadmaps Suggestion Row core */
    .roadmap-item {
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 0.75rem;
        border-left: 5px solid #4f46e5;
    }
    .roadmap-item-high { border-left-color: #ef4444; }
    .roadmap-item-medium { border-left-color: #f59e0b; }
    .roadmap-item-low { border-left-color: #3b82f6; }
    
    .roadmap-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .roadmap-area {
        font-weight: 700;
        font-size: 1.05rem;
    }
    .roadmap-desc {
        font-size: 0.925rem;
        line-height: 1.5;
    }
    
    /* Skill Badges & Tags */
    .skill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.35rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
        line-height: 1.25rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- MAIN UI RENDER -----------------

st.markdown("""
<div class="header-container">
    <div class="header-title">CareerBoost AI Resume Suite</div>
    <div class="header-subtitle">Enterprise continuous resume health audits, skill gap alignments, and interactive interview readiness dashboards</div>
</div>
""", unsafe_allow_html=True)

# Check state
if not st.session_state.analysis_results:
    st.info("👋 Welcome to CareerBoost AI! Select a built-in demo profile in the sidebar or upload your own resume PDF, then click 'Analyze Resume' to generate your SaaS evaluation dashboard.")
    
    # Feature Showcase Grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="saas-kpi-card" style="border-top: 4px solid #6366f1;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
            <h4 style="margin-top: 0px; margin-bottom: 5px;">Continuous Audits</h4>
            <p style="font-size: 0.9rem; margin-bottom: 0px;">Full-spectrum ATS scans matching profile completeness, keywords index, and structuring criteria.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="saas-kpi-card" style="border-top: 4px solid #10b981;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
            <h4 style="margin-top: 0px; margin-bottom: 5px;">Skill Alignments</h4>
            <p style="font-size: 0.9rem; margin-bottom: 0px;">Pinpoint and compare technical/soft alignments, highlighting critical missing requirements.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="saas-kpi-card" style="border-top: 4px solid #f43f5e;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💬</div>
            <h4 style="margin-top: 0px; margin-bottom: 5px;">Interview Readiness</h4>
            <p style="font-size: 0.9rem; margin-bottom: 0px;">Generate custom mock interview queries tailored specifically to your experiences and matches.</p>
        </div>
        """, unsafe_allow_html=True)
else:
    # Results dashboard variables
    res = st.session_state.analysis_results
    match_res = st.session_state.match_results
    
    # ----------------- SAAS KPI METRIC CARDS ROW -----------------
    ats_score = res.get("ats_score", 0)
    resume_strength = res.get("resume_strength", 0)
    missing_skills_count = len(res.get("missing_skills", []))

    # Job match percentage
    if match_res:
        match_percentage = match_res.get("match_score", 0)
        match_label = f"{match_percentage}%"
        match_badge_class = "saas-badge-green" if match_percentage >= 75 else "saas-badge-orange" if match_percentage >= 50 else "saas-badge-red"
        match_status = "High Match" if match_percentage >= 75 else "Medium Match" if match_percentage >= 50 else "Weak Match"
        
        # Override missing skills count with target job missing skills if match mode is active
        missing_skills_count = len(match_res.get("missing_skills", []))
    else:
        match_label = "N/A"
        match_badge_class = "saas-badge-gray"
        match_status = "JD Not Provided"

    # ATS Status
    ats_status = "Outstanding" if ats_score >= 80 else "Acceptable" if ats_score >= 60 else "Needs Optimization"
    ats_badge_class = "saas-badge-green" if ats_score >= 80 else "saas-badge-orange" if ats_score >= 60 else "saas-badge-red"

    # Strength status
    strength_status = "Highly Competitive" if resume_strength >= 85 else "Strong Profile" if resume_strength >= 70 else "Basic Profile"
    strength_badge_class = "saas-badge-green" if resume_strength >= 85 else "saas-badge-blue" if resume_strength >= 70 else "saas-badge-orange"

    # Gaps status
    gaps_badge_class = "saas-badge-red" if missing_skills_count > 3 else "saas-badge-orange" if missing_skills_count > 0 else "saas-badge-green"
    gaps_status = f"{missing_skills_count} Gaps Found" if missing_skills_count > 0 else "No Gaps Found"

    # Render KPI Cards in a row (4 columns)
    kpi_cols = st.columns(4)

    with kpi_cols[0]:
        st.markdown(f"""
        <div class="saas-kpi-card" style="border-top: 4px solid #3b82f6;">
            <div class="saas-kpi-title">ATS Score</div>
            <div class="saas-kpi-value" style="color: #3b82f6;">{ats_score}%</div>
            <span class="saas-kpi-badge {ats_badge_class}">{ats_status}</span>
        </div>
        """, unsafe_allow_html=True)

    with kpi_cols[1]:
        st.markdown(f"""
        <div class="saas-kpi-card" style="border-top: 4px solid #10b981;">
            <div class="saas-kpi-title">Job Match</div>
            <div class="saas-kpi-value" style="color: #10b981;">{match_label}</div>
            <span class="saas-kpi-badge {match_badge_class}">{match_status}</span>
        </div>
        """, unsafe_allow_html=True)

    with kpi_cols[2]:
        st.markdown(f"""
        <div class="saas-kpi-card" style="border-top: 4px solid #8b5cf6;">
            <div class="saas-kpi-title">Resume Strength</div>
            <div class="saas-kpi-value" style="color: #8b5cf6;">{resume_strength}%</div>
            <span class="saas-kpi-badge {strength_badge_class}">{strength_status}</span>
        </div>
        """, unsafe_allow_html=True)

    with kpi_cols[3]:
        st.markdown(f"""
        <div class="saas-kpi-card" style="border-top: 4px solid #f43f5e;">
            <div class="saas-kpi-title">Missing Skills</div>
            <div class="saas-kpi-value" style="color: #f43f5e;">{missing_skills_count}</div>
            <span class="saas-kpi-badge {gaps_badge_class}">{gaps_status}</span>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    
    # Active file info banner
    st.markdown(f"""
    <div class="custom-alert">
        <strong>Active Workspace File:</strong> {source_label} &nbsp;&nbsp;|&nbsp;&nbsp; 
        <strong>Analysis Mode:</strong> {"Job Alignment Matcher Activated" if match_res else "Standard Profile Audit"}
    </div>
    """, unsafe_allow_html=True)

    # ----------------- TABS SETUP -----------------
    tab_labels = ["📊 Overview Dashboard", "💡 Optimization Roadmap", "💬 Interview Prep", "📄 Parsed Text"]
    if match_res:
        tab_labels.insert(1, "🎯 Job Alignment")
        
    tabs = st.tabs(tab_labels)
    tab_index = 0
    
    # TABS: 1. Overview Dashboard
    with tabs[tab_index]:
        col_left, col_right = st.columns([3, 2])
        
        with col_left:
            # Executive Summary card
            st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
            st.markdown('<div class="saas-panel-title">📋 Professional Summary</div>', unsafe_allow_html=True)
            st.write(res.get("profile_summary", ""))
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Recommended roles
            st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
            st.markdown('<div class="saas-panel-title">💼 Recommended Job Roles</div>', unsafe_allow_html=True)
            recommended = res.get("recommended_roles", [])
            if recommended:
                badges_html = "".join([f'<span class="badge badge-role">{role}</span>' for role in recommended])
                st.markdown(f'<div class="skill-container">{badges_html}</div>', unsafe_allow_html=True)
            else:
                st.info("No job recommendations generated.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_right:
            # Technical skills
            st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
            st.markdown('<div class="saas-panel-title">💻 Technical Skills Inventory</div>', unsafe_allow_html=True)
            tech_skills = res.get("technical_skills", [])
            if tech_skills:
                badges_html = "".join([f'<span class="badge badge-tech">{s}</span>' for s in tech_skills])
                st.markdown(f'<div class="skill-container">{badges_html}</div>', unsafe_allow_html=True)
            else:
                st.info("No technical skills detected.")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Soft skills
            st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
            st.markdown('<div class="saas-panel-title">🤝 Soft Skills & Attributes</div>', unsafe_allow_html=True)
            soft_skills = res.get("soft_skills", [])
            if soft_skills:
                badges_html = "".join([f'<span class="badge badge-soft">{s}</span>' for s in soft_skills])
                st.markdown(f'<div class="skill-container">{badges_html}</div>', unsafe_allow_html=True)
            else:
                st.info("No soft skills detected.")
            st.markdown('</div>', unsafe_allow_html=True)
            
    tab_index += 1
    
    # TABS: 2. Job Alignment (If JD provided)
    if match_res:
        with tabs[tab_index]:
            col_match_left, col_match_right = st.columns([3, 2])
            
            with col_match_left:
                st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
                st.markdown('<div class="saas-panel-title">🎯 Fitment Alignment Assessment</div>', unsafe_allow_html=True)
                st.write(match_res.get("job_description_alignment", ""))
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
                st.markdown('<div class="saas-panel-title">📋 Matching Profile Fit Overview</div>', unsafe_allow_html=True)
                st.write(match_res.get("profile_summary", ""))
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_match_right:
                st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
                st.markdown('<div class="saas-panel-title">✅ Matching Skills / Keywords</div>', unsafe_allow_html=True)
                matching = match_res.get("matching_skills", [])
                if matching:
                    badges_html = "".join([f'<span class="badge badge-soft">{s}</span>' for s in matching])
                    st.markdown(f'<div class="skill-container">{badges_html}</div>', unsafe_allow_html=True)
                else:
                    st.warning("No overlapping skills found.")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="saas-panel">', unsafe_allow_html=True)
                st.markdown('<div class="saas-panel-title">❌ Missing Skills / Keywords</div>', unsafe_allow_html=True)
                missing = match_res.get("missing_skills", [])
                if missing:
                    badges_html = "".join([f'<span class="badge badge-missing">{s}</span>' for s in missing])
                    st.markdown(f'<div class="skill-container">{badges_html}</div>', unsafe_allow_html=True)
                else:
                    st.success("No missing skills found!")
                st.markdown('</div>', unsafe_allow_html=True)
                
        tab_index += 1
        
    # TABS: 3. Optimization Roadmap
    with tabs[tab_index]:
        st.markdown("### 💡 Resume Optimization Roadmap")
        
        suggestions = []
        if match_res and match_res.get("improvement_suggestions"):
            st.info("🎯 The tasks below are prioritized specifically to match your target Job Description.")
            suggestions = match_res.get("improvement_suggestions", [])
        else:
            st.info("📋 The tasks below are general improvements recommended for your career profile.")
            suggestions = res.get("improvement_suggestions", [])
            
        if suggestions:
            # Sort suggestions by priority: High, Medium, Low
            high_items = [s for s in suggestions if s.get("priority", "").lower() == "high"]
            med_items = [s for s in suggestions if s.get("priority", "").lower() == "medium"]
            low_items = [s for s in suggestions if s.get("priority", "").lower() == "low" or not s.get("priority")]
            
            sorted_suggestions = high_items + med_items + low_items
            
            for item in sorted_suggestions:
                prio = item.get("priority", "Low")
                prio_lower = prio.lower()
                prio_badge_class = "saas-badge-red" if prio_lower == "high" else "saas-badge-orange" if prio_lower == "medium" else "saas-badge-blue"
                border_class = f"roadmap-item-{prio_lower}" if prio_lower in ["high", "medium", "low"] else "roadmap-item-low"
                
                st.markdown(f"""
                <div class="roadmap-item {border_class}">
                    <div class="roadmap-header">
                        <div class="roadmap-area">🛠️ {item.get('area', 'General')}</div>
                        <span class="saas-kpi-badge {prio_badge_class}">{prio} Priority</span>
                    </div>
                    <div class="roadmap-desc">{item.get('suggestion', '')}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("No improvement suggestions provided. Your resume is in excellent shape!")
            
    tab_index += 1
    
    # TABS: 4. Interview Prep
    with tabs[tab_index]:
        st.markdown("### 💬 Tailored Interview Preparation")
        st.info("💡 The following mock interview questions are tailored specifically to your resume accomplishments to prepare you for recruiter reviews.")
        
        questions = []
        if match_res and match_res.get("interview_questions"):
            st.markdown("#### 🎯 Target Job Matching Questions")
            questions = match_res.get("interview_questions", [])
        else:
            st.markdown("#### 📋 Profile Audited General Questions")
            questions = res.get("interview_questions", [])
            
        if questions:
            for idx, q in enumerate(questions):
                st.markdown(f"""
                <div class="saas-panel">
                    <div style="font-weight:800; color:#6366f1; font-size:1.1rem; margin-bottom:0.5rem;">Q{idx+1}: {q.get('question', '')}</div>
                    <div style="font-size:0.85rem; color:#6b7280; font-style:italic; margin-bottom:0.75rem;">Recruiter Intent: {q.get('intent', '')}</div>
                    <div style="font-size:0.95rem; background-color:rgba(99, 102, 241, 0.05); padding:1rem; border-radius:6px; border-left:3px solid #6366f1;">
                        <strong>Suggested Strategy:</strong><br>{q.get('suggested_answer', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No interview preparation questions generated.")
            
    tab_index += 1
    
    # TABS: 5. Parsed Text
    with tabs[tab_index]:
        st.markdown("### 📄 Parsed Resume Text")
        st.write("This is the exact plain text extracted from your PDF and analyzed by Google Gemini AI:")
        st.text_area("Extracted Resume Text", value=st.session_state.resume_text, height=450, disabled=True)
