from db_connection import conn
import pandas as pd

###  THIS MODULE IS USED TO POPULATE RESUME DATABASE FOR FURTHER DEVELOPMENT


expertise = [
    "Certified Public Accountant (CPA) from 1993 until 2020",
    "Computer programming, web development and data analytics",
    "Department of Defense Procurement and Cost Accounting",
    "Project Management, Manufacturing, Healthcare and NonProfits",
    "Federal and State Budgeting and Financial Reporting",
]


skills = [
    "Programming Language: Python(Pandas, SQLAlchemy)",
    "Web Development: Python (Plotly-Dash, Streamlit), HTML/CSS",
    "Data Visualization: Plotly-Dash, AG-Grid, MS Excel",
    "Data Management: PostgreSQL, MS SQL Server",
    "Accounting/Budgeting: General Ledger, Management Reporting, Cost Accounting",
    "Auditing: Financial, Regulatory Compliance, Inventory",
]

work_history = [
    'President - Tynan Properties LLC (2010-Present)',
    'Contractor IT Financial Administrator - CapitalOne (2007-2010)',
    'CFO - Virginia Health Quality Corporation (2005-2007)',
    'Contractor Financial Manager - US Nuclear Security Administration (2000-2002)',
    'Manager Management Consulting, Grant Thornton LLP (1993-1994, 1998-2000)',
    'Manager Strategic Analytics, PricewaterhouseCoopers LLP (1995-1998)',
    'Senior Accountant - Science Applications International Corporation (SAIC) (1988-1993)',
    'Budget Officer - Captain US Air Force (1983-1988)'
    ]

highlights = [
    "Developed multi-page interactive web application prototype to capture healthcare insurance claim information "
    "for policy holder and insurance company managers",
    "Engaged as financial expert on two separate class action lawsuits involving overbilling of electricity by public "
    "housing authorities.  Was responsible for extracting utility billing data, creating MS SQL database, and reporting"
    " results to management.  Developed interactive web application prototype years.",
    "Financial administrator for CapitalOne Corporate IT.  Responsible for inventory control of hardware, "
    "software and maintenance agreements for data center operations and data network. Assisted IT team with major "
    "corporate initiative to consolidate data centers throughout the world, dispose of obsolete hardware, "
    "remove unused software, and renegotiate license agreements with suppliers.",
    "Financial manager for classified US Nuclear NonProliferation program within US Department of Energy.  Assisted "
    "program managers with managing $500M operating budget, tracking progress and reporting status to US Congress.",
    "Active Duty Captain in US Air Force responsible for budget policy affecting $1B Alaska command operating budget"
    ]


python_dict = {
    'Pandas': 'Processing large datasets',
    'Dash-Plotly': 'Web Interactive Components (HTML/CSS, JavaScript-React)',
    'AG-Grid':'Interactive Tables and Components',
    'SQLAlchemy': 'Object Mapping Data Classes and SQL Queries',
    'Streamlit': 'Rapid web deployment (HTML/CSS, JavaScript-React)',
    'Flask': 'Web Framework (HTML/CSS)',
    'Plotly': 'Interactive Data Visualization',
    'Editors': 'PyCharm, IntelliJ, JupyterLab'
}

database_dict = {
    'MS SQL': 'TSQL Queries, Server Reporting Services',
    'PostgreSQL': 'pgAdmin interface with SQLAlchemy, SQLite, Web Applications',
    'SQLite': 'SQL interface with PostgreSQL, CSV, Web Applications',
    'MS Access': 'MS Access Query'
}

accounting_dict = {
    'Financial Reporting': 'Profit & Loss Statements, Balance Sheets and Cash Flow',
    'Project Accounting': 'Tracking actual labor, material, overhead and measuring progress towards completion ',
    'Product Accounting': 'Analyzing product actual vs standard costs for labor, materials and overhead',
    'Contract Pricing': 'Preparing cost proposals for large federal contracts ($100M+)',
    'Budgeting': 'Preparing and modeling business sales, product, labor and administrative costs',
    'Auditing': 'Financial records, Sarbanes-Oxley compliance, inventory',
    'Mergers/Acquisitions': 'Sales and Cost modeling, Gap Analysis and Change Mapping',
    'Microsoft Tools': 'Excel pivot tables, lookup tables, Oracle Hyperion, other'
}

