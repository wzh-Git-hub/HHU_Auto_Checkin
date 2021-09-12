import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import smtplib
from email.mime.text import MIMEText

UID = os.environ["USERNAME"]
PWD = os.environ["PASSWORD"]
RNDTM = os.environ["RANDOMTIME"]
MAIL_RECIVER = os.environ["RECIVERMAIL"]

def mail(rec):
    # ----------1.跟发件相关的参数------
    # smtpserver = "smtp.163.com"         # 发件服务器
    MAIL_SENDER = os.environ["SENDER"]  # 发件箱
    MAIL_PWD = os.environ["MAIL_PWD"]      # 发件箱授权码
#     MAIL_SENDER = MAIL_SENDER # 发件箱
#     MAIL_PWD = MAIL_PWD      # 发件箱授权码
    smtpserver = "smtp.qq.com"
    port = 465                   # 端口
    sender = MAIL_SENDER         # 发件人
    psw = MAIL_PWD               # 密码
    receiver = rec               # 接收人
    
    # ----------2.编辑邮件的内容------
    subject =  '成功打卡提醒'             #邮件主题
    body = '<p>今日已成功打卡</p>'     # 定义邮件正文为html格式
    msg = MIMEText(body, "html", "utf-8")
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject

    # ----------3.发送邮件------
    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)                                 # 连服务器
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)                                      # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()                                                        # 关闭

#出错处理
def is_element_present(browser, xpath):
    from selenium.common.exceptions import NoSuchElementException

    try:
        element = browser.find_element_by_xpath(xpath)
    except NoSuchElementException as e:
        print(e)
        return False
    else:
        return True

#登录打卡
def sign_in(uid, pwd):
    msg=""
    url=""
    img_list=list()
    a_list=list()
    # set to no-window
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    browser.get("http://ids.hhu.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fform.hhu.edu.cn%2Fpdc%2Fform%2Flist")
    # 打印当前页面title
    print(browser.title)

    try:
        # input uid and password
        print("Inputting the UID and Password of User {0}".format(uid))
        browser.find_element_by_id("IDToken1").send_keys(uid)
        browser.find_element_by_id("IDToken2").send_keys(pwd)
        # click to sign in
        #browser.find_element_by_xpath("/html/body/table[1]/tr[2]/td[1]/table[2]/tr[2]/td[2]/table[1]/tr[3]/td[1]/IMG[1]").click()
        img_list=browser.find_elements_by_tag_name("IMG")
        '''
        for li in img_list:
            print(li)
        '''
        img_list[4].click()
        time.sleep(3)
    
        #打印当前页面URL
        msg=browser.title
        url=browser.current_url
    
        print("Checking whether User {0} has signed in".format(uid))
        if msg == "防疫上报统计系统":
            print(msg)
            print(url)
            a_list=browser.find_elements_by_tag_name("a")
            a_list[0].click()
            time.sleep(2)
            msg=browser.title
            url=browser.current_url
            print(msg)
            print(url)
	    time.sleep(1)
            browser.find_element_by_id("saveBtn").click()
            msg=browser.title
            url=browser.current_url
            print(msg)
            print(url)
        else:
            print('fail to sign')
            return False

    except Exception as e:
        msg = "while signing in for user " + uid + " there is an exception: \n" + str(e)
        print(msg)
    finally:
        browser.quit()
        
    # quit the browser
    print("Singing in for User {0} is finished".format(uid))
    return True

#随机时间
def randomTime(seconds=3600):
    randomnumber = random.randint(0, seconds)
    counter = 0
    while counter < randomnumber:
        restTime = randomnumber - counter
        restMinutes = int(restTime / 60)
        restSeconds = restTime % 60
        if restTime < 300:
            if restTime < 60:
                print("倒计时: "+ str(restSeconds) + "秒")
            else:
                print("倒计时: " + str(restMinutes) + "分" + str(restSeconds) + "秒")
            time.sleep(restTime)
            counter += restTime
        else:
            print("倒计时: " + str(restMinutes) + "分" + str(restSeconds) + "秒")
            time.sleep(300)
            counter += 300

if __name__ == "__main__":
	#检查账号密码数量是否一致
    if not PWD or not UID:
        print("你还没有添加账户\n")
        exit(1)
    uid_list = UID.split()
    pwd_list = PWD.split()
    mail_list = MAIL_RECIVER.split()
    uid_length = len(uid_list)
    pwd_length = len(pwd_list)
    if uid_length!=pwd_length:
        print("账号和密码数量不一致\n");
        exit(1)
    #随机时间
#     if RNDTM:
#         randomTime(int(RNDTM)*60)
#     else:
#         randomTime(3600)
    #开始打卡
    for i in range(pwd_length):
        print("**************************************\n正在给第 "+str(i+1)+" 个账号打卡")
        flag=sign_in(uid_list[i], pwd_list[i])
        if flag:
            print("第 "+str(i+1)+" 个账号打卡成功!")
            mail(mail_list[i])
        else:
            print("第 "+str(i+1)+" 个账号打卡失败!\n正在发起第2次尝试")
            flag = sign_in(uid_list[i], pwd_list[i])
            if flag:
                print("第 2 次尝试成功!")
                mail(mail_list[i])
            else:
                print("第 2 次尝试失败!")
        print()
        time.sleep(30)
    print("本次任务执行完毕")
