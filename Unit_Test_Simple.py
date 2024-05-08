from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.python.org")
print(driver.title)


search_bar = driver.find_element(By.ID,"id-search-field")

search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)
driver.close()



# Q1: What to assert for? if it can be click, then ,click it.


import unittest

# 加法函数
def add(x, y):
    return x + y

# 字符串反转函数
def reverse_string(s):
    return s[::-1]

# 列表排序函数
def sort_list(lst):
    return sorted(lst)

# 检查素数的函数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 计算阶乘的函数
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 定义测试类
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 2), 5)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertNotEqual(reverse_string("Python"), "Python")

    def test_sort_list(self):
        self.assertEqual(sort_list([12, 4, 5, 6, 1]), [1, 4, 5, 6, 12])
        self.assertEqual(sort_list([]), [])
        self.assertEqual(sort_list([-2, -1, -3]), [-3, -2, -1])

    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(11))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

# 主执行函数
if __name__ == '__main__':
    unittest.main()



