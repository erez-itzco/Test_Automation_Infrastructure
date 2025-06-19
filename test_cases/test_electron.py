import allure
import pytest

from extentions.verifications import Verifications
from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class Test_Electron:
    @allure.title('Test01: Add and Verify New Task')
    @allure.description('This test adds a new task and verifies it in the list of tasks')
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task_flow('Learn Python')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 1)

    @allure.title('Test02: Add and Verify New Tasks')
    @allure.description('This test adds a new tasks and verifies it in the list of tasks')
    def test_add_and_verify_new_tasks(self):
        ElectronFlows.add_new_task_flow('Learn Playwright')
        ElectronFlows.add_new_task_flow('Learn JS')
        ElectronFlows.add_new_task_flow('Learn C++')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3)

    def teardown_method(self):
        ElectronFlows.empty_list_flow()






