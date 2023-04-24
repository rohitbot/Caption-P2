import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic=read_utils.get_value_from_json("../test_data/config.json")

        des_cap = {
            "platformName": "android",
            "deviceName": "Pixel 4 API 33",
            "appPackage": json_dic["appPackage"],
            "appActivity": json_dic["appActivity"],
            "noReset": True,
            "udid": json_dic["udid"]
        }
        self.driver = webdriver.Remote(command_executor=f"http://localhost:{json_dic['port']}/wd/hub", desired_capabilities=des_cap)