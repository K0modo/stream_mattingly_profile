import pandas as pd


fetch_table = {
    'expertise': "Select * from expertise_table",
    'skills': "Select * from skills_table ",
    "work_history": "Select * from work_history_table ",
    'highlights': "Select * from highlights_table ",
    "python": "Select * from python_skills ",
    "database": "Select * from database_skills ",
    "accounting": "Select * from accounting_skills ",
    "project_links": "Select * from project_links",
    "online_courses": "Select * from online_courses",
    "video_training": "Select * from video_training"
}

fetch_dict_list = ['python', 'database', "accounting"]


class Profiles:
    def __init__(self, conn):
        self.conn = conn
        self.expertise = self.fetch_profile_table('expertise')
        self.skills = self.fetch_profile_table('skills')
        self.work_history = self.fetch_profile_table("work_history")
        self.highlights = self.fetch_profile_table('highlights')
        self.python = self.fetch_profile_table('python')
        self.database = self.fetch_profile_table("database")
        self.accounting = self.fetch_profile_table("accounting")
        self.project_links = self.fetch_profile_table("project_links")
        self.online_courses = self.fetch_profile_table("online_courses")
        self.video_training = self.fetch_profile_table("video_training")

    def fetch_profile_table(self, table):
        db_query = fetch_table[table]
        result = self.conn.query(db_query)
        if table in fetch_dict_list:
            result.set_index('index', inplace=True)
        else:
            result = pd.DataFrame(result)
        return result

    ###  DATABASE TABLES
    def fetch_tables_conn(self):
        db_query = "SELECT name FROM sqlite_master WHERE type='table'"
        result = pd.read_sql_query(db_query, self.conn)
        return result
