# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # create webdriver object
    driver = webdriver.Firefox()

    # get geeksforgeeks.org
    driver.get("https://www.geeksforgeeks.org/")

    # get element
    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Courses")

    # create action chain object
    action = ActionChains(driver)

    # click the item
    action.click(on_element=element)

    # perform the operation
    action.perform()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
