# 1. 访问天气查询网站（网址如下），查询江苏省天气
# http://www.weather.com.cn/html/province/jiangsu.shtml
#
# 2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
# 温度最低为12℃, 城市有连云港 盐城
from selenium import webdriver
drvier=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
drvier.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
element_text=drvier.find_element_by_id('forecastID')
list=element_text.text.split('℃\n')
dict={}
list1=[]
for i in range(0,len(list)):
    city = list[i].split('\n')[0]
    if '℃' not in list[i]:
        weather = int(list[i].split('\n')[1].split('/')[-1])
    else:
        weather = int(list[i].split('\n')[1].split('/')[-1].split('℃')[0])
        dict[city] = weather
for key, value in dict.items():
    if value == min(dict.values()):
        list1.append(key)

print(element_text.text)
print(f'温度最低为{min(dict.values())}℃,城市有{" ".join(list1)}')
input()
drvier.quit()




