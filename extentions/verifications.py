import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify equals failed, Actual: ' + str(actual) + ' is not equals to expected: ' + str(expected)


    @staticmethod
    @allure.step('verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify is displayed failed, Element: ' + elem.text + ' is not displayed '


    @staticmethod
    @allure.step('soft verifications (assert) of elements using smart-assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()


    @staticmethod
    @allure.step('soft verifications (assert) of elements using my implementation')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.append(elems[i].get_attribute('aria-label'))
        if failed_elems:
            for failed_elem in failed_elems:
                print('Soft Displayed Failed, Elements which have Failed: ' + str(failed_elem))
            raise AssertionError('Soft Displayed Failed')

    @staticmethod
    @allure.step('verify number of elements in list')
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'Number of elements in list: ' + str(len(elems)) + ' does not match expected: ' + str(size)

    