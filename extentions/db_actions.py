import allure
import test_cases.conftest as conf


class DBActions:
    database = None  # Shared DB connection inside the class

    @staticmethod
    @allure.step('Query Builder')
    # Example: "SELECT user,password FROM Employees WHERE comments = 'correct'
    def query_builder(columns, table, where_name, where_value):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + where_name + " = '" + where_value + "'"
        return query

    @staticmethod
    @allure.step("Get Query Results")
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        return result #Return List Of Tuples
