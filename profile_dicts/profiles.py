import pandas as pd


class Profiles:
    def __init__(self, conn):
        self.conn = conn
        self.expertise = self.fetch_expertise_table()
        self.skills = self.fetch_skills_table()
        self.work_history = self.fetch_work_history_table()
        self.highlights = self.fetch_highlights_table()
        self.python = self.fetch_python_skills()
        self.database = self.fetch_database_skills()
        self.accounting = self.fetch_accounting_skills()
        self.links = self.fetch_project_links()

    def fetch_expertise_table(self):
        db_query = "Select * from expertise_table "
        result = self.conn.query(db_query)
        result = pd.DataFrame(result)
        return result

    def fetch_skills_table(self):
        db_query = "Select * from skills_table "
        result = self.conn.query(db_query)
        result = pd.DataFrame(result)
        return result

    def fetch_work_history_table(self):
        db_query = "Select * from work_history_table "
        result = self.conn.query(db_query)
        result = pd.DataFrame(result)
        return result

    def fetch_highlights_table(self):
        db_query = "Select * from highlights_table "
        result = self.conn.query(db_query)
        result = pd.DataFrame(result)
        return result

    def fetch_python_skills(self):
        db_query = "Select * from python_skills "
        result = self.conn.query(db_query)
        result.set_index('index', inplace=True)
        return result

    def fetch_database_skills(self):
        db_query = "Select * from database_skills "
        result = self.conn.query(db_query)
        result.set_index('index', inplace=True)
        return result

    def fetch_accounting_skills(self):
        db_query = "Select * from accounting_skills "
        result = self.conn.query(db_query)
        result.set_index('index', inplace=True)
        return result

    def fetch_project_links(self):
        db_query = "Select * from project_links"
        result = self.conn.query(db_query)
        result = pd.DataFrame(result)
        return result
