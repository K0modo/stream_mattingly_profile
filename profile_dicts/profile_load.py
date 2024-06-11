from app import conn
import pandas as pd

###  THIS MODULE IS USED TO POPULATE RESUME DATABASE FOR FURTHER DEVELOPMENT


###  DATABASE TABLES
def fetch_tables_conn(conn):
    db_query = "SELECT name FROM sqlite_master WHERE type='table'"
    result = pd.read_sql_query(db_query, conn)
    return result


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
    "Developed interactive web application prototype for defense of class action lawsuit for overbilling more than 5,000 "
    "customers over multiple years.  Engaged as financial expert on two separate cases and responsible for extracting"
    "utility billing data, building database, performing 'what-if' scenario's and reporting results.",
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


def store_highlights_data(conn, profile_data):
    result = pd.DataFrame(profile_data)
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

