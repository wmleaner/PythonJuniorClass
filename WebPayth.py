from selenium import webdriver  #从selenium工具导入webdriver库
import time
def login(username,password,vorified,driver):
    #登录   因为没必要现在就开会话，没有初始化driver所以要设置成参数
    time.sleep(10)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('vertify').send_keys(vorified)
    driver.find_element_by_name('submit').click()
def openurl(url,driver):#打开页面
    driver.get(url)
    driver.maximize_window()
def pduser(driver):
    login_user=driver.find_element_by_xpath("//dl[2]/dt[@class='name']").text  #获取登录用户名
    if login_user=='admin':
        print('这个登陆的用户是：{}'.format(login_user))
    else:
        print('本条测试用例不通过')
def change_syatm(driver):
    driver.find_element_by_xpath("//div/ul/li[@data-param='system']").click()  #找到系统选项
    driver.find_element_by_xpath("//dt/a/span[@class='ico-system-1']/..").click()#找到会员
    driver.switch_to.frame('workspace')#切换子页面
#输入搜索项，点击搜素
def search(vsearch,driver):
    driver.find_element_by_xpath("//input[@id='search_key']").send_keys(vsearch)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(20)
    search_nickename=driver.find_element_by_xpath("//td[3]/div").text
    '''搜索前会员列表得几个数据标签都一致，所以必须要等待搜索成功后再来判断'''
    if vsearch==search_nickename:
        print("成功搜索到用户昵称：{}".format(search_nickename))
    else:
        print('搜索框输入', vsearch)
        print("没有搜到数据")


