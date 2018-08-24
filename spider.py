from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = r'/Applications/Google Chrome.app'
driver = webdriver.Chrome()


url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

csv_file = open('playlist.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '连接'])

while url != 'javascript:viod(0)':
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')
    for i in range(len(data)):
        nb = data[i].find_elements_by_class_name('nb').text
        if '万' in nb and  int(nb.split('万')[0]) > 500:
            msk = data[i].find_elements_by_css_selector('a.msk')
            writer.writerow([msk.__getattribute__('title'), nb, msk.__getattribute__('href')])
    url = driver.find_elements_by_css_selector('a.zbtn.znxt').__getattribute__('href')
csv_file.close()