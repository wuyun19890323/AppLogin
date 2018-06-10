from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def send_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc, timeout=30, poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
            # print(value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc, timeout=30, poll=0.5):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def make_xpath_with_unit_feature(self, loc):
        key_index = 0
        value_index = 1
        option_index = 2
        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "

            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_with_unit_feature(loc)

        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)
        feature = feature.rstrip("and ")
        loc = feature_start + feature + feature_end
        return loc

    def find_toast(self, message, timeout=3, poll=0.1):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element = self.find_element((By.XPATH, message), timeout, poll)
        return element.text

    def is_toast_exist(self, message, timeout=3, poll=0.1):
        try:
            self.find_toast(message, timeout, poll)
            return True
        except Exception:
            return False
