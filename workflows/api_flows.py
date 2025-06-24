import allure

from extentions.api_actions import APIActions
from utilities.common_ops import get_data

# Load configuration data
url = get_data('Url')
user = get_data('UserName')
password = get_data('Password')

class APIFlows:
    @staticmethod
    @allure.step('Get value from grafana api flow')
    def get_value_from_api(nodes):
        # Send GET request and extract value
        response = APIActions.get(url + 'api/teams/search', user, password)
        return APIActions.extract_value_from_response(response, nodes)

    @staticmethod
    @allure.step('Create new team in Grafana flow')
    def create_team(name, email):
        # Prepare payload and send POST request
        payload = {'name': name, 'email': email}
        status_code = APIActions.post(url + 'api/teams', payload, user, password)
        return status_code

    @staticmethod
    @allure.step('Update team in Grafana flow')
    def update_team(name, email, id):
        # Prepare payload and send PUT request
        payload = {'name': name, 'email': email}
        status_code = APIActions.put(url + 'api/teams/' + str(id), payload, user, password)
        return status_code

    @staticmethod
    @allure.step('Delete team in Grafana flow')
    def delete_team(id):
        # Send DELETE request
        status_code = APIActions.delete(url + 'api/teams/' +  str(id), user, password)
        return status_code



