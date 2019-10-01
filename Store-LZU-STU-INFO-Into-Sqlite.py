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
# 导入html解析库 Import HTML parsing library
from lxml import etree
import os
# 导入sqlite3库（请确保电脑已安装sqlite3并且已经加入到path变量中）
# Import the sqlite3 Library (please ensure that the computer has installed sqlite3 and has been added to the path variable).
import sqlite3

# 连接数据库 Connect to the database
conn = sqlite3.connect('Student.db')
target_path = "./data"
for base_path, folder_list, file_list in os.walk(target_path):
    for file_name in file_list:
        file_path = os.path.join(base_path, file_name)
        file_ext = file_path.rsplit('.', maxsplit=1)
        if len(file_ext) != 2:
            # 没有后缀名 No suffix name
            continue
        if file_ext[1] != 'html':
            # 不是html文件 Not an HTML file
            continue
        with open(file_path, encoding='utf-8') as f:
            html = f.read()
            tree = etree.HTML(html)
            # 解析html中数据 Parsing data in HTML
            学号 = tree.xpath(
                "/html/body/center/form/table[1]/tr[1]/td[1]/text()")
            if 学号:
                学号 = str(学号[0])
            else:
                学号 = ""
            姓名 = tree.xpath(
                "/html/body/center/form/table[1]/tr[2]/td[1]/text()")
            if 姓名:
                姓名 = str(姓名[0])
            else:
                姓名 = ""
            姓名拼音 = tree.xpath(
                "/html/body/center/form/table[1]/tr[2]/td[2]/text()")
            if 姓名拼音:
                姓名拼音 = str(姓名拼音[0])
            else:
                姓名拼音 = ""
            性别 = tree.xpath(
                "/html/body/center/form/table[1]/tr[3]/td[2]/text()")
            if 性别:
                性别 = str(性别[0])
            else:
                性别 = ""
            出生日期 = tree.xpath(
                "/html/body/center/form/table[1]/tr[4]/td[1]/text()")
            if 出生日期:
                出生日期 = str(出生日期[0])
            else:
                出生日期 = ""
            国籍 = tree.xpath(
                "/html/body/center/form/table[1]/tr[5]/td[1]/text()")
            if 国籍:
                国籍 = str(国籍[0])
            else:
                国籍 = ""
            籍贯 = tree.xpath(
                "/html/body/center/form/table[1]/tr[5]/td[2]/text()")
            if 籍贯:
                籍贯 = str(籍贯[0])
            else:
                籍贯 = ""
            证件类型 = tree.xpath(
                "/html/body/center/form/table[1]/tr[6]/td[1]/text()")
            if 证件类型:
                证件类型 = str(证件类型[0])
            else:
                证件类型 = ""
            证件号码 = tree.xpath(
                "/html/body/center/form/table[1]/tr[6]/td[2]/text()")
            if 证件号码:
                证件号码 = str(证件号码[0])
            else:
                证件号码 = ""
            民族 = tree.xpath(
                "/html/body/center/form/table[1]/tr[7]/td[1]/text()")
            if 民族:
                民族 = str(民族[0])
            else:
                民族 = ""
            政治面貌 = tree.xpath(
                "/html/body/center/form/table[1]/tr[7]/td[2]/text()")
            if 政治面貌:
                政治面貌 = str(政治面貌[0])
            else:
                政治面貌 = ""
            是否本市户籍 = tree.xpath(
                "/html/body/center/form/table[1]/tr[8]/td[1]/text()")
            if 是否本市户籍:
                是否本市户籍 = str(是否本市户籍[0])
            else:
                是否本市户籍 = ""
            婚姻状况 = tree.xpath(
                "/html/body/center/form/table[1]/tr[9]/td[1]/text()")
            if 婚姻状况:
                婚姻状况 = str(婚姻状况[0])
            else:
                婚姻状况 = ""
            文化程度 = tree.xpath(
                "/html/body/center/form/table[1]/tr[9]/td[2]/text()")
            if 文化程度:
                文化程度 = str(文化程度[0])
            else:
                文化程度 = ""
            外语语种 = tree.xpath(
                "/html/body/center/form/table[1]/tr[10]/td[1]/text()")
            if 外语语种:
                外语语种 = str(外语语种[0])
            else:
                外语语种 = ""
            健康状况 = tree.xpath(
                "/html/body/center/form/table[1]/tr[11]/td[1]/text()")
            if 健康状况:
                健康状况 = str(健康状况[0])
            else:
                健康状况 = ""
            学生来源 = tree.xpath(
                "/html/body/center/form/table[1]/tr[11]/td[2]/text()")
            if 学生来源:
                学生来源 = str(学生来源[0])
            else:
                学生来源 = ""
            考区 = tree.xpath(
                "/html/body/center/form/table[1]/tr[12]/td[1]/text()")
            if 考区:
                考区 = str(考区[0])
            else:
                考区 = ""
            高考总分 = tree.xpath(
                "/html/body/center/form/table[1]/tr[15]/td[1]/text()")
            if 高考总分:
                高考总分 = str(高考总分[0])
            else:
                高考总分 = ""
            入学准考证号 = tree.xpath(
                "/html/body/center/form/table[1]/tr[15]/td[2]/text()")
            if 入学准考证号:
                入学准考证号 = str(入学准考证号[0])
            else:
                入学准考证号 = ""
            入学录取证号 = tree.xpath(
                "/html/body/center/form/table[1]/tr[16]/td[1]/text()")
            if 入学录取证号:
                入学录取证号 = str(入学录取证号[0])
            else:
                入学录取证号 = ""
            中学名 = tree.xpath(
                "/html/body/center/form/table[1]/tr[16]/td[2]/text()")
            if 中学名:
                中学名 = str(中学名[0])
            else:
                中学名 = ""
            入学年级 = tree.xpath(
                "/html/body/center/form/table[1]/tr[18]/td[2]/text()")
            if 入学年级:
                入学年级 = str(入学年级[0])
            else:
                入学年级 = ""
            入学日期 = tree.xpath(
                "/html/body/center/form/table[1]/tr[19]/td[1]/text()")
            if 入学日期:
                入学日期 = str(入学日期[0])
            else:
                入学日期 = ""
            入学方式 = tree.xpath(
                "/html/body/center/form/table[1]/tr[19]/td[2]/text()")
            if 入学方式:
                入学方式 = str(入学方式[0])
            else:
                入学方式 = ""
            培养方式 = tree.xpath(
                "/html/body/center/form/table[1]/tr[20]/td[1]/text()")
            if 培养方式:
                培养方式 = str(培养方式[0])
            else:
                培养方式 = ""
            院系 = tree.xpath(
                "/html/body/center/form/table[1]/tr[21]/td[1]/text()")
            if 院系:
                院系 = str(院系[0])
            else:
                院系 = ""
            专业 = tree.xpath(
                "/html/body/center/form/table[1]/tr[21]/td[2]/div/text()")
            if 专业:
                专业 = str(专业[0])
            else:
                专业 = ""
            年级 = tree.xpath(
                "/html/body/center/form/table[1]/tr[22]/td[1]/div/text()")
            if 年级:
                年级 = str(年级[0])
            else:
                年级 = ""
            学生类别 = tree.xpath(
                "/html/body/center/form/table[1]/tr[22]/td[2]/div/text()")
            if 学生类别:
                学生类别 = str(学生类别[0])
            else:
                学生类别 = ""
            班级 = tree.xpath(
                "/html/body/center/form/table[1]/tr[23]/td[1]/div/text()")
            if 班级:
                班级 = str(班级[0])
            else:
                班级 = ""
            校区 = tree.xpath(
                "/html/body/center/form/table[1]/tr[24]/td[1]/div/text()")
            if 校区:
                校区 = str(校区[0])
            else:
                校区 = ""
            考生号 = tree.xpath(
                "/html/body/center/form/table[1]/tr[24]/td[2]/text()")
            if 考生号:
                考生号 = str(考生号[0])
            else:
                考生号 = ""
            是否有学籍 = tree.xpath(
                "/html/body/center/form/table[1]/tr[25]/td[1]/text()")
            if 是否有学籍:
                是否有学籍 = str(是否有学籍[0])
            else:
                是否有学籍 = ""
            是否在校 = tree.xpath(
                "/html/body/center/form/table[1]/tr[25]/td[2]/text()")
            if 是否在校:
                是否在校 = str(是否在校[0])
            else:
                是否在校 = ""
            学习形式 = tree.xpath(
                "/html/body/center/form/table[1]/tr[28]/td[1]/text()")
            if 学习形式:
                学习形式 = str(学习形式[0])
            else:
                学习形式 = ""
            学习方式 = tree.xpath(
                "/html/body/center/form/table[1]/tr[28]/td[2]/text()")
            if 学习方式:
                学习方式 = str(学习方式[0])
            else:
                学习方式 = ""
            毕业去向 = tree.xpath(
                "/html/body/center/form/table[1]/tr[29]/td[2]/text()")
            if 毕业去向:
                毕业去向 = str(毕业去向[0])
            else:
                毕业去向 = ""
            毕业日期 = tree.xpath(
                "/html/body/center/form/table[1]/tr[30]/td[2]/text()")
            if 毕业日期:
                毕业日期 = str(毕业日期[0])
            else:
                毕业日期 = ""
            电子邮箱 = tree.xpath(
                "/html/body/center/form/table[1]/tr[34]/td[1]/text()")
            if 电子邮箱:
                电子邮箱 = str(电子邮箱[0])
            else:
                电子邮箱 = ""
            移动电话 = tree.xpath(
                "/html/body/center/form/table[1]/tr[34]/td[2]/text()")
            if 移动电话:
                移动电话 = str(移动电话[0])
            else:
                移动电话 = ""
            联系电话 = tree.xpath(
                "/html/body/center/form/table[2]/tr[1]/td[1]/text()")
            if 联系电话:
                联系电话 = str(联系电话[0])
            else:
                联系电话 = ""
            邮政编码 = tree.xpath(
                "/html/body/center/form/table[2]/tr[1]/td[2]/text()")
            if 邮政编码:
                邮政编码 = str(邮政编码[0])
            else:
                邮政编码 = ""
            通讯地址 = tree.xpath(
                "/html/body/center/form/table[2]/tr[1]/td[3]/text()")
            if 通讯地址:
                通讯地址 = str(通讯地址[0])
            else:
                通讯地址 = ""
            宿舍地址 = tree.xpath(
                "/html/body/center/form/table[2]/tr[3]/td[3]/text()")
            if 宿舍地址:
                宿舍地址 = str(宿舍地址[0])
            else:
                宿舍地址 = ""
            家庭电话 = tree.xpath(
                "/html/body/center/form/table[2]/tr[4]/td[1]/text()")
            if 家庭电话:
                家庭电话 = str(家庭电话[0])
            else:
                家庭电话 = ""
            家庭邮政编码 = tree.xpath(
                "/html/body/center/form/table[2]/tr[4]/td[2]/text()")
            if 家庭邮政编码:
                家庭邮政编码 = str(家庭邮政编码[0])
            else:
                家庭邮政编码 = ""
            家庭住址 = tree.xpath(
                "/html/body/center/form/table[2]/tr[4]/td[3]/text()")
            if 家庭住址:
                家庭住址 = str(家庭住址[0])
            else:
                家庭住址 = ""
            备注 = tree.xpath("/html/body/center/form/table[3]/tr/td/text()")
            if 备注:
                备注 = str(备注[0])
            else:
                备注 = ""
            家庭情况姓名1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[1]/text()")
            if 家庭情况姓名1:
                家庭情况姓名1 = str(家庭情况姓名1[0])
            else:
                家庭情况姓名1 = ""
            家庭情况与本人关系1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[2]/text()")
            if 家庭情况与本人关系1:
                家庭情况与本人关系1 = str(家庭情况与本人关系1[0])
            else:
                家庭情况与本人关系1 = ""
            家庭情况政治面貌1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[3]/text()")
            if 家庭情况政治面貌1:
                家庭情况政治面貌1 = str(家庭情况政治面貌1[0])
            else:
                家庭情况政治面貌1 = ""
            家庭情况职业1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[4]/text()")
            if 家庭情况职业1:
                家庭情况职业1 = str(家庭情况职业1[0])
            else:
                家庭情况职业1 = ""
            家庭情况职务1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[5]/text()")
            if 家庭情况职务1:
                家庭情况职务1 = str(家庭情况职务1[0])
            else:
                家庭情况职务1 = ""
            家庭情况工作单位1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[6]/text()")
            if 家庭情况工作单位1:
                家庭情况工作单位1 = str(家庭情况工作单位1[0])
            else:
                家庭情况工作单位1 = ""
            家庭情况联系电话1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[7]/text()")
            if 家庭情况联系电话1:
                家庭情况联系电话1 = str(家庭情况联系电话1[0])
            else:
                家庭情况联系电话1 = ""
            家庭情况证件类型1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[8]/text()")
            if 家庭情况证件类型1:
                家庭情况证件类型1 = str(家庭情况证件类型1[0])
            else:
                家庭情况证件类型1 = ""
            家庭情况证件号码1 = tree.xpath(
                "/html/body/center/form/table[4]/tr[2]/td[9]/text()")
            if 家庭情况证件号码1:
                家庭情况证件号码1 = str(家庭情况证件号码1[0])
            else:
                家庭情况证件号码1 = ""
            家庭情况姓名2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[1]/text()")
            if 家庭情况姓名2:
                家庭情况姓名2 = str(家庭情况姓名2[0])
            else:
                家庭情况姓名2 = ""
            家庭情况与本人关系2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[2]/text()")
            if 家庭情况与本人关系2:
                家庭情况与本人关系2 = str(家庭情况与本人关系2[0])
            else:
                家庭情况与本人关系2 = ""
            家庭情况政治面貌2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[3]/text()")
            if 家庭情况政治面貌2:
                家庭情况政治面貌2 = str(家庭情况政治面貌2[0])
            else:
                家庭情况政治面貌2 = ""
            家庭情况职业2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[4]/text()")
            if 家庭情况职业2:
                家庭情况职业2 = str(家庭情况职业2[0])
            else:
                家庭情况职业2 = ""
            家庭情况职务2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[5]/text()")
            if 家庭情况职务2:
                家庭情况职务2 = str(家庭情况职务2[0])
            else:
                家庭情况职务2 = ""
            家庭情况工作单位2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[6]/text()")
            if 家庭情况工作单位2:
                家庭情况工作单位2 = str(家庭情况工作单位2[0])
            else:
                家庭情况工作单位2 = ""
            家庭情况联系电话2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[7]/text()")
            if 家庭情况联系电话2:
                家庭情况联系电话2 = str(家庭情况联系电话2[0])
            else:
                家庭情况联系电话2 = ""
            家庭情况证件类型2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[8]/text()")
            if 家庭情况证件类型2:
                家庭情况证件类型2 = str(家庭情况证件类型2[0])
            else:
                家庭情况证件类型2 = ""
            家庭情况证件号码2 = tree.xpath(
                "/html/body/center/form/table[4]/tr[3]/td[9]/text()")
            if 家庭情况证件号码2:
                家庭情况证件号码2 = str(家庭情况证件号码2[0])
            else:
                家庭情况证件号码2 = ""
            家庭情况姓名3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[1]/text()")
            if 家庭情况姓名3:
                家庭情况姓名3 = str(家庭情况姓名3[0])
            else:
                家庭情况姓名3 = ""
            家庭情况与本人关系3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[2]/text()")
            if 家庭情况与本人关系3:
                家庭情况与本人关系3 = str(家庭情况与本人关系3[0])
            else:
                家庭情况与本人关系3 = ""
            家庭情况政治面貌3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[3]/text()")
            if 家庭情况政治面貌3:
                家庭情况政治面貌3 = str(家庭情况政治面貌3[0])
            else:
                家庭情况政治面貌3 = ""
            家庭情况职业3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[4]/text()")
            if 家庭情况职业3:
                家庭情况职业3 = str(家庭情况职业3[0])
            else:
                家庭情况职业3 = ""
            家庭情况职务3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[5]/text()")
            if 家庭情况职务3:
                家庭情况职务3 = str(家庭情况职务3[0])
            else:
                家庭情况职务3 = ""
            家庭情况工作单位3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[6]/text()")
            if 家庭情况工作单位3:
                家庭情况工作单位3 = str(家庭情况工作单位3[0])
            else:
                家庭情况工作单位3 = ""
            家庭情况联系电话3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[7]/text()")
            if 家庭情况联系电话3:
                家庭情况联系电话3 = str(家庭情况联系电话3[0])
            else:
                家庭情况联系电话3 = ""
            家庭情况证件类型3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[8]/text()")
            if 家庭情况证件类型3:
                家庭情况证件类型3 = str(家庭情况证件类型3[0])
            else:
                家庭情况证件类型3 = ""
            家庭情况证件号码3 = tree.xpath(
                "/html/body/center/form/table[4]/tr[4]/td[9]/text()")
            if 家庭情况证件号码3:
                家庭情况证件号码3 = str(家庭情况证件号码3[0])
            else:
                家庭情况证件号码3 = ""
            异动类型1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[1]/text()")
            if 异动类型1:
                异动类型1 = str(异动类型1[0])
            else:
                异动类型1 = ""
            异动日期1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[2]/text()")
            if 异动日期1:
                异动日期1 = str(异动日期1[0])
            else:
                异动日期1 = ""
            异动原因1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[3]/text()")
            if 异动原因1:
                异动原因1 = str(异动原因1[0])
            else:
                异动原因1 = ""
            异动前班级1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[4]/text()")
            if 异动前班级1:
                异动前班级1 = str(异动前班级1[0])
            else:
                异动前班级1 = ""
            异动后班级1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[5]/text()")
            if 异动后班级1:
                异动后班级1 = str(异动后班级1[0])
            else:
                异动后班级1 = ""
            最后修改时间1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[6]/text()")
            if 最后修改时间1:
                最后修改时间1 = str(最后修改时间1[0])
            else:
                最后修改时间1 = ""
            审批日期1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[7]/text()")
            if 审批日期1:
                审批日期1 = str(审批日期1[0])
            else:
                审批日期1 = ""
            审批文号1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[8]/text()")
            if 审批文号1:
                审批文号1 = str(审批文号1[0])
            else:
                审批文号1 = ""
            备注1 = tree.xpath(
                "/html/body/center/form/table[5]/tr[2]/td[9]/text()")
            if 备注1:
                备注1 = str(备注1[0])
            else:
                备注1 = ""
            异动类型2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[1]/text()")
            if 异动类型2:
                异动类型2 = str(异动类型2[0])
            else:
                异动类型2 = ""
            异动日期2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[2]/text()")
            if 异动日期2:
                异动日期2 = str(异动日期2[0])
            else:
                异动日期2 = ""
            异动原因2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[3]/text()")
            if 异动原因2:
                异动原因2 = str(异动原因2[0])
            else:
                异动原因2 = ""
            异动前班级2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[4]/text()")
            if 异动前班级2:
                异动前班级2 = str(异动前班级2[0])
            else:
                异动前班级2 = ""
            异动后班级2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[5]/text()")
            if 异动后班级2:
                异动后班级2 = str(异动后班级2[0])
            else:
                异动后班级2 = ""
            最后修改时间2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[6]/text()")
            if 最后修改时间2:
                最后修改时间2 = str(最后修改时间2[0])
            else:
                最后修改时间2 = ""
            审批日期2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[7]/text()")
            if 审批日期2:
                审批日期2 = str(审批日期2[0])
            else:
                审批日期2 = ""
            审批文号2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[8]/text()")
            if 审批文号2:
                审批文号2 = str(审批文号2[0])
            else:
                审批文号2 = ""
            备注2 = tree.xpath(
                "/html/body/center/form/table[5]/tr[3]/td[9]/text()")
            if 备注2:
                备注2 = str(备注2[0])
            else:
                备注2 = ""
            异动类型3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[1]/text()")
            if 异动类型3:
                异动类型3 = str(异动类型3[0])
            else:
                异动类型3 = ""
            异动日期3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[2]/text()")
            if 异动日期3:
                异动日期3 = str(异动日期3[0])
            else:
                异动日期3 = ""
            异动原因3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[3]/text()")
            if 异动原因3:
                异动原因3 = str(异动原因3[0])
            else:
                异动原因3 = ""
            异动前班级3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[4]/text()")
            if 异动前班级3:
                异动前班级3 = str(异动前班级3[0])
            else:
                异动前班级3 = ""
            异动后班级3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[5]/text()")
            if 异动后班级3:
                异动后班级3 = str(异动后班级3[0])
            else:
                异动后班级3 = ""
            最后修改时间3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[6]/text()")
            if 最后修改时间3:
                最后修改时间3 = str(最后修改时间3[0])
            else:
                最后修改时间3 = ""
            审批日期3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[7]/text()")
            if 审批日期3:
                审批日期3 = str(审批日期3[0])
            else:
                审批日期3 = ""
            审批文号3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[8]/text()")
            if 审批文号3:
                审批文号3 = str(审批文号3[0])
            else:
                审批文号3 = ""
            备注3 = tree.xpath(
                "/html/body/center/form/table[5]/tr[4]/td[9]/text()")
            if 备注3:
                备注3 = str(备注3[0])
            else:
                备注3 = ""
            # 执行sql语句，写入数据库 Execute SQL statement and write to database
            insertSql = 'insert into Undergraduate(学号,姓名,姓名拼音,性别,出生日期,国籍,籍贯,证件类型,证件号码,民族,政治面貌,是否本市户籍,婚姻状况,文化程度,外语语种,健康状况,学生来源,考区,高考总分,入学准考证号,入学录取证号,中学名,入学年级,入学日期,入学方式,培养方式,院系,专业,年级,学生类别,班级,校区,考生号,是否有学籍,是否在校,学习形式,学习方式,毕业去向,毕业日期,电子邮箱,移动电话,联系电话,邮政编码,通讯地址,宿舍地址,家庭电话,家庭邮政编码,家庭住址,备注,家庭情况姓名1,家庭情况与本人关系1,家庭情况政治面貌1,家庭情况职业1,家庭情况职务1,家庭情况工作单位1,家庭情况联系电话1,家庭情况证件类型1,家庭情况证件号码1,家庭情况姓名2,家庭情况与本人关系2,家庭情况政治面貌2,家庭情况职业2,家庭情况职务2,家庭情况工作单位2,家庭情况联系电话2,家庭情况证件类型2,家庭情况证件号码2,家庭情况姓名3,家庭情况与本人关系3,家庭情况政治面貌3,家庭情况职业3,家庭情况职务3,家庭情况工作单位3,家庭情况联系电话3,家庭情况证件类型3,家庭情况证件号码3,异动类型1,异动日期1,异动原因1,异动前班级1,异动后班级1,最后修改时间1,审批日期1,审批文号1,备注1,异动类型2,异动日期2,异动原因2,异动前班级2,异动后班级2,最后修改时间2,审批日期2,审批文号2,备注2,异动类型3,异动日期3,异动原因3,异动前班级3,异动后班级3,最后修改时间3,审批日期3,审批文号3,备注3) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            conn.execute(insertSql, (学号, 姓名, 姓名拼音, 性别, 出生日期, 国籍, 籍贯, 证件类型, 证件号码, 民族, 政治面貌, 是否本市户籍, 婚姻状况, 文化程度, 外语语种, 健康状况, 学生来源, 考区, 高考总分, 入学准考证号, 入学录取证号, 中学名, 入学年级, 入学日期, 入学方式, 培养方式, 院系, 专业, 年级, 学生类别, 班级, 校区, 考生号, 是否有学籍, 是否在校, 学习形式, 学习方式, 毕业去向, 毕业日期, 电子邮箱, 移动电话, 联系电话, 邮政编码, 通讯地址, 宿舍地址, 家庭电话, 家庭邮政编码, 家庭住址, 备注, 家庭情况姓名1, 家庭情况与本人关系1, 家庭情况政治面貌1, 家庭情况职业1, 家庭情况职务1, 家庭情况工作单位1, 家庭情况联系电话1, 家庭情况证件类型1, 家庭情况证件号码1,
                                     家庭情况姓名2, 家庭情况与本人关系2, 家庭情况政治面貌2, 家庭情况职业2, 家庭情况职务2, 家庭情况工作单位2, 家庭情况联系电话2, 家庭情况证件类型2, 家庭情况证件号码2, 家庭情况姓名3, 家庭情况与本人关系3, 家庭情况政治面貌3, 家庭情况职业3, 家庭情况职务3, 家庭情况工作单位3, 家庭情况联系电话3, 家庭情况证件类型3, 家庭情况证件号码3, 异动类型1, 异动日期1, 异动原因1, 异动前班级1, 异动后班级1, 最后修改时间1, 审批日期1, 审批文号1, 备注1, 异动类型2, 异动日期2, 异动原因2, 异动前班级2, 异动后班级2, 最后修改时间2, 审批日期2, 审批文号2, 备注2, 异动类型3, 异动日期3, 异动原因3, 异动前班级3, 异动后班级3, 最后修改时间3, 审批日期3, 审批文号3, 备注3))
            conn.commit()
            # succeed in adding into the sqlite database
            print(file_name+"成功添加进数据库！")
