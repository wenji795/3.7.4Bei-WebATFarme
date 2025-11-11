#keywords.py

import logging
import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.keywords_utils import kw_step


class Keywords:
    """
    把 WebDriver（浏览器对象）作为参数传进来；
    封装所有可复用的浏览器操作；
    提供一个统一接口给测试用例调用。
    """
    def __init__(self, driver):
        self.driver = driver

    # ================== 基础定位方法 ==================
    def find(self, step):
        wait = WebDriverWait(self.driver,10)
        locator = step['by'], step['value']

        if step["index"] is None:
            return wait.until(EC.presence_of_element_located(locator))#只要元素出现在DOM中就定位
        else:
            return wait.until(EC.presence_of_all_elements_located(locator))[step["index"]]

    # ================== 核心操作关键字 ==================
    # 每个关键字实际上是对应一个步骤
    @kw_step
    def open(self, step):
        #打开网址
        self.driver.get(step["data"])#每个关键字函数都能通过 self.driver 去控制浏览器；

    @kw_step
    def click(self, step):
        #点击
        self.find(step).click()

    @kw_step
    def input(self, step):
        #输入文本
        self.find(step).send_keys(step["data"])

    @kw_step
    def clear(self, step):
        #清空
        self.find(step).clear()


    def wait(self, step):
        #等待
        with allure.step(f'第{step["step_num"]}步: {step["step_name"]}'):
            logging.info(f'第{step["step_num"]}步: {step["step_name"]}')
            time.sleep(step["data"])

    # ================== 断言关键字 ==================
    @kw_step
    def assert_url(self, step):
        """URL 断言：实际 URL 要包含预期的片段"""
        expected_url = step["data"]            # Excel 里写的期望值
        actual_url = self.driver.current_url   # 浏览器当前的 URL
        # 不包含就抛 AssertionError，pytest 会标红
        assert expected_url in actual_url, f"❌ 当前URL: {actual_url} 不包含 预期URL: {expected_url}"
        logging.info(f"✅ 当前URL: {actual_url} 包含 预期URL: {expected_url}")







