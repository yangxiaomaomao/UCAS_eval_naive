from selenium import webdriver

#用户名，一般为邮箱
name = ""
#密码
pwd = ""
#课程总数
class_num = 9
#老师总数
teacher_num = 21
#你是否评价过，评价过选True，没有则选False
hasFinish = True


#open browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://onestop.ucas.ac.cn")

#login
driver.find_element_by_id("menhuusername").send_keys(name)
driver.find_element_by_id("menhupassword").send_keys(pwd)
driver.find_element_by_class_name("loginbtn").click()

#wait to load
while driver.current_url[0:21] != "http://sep.ucas.ac.cn":
    print(driver.current_url[0:21])
    continue

#enter XKXT
driver.find_element_by_css_selector(r"div#main-metro>ul>li.app-black.m-black-col3>a[title=选课系统]>h5").click()

#process alert
if not hasFinish:
    driver.switch_to_alert().accept()

#eval view
driver.find_element_by_css_selector("#sidebar > ul > li:nth-child(4) > a > span:nth-child(2)").click()
driver.find_element_by_css_selector("#sidebar > ul > li.bsm-item.open > ul > li > a").click()

#initial location of all teachers
big_loc = 100

#start to eval class
for item in range(1,class_num + 1):
    #initial location of this teacher
    loc = 100

    #choose this class
    driver.find_element_by_css_selector("#main-content > div > div.m-cbox.m-lgray > div.mc-body > table > tbody > tr:nth-child(%d) > td:nth-child(8) > a"%item).click()
    
    #comment list
    comment_list = ["老师幽默风趣，讲解知识生动形象。",
                    "增加课堂测验，提高同学们的积极性。",
                    "我平均每周在这门课程上花费3小时。",
                    "很感兴趣，所以选了这门课来扩展自己的知识面。",
                    "比较高，课上积极回答老师提出的问题。"]
    #dot choice
    for i in [2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,24,25,26,27]:
        driver.find_element_by_css_selector("#regfrm > table > tbody > tr:nth-child(%d) > td:nth-child(3) > input"%i).click()
        js="var q=document.documentElement.scrollTop=%d"%loc  
        driver.execute_script(js)
        loc = loc + 40

    #long jump
    loc = loc + 120

    #comment
    for i in range(243,248):
        sel = "#item_" + str(i)
        driver.find_element_by_css_selector(sel).clear()
        driver.find_element_by_css_selector(sel).send_keys(comment_list[i - 243])     
        js="var q=document.documentElement.scrollTop=%d"%loc  
        driver.execute_script(js)
        loc = loc + 120
    
    #long jump
    loc = loc + 400
    js="var q=document.documentElement.scrollTop=%d"%loc  
    driver.execute_script(js)

    #single or double, choices(55,56,57)
    for i in [49,56,57]:
        driver.find_element_by_css_selector("#\\32 %d"%i).click()

    #save
    driver.find_element_by_css_selector("#sb1").click()

    #confirm to submit
    driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button:nth-child(2)").click()
    
    #next class
    big_loc = big_loc + 40
    js="var q=document.documentElement.scrollTop=%d"%big_loc  
    driver.execute_script(js)
print("Finish class eval")
#go to top
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)


#switch to eval teachers
driver.find_element_by_css_selector("#main-content > div > div:nth-child(2) > ul > li:nth-child(2) > a").click()

#initial location of all teachers
big_loc = 100

#every teacher
for i in range(1,teacher_num + 1):
    #initial location of this teacher
    loc = 0

    #choose this teacher
    driver.find_element_by_css_selector("#main-content > div > div.m-cbox.m-lgray > div.mc-body > table > tbody > tr:nth-child(%d) > td:nth-child(8) > a"%i).click()
    
    #dot choice
    for i in [2,3,5,6,8,9,10,11,12,13,15,16,17,18,19,20,22,23,24,25,26]:
        driver.find_element_by_css_selector("#regfrm > table > tbody > tr:nth-child(%d) > td:nth-child(3) > input"%i).click()
        js="var q=document.documentElement.scrollTop=%d"%loc  
        driver.execute_script(js)
        loc = loc + 50

    #long jump
    loc = loc + 200
    js="var q=document.documentElement.scrollTop=%d"%loc  
    driver.execute_script(js)

    #comment
    driver.find_element_by_css_selector("#item_291").clear()
    driver.find_element_by_css_selector("#item_291").send_keys("幽默风趣，详细认真，善于调用班级氛围")
    driver.find_element_by_css_selector("#item_292").clear()
    driver.find_element_by_css_selector("#item_292").send_keys("希望可以更加多的提问，多布置小组作业")

    #save
    driver.find_element_by_css_selector("#sb1").click()

    #confirm submit
    driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button:nth-child(2)").click()

    #next teacher
    big_loc = big_loc + 55
    js="var q=document.documentElement.scrollTop=%d"%big_loc  
    driver.execute_script(js)

print("Finish all")