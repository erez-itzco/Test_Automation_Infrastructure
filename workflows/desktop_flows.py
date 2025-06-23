import allure

from extentions.ui_actions import UiActions
import utilities.manage_pages as page

class DesktopFlows:
    @staticmethod
    @allure.step('Calculate equation')
    def calculate_flow(equation):
        # Click each character in the equation
        for i in equation:
            DesktopFlows.calculator_click(i)
            # Click '=' to get the result
        UiActions.click(page.standard_calc.get_equals())

    @staticmethod
    def calculator_click(value):
        # Map each character to its corresponding button
        if value == '0':
            UiActions.click(page.standard_calc.get_zero())
        elif value == '1':
            UiActions.click(page.standard_calc.get_one())
        elif value == '2':
            UiActions.click(page.standard_calc.get_two())
        elif value == '3':
            UiActions.click(page.standard_calc.get_three())
        elif value == '4':
            UiActions.click(page.standard_calc.get_four())
        elif value == '5':
            UiActions.click(page.standard_calc.get_five())
        elif value == '6':
            UiActions.click(page.standard_calc.get_six())
        elif value == '7':
            UiActions.click(page.standard_calc.get_seven())
        elif value == '8':
            UiActions.click(page.standard_calc.get_eight())
        elif value == '9':
            UiActions.click(page.standard_calc.get_nine())
        elif value == '+':
            UiActions.click(page.standard_calc.get_plus())
        elif value == '-':
            UiActions.click(page.standard_calc.get_minus())
        elif value == '*':
            UiActions.click(page.standard_calc.get_mult())
        elif value == '/':
            UiActions.click(page.standard_calc.get_divide())
        else:
            # Raise exception for unsupported input
            raise Exception('Invalid Input' + value)

    @staticmethod
    @allure.step('Get calculator result')
    def get_result_flow():
        # Get and clean result text
        result = page.standard_calc.get_result().text.replace("Display is","").strip()
        return result

    @staticmethod
    @allure.step('Clear calculator page')
    def clear_flow():
        # Click 'Clear' button
        UiActions.click(page.standard_calc.get_clear())