project_links = [
    ["Multi-Page Medical Claims Dashboard", "https://tynan-1.onrender.com", "https://github.com/K0modo/tynan_1",],
    ["Medical Claims Dashboard", "https://tynan-stream-basic.onrender.com", "https://github.com/K0modo/tynan_stream_basic"],
    ["System Conversion Data Wrangling", "", "https://github.com/K0modo/system_conversion_wrangling"],
    ["Litigation Damages Overview", "https://streamlit-damages.onrender.com", "https://github.com/K0modo/streamlit_damages"],
    ["My Profile", "", "https://stream-mattingly-profile.onrender.com"]
]


online_courses = [
    ["Computer Programming", "Learn Python Programming Masterclass",
     "https://www.udemy.com/course/python-the-complete-python-developer-course/?couponCode=OF53124"],
    ["Data Science", "Python Data Analysis: NumPy & Pandas Masterclass",
     "https://www.udemy.com/course/python-pandas/?couponCode=OF53124"],
    ["Data Science", "Python for Data Analysis & Business Intelligence",
     "https://www.udemy.com/course/python-foundations-for-data-analysis/?couponCode=OF53124"],
    ["Data Science", "Python Data Visualization: Dashboards with Plotly & Dash",
     "https://www.udemy.com/course/python-dashboards-plotly-dash/?couponCode=OF53124"],
    ["Data Science", "Python for Data Science and Machine Learning Bootcamp",
     "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/?couponCode=OF53124"],
    ["Data Science", "Data Analysis with Pandas and Python",
     "https://www.udemy.com/course/data-analysis-with-pandas/?couponCode=OF53124"],
    ["Database Management", "Querying Microsoft SQL Server with Transact-SQL",
     "https://www.udemy.com/course/70-461-session-2-querying-microsoft-sql-server-2012/?couponCode=OF53124"],
    ["Database Management", "SQL Server Reporting Services Part 1 (SSRS)",
     "https://www.udemy.com/course/sql-server-reporting-services-part-1-ssrs/?couponCode=OF53124"],
    ["Database Management", "SQL Server Reporting Services Part 2 (SSRS)",
     "https://www.udemy.com/course/sql-server-reporting-services-part-2-ssrs/?couponCode=OF53124"],
]

video_training = [
    ["Computer Programming","Python Coding - John Paul Jones","https://www.youtube.com/playlist?list=PL6lxxT7IdTxFKo9DguLxGM2dhgb8-u976"],
    ["Computer Programming","Python Coding - Arjan Codes","https://www.youtube.com/playlist?list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N"],
    ["Computer Programming","Python Coding - David Blaike","https://www.youtube.com/@davidblaikie2333/playlists"],
    ["Data Science","Python Plotly Dash - Charming Data","https://www.youtube.com/@CharmingData/playlists"],
    ["Data Science","Python Pandas & Data Science - Data School","https://www.youtube.com/@dataschool/playlists"],
    ["Database Management","SQL Server - Pragim Technologies","https://www.youtube.com/playlist?list=PL08903FB7ACA1C2FB"],
    ["Web Development","Python Streamlit - Data Professor","https://www.youtube.com/@DataProfessor/playlists"],
    ["Web Development","Web Design and Layout - Net Ninja","https://www.youtube.com/@NetNinja/playlists"],
    ["Web Development","Web Design and Layout - Kevin Powell","https://www.youtube.com/@KevinPowell/playlists"],
]



###  STORE RESUME DATA INTO DATABASE
def store_expertise_data(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('expertise_table', conn, if_exists='replace', index=False)
    return result


def store_skills_data(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('skills_table', conn, if_exists='replace', index=False)
    return result


def store_work_history_data(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('work_history_table', conn, if_exists='replace', index=False)
    return result


def store_highlights_data(conn, highlights):
    result = pd.DataFrame(highlights)
    result.to_sql('highlights_table', conn, if_exists='replace', index=False)
    return result


def store_python_skills(conn, profile_data):
    result = pd.Series(profile_data)
    result.to_sql('python_skills', conn, if_exists='replace', index=True)
    return result


def store_database_skills(conn, profile_data):
    result = pd.Series(profile_data)
    result.to_sql('database_skills', conn, if_exists='replace', index=True)
    return result


def store_accounting_skills(conn, profile_data):
    result = pd.Series(profile_data)
    result.to_sql('accounting_skills', conn, if_exists='replace', index=True)
    return result


def store_project_links(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('project_links', conn, if_exists='replace', index=False)
    return result


def store_online_courses(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('online_courses', conn, if_exists='replace', index=False)

    return result


def store_video_training(conn, profile_data):
    result = pd.DataFrame(profile_data)
    result.to_sql('video_training', conn, if_exists='replace', index=False)

    return result
