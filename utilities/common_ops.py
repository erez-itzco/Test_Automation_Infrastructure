import csv
import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


##############################################################
# Function Name: get_data
# Function Description: This function reads data from external xml file
# Function Parameters: String - node(tag) name
# Function Return: String - node(tag) value
##############################################################

def get_data(node_name):
    root = ET.parse('C:/Automation/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


##############################################################
# Function Name: wait
# Function Description: This function waits for an element to exist or be displayed
# Function Parameters:
#   for_element - String: Type of wait condition ('element_exists' or 'element_displayed')
#   elem - Tuple: Element locator (By, value)
# Function Return: None
##############################################################


def wait(for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))


##############################################################
# Function Name: read_csv
# Function Description: This function reads rows of data from a CSV file
# Function Parameters: String - CSV file path
# Function Return: List - data from CSV file as a list of rows
##############################################################


def read_csv(file_name):
    data = []
    with open(file_name, newline= '') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


##############################################################
# Function Name: get_time_stamp
# Function Description: This function returns the current timestamp
# Function Parameters: None
# Function Return: Float - current time in seconds since epoch
##############################################################


def get_time_stamp():
    return time.time()


# Enum for selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'

# Enum for selecting row from table to delete
class By:
    USER = 'user'
    INDEX = 'index'

# Enum for selecting whether we want to save mortgage transaction or not
class Save:
    Yes = True
    No = False

# Enum for selecting whether we want to choose the swipe direction
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'



