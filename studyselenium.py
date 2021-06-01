from selenium import webdriver

driver = webdriver.Chrome(r'f:\chromedriver.exe')
driver.implicitly_wait(10)

driver.input('python')

ele = driver.find_element_by_id('kwdselected')

ele.send_keys('python')

ele = driver.find_element_by_id('work_position_input')

ele.click()

eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_0000 em[class=on]')

for ele in eles:
    ele.click()
#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_000000_080200').click()

#保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_element_by_css_selector('.ush    button').click()

#搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFields = [field.text for field in fields]
    print(' | '.join(stringFields))

#创建一个Excel workbook对象
book = xlwt.Workbook()

#增加一个sheet
sh = book.add_sheet('统计')

#写入内容
row = 0
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    col = 0
    for field in fields:
        text = field.text
        print(text,end='')
        sh.write(row,col,text)
        col += 1

    print('')
    row += 1

#保存文件
book.save('g:\\52job.xls')

driver.quit()