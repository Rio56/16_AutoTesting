# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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

def Formy_Buttons_InputText():
    # create webdriver object
    driver = webdriver.Firefox()

    # get https://formy-project.herokuapp.com/buttons
    driver.get("https://formy-project.herokuapp.com/buttons")

    element_Primary = driver.find_element(By.XPATH, "//button[normalize-space()='Primary']")
    element_Success = driver.find_element(By.XPATH, "//button[normalize-space()='Success']")
    element_navbarDropdownMenuLink = driver.find_element(By.ID, "navbarDropdownMenuLink")

    element_Enabled_disabled_elements = driver.find_element(By.XPATH, "//a[normalize-space()='Enabled and disabled elements']")



    #element_Primary.click()
    #driver.implicitly_wait(10)
    #element_Success.click()

    # create action chain object
    action = ActionChains(driver)

    # click the item
    action.click(on_element=element_Primary)
    driver.implicitly_wait(5)
    action.click(on_element=element_Success)
    driver.implicitly_wait(5)
    action.click(on_element=element_navbarDropdownMenuLink)
    driver.implicitly_wait(5)
    action.click(on_element=element_Enabled_disabled_elements).perform()
    driver.implicitly_wait(5)

    element_input = driver.find_element(By.XPATH,"//input[@id='input']")
    # 点击输入框以确保其获得焦点
    action.click(on_element=element_input)

    # 发送文本信息
    action.send_keys("I AM RIO")

    # perform the operation
    action.perform()


    #implict can set for the whole code. not only for one item.
    # wait = WebDriverWait(driver, 10) can set for certain code.



    pass


def Formy_NewWindow_Scrolling():
    # create webdriver object
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # get https://formy-project.herokuapp.com/buttons
    driver.get("https://formy-project.herokuapp.com/buttons")

    element_navbarDropdownMenuLink = driver.find_element(By.ID, "navbarDropdownMenuLink")
    element_Switch_Window = driver.find_element(By.XPATH, "//a[normalize-space()='Switch Window']")

    action = ActionChains(driver)

    action.click(on_element=element_navbarDropdownMenuLink)
    action.click(on_element=element_Switch_Window).perform()

    element_Alert = driver.find_element(By.XPATH, "//button[@id='alert-button']")
    #action.click(on_element=element_Alert).perform()

    # 处理弹出的警告框
    #alert = driver.switch_to.alert
    #alert_text = alert.text  # 读取警告框的文本内容
    # 处理弹出的警告框
    #WebDriverWait(driver, 10)
    #print("Alert text is:", alert_text)  # 打印警告框的文本内容
    #alert.accept()  # 点击警告框的确认按钮来关闭警告框

    element_new_tab = driver.find_element(By.XPATH, "//button[@id='new-tab-button']")
    action.click(on_element=element_new_tab).perform()

    WebDriverWait(driver, 10)
    # 假设某个操作会打开新标签页
    original_window = driver.current_window_handle
    # 等待新标签页打开并获取所有窗口句柄
    all_windows = driver.window_handles
    new_window = None
    # 确保新窗口已经打开
    for window in all_windows:
        print(driver.current_url)
        if window != original_window:
            print("!")
            new_window = window
            break
    # 切换到新窗口
    if new_window:
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://formy-project.herokuapp.com/"))
        print("Switched to new window/tab with URL:", driver.current_url)
    print("1,Switched to new window/tab with URL:", driver.current_url)
    element_page_scroll = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/li[11]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView(true);", element_page_scroll)
    action.click(on_element= element_page_scroll).perform()
    print("2,Switched to new window/tab with URL:", driver.current_url)
    print("Switched to new window/tab with URL:")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, 0);")
    # 向下滚动 1000 像素
    driver.execute_script("window.scrollBy(0, 1000);")

    # 向上滚动 1000 像素
    driver.execute_script("window.scrollBy(0, -1000);")

    # 滚动到页面底部，然后回到顶部
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    # 滚动至特定元素
    element_page_scroll = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Page Scroll']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", element_page_scroll)
    time.sleep(1)

    # 通过修改页面滚动位置验证滚动效果
    driver.execute_script("window.scrollBy(0, 1000);")  # 向下滚动1000像素
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -1000);")  # 向上滚动1000像素
    time.sleep(1)

    print("Finished scrolling.")

    # 清理工作
    driver.quit()

def Form_CheckBox():

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # get https://formy-project.herokuapp.com/buttons
    driver.get("https://formy-project.herokuapp.com/checkbox")

    element_1 = driver.find_element(By.XPATH, "//input[@id='checkbox-1']")
    element_2 = driver.find_element(By.XPATH, "//input[@id='checkbox-2']")
    element_3 = driver.find_element(By.XPATH, "//input[@id='checkbox-3']")

    #element_1.click()  # 选中
    #element_2.click()  # 选中

    action = ActionChains(driver)

    action.click(on_element=element_1).perform()
    time.sleep(2)
    action.click(on_element=element_2).perform()
    time.sleep(2)
    action.click(on_element=element_3).perform()
    time.sleep(2)
    action.click(on_element=element_1).perform()


def Form_Datepicker():

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # get https://formy-project.herokuapp.com/buttons
    driver.get("https://formy-project.herokuapp.com/datepicker")

    element_1 = driver.find_element(By. ID , "datepicker")
    # element_2 = driver.find_element(By.XPATH, "//input[@id='checkbox-2']")
    # element_3 = driver.find_element(By.XPATH, "//input[@id='checkbox-3']")
    #element_1.click()
    #element_Month = driver.find_element(By.XPATH,"//th[normalize-space()='May 2024']")
    #element_Day = driver.find_element(By.XPATH,"//td[normalize-space()='18']")
    #element_Month.click()
    #element_Day.click()

    element_1.send_keys("07/07/2023")

    action = ActionChains(driver)
    action.click(on_element=element_1).perform()
    time.sleep(2)
    print("datepicker")

    # Locating the calendar and navigation elements
    #calendar = driver.find_element(By.XPATH, "//div[@class='calendar']")
    prev_button = element_1.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='prev'][normalize-space()='«']")
    next_button = element_1.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='next'][normalize-space()='»']")

    # Clicking the Previous button to navigate to the previous month's
    prev_button.click()
    time.sleep(2)
    prev_button.click()
    time.sleep(2)

    # Clicking the Next button to navigate to the next month's
    next_button.click()
    time.sleep(2)

    # Waiting for the desired month/year to be visible (optional)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//th[normalize-space()='December 2023']"), "December 2023"))


    # Selecting a specific date from the calendar
    date_element = element_1.find_element(By.XPATH, "//td[normalize-space()='22']")
    date_element.click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # Formy_Buttons_InputText()
    # Formy_NewWindow_Scrolling()
    # Form_CheckBox()
    Form_Datepicker()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
