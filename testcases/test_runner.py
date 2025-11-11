import logging
import sys
import os
from jinja2 import Template

from core.keywords import Keywords
from utils.allure_utils import allure_init
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from utils.excel_utils import read_excel

class TestRunner:


    #读取测试用例文件中的全部数据，用属性保存
    data = read_excel()

    #不确定后续是否需要提取
    # all = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case, driver_handler):

            # 引用全局的all
            # all = self.all
            #根据all的值，渲染case
            # case = eval(Template(str(case)).render(all))


            #初始化allure报告
            allure_init(case=case)#形参=实参  参数只有一个时形参可以不写
            # allure.dynamic.feature(case["feature"])
            # allure.dynamic.story(case["story"])
            # allure.dynamic.title(f"ID:{case["id"]} -- {case["title"]}")
            # logging.info(f'用例ID：{case["id"]} 模块：{case["feature"]} 场景：{case["story"]} 标题：{case["title"]}')

            #创建关键字对象
            keywords = Keywords(driver_handler)

            #执行每一步
            for step in case["steps"]:
                logging.info(f'步骤: {step}')
                # 匹配关键字，__getattritubute__(属性名或方法名) -> 返回一个绑定方法 对象类型的数据
                function_name = keywords.__getattribute__(step["keyword"])
                # print(function_name)
                # 执行方法
                # function_name(step["by"], step["value"], step["data"])
                function_name(step)


