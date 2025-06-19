import allure
import pytest

from utilities.common_ops import get_data, By
from workflows import web_flows
from workflows.web_flows import WebFlows
import  test_cases.conftest as conf


@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
    @allure.title('Test01: Verify Login Grafana')
    @allure.description('this test verifies a successful login to grafana')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebFlows.verify_grafana_title('Welcome to Grafana')

    @allure.title('Test02: Verify Upper Menu Buttons')
    @allure.description('this test verifies upper menu buttons are displayed')
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertions() # smart-assertions
        #WebFlows.verify_menu_buttons_flow()                 # My Implementation

    @allure.title('Test03: Verify New User')
    @allure.description('this test creates and verifies a new user')
    def test_verify_new_user(self):
        WebFlows.open_users()
        WebFlows.create_user('Erez', 'erez@gmail.com', 'erezi', '12345')
        WebFlows.create_user('Alona', 'alona@gmail.com', 'alonai', '12345')
        WebFlows.verify_number_of_users(3)

    @allure.title('Test04: Filtering Users')
    @allure.description('this test filters users')
    @pytest.mark.parametrize('search_value, expected_users', web_flows.testdata)
    def test_csv(self, search_value, expected_users):
        WebFlows.open_users()
        WebFlows.search_user(search_value)
        WebFlows.verify_number_of_users(int(expected_users))

    @allure.title('Test05: Delete User')
    @allure.description('this test verifies deleted users')
    def test_verify_deleted_user(self):
        WebFlows.open_users()
        WebFlows.delete_user(By.USER, 'erezi') # Option1
        WebFlows.open_users()
        WebFlows.delete_user(By.INDEX, 1)      # Option2
        WebFlows.verify_number_of_users(1)

    def teardown_method(self):
        WebFlows.grafana_home()

    @allure.title('Test06: Visual Testing')
    @allure.description('this test verifies visually users table')
    @pytest.mark.skipif(get_data('Execute_Applitools').lower() == 'no', reason='run this test only on selenium 3.141.0 & appium 1.3.0')
    def test_visual_verify_deleted_user(self):
        conf.eyes.open(self.driver, 'Grafana', 'Grafana Testing User Table')
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        conf.driver.get('http://localhost:3000/admin/users')
        conf.eyes.check_window('Users Table')







