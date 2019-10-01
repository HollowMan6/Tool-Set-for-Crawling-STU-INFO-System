# Spider-for-LZU-STU-INFO-System

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/)

Spider-for-LZU-STU-INFO-System(LZU教务管理信息系统爬虫)

**新**: 新增 将学生信息存入Sqlite数据库 [脚本](Store-LZU-STU-INFO-Into-Sqlite.py) 和 将研究生综合管理信息存入Sqlite数据库 [脚本](Store-LZU-GraduateSTU-INFO-Into-Sqlite.py) , 使用前请 ***确保Data文件夹下存放着所有经爬取过的html文件***，并且 ***电脑上已经安装了Sqlite3并且已经将Sqlite3添加到了系统Path变量中***。此仓库下已经包含了sqlite数据库文件[Student.db](Student.db), 其生成SQL语句见附录。

**新**: 新增 学生信息系统爬虫带UI版 [脚本](Spider-for-Student-Information-System-With-UI.py)

[Win程序:](Spider-for-Student-Information-System-With-UI.exe) 

![](Spider-for-Student-Information-System-With-UI.PNG) 

研究生综合管理信息系统爬虫带UI版 [脚本](Spider-for-Graduate-Student-Information-System-With-UI.py)

[Win程序:](Spider-for-Graduate-Student-Information-System-With-UI.exe) 

 ![](Spider-for-Graduate-Student-Information-System-With-UI.PNG)

