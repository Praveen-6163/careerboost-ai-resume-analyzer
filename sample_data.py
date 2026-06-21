# sample_data.py
# Preloaded sample resume data for 10 different professional domains.
# Used for instant preview / demo mode in CareerBoost AI.

DOMAINS = {
    "Software Engineer": {
        "resume_text": """
John Doe - Senior Software Engineer
Summary:
Highly skilled Senior Software Engineer with over 6 years of experience designing and deploying scalable web applications. Expert in Python backend development, PostgreSQL, and Streamlit-based tools. Led agile sprint teams and mentored junior engineers.

Skills: Python, Java, FastAPI, Django, PostgreSQL, Git, AWS, CI/CD, Streamlit
""",
        "job_desc": """
Senior Python Backend Developer
Looking for a Senior Python Developer with strong backend skills in FastAPI/Django, SQL database design, and AWS cloud hosting. Strong communication skills are a must.
""",
        "analysis": {
            "ats_score": 85,
            "resume_strength": 90,
            "profile_summary": "Strong Software Engineer with extensive experience in Python backends, database design, and web dashboards. Good team leadership skills.",
            "technical_skills": ["Python", "Java", "FastAPI", "Django", "PostgreSQL", "Git", "AWS", "CI/CD", "Streamlit"],
            "soft_skills": ["Leadership", "Mentoring", "Agile Leadership", "Communication"],
            "missing_skills": ["Docker", "Kubernetes", "Redis", "NoSQL"],
            "recommended_roles": ["Senior Python Developer", "Backend Engineer", "Software Architect"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Containerization", "suggestion": "Add containerization tools (Docker/Kubernetes) as they are core requirements for modern backend roles."},
                {"priority": "Medium", "area": "Metrics", "suggestion": "Quantify your achievements. Mention the scale of the databases or the percentage reduction in API latency."}
            ],
            "interview_questions": [
                {"question": "How do you optimize slow queries in PostgreSQL?", "intent": "Assess database optimization expertise.", "suggested_answer": "Discuss indexing strategy, using EXPLAIN ANALYZE, vacuuming, and caching query results."},
                {"question": "Explain a scenario where you migrated a service to FastAPI.", "intent": "Assess experience with FastAPI migration.", "suggested_answer": "Focus on the performance gains, async capabilities, and clean documentation benefits."}
            ]
        },
        "match": {
            "match_score": 88,
            "resume_strength": 90,
            "profile_summary": "Highly aligned for the Senior Python Backend Developer position, matching backend languages, frameworks, and cloud capabilities.",
            "matching_skills": ["Python", "FastAPI", "Django", "SQL", "AWS", "Communication"],
            "missing_skills": ["Docker", "Redis"],
            "job_description_alignment": "Candidate fits backend requirements perfectly but lacks caching and orchestration layers.",
            "improvement_suggestions": [
                {"priority": "High", "area": "DevOps", "suggestion": "Highlight any Docker knowledge explicitly to align with modern microservices setups."}
            ],
            "interview_questions": [
                {"question": "How do you secure endpoints in FastAPI?", "intent": "Security best practices.", "suggested_answer": "Detail JWT tokens, OAuth2 scopes, SSL enforcement, and rate-limiting middleware."}
            ]
        }
    },
    "DevOps Engineer": {
        "resume_text": """
Sarah Smith - DevOps Engineer
Summary:
DevOps Engineer with 4 years of experience focusing on infrastructure automation, Kubernetes orchestration, and cloud architecture on Azure.
Skills: Kubernetes, Docker, Terraform, Azure, Linux, Python, Jenkins, GitHub Actions
""",
        "job_desc": """
Cloud DevOps & Site Reliability Engineer
Requirements:
- Hands-on Terraform infrastructure-as-code scripting.
- Advanced container scheduling using Kubernetes.
- Multi-cloud hosting (Azure/AWS) and automated CI/CD configurations.
""",
        "analysis": {
            "ats_score": 82,
            "resume_strength": 84,
            "profile_summary": "Qualified DevOps Engineer with solid skills in cloud orchestration, automated CI/CD build scripts, and infra coding.",
            "technical_skills": ["Kubernetes", "Docker", "Terraform", "Azure", "Linux", "Python", "Jenkins", "GitHub Actions"],
            "soft_skills": ["Collaboration", "Automation Focus", "Problem Solving"],
            "missing_skills": ["AWS", "Helm", "Prometheus", "Grafana"],
            "recommended_roles": ["DevOps Engineer", "Cloud Infrastructure Architect", "Site Reliability Engineer"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Monitoring", "suggestion": "Add Prometheus/Grafana or other observability frameworks to demonstrate system health tracing."},
                {"priority": "Medium", "area": "Multi-cloud", "suggestion": "Try to build exposure in AWS to complement your existing Azure expertise."}
            ],
            "interview_questions": [
                {"question": "Explain state management in Terraform.", "intent": "Assess understanding of IaC integrity.", "suggested_answer": "Discuss terraform.tfstate, remote backends, state locking (e.g. via DynamoDB/Blob lock), and import commands."}
            ]
        },
        "match": {
            "match_score": 80,
            "resume_strength": 84,
            "profile_summary": "Strong alignment with azure infra coding. Cloud DevOps needs slightly more multi-cloud exposure.",
            "matching_skills": ["Kubernetes", "Docker", "Terraform", "Azure", "GitHub Actions"],
            "missing_skills": ["AWS"],
            "job_description_alignment": "Well-suited for containerization and scripting. Lacks AWS-specific cloud infrastructure elements.",
            "improvement_suggestions": [
                {"priority": "High", "area": "Multi-cloud", "suggestion": "Explicitly state any secondary AWS training or certifications to prove multi-cloud adaptability."}
            ],
            "interview_questions": [
                {"question": "How do you manage secrets in Kubernetes?", "intent": "Verify secure configuration practices.", "suggested_answer": "Explain K8s Secrets, encryption at rest, integration with Azure Key Vault, or HashiCorp Vault integrations."}
            ]
        }
    },
    "Data Scientist": {
        "resume_text": """
Alex Johnson - Data Scientist
Summary:
Data Scientist with 5 years of experience deploying machine learning algorithms, deep learning models, and processing big data.
Skills: Python, R, TensorFlow, PyTorch, SQL, Pandas, Tableau, Machine Learning, NLP
""",
        "job_desc": """
Lead AI & Machine Learning Scientist
Looking for an experienced ML Scientist to design generative AI solutions, deep learning models, and establish high-throughput feature stores.
""",
        "analysis": {
            "ats_score": 79,
            "resume_strength": 82,
            "profile_summary": "Experienced Data Scientist with classic ML, NLP, and Deep Learning training. Ready for senior statistical analysis roles.",
            "technical_skills": ["Python", "TensorFlow", "PyTorch", "SQL", "Pandas", "Tableau", "Machine Learning", "NLP"],
            "soft_skills": ["Data Storytelling", "Scientific Thinking", "Curiosity"],
            "missing_skills": ["MLOps", "Generative AI", "Docker", "Spark"],
            "recommended_roles": ["Machine Learning Engineer", "Data Scientist", "AI Engineer"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Modern AI Keywords", "suggestion": "Add mentions of LLMs, Prompt Engineering, or Vector Databases (e.g., Pinecone/Milvus) to match the generative AI trends."}
            ],
            "interview_questions": [
                {"question": "Explain the vanishing gradient problem in Deep Learning.", "intent": "Core neural network comprehension.", "suggested_answer": "Describe how gradients shrink exponentially during backpropagation. Solutions: ReLU activation, Batch Norm, ResNet skip connections."}
            ]
        },
        "match": {
            "match_score": 72,
            "resume_strength": 82,
            "profile_summary": "Good baseline ML modeling expertise. Gap in Generative AI tech stack (LLMs, LangChain) relative to job description.",
            "matching_skills": ["Python", "TensorFlow", "PyTorch", "SQL", "Machine Learning"],
            "missing_skills": ["Generative AI", "MLOps"],
            "job_description_alignment": "Meets quantitative deep learning needs, but does not cover the modern GenAI stack requested.",
            "improvement_suggestions": [
                {"priority": "High", "area": "Generative AI Stack", "suggestion": "Update projects to highlight any prompt customization or chatbot implementations using OpenAI/Gemini endpoints."}
            ],
            "interview_questions": [
                {"question": "What is the difference between Fine-tuning and RAG?", "intent": "Generative AI systems understanding.", "suggested_answer": "Fine-tuning updates model weights. RAG injects dynamic document contexts in prompt payloads without changing weights."}
            ]
        }
    },
    "Product Manager": {
        "resume_text": """
Emily Chen - Product Manager
Summary:
Product Manager with 5 years of experience owning roadmap prioritization, writing PRDs, and launching consumer SaaS features.
Skills: Agile, Scrum, Jira, Product Strategy, SQL, User Research, Wireframing, AB Testing
""",
        "job_desc": """
Senior Product Manager - Cloud SaaS
Requirements:
- Strong roadmap design and backlog ownership.
- Experience managing SaaS product lifecycle metrics (LTV, Churn, CAC).
- Analytical data mindset using SQL and BI visualization tools.
""",
        "analysis": {
            "ats_score": 84,
            "resume_strength": 86,
            "profile_summary": "SaaS Product Manager with experience launching consumer features. Highly organized roadmap owner.",
            "technical_skills": ["Agile", "Scrum", "Jira", "SQL", "AB Testing", "Wireframing"],
            "soft_skills": ["Product Strategy", "User Research", "Stakeholder Management", "Cross-functional Collaboration"],
            "missing_skills": ["SaaS Metrics (LTV/CAC)", "Growth Hacking", "Product Analytics (Amplitude/Mixpanel)"],
            "recommended_roles": ["Product Manager", "SaaS Product Manager", "Technical Product Manager"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Metrics Definition", "suggestion": "Explicitly highlight SaaS business metrics (e.g., churn rate reduction, active user growth) in your project bullet points."}
            ],
            "interview_questions": [
                {"question": "How do you decide what features to build next?", "intent": "Verify prioritization methodology.", "suggested_answer": "Discuss frameworks like RICE (Reach, Impact, Confidence, Effort), customer interviews, and business strategy goals."}
            ]
        },
        "match": {
            "match_score": 83,
            "resume_strength": 86,
            "profile_summary": "Strong fit for SaaS product roles. Needs slightly more emphasis on business metrics.",
            "matching_skills": ["Agile", "Roadmap backlog", "SQL", "User Research", "Scrum"],
            "missing_skills": ["SaaS lifecycle metrics (LTV/CAC)"],
            "job_description_alignment": "Highly aligned in product management practices, but missing growth/financial metrics alignment.",
            "improvement_suggestions": [
                {"priority": "Medium", "area": "Business Impact", "suggestion": "Show how your product launches improved active usage, retention, or subscriber counts."}
            ],
            "interview_questions": [
                {"question": "Describe a failed product feature and your learnings.", "intent": "Self-awareness and metric tracking.", "suggested_answer": "Give a specific instance where user response wasn't as expected, how data pointed out the issue, and how you iterated."}
            ]
        }
    },
    "UX Designer": {
        "resume_text": """
Markus Vance - UX/UI Designer
Summary:
UX/UI Designer with 5 years of experience creating responsive mobile apps and interactive design systems.
Skills: Figma, Adobe XD, User Flow, Prototyping, Wireframing, HTML, CSS, User Journeys
""",
        "job_desc": """
Lead UX & Interaction Designer
Seeking a UX leader to establish Figma Design Systems, perform usability tests, and translate complex enterprise dashboards into clean interfaces.
""",
        "analysis": {
            "ats_score": 80,
            "resume_strength": 82,
            "profile_summary": "Qualified designer with extensive wireframing, prototype creation, and standard mockup experience using Figma.",
            "technical_skills": ["Figma", "Adobe XD", "User Flow", "Prototyping", "Wireframing", "HTML", "CSS"],
            "soft_skills": ["User Empathy", "Design Thinking", "Feedback Processing"],
            "missing_skills": ["Design Systems", "Usability Testing", "UX Research Methods"],
            "recommended_roles": ["UX Designer", "UI Designer", "Product Designer"],
            "improvement_suggestions": [
                {"priority": "High", "area": "UX Testing", "suggestion": "Mention usability testing methods (moderated, unmoderated) to prove validation of your design choices."}
            ],
            "interview_questions": [
                {"question": "Walk us through your design process.", "intent": "Check structure in design thinking.", "suggested_answer": "Discuss Empathize (research), Define (flows), Ideate (wireframes), Prototype, and Test (iterations)."}
            ]
        },
        "match": {
            "match_score": 78,
            "resume_strength": 82,
            "profile_summary": "Strong designer matches Figma tool usage. Lacks structural leadership in user validation techniques.",
            "matching_skills": ["Figma", "Prototyping", "Wireframing", "Dashboard interfaces"],
            "missing_skills": ["Usability Testing", "Design Systems"],
            "job_description_alignment": "Meets operational design design requirements, but lacks architectural system-level design practices.",
            "improvement_suggestions": [
                {"priority": "Medium", "area": "Design Systems", "suggestion": "Detail your experience creating component-driven Figma systems rather than just static screens."}
            ],
            "interview_questions": [
                {"question": "How do you handle developer feedback that a design is too hard to implement?", "intent": "Collaboration skills.", "suggested_answer": "Explain collaboration with engineering, assessing trade-offs, and scaling back elements without losing user value."}
            ]
        }
    },
    "Marketing Manager": {
        "resume_text": """
Sophia Ruiz - Digital Marketing Manager
Summary:
Marketing Manager with 6 years of experience driving user acquisition, content strategy, and running paid ad campaigns.
Skills: SEO, SEM, Google Analytics, Copywriting, Social Media Marketing, Email Marketing, Hubspot
""",
        "job_desc": """
Performance & Growth Marketing Director
Requirements:
- Data-driven performance marketing manager to lead multi-million dollar ad spends.
- Advanced customer acquisition analytics and attribution modeling.
- Direct management of CRM platforms and retargeting campaigns.
""",
        "analysis": {
            "ats_score": 81,
            "resume_strength": 84,
            "profile_summary": "Competent digital marketer with experience across writing, organic growth, and search engine optimization. Well-rounded branding history.",
            "technical_skills": ["SEO", "SEM", "Google Analytics", "Hubspot", "Email Marketing", "Social Media"],
            "soft_skills": ["Creative Phrasing", "Brand Advocacy", "Team Coordination"],
            "missing_skills": ["Performance Analytics (ROI/ROAS)", "Attribution Models", "Retargeting Ads (Meta/Google Adwords)"],
            "recommended_roles": ["Marketing Manager", "Growth Marketer", "SEO Specialist"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Performance Metrics", "suggestion": "Add explicit metrics showing your ad spend budget scales, cost per lead (CPL) reductions, or ROI/ROAS values."}
            ],
            "interview_questions": [
                {"question": "How do you audit an underperforming SEO page?", "intent": "Assess technical marketing ability.", "suggested_answer": "Analyze keywords indexing, page load speeds, search console impressions, backlink checks, and content freshness."}
            ]
        },
        "match": {
            "match_score": 74,
            "resume_strength": 84,
            "profile_summary": "Qualified for general branding and content marketing, but lacks analytical tracking metrics required for the director-level role.",
            "matching_skills": ["SEO", "SEM", "Google Analytics", "Hubspot"],
            "missing_skills": ["Attribution Modeling", "Performance Analytics (ROAS)"],
            "job_description_alignment": "Strong branding baseline, but misses the budget and ROI leadership metrics requested.",
            "improvement_suggestions": [
                {"priority": "High", "area": "ROAS Metrics", "suggestion": "State the size of the budgets you managed and what percentage increase in conversions was achieved."}
            ],
            "interview_questions": [
                {"question": "Explain how multi-touch attribution works.", "intent": "Attribution model familiarity.", "suggested_answer": "Detail how touchpoints (first-click, last-click, linear, W-shaped) distribute conversion credit across the customer journey."}
            ]
        }
    },
    "Financial Analyst": {
        "resume_text": """
Lucas Baker - Senior Financial Analyst
Summary:
Financial Analyst with 5 years of experience in budgeting, forecasting, cash flow modeling, and variance analysis.
Skills: Excel, VBA, Power BI, SQL, Financial Modeling, Reporting, Risk Assessment
""",
        "job_desc": """
Lead Finance & Corporate Strategy Partner
Requirements:
- Advanced financial statement analysis and cash flow forecasting.
- Strategic business variance modeling and corporate M&A evaluation.
- Enterprise ERP experience (SAP or Oracle Financials).
""",
        "analysis": {
            "ats_score": 83,
            "resume_strength": 85,
            "profile_summary": "Senior analyst with strong Excel and statistical business model capabilities. Solid history of reports production.",
            "technical_skills": ["Excel", "VBA", "Power BI", "SQL", "Financial Modeling", "Reporting"],
            "soft_skills": ["Attention to Detail", "Quantitative Reasoning", "Stakeholder Communication"],
            "missing_skills": ["SAP/Oracle ERP", "M&A Valuation", "Capital Budgeting"],
            "recommended_roles": ["Financial Analyst", "Finance Manager", "Corporate Strategy Consultant"],
            "improvement_suggestions": [
                {"priority": "Medium", "area": "ERP tools", "suggestion": "Mention any enterprise accounting tools (Oracle/SAP) that you have worked with during financial consolidation audits."}
            ],
            "interview_questions": [
                {"question": "How do you build a 3-statement financial model?", "intent": "Check core modeling expertise.", "suggested_answer": "Explain linking the Income Statement, Balance Sheet, and Cash Flow Statement via net income, working capital, and cash balances."}
            ]
        },
        "match": {
            "match_score": 78,
            "resume_strength": 85,
            "profile_summary": "Highly compatible for forecasting and spreadsheet modeling. Lacks corporate ERP systems qualifications.",
            "matching_skills": ["Financial Modeling", "Forecasting", "Reporting", "Excel", "SQL"],
            "missing_skills": ["SAP ERP", "M&A Valuation"],
            "job_description_alignment": "Meets analytical requirements but falls short on strategic enterprise architecture tools and M&A valuation techniques.",
            "improvement_suggestions": [
                {"priority": "Medium", "area": "Valuation", "suggestion": "Incorporate any DCF (Discounted Cash Flow) or LBO model experience explicitly."}
            ],
            "interview_questions": [
                {"question": "What happens to the cash flow statement if depreciation increases by $10?", "intent": "Financial statement fluency.", "suggested_answer": "Net income drops by $6 (assuming 40% tax). Add back $10 depreciation, so cash from operations increases by $4."}
            ]
        }
    },
    "HR Specialist": {
        "resume_text": """
Clara Oswald - Human Resources Specialist
Summary:
HR Specialist with 4 years of experience focusing on talent acquisition, employee relations, and payroll system management.
Skills: Workday, Recruiting, Performance Management, Onboarding, Employee Engagement, Excel
""",
        "job_desc": """
HR Director & People Operations Manager
Requirements:
- Global talent acquisition leadership and employee retention plans.
- Compensation structuring, benefits strategy, and Workday HRIS mastery.
- Strategic labor compliance and organizational design.
""",
        "analysis": {
            "ats_score": 81,
            "resume_strength": 83,
            "profile_summary": "HR professional with strong operational experience in onboarding, HRIS (Workday), and hiring pipelines.",
            "technical_skills": ["Workday", "Recruiting", "Payroll systems", "Excel"],
            "soft_skills": ["Employee Relations", "Onboarding", "Conflict Resolution", "Performance Management"],
            "missing_skills": ["Compensation Structuring", "Strategic HR Compliance", "HR Metrics (Retention/Attrition)"],
            "recommended_roles": ["HR Generalist", "HR Specialist", "People Operations Manager"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Compliance & Policy", "suggestion": "Add state/federal compliance audits experience or payroll compliance certificates."}
            ],
            "interview_questions": [
                {"question": "How do you design a retention plan during a high-turnover phase?", "intent": "Assess HR strategic leadership.", "suggested_answer": "Perform exit interviews, implement feedback loops, review compensation benchmarks, and improve onboarding and training paths."}
            ]
        },
        "match": {
            "match_score": 76,
            "resume_strength": 83,
            "profile_summary": "Great match for HR operations and recruitment tools (Workday). Lacks director-level compliance and design credentials.",
            "matching_skills": ["Workday", "Recruiting", "Onboarding", "Employee Relations"],
            "missing_skills": ["Compensation Structuring", "Strategic Compliance"],
            "job_description_alignment": "Very suited for daily employee care, but missing corporate policy design experience.",
            "improvement_suggestions": [
                {"priority": "Medium", "area": "Metrics", "suggestion": "Mention attrition rate metrics or cost-per-hire reductions you achieved."}
            ],
            "interview_questions": [
                {"question": "Describe a difficult employee relations issue you resolved.", "intent": "De-escalation and policy application.", "suggested_answer": "Detail investigation steps, neutral documentation, policy references, and the constructive outcome reached."}
            ]
        }
    },
    "Sales Executive": {
        "resume_text": """
Robert Vance - Sales Executive
Summary:
Sales professional with 5 years of experience in B2B client acquisition, account management, and CRM pipelines.
Skills: Salesforce, Cold Calling, Negotiation, Lead Generation, Account Management, Presentation
""",
        "job_desc": """
Enterprise Account Executive - B2B SaaS
Requirements:
- Manage complex multi-stakeholder contract negotiations.
- Experience hit sales quotas exceeding $1M ARR.
- CRM mastery using Salesforce.
""",
        "analysis": {
            "ats_score": 82,
            "resume_strength": 85,
            "profile_summary": "Productive Sales Executive with excellent cold calling, lead generation, and account ownership credentials.",
            "technical_skills": ["Salesforce", "Lead Generation", "Account Management", "CRM Pipelines"],
            "soft_skills": ["Negotiation", "Presentation", "Relationship Building", "Cold Calling"],
            "missing_skills": ["ARR/MRR SaaS Metrics", "Enterprise Sales Cycle", "Value Selling Frameworks"],
            "recommended_roles": ["Account Executive", "Sales Representative", "Business Development Manager"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Sales Quota", "suggestion": "Clearly state your historical quota achievement percentages (e.g. 'Hit 120% of sales quota consistently')."}
            ],
            "interview_questions": [
                {"question": "How do you handle a prospect who objects on pricing?", "intent": "Check sales objection strategy.", "suggested_answer": "Validate the concern, pivot to return-on-investment value metrics, unpack key features matching their pain points, and offer flexible package terms."}
            ]
        },
        "match": {
            "match_score": 79,
            "resume_strength": 85,
            "profile_summary": "Strong CRM and client handling skills. Needs ARR/MRR SaaS context to match the enterprise level requested.",
            "matching_skills": ["Salesforce", "Negotiation", "Account Management", "Presentation"],
            "missing_skills": ["ARR/MRR Metrics", "Enterprise Sales Cycles"],
            "job_description_alignment": "Meets sales execution needs. Needs B2B SaaS deal sizes and contract values added.",
            "improvement_suggestions": [
                {"priority": "High", "area": "ARR metrics", "suggestion": "Incorporate B2B SaaS deal sizing (ARR/MRR values) explicitly in your achievements list."}
            ],
            "interview_questions": [
                {"question": "What is your typical sales cycle length for a $100k contract?", "intent": "Assess experience with enterprise cycles.", "suggested_answer": "Outline stages: discovery, demo, custom pilot, stakeholder security review, procurement, and contract close (typically 3-6 months)."}
            ]
        }
    },
    "Cybersecurity Analyst": {
        "resume_text": """
Diana Prince - Cybersecurity Analyst
Summary:
Cybersecurity professional with 4 years of experience specializing in network security auditing, threat detection, and incident response.
Skills: Wireshark, Splunk, Python, Linux, Network Security, Ethical Hacking, Firewalls, CompTIA Security+
""",
        "job_desc": """
Senior Security Operations Center (SOC) Specialist
Requirements:
- Advanced SIEM analysis (Splunk/QRadar) and incident triage.
- Penetration testing, malware analysis, and scripting automation in Python.
- Industry certifications: CISSP or CEH.
""",
        "analysis": {
            "ats_score": 83,
            "resume_strength": 85,
            "profile_summary": "Skilled Security Analyst with strong background in network monitoring, SIEM tool usage (Splunk), and CompTIA training.",
            "technical_skills": ["Wireshark", "Splunk", "Python", "Linux", "Network Security", "Ethical Hacking", "Firewalls", "CompTIA Security+"],
            "soft_skills": ["Incident Response", "Analytical Thinking", "Threat Assessment"],
            "missing_skills": ["CISSP", "CEH", "Malware Analysis", "Penetration Testing Tools (Metasploit)"],
            "recommended_roles": ["SOC Analyst", "Security Engineer", "Information Security Consultant"],
            "improvement_suggestions": [
                {"priority": "High", "area": "Certifications", "suggestion": "Consider preparing for advanced security credentials such as CEH (Certified Ethical Hacker) or CISSP to unlock senior titles."}
            ],
            "interview_questions": [
                {"question": "What is the difference between a False Positive and a False Negative?", "intent": "SOC triage terminology check.", "suggested_answer": "False Positive alerts on benign activity. False Negative completely misses malicious activity. False Negatives are far more dangerous."}
            ]
        },
        "match": {
            "match_score": 81,
            "resume_strength": 85,
            "profile_summary": "Highly compatible baseline threat analyst. Missing advanced senior penetration testing tools and CISSP/CEH certs.",
            "matching_skills": ["Splunk", "Python", "Linux", "Network Security", "Threat detection", "Incident response"],
            "missing_skills": ["CISSP", "Malware analysis"],
            "job_description_alignment": "Meets SOC analyst metrics, but needs higher-level incident management credentials.",
            "improvement_suggestions": [
                {"priority": "Medium", "area": "SOC Operations", "suggestion": "Highlight any scripting automation done in Python to parse security logs."}
            ],
            "interview_questions": [
                {"question": "How do you trace a potential SQL Injection attack using Splunk?", "intent": "SIEM querying competency.", "suggested_answer": "Search web access logs for characters like single quotes, SELECT keywords, or UNION queries in HTTP parameters."}
            ]
        }
    }
}
