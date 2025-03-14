import sqlite3
import os

class SQLite:
    def __init__(self):
        # Use raw string to avoid escape sequence issues
        self.base_path = r"C:\Users\O.Feronel\OneDrive - ams OSRAM\Documents\PYTHON\MY_APP_STORE\.database"

        # Check and create directory
        if not os.path.exists(self.base_path):
            try:
                os.makedirs(self.base_path)  # Create directory
                print(f"Created directory: {self.base_path}")
            except PermissionError:
                print(f"Permission denied: Unable to create directory at {self.base_path}.")
                # Use an alternative path in the user's home directory
                self.base_path = os.path.expanduser(r"~\.database")
                os.makedirs(self.base_path, exist_ok=True)
                print(f"Created directory in user space: {self.base_path}")

        # Database path
        self.db_path = os.path.join(self.base_path, "app_store.db")
        print(f'Database path: {self.db_path}')

        # Initialize tables
        # self.create_tables_if_not_exist()

    def connect(self):
        '''Connect to the SQLite database.'''
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Critical: Error connecting to SQLite database: {e}")
            return None

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        '''Execute SQL query with optional fetching options.'''
        conn = self.connect()
        if conn is None:
            return None  # Return None if connection failed

        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch_one:
                return cursor.fetchone()
            elif fetch_all:
                return cursor.fetchall()
            else:
                return None  # For INSERT, UPDATE, DELETE queries
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
            return None
        finally:
            conn.commit()
            conn.close()

    def create_tables_if_not_exist(self):
        '''Define and create tables if they don't exist.'''
        tables = {
            "USERS": [
                "ID INTEGER PRIMARY KEY AUTOINCREMENT",
                "USERNAME TEXT UNIQUE NOT NULL",
                "ACCESS TEXT NOT NULL",  # e.g., 'user' or 'admin'
            ],
            "APPS": [
                "ID INTEGER PRIMARY KEY AUTOINCREMENT",
                "NAME TEXT UNIQUE NOT NULL",
                "PATH TEXT NOT NULL",
                "DESCRIPTION TEXT",
                "ICON TEXT",
            ],
            "USER_APPS": [
                "USER_ID INTEGER NOT NULL",
                "APP_ID INTEGER NOT NULL",
                "FOREIGN KEY (USER_ID) REFERENCES USERS(ID)",
                "FOREIGN KEY (APP_ID) REFERENCES APPS(ID)",
                "PRIMARY KEY (USER_ID, APP_ID)",
            ],
        }

        conn = self.connect()
        if conn is None:
            return  # Return if connection failed

        try:
            cursor = conn.cursor()
            for table_name, columns in tables.items():
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
                cursor.execute(query)
                print(f"INFO: Table '{table_name}' created or already exists.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            conn.commit()
            conn.close()

    ##############################################################################
    #####                           Query Commands                             #####
    ##############################################################################

    def add_user(self, username, access):
        '''Add a new user to the USERS table.'''
        query = "INSERT INTO USERS (USERNAME, ACCESS) VALUES (?, ?)"
        params = (username, access)
        return self.execute_query(query, params)

    def add_app(self, name, path, description=None, icon=None):
        '''Add a new app to the APPS table.'''
        query = "INSERT INTO APPS (NAME, PATH, DESCRIPTION, ICON) VALUES (?, ?, ?, ?)"
        params = (name, path, description, icon)
        return self.execute_query(query, params)

    def assign_app_to_user(self, user_id, app_id):
        '''Assign an app to a user in the USER_APPS table.'''
        query = "INSERT INTO USER_APPS (USER_ID, APP_ID) VALUES (?, ?)"
        params = (user_id, app_id)
        return self.execute_query(query, params)

    def get_user_id(self, username):
        '''Get the ID of a user by their username.'''
        query = "SELECT ID FROM USERS WHERE USERNAME = ?"
        params = (username,)
        result = self.execute_query(query, params, fetch_one=True)
        return result[0] if result else None

    def get_app_id(self, app_name):
        '''Get the ID of an app by its name.'''
        query = "SELECT ID FROM APPS WHERE NAME = ?"
        params = (app_name,)
        result = self.execute_query(query, params, fetch_one=True)
        return result[0] if result else None

    def get_user_apps(self, user_id):
        '''Get all apps assigned to a user.'''
        query = """
            SELECT APPS.NAME, APPS.PATH, APPS.DESCRIPTION, APPS.ICON
            FROM APPS
            JOIN USER_APPS ON APPS.ID = USER_APPS.APP_ID
            WHERE USER_APPS.USER_ID = ?
        """
        params = (user_id,)
        return self.execute_query(query, params, fetch_all=True)

    def get_user_stats(self, username):
        '''Check if the user is an admin.'''
        print(username)
        query = "SELECT ACCESS FROM USERS WHERE USERNAME = ?"
        params = (username,)
        result = self.execute_query(query, params, fetch_one=True)
        
        # Return True if the user is an admin (assuming is_admin is 1 for admin, 0 for regular users)
        return result[0] == 'Admin' if result else False

    
# # Example usage
# if __name__ == "__main__":
#     db = SQLite()

#     # Add a user
#     db.add_user("O.Feronel", "Admin")
#     # db.add_user("user1", "user")

    # # Add an app
    # db.add_app("Notepad", r"C:\Windows\System32\notepad.exe", "Text Editor", "notepad.ico")

    # # Assign app to user
    # user_id = db.get_user_id("user1")
    # app_id = db.get_app_id("Notepad")
    # if user_id and app_id:
    #     db.assign_app_to_user(user_id, app_id)

    # # Get user's apps
    # user_apps = db.get_user_apps(user_id)
    # print("User's Apps:", user_apps)


    
    
    
    
    
    
    
    
    
    
    
    
    
    # def get_module_badge_data(self):
    #     print("Get module and badge data")
    #     query = "SELECT MODULE , BADGE FROM DETAILS"
    #     result = self.execute_query(query, fetch_all=True)
    #     if result:
    #         return result[0] # ex return ('MOD_2', '111111')
    #     return None
    
    # def insert_or_update_module_badge_data(self, module, badge):
    #     print("Insert or update module and badge")
    #     query = """
    #         INSERT OR REPLACE INTO DETAILS (ID, MODULE, BADGE)
    #         VALUES (1, ?, ?)
    #     """
    #     params = (module, badge)
    #     self.execute_query(query, params)


    # def save_to_database(self, name, device, project, profit):
    #     '''Save data to add new persons.'''
    #     query = """
    #                 INSERT INTO TIMESHEET (NAME, DEVICE, PROJECTNUMBER, PROFITCENTER)
    #                 VALUES (?, ?, ?, ?)
    #             """  # Ensure the column names match your database schema
    #     params = (name, device, project, profit)
    #     self.execute_query(query, params)  # Execute query with provided parameters

    # def delete_all_data(self):
    #     """Clear all TIMESHEET device."""
    #     query = "DELETE FROM TIMESHEET"
    #     print("Executing query:", query)
    #     self.execute_query(query)

    # def save_results(self, date, tester, time, profit):
    #     """Save test results."""
    #     query = """
    #                 INSERT INTO RESULT (DATE, TESTER, TIMEUSE, PROFITCENTER)
    #                 VALUES (?, ?, ?, ?)
    #             """
    #     params = (date, tester, time, profit)
    #     self.execute_query(query, params)

    # def get_profit_center(self, device):
    #     """Get profit center."""
    #     query = "SELECT PROFITCENTER FROM TIMESHEET WHERE DEVICE = ?"
    #     params = (device,)  # Use a parameterized query to prevent SQL injection
    #     result = self.execute_query(query, params, fetch_one=True)
    #     if result:
    #         return result[0]  # Return the first column of the fetched row
    #     return None

    # def delete_all_results(self):
    #     """Clear all RESULTS data."""
    #     query = "DELETE FROM RESULT"
    #     print("Executing query:", query)
    #     self.execute_query(query)
        

    # def get_unique_dates(self):
    #     """Get unique dates from the RESULT table."""
    #     query = "SELECT DISTINCT DATE FROM RESULT"
    #     return self.execute_query(query, fetch_all=True)

    # def get_time_sum_by_date(self, date):
    #     """Get the sum of TIMEUSE for a specific date."""
    #     query = "SELECT SUM(TIMEUSE) FROM RESULT WHERE DATE = ?"
    #     result = self.execute_query(query, (date,), fetch_one=True)
    #     if result and result[0]:
    #         return result[0]  # Return the sum if it's not None
    #     return 0  # Return 0 if there are no results


    # def get_unique_profit_centers(self):
    #     """Get unique profit centers from the RESULT table."""
    #     query = "SELECT DISTINCT PROFITCENTER FROM RESULT"
    #     return self.execute_query(query, fetch_all=True)

    # def get_time_sum_by_profit_center(self, profit):
    #     """Get the sum of TIMEUSE for a specific profit center."""
    #     query = "SELECT SUM(TIMEUSE) FROM RESULT WHERE PROFITCENTER = ?"
    #     result = self.execute_query(query, (profit,), fetch_one=True)
    #     if result and result[0]:
    #         return result[0]  # Return the sum if it's not None
    #     return 0  # Return 0 if there are no results

    # def get_unique_profit_centers_by_date(self, date):
    #     """Get unique profit centers and their total TIMEUSE for a specific date."""
    #     query = """
    #         SELECT PROFITCENTER, SUM(TIMEUSE) 
    #         FROM RESULT 
    #         WHERE DATE = ? 
    #         GROUP BY PROFITCENTER
    #     """
    #     return self.execute_query(query, (date,), fetch_all=True)
    

    # def select_all_timesheet(self):
    #     '''Get all data from table timesheet'''

    #     query = "SELECT * FROM timesheet"
    #     return self.execute_query(query, fetch_all=True)
    
    # def dark_mode_status(self):
    #     '''Get dark mode status'''
    #     print("dark mode status")
    #     query = "SELECT DARK_MODE FROM SYTEM_STATUS WHERE ID = 1"
    #     result = self.execute_query(query, fetch_one=True)
    #     if result:
    #         return result[0]
    #     return False
    
    # def update_dark_mode_status(self, status):
    #     '''Update dark mode status'''
    #     # print("update dark mode status")
        
    #     # Check if row with ID = 1 exists
    #     check_query = "SELECT COUNT(*) FROM SYTEM_STATUS WHERE ID = 1"
    #     result = self.execute_query(check_query, fetch_one=True)
        
    #     if result[0] == 0:
    #         # Insert a new row with ID = 1 if it doesn't exist
    #         insert_query = "INSERT INTO SYTEM_STATUS (ID, DARK_MODE) VALUES (1, ?)"
    #         self.execute_query(insert_query, (status,))
    #     else:
    #         # Update the existing row
    #         update_query = "UPDATE SYTEM_STATUS SET DARK_MODE = ? WHERE ID = 1"
    #         self.execute_query(update_query, (status,))