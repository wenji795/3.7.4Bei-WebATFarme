import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Fixture 就是可复用的“测试前置与清理”（setup/teardown）或测试数据，pytest 会按名字自动注入到测试里。
#用来干嘛？
#准备资源：浏览器驱动、数据库连接、API 客户端、临时文件夹等
#自动清理：测试结束后关闭浏览器、断开连接、删除临时数据
#共享状态：按范围（scope）控制复用次数，避免重复创建
#提供数据/配置：把测试数据、环境配置用统一入口提供给用例
#依赖组合：一个 fixture 可以依赖另一个 fixture
from utils.driver_utils import get_chrome_driver




#driver_handler → fixture 返回的 driver 对象 → 交给 Keywords → 控制浏览器。
@pytest.fixture(scope="function")
def driver_handler():
    driver = get_chrome_driver()
    yield driver
    driver.quit()
