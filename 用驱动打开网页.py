from selenium import webdriver
drvier=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')#导入谷歌驱动
drvier.get(r'https:\\www.baidu.com')
elements_keyword=drvier.find_element_by_id('kw')
elements_keyword.send_keys('相亲')
elements_button=drvier.find_element_by_id('su')
elements_button.click()
import time
time.sleep(4)
ret=drvier.find_element_by_id('3001')
print(ret.text)
if ret.text.startswith('相亲'):
    print('测试通过！')
else:
    print('测试不通过！')

drvier.quit()

