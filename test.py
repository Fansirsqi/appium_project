from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
import asyncio

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '12',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': 'com.bilibili.search.main.BiliMainSearchActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def get_title(driver):
    # 选择（定位）所有视频标题
    eles = driver.find_elements(By.ID, 'title')
    for i in eles:
        print(i.text)
    driver.implicitly_wait(1)


def swip_down_fast(driver):
    """快速下滑"""
    driver.swipe(start_x=540, start_y=2294, end_x=540, end_y=243, duration=800)
    driver.implicitly_wait(1)


def _do(driver):
    for i in range(10):
        get_title(driver)
        swip_down_fast(driver)


# 设置缺省等待时间
# driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements(By.ID, "text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element(By.ID, 'search_src_text').click()

# 根据id定位搜索输入框，点击
input_box = driver.find_element(By.ID, 'search_src_text')
input_box.send_keys('依旧归七')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

_do(driver)

input('**** Press to quit..')
driver.quit()
