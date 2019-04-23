# Spider-for-LZU-STU-INFO-System

Spider-for-LZU-STU-INFO-System(LZU教务管理信息系统爬虫)

**新**: 新增 [LZU综合管理信息系统爬虫](http://gms.lzu.edu.cn/graduate/index.do) [脚本](Spider-for-LZU-GraduateSTU-INFO-System.py)

**新**: 新增 学生信息系统爬虫带UI版 [脚本](Spider-for-Student-Information-System-With-UI.py). ![](Spider-for-Student-Information-System-With-UI.PNG) 

研究生综合管理信息系统爬虫带UI版 [脚本](Spider-for-Graduate-Student-Information-System-With-UI.py). ![](Spider-for-Graduate-Student-Information-System-With-UI.PNG)

适用于 [LZU](http://jwk.lzu.edu.cn) , [QDU](http://jw.qdu.edu.cn/academic/common/security/login.jsp) , [CUC](http://jw.cuc.edu.cn/academic/common/security/login.jsp)等同类教务系统。

验证码采用Tesseract-OCR识别,其中LZU综合管理信息系统爬虫验证码识别准确率在2/3左右。

采用多线程编程，爬取速度获得了很大提升！

爬取结束后，你可以选用[数据去重脚本](De-duplication.py)去除因重复爬取而产生的重复数据。

UI版使用Tkinter


**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***

**NEW**: Add [Spider-for-LZU-GraduateSTU-INFO-System](http://gms.lzu.edu.cn/graduate/index.do) [Script](Spider-for-LZU-GraduateSTU-INFO-System.py)

**NEW**: Add Spider-for-Student-Information-System-With-UI [Script](Spider-for-Student-Information-System-With-UI.py),Spider-for-Graduate-Student-Information-System-With-UI [Script](Spider-for-Graduate-Student-Information-System-With-UI.py)

It is suitable for STU-INFO systems such as [LZU](http://jwk.lzu.edu.cn) , [QDU](http://jw.qdu.edu.cn/academic/common/security/login.jsp) and [CUC](http://jw.cuc.edu.cn/academic/common/security/login.jsp).

The Captcha is identified by Tesseract-OCR, Captcha recognition accuracy in Spider-for-LZU-GraduateSTU-INFO-System is about 2/3.

Using multithreading programming, the Spider's speed has been greatly improved!

After the crawl, you can choose [De-duplication Script](De-duplication.py) to remove duplicate data caused by repeated crawling.

UI Coded with Tkinter

**Warning**:

***For TESTING ONLY, not for any ILLIGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***