import allure
import pytest

from extentions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures('init_desktop_driver')
class Test_Desktop:
    @allure.title('Test01: Adding 2 Numbers')
    @allure.description('This test adds 2 numbers and verify the result')
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow('17+9')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '26')

    @allure.title('Test02: Arithmetic Actions ')
    @allure.description('This test does some arithmetics actions and verifies it')
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flow('72-16*66/4')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '924')

    def teardown_method(self):
        DesktopFlows.clear_flow()


