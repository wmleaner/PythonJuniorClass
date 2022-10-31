from selenium import webdriver  #从selenium工具导入webdriver库
import time #导入内置库time
driver=webdriver.Chrome()#选择谷歌浏览器操作，初始化driver驱动，建立回话
driver.get("http://127.0.0.1/index.php/Home/user/login.html")#打开一个网址
driver.maximize_window()#最大化窗口
#关闭驱动，会话关闭
#driver.quit()

driver.find_element_by_id("username").send_keys('2863463318@qq.com')  #注意一个是element一个是elemrnts,前面那个才有send_key
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('verify_code').send_keys('8888')
driver.find_element_by_class_name('J-login-submit').click()
driver.refresh()
driver.back()