**新**: 新增 [LZU研究生综合管理信息系统爬虫](http://gms.lzu.edu.cn/graduate/index.do) [脚本](Spider-for-LZU-GraduateSTU-INFO-System.py)

学生信息系统爬虫适用于 [LZU](http://jwk.lzu.edu.cn) , [QDU](http://jw.qdu.edu.cn/academic/common/security/login.jsp) , [CUC](http://jw.cuc.edu.cn/academic/common/security/login.jsp)等的同类教务系统（完美贴合优慕课在线教育教务系统）。

验证码采用Tesseract-OCR识别,其中LZU综合管理信息系统爬虫验证码识别准确率在2/3左右。

采用多线程编程，爬取速度获得了很大提升！

爬取结束后，你可以选用[数据去重脚本](De-duplication.py)去除因重复爬取而产生的重复数据。

UI版使用Tkinter

***Win UI版直接运行使用时请确保已经安装了Tesseract-OCR并且已经将Tesseract添加到了系统Path变量中。***

*运行Python脚本时还需要满足requirements.txt中的库要求*

**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***

**NEW**: add [Store-LZU-STU-INFO-Into-Sqlite](Store-LZU-STU-INFO-Into-Sqlite.py) and [Store-LZU-GraduateSTU-INFO-Into-Sqlite](Store-LZU-GraduateSTU-INFO-Into-Sqlite.py). Before using it, please ***ensure that all crawled HTML files are stored under the Data folder*** and ***the computer has already installed Sqlite3 and Sqlite3 has been added to the system Path variable***. The SQLite database file [Student.db](Student.db) has been included in the repository. The SQL statements generating Student.db are listed in the appendix.

**NEW**: Add Spider-for-Student-Information-System-With-UI [Script](Spider-for-Student-Information-System-With-UI.py) , [Windows Program](Spider-for-Student-Information-System-With-UI.exe) 

Spider-for-Graduate-Student-Information-System-With-UI [Script](Spider-for-Graduate-Student-Information-System-With-UI.py) , [Windows Program](Spider-for-Graduate-Student-Information-System-With-UI.exe) 

**NEW**: Add [Spider-for-LZU-GraduateSTU-INFO-System](http://gms.lzu.edu.cn/graduate/index.do) [Script](Spider-for-LZU-GraduateSTU-INFO-System.py).

Spider-for-Student-Information-Systemm It is suitable for STU-INFO systems such as [LZU](http://jwk.lzu.edu.cn) , [QDU](http://jw.qdu.edu.cn/academic/common/security/login.jsp) and [CUC](http://jw.cuc.edu.cn/academic/common/security/login.jsp). (Perfect fit for online educational administration system of 优慕课)

The Captcha is identified by Tesseract-OCR, Captcha recognition accuracy in Spider-for-LZU-GraduateSTU-INFO-System is about 2/3.

Using multithreading programming, the Spider's speed has been greatly improved!

After the crawl, you can choose [De-duplication Script](De-duplication.py) to remove duplicate data caused by repeated crawling.

UI Coded with Tkinter

***When you run Win UI version directly, make sure that Tesseract-OCR is installed and that Tesseract has been added to the system Path variable.***

*When running Python scripts, you also need to meet library requirements in requirements.txt*

**Warning**:

***For TESTING ONLY, not for any ILLIGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***

## 附录 Appendix

```SQL
CREATE TABLE [Postgraduate](
  [学号] CHAR(12) PRIMARY KEY ASC NOT NULL,
  [姓名] VARCHAR(32),
  [姓名拼音] VARCHAR(32),
  [性别] CHAR(1),
  [出生日期] DATE,
  [证件类型] VARCHAR(12),
  [证件号码] VARCHAR(24),
  [民族] VARCHAR(8),
  [政治面貌] VARCHAR(12),
  [录取类别] VARCHAR(8),
  [所在校区] VARCHAR(4),
  [年级] CHAR(5),
  [国籍] VARCHAR(16),
  [籍贯] VARCHAR(12),
  [入学日期] DATE,
  [学制] CHAR(2),
  [学生类别] VARCHAR(8),
  [培养层次] VARCHAR(8),
  [院系] VARCHAR(12),
  [一级学科] VARCHAR(12),
  [专业] VARCHAR(24),
  [考试方式] VARCHAR(8),
  [学习形式] VARCHAR(8),
  [导师姓名] VARCHAR(16),
  [副导师姓名] VARCHAR(16),
  [导师指导小组成员姓名] VARCHAR(24),
  [定向委培单位所在省] VARCHAR(16),
  [定向委培或在职单位] VARCHAR(24),
  [外语语种] VARCHAR(8),
  [专项计划] VARCHAR(8),
  [生源地] VARCHAR(16),
  [生源地码] INT,
  [是否有学籍] CHAR(1),
  [是否在校] CHAR(1),
  [毕业状态] VARCHAR(4),
  [毕业时间] VARCHAR(8),
  [毕业类型] VARCHAR(8),
  [乘车目的地] VARCHAR(16),
  [是否在职] CHAR(1),
  [异动信息] VARCHAR(50),
  [是否国防生] CHAR(1),
  [是否保留学籍] CHAR(1),
  [思想政治表现] VARCHAR(50),
  [在校联系电话] CHAR(11),
  [手机] VARCHAR(11),
  [电子邮箱] VARCHAR(32),
  [是否在校住宿] CHAR(1),
  [宿舍号码] VARCHAR(8),
  [宿舍电话] CHAR(11)
  [住宿地址] VARCHAR(50),
  [目前所在地] VARCHAR(50),
  [银行卡号] VARCHAR(24),
  [入学奖学金] VARCHAR(12),
  [婚姻状况] CHAR(2),
  [家庭联系电话] VARCHAR(16),
  [家庭通讯地址] VARCHAR(50),
  [家庭邮政编码] CHAR(6),
  [家庭主要成员] VARCHAR(64),
  [监护人1姓名] VARCHAR(16),
  [监护人1证件类型] VARCHAR(12),
  [监护人1证件号码] VARCHAR(24),
  [监护人2姓名] VARCHAR(16),
  [监护人2证件类型] VARCHAR(12),
  [监护人2证件号码] VARCHAR(24),
  [个人简历] VARCHAR(64),
  [准考证号] VARCHAR(24),
  [考生来源] VARCHAR(32),
  [入学前最后学历] VARCHAR(12),
  [入校前最后学位] VARCHAR(12),
  [入学前毕业时间] VARCHAR(12),
  [毕业学校] VARCHAR(16),
  [毕业专业名称] VARCHAR(16),
  [毕业专业代码] VARCHAR(8),
  [毕业证书编号] VARCHAR(24),
  [学位证书编号] VARCHAR(24),
  [最后工作单位] VARCHAR(16),
  [最后工作省市] VARCHAR(12),
  [报考前户口所在省份] VARCHAR(64),
  [离校方式] VARCHAR(8),
  [英语分级] VARCHAR(16),
  [转博分类] VARCHAR(8),
  [硕士阶段学号] VARCHAR(16),
  [备注] VARCHAR(64)
);

CREATE TABLE [Undergraduate](
  [学号] CHAR(12) PRIMARY KEY ASC NOT NULL,
  [姓名] VARCHAR(32),
  [姓名拼音] VARCHAR(32),
  [性别] CHAR(1),
  [出生日期] DATE,
  [国籍] VARCHAR(16),
  [籍贯] VARCHAR(12),
  [证件类型] VARCHAR(12),
  [证件号码] VARCHAR(24),
  [民族] VARCHAR(8),
  [政治面貌] VARCHAR(16),
  [是否本市户籍] CHAR(1),
  [婚姻状况] CHAR(2),
  [文化程度] CHAR(2),
  [外语语种] VARCHAR(8),
  [健康状况] VARCHAR(2),
  [学生来源] VARCHAR(4),
  [考区] VARCHAR(12),
  [高考总分] FLOAT,
  [入学准考证号] VARCHAR(16),
  [入学录取证号] CHAR(8),
  [中学名] VARCHAR(16),
  [入学年级] CHAR(5),
  [入学日期] DATE,
  [入学方式] VARCHAR(8),
  [培养方式] VARCHAR(8),
  [院系] VARCHAR(12),
  [专业] VARCHAR(24),
  [年级] CHAR(5),
  [学生类别] VARCHAR(12),
  [班级] VARCHAR(16),
  [校区] CHAR(4),
  [考生号] VARCHAR(16),
  [是否有学籍] CHAR(1),
  [是否在校] CHAR(1),
  [学习形式] VARCHAR(16),
  [学习方式] VARCHAR(8),
  [毕业去向] VARCHAR(8),
  [毕业日期] DATE,
  [电子邮箱] VARCHAR(32),
  [移动电话] CHAR(11),
  [联系电话] VARCHAR(14),
  [邮政编码] CHAR(6),
  [通讯地址] VARCHAR(50),
  [宿舍地址] VARCHAR(8),
  [家庭电话] VARCHAR(14),
  [家庭邮政编码] VARCHAR(6),
  [家庭住址] VARCHAR(50),
  [备注] VARCHAR(64),
  [家庭情况姓名1] VARCHAR(32),
  [家庭情况与本人关系1] VARCHAR(6),
  [家庭情况政治面貌1] VARCHAR(6),
  [家庭情况职业1] VARCHAR(16),
  [家庭情况职务1] VARCHAR(16),
  [家庭情况工作单位1] VARCHAR(16),
  [家庭情况联系电话1] VARCHAR(12),
  [家庭情况证件类型1] VARCHAR(8),
  [家庭情况证件号码1] VARCHAR(24),
  [家庭情况姓名2] VARCHAR(32),
  [家庭情况与本人关系2] VARCHAR(6),
  [家庭情况政治面貌2] VARCHAR(6),
  [家庭情况职业2] VARCHAR(16),
  [家庭情况职务2] VARCHAR(16),
  [家庭情况工作单位2] VARCHAR(16),
  [家庭情况联系电话2] VARCHAR(12),
  [家庭情况证件类型2] VARCHAR(8),
  [家庭情况证件号码2] VARCHAR(24),
  [家庭情况姓名3] VARCHAR(32),
  [家庭情况与本人关系3] VARCHAR(6),
  [家庭情况政治面貌3] VARCHAR(6),
  [家庭情况职业3] VARCHAR(16),
  [家庭情况职务3] VARCHAR(16),
  [家庭情况工作单位3] VARCHAR(16),
  [家庭情况联系电话3] VARCHAR(12),
  [家庭情况证件类型3] VARCHAR(8),
  [家庭情况证件号码3] VARCHAR(24),
  [异动类型1] VARCHAR(8),
  [异动日期1] DATE,
  [异动原因1] VARCHAR(8),
  [异动前班级1] VARCHAR(16),
  [异动后班级1] VARCHAR(16),
  [最后修改时间1] DATE,
  [审批日期1] DATE,
  [审批文号1] VARCHAR(16),
  [备注1] VARCHAR(32),
  [异动类型2] VARCHAR(8),
  [异动日期2] DATE,
  [异动原因2] VARCHAR(8),
  [异动前班级2] VARCHAR(16),
  [异动后班级2] VARCHAR(16),
  [最后修改时间2] DATE,
  [审批日期2] DATE,
  [审批文号2] VARCHAR(16),
  [备注2] VARCHAR(32),
  [异动类型3] VARCHAR(8),
  [异动日期3] DATE,
  [异动原因3] VARCHAR(8),
  [异动前班级3] VARCHAR(16),
  [异动后班级3] VARCHAR(16),
  [最后修改时间3] DATE,
  [审批日期3] DATE,
  [审批文号3] VARCHAR(16),
  [备注3] VARCHAR(32)
);
```
