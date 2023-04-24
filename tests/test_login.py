from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from assertpy import assert_that

from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_enter_value_and_verify(self):
        self.driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue").click()
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1").send_keys("Hello")
        self.driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Btn1").click()
        actual_text = self.driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Tv1").text
        assert_that("Hello World").is_equal_to(actual_text)


    def test_scroll_view(self):
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='Btn3']").click()
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("BUTTON16")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text,'BUTTON16']").click()
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        actual_text = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView").text
        assert_that(actual_text).is_equal_to("KWADemo")

    def test_move_element(self):
        action = TouchAction(self.driver)
        self.driver.swipe(350, 1250, 350,350 )
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/drag").click()
        ele = self.driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ingvw")
        action.press(ele).move_to(x=375, y=850).wait(2000).release().perform()

    def test_info(self):
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ContactUs").click()
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et2").click()
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et2").send_keys("paras")
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et3").send_keys("paras@gmail.com")
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et6").send_keys("paras222")
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et7").send_keys("98986622")
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn2").click()
        self.driver.press_keycode("04")
        actual_name = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv2").text
        actual_email = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv7").text
        actual_password = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv5").text
        actual_mobile = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv6").text
        assert_that(actual_name).is_equal_to("Name: Maulin")
        assert_that(actual_email).is_equal_to("Email: maulin@gmail.com")
        assert_that(actual_password).is_equal_to("Password: maulin222")
        assert_that(actual_mobile).is_equal_to("Mobile: 98186622")
