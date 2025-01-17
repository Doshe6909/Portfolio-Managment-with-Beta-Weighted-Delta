from model.database.queries.users import *
from controller.user.user_portfolio_sync import *

class UserBuilder():
    def __init__(self):
        self._instance = None
    
    def __call__(self,
                database_interface,
                **_ignored):

        if not self._instance:
            self._instance = Users(database_interface)
        return self._instance

class Users():
    def __init__(self, database):
        self.database = database

    def get_user(self, username=None):
        command_string = get_user(username)
        return self.database.execute(command_string, with_return = True, num_of_rows = 1)[0]

    def get_all_users(self, num_of_rows = None):
        command_string = get_all_users(num_of_rows)
        return self.database.execute(command_string, with_return = True, num_of_rows = num_of_rows)
    
    def get_numof_users(self):
        command_string = get_numof_users()
        return self.database.execute(command_string, with_return = True)[0][0]

    def add_user(self, username, total_capital):
        portfolio_id = check_last_portfolio_id(self)
        command_string = add_user(username, total_capital, portfolio_id)
        self.database.execute(command_string)

    def delete_user(self, user_name = None, last_user = False):
        """should also delete the portfolio"""
        command_string = delete_user(user_name, last_user)
        self.database.execute(command_string)
    