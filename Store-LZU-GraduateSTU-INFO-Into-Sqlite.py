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
            学号 = tree.xpath("/html/body/div/div[3]/table[1]/tr[1]/td[1]/text()")
            if 学号:
                学号 = str(学号[0]).replace(" ","").replace("\n","")
            else:
                学号 = ""
            姓名 = tree.xpath("/html/body/div/div[3]/table[1]/tr[2]/td/text()")
            if 姓名:
                姓名 = str(姓名[0])
            else:
                姓名 = ""
            姓名拼音 = tree.xpath("/html/body/div/div[3]/table[1]/tr[3]/td/text()")
            if 姓名拼音:
                姓名拼音 = str(姓名拼音[0])
            else:
                姓名拼音 = ""
            性别 = tree.xpath("/html/body/div/div[3]/table[1]/tr[4]/td/text()")
            if 性别:
                性别 = str(性别[0])
            else:
                性别 = ""
            出生日期 = tree.xpath("/html/body/div/div[3]/table[1]/tr[5]/td/text()")
            if 出生日期:
                出生日期 = str(出生日期[0])
            else:
                出生日期 = ""
            证件类型 = tree.xpath("/html/body/div/div[3]/table[1]/tr[6]/td/text()")
            if 证件类型:
                证件类型 = str(证件类型[0])
            else:
                证件类型 = ""
            证件号码 = tree.xpath("/html/body/div/div[3]/table[1]/tr[7]/td/text()")
            if 证件号码:
                证件号码 = str(证件号码[0])
            else:
                证件号码 = ""
            民族 = tree.xpath("/html/body/div/div[3]/table[2]/td[1]/text()")
            if 民族:
                民族 = str(民族[0])
            else:
                民族 = ""
            政治面貌 = tree.xpath("/html/body/div/div[3]/table[2]/td[2]/text()")
            if 政治面貌:
                政治面貌 = str(政治面貌[0])
            else:
                政治面貌 = ""
            录取类别 = tree.xpath("/html/body/div/div[3]/table[2]/td[3]/text()")
            if 录取类别:
                录取类别 = str(录取类别[0])
            else:
                录取类别 = ""
            所在校区 = tree.xpath("/html/body/div/div[3]/table[2]/td[4]/text()")
            if 所在校区:
                所在校区 = str(所在校区[0])
            else:
                所在校区 = ""
            年级 = tree.xpath("/html/body/div/div[3]/table[2]/td[5]/text()")
            if 年级:
                年级 = str(年级[0])
            else:
                年级 = ""
            国籍 = tree.xpath("/html/body/div/div[3]/table[2]/td[6]/text()")
            if 国籍:
                国籍 = str(国籍[0])
            else:
                国籍 = ""
            籍贯 = tree.xpath("/html/body/div/div[3]/table[2]/td[7]/text()")
            if 籍贯:
                籍贯 = str(籍贯[0])
            else:
                籍贯 = ""
            入学日期 = tree.xpath("/html/body/div/div[3]/table[2]/td[8]/text()")
            if 入学日期:
                入学日期 = str(入学日期[0])
            else:
                入学日期 = ""
            学制 = tree.xpath("/html/body/div/div[3]/table[2]/td[9]/text()")
            if 学制:
                学制 = str(学制[0])
            else:
                学制 = ""
            学生类别 = tree.xpath("/html/body/div/div[3]/table[2]/td[10]/text()")
            if 学生类别:
                学生类别 = str(学生类别[0])
            else:
                学生类别 = ""
            培养层次 = tree.xpath("/html/body/div/div[3]/table[2]/td[11]/text()")
            if 培养层次:
                培养层次 = str(培养层次[0]).replace(" ","").replace("\n","")
            else:
                培养层次 = ""
            院系 = tree.xpath("/html/body/div/div[3]/table[2]/td[12]/text()")
            if 院系:
                院系 = str(院系[0])
            else:
                院系 = ""
            一级学科 = tree.xpath("/html/body/div/div[3]/table[2]/td[13]/text()")
            if 一级学科:
                一级学科 = str(一级学科[0])
            else:
                一级学科 = ""
            专业 = tree.xpath("/html/body/div/div[3]/table[2]/td[14]/text()")
            if 专业:
                专业 = str(专业[0])
            else:
                专业 = ""
            考试方式 = tree.xpath("/html/body/div/div[3]/table[2]/td[16]/text()")
            if 考试方式:
                考试方式 = str(考试方式[0])
            else:
                考试方式 = ""
            学习形式 = tree.xpath("/html/body/div/div[3]/table[2]/td[17]/text()")
            if 学习形式:
                学习形式 = str(学习形式[0])
            else:
                学习形式 = ""
            导师姓名 = tree.xpath("/html/body/div/div[3]/table[2]/td[18]/text()")
            if 导师姓名:
                导师姓名 = str(导师姓名[0])
            else:
                导师姓名 = ""
            副导师姓名 = tree.xpath("/html/body/div/div[3]/table[2]/td[19]/text()")
            if 副导师姓名:
                副导师姓名 = str(副导师姓名[0]).replace(" ","").replace("\n","")
            else:
                副导师姓名 = ""
            导师指导小组成员姓名 = tree.xpath("/html/body/div/div[3]/table[2]/td[20]/text()")
            if 导师指导小组成员姓名:
                导师指导小组成员姓名 = str(导师指导小组成员姓名[0]).replace(" ","").replace("\n","")
            else:
                导师指导小组成员姓名 = ""
            定向委培单位所在省 = tree.xpath("/html/body/div/div[3]/table[2]/td[21]/text()")
            if 定向委培单位所在省:
                定向委培单位所在省 = str(定向委培单位所在省[0])
            else:
                定向委培单位所在省 = ""
            定向委培或在职单位 = tree.xpath("/html/body/div/div[3]/table[2]/td[22]/text()")
            if 定向委培或在职单位:
                定向委培或在职单位 = str(定向委培或在职单位[0])
            else:
                定向委培或在职单位 = ""
            外语语种 = tree.xpath("/html/body/div/div[3]/table[2]/td[23]/text()")
            if 外语语种:
                外语语种 = str(外语语种[0])
            else:
                外语语种 = ""
            专项计划 = tree.xpath("/html/body/div/div[3]/table[2]/td[24]/text()")
            if 专项计划:
                专项计划 = str(专项计划[0])
            else:
                专项计划 = ""
            生源地 = tree.xpath("/html/body/div/div[3]/table[2]/td[25]/text()")
            if 生源地:
                生源地 = str(生源地[0])
            else:
                生源地 = ""
            生源地码 = tree.xpath("/html/body/div/div[3]/table[2]/td[26]/text()")
            if 生源地码:
                生源地码 = str(生源地码[0])
            else:
                生源地码 = ""
            是否有学籍 = tree.xpath("/html/body/div/div[3]/table[2]/td[27]/em/text()")
            if 是否有学籍:
                是否有学籍 = str(是否有学籍[0]).replace(" ","")
            else:
                是否有学籍 = ""
            是否在校 = tree.xpath("/html/body/div/div[3]/table[2]/td[28]/em/text()")
            if 是否在校:
                是否在校 = str(是否在校[0]).replace(" ","")
            else:
                是否在校 = ""
            毕业状态 = tree.xpath("/html/body/div/div[3]/table[2]/td[29]/text()")
            if 毕业状态:
                毕业状态 = str(毕业状态[0])
            else:
                毕业状态 = ""
            毕业时间 = tree.xpath("/html/body/div/div[3]/table[2]/td[30]/text()")
            if 毕业时间:
                毕业时间 = str(毕业时间[0]).replace(" ","")
            else:
                毕业时间 = ""
            毕业类型 = tree.xpath("/html/body/div/div[3]/table[2]/td[31]/text()")
            if 毕业类型:
                毕业类型 = str(毕业类型[0])
            else:
                毕业类型 = ""
            乘车目的地 = tree.xpath("/html/body/div/div[3]/table[2]/td[32]/text()")
            if 乘车目的地:
                乘车目的地 = str(乘车目的地[0])
            else:
                乘车目的地 = ""
            是否在职 = tree.xpath("/html/body/div/div[3]/table[2]/td[33]/text()")
            if 是否在职:
                是否在职 = str(是否在职[0])
            else:
                是否在职 = ""
            异动信息 = tree.xpath("/html/body/div/div[3]/table[2]/td[34]/text()")
            if 异动信息:
                异动信息 = str(异动信息[0])
            else:
                异动信息 = ""
            是否国防生 = tree.xpath("/html/body/div/div[3]/table[2]/td[35]/text()")
            if 是否国防生:
                是否国防生 = str(是否国防生[0])
            else:
                是否国防生 = ""
            是否保留学籍 = tree.xpath("/html/body/div/div[3]/table[2]/td[36]/text()")
            if 是否保留学籍:
                是否保留学籍 = str(是否保留学籍[0])
            else:
                是否保留学籍 = ""
            思想政治表现 = tree.xpath("/html/body/div/div[3]/table[2]/td[37]/text()")
            if 思想政治表现:
                思想政治表现 = str(思想政治表现[0])
            else:
                思想政治表现 = ""
            在校联系电话 = tree.xpath("/html/body/div/div[5]/table/td[1]/text()")
            if 在校联系电话:
                在校联系电话 = str(在校联系电话[0])
            else:
                在校联系电话 = ""
            手机 = tree.xpath("/html/body/div/div[5]/table/td[2]/text()")
            if 手机:
                手机 = str(手机[0])
            else:
                手机 = ""
            电子邮箱 = tree.xpath("/html/body/div/div[5]/table/td[3]/text()")
            if 电子邮箱:
                电子邮箱 = str(电子邮箱[0])
            else:
                电子邮箱 = ""
            是否在校住宿 = tree.xpath("/html/body/div/div[5]/table/td[4]/text()")
            if 是否在校住宿:
                是否在校住宿 = str(是否在校住宿[0])
            else:
                是否在校住宿 = ""
            宿舍号码 = tree.xpath("/html/body/div/div[5]/table/td[5]/text()")
            if 宿舍号码:
                宿舍号码 = str(宿舍号码[0])
            else:
                宿舍号码 = ""
            宿舍电话 = tree.xpath("/html/body/div/div[5]/table/td[6]/text()")
            if 宿舍电话:
                宿舍电话 = str(宿舍电话[0])
            else:
                宿舍电话 = ""
            住宿地址 = tree.xpath("/html/body/div/div[5]/table/td[7]/text()")
            if 住宿地址:
                住宿地址 = str(住宿地址[0])
            else:
                住宿地址 = ""
            目前所在地 = tree.xpath("/html/body/div/div[5]/table/td[8]/text()")
            if 目前所在地:
                目前所在地 = str(目前所在地[0])
            else:
                目前所在地 = ""
            银行卡号 = tree.xpath("/html/body/div/div[7]/table/td[1]/text()")
            if 银行卡号:
                银行卡号 = str(银行卡号[0])
            else:
                银行卡号 = ""
            入学奖学金 = tree.xpath("/html/body/div/div[7]/table/td[2]/text()")
            if 入学奖学金:
                入学奖学金 = str(入学奖学金[0])
            else:
                入学奖学金 = ""
            婚姻状况 = tree.xpath("/html/body/div/div[9]/table/td[1]/text()")
            if 婚姻状况:
                婚姻状况 = str(婚姻状况[0])
            else:
                婚姻状况 = ""
            家庭联系电话 = tree.xpath("/html/body/div/div[9]/table/td[2]/text()")
            if 家庭联系电话:
                家庭联系电话 = str(家庭联系电话[0])
            else:
                家庭联系电话 = ""
            家庭通讯地址 = tree.xpath("/html/body/div/div[9]/table/td[3]/text()")
            if 家庭通讯地址:
                家庭通讯地址 = str(家庭通讯地址[0])
            else:
                家庭通讯地址 = ""
            家庭邮政编码 = tree.xpath("/html/body/div/div[9]/table/td[4]/text()")
            if 家庭邮政编码:
                家庭邮政编码 = str(家庭邮政编码[0])
            else:
                家庭邮政编码 = ""
            家庭主要成员 = tree.xpath("/html/body/div/div[9]/table/td[5]/text()")
            if 家庭主要成员:
                家庭主要成员 = str(家庭主要成员[0])
            else:
                家庭主要成员 = ""
            监护人1姓名 = tree.xpath("/html/body/div/div[9]/table/td[6]/text()")
            if 监护人1姓名:
                监护人1姓名 = str(监护人1姓名[0])
            else:
                监护人1姓名 = ""
            监护人1证件类型 = tree.xpath("/html/body/div/div[9]/table/td[7]/text()")
            if 监护人1证件类型:
                监护人1证件类型 = str(监护人1证件类型[0])
            else:
                监护人1证件类型 = ""
            监护人1证件号码 = tree.xpath("/html/body/div/div[9]/table/td[8]/text()")
            if 监护人1证件号码:
                监护人1证件号码 = str(监护人1证件号码[0])
            else:
                监护人1证件号码 = ""
            监护人2姓名 = tree.xpath("/html/body/div/div[9]/table/td[9]/text()")
            if 监护人2姓名:
                监护人2姓名 = str(监护人2姓名[0])
            else:
                监护人2姓名 = ""
            监护人2证件类型 = tree.xpath("/html/body/div/div[9]/table/td[10]/text()")
            if 监护人2证件类型:
                监护人2证件类型 = str(监护人2证件类型[0])
            else:
                监护人2证件类型 = ""
            监护人2证件号码 = tree.xpath("/html/body/div/div[9]/table/td[11]/text()")
            if 监护人2证件号码:
                监护人2证件号码 = str(监护人2证件号码[0])
            else:
                监护人2证件号码 = ""
            个人简历 = tree.xpath("/html/body/div/div[9]/table/td[12]/text()")
            if 个人简历:
                个人简历 = str(个人简历[0])
            else:
                个人简历 = ""
            准考证号 = tree.xpath("/html/body/div/div[11]/table/td[2]/text()")
            if 准考证号:
                准考证号 = str(准考证号[0])
            else:
                准考证号 = ""
            考生来源 = tree.xpath("/html/body/div/div[11]/table/td[3]/text()")
            if 考生来源:
                考生来源 = str(考生来源[0])
            else:
                考生来源 = ""
            入学前最后学历 = tree.xpath("/html/body/div/div[11]/table/td[4]/text()")
            if 入学前最后学历:
                入学前最后学历 = str(入学前最后学历[0])
            else:
                入学前最后学历 = ""
            入校前最后学位 = tree.xpath("/html/body/div/div[11]/table/td[5]/text()")
            if 入校前最后学位:
                入校前最后学位 = str(入校前最后学位[0])
            else:
                入校前最后学位 = ""
            入学前毕业时间 = tree.xpath("/html/body/div/div[11]/table/td[6]/text()")
            if 入学前毕业时间:
                入学前毕业时间 = str(入学前毕业时间[0])
            else:
                入学前毕业时间 = ""
            毕业学校 = tree.xpath("/html/body/div/div[11]/table/td[7]/text()")
            if 毕业学校:
                毕业学校 = str(毕业学校[0])
            else:
                毕业学校 = ""
            毕业专业名称 = tree.xpath("/html/body/div/div[11]/table/td[8]/text()")
            if 毕业专业名称:
                毕业专业名称 = str(毕业专业名称[0])
            else:
                毕业专业名称 = ""
            毕业专业代码 = tree.xpath("/html/body/div/div[11]/table/td[9]/text()")
            if 毕业专业代码:
                毕业专业代码 = str(毕业专业代码[0])
            else:
                毕业专业代码 = ""
            毕业证书编号 = tree.xpath("/html/body/div/div[11]/table/td[11]/text()")
            if 毕业证书编号:
                毕业证书编号 = str(毕业证书编号[0])
            else:
                毕业证书编号 = ""
            学位证书编号 = tree.xpath("/html/body/div/div[11]/table/td[12]/text()")
            if 学位证书编号:
                学位证书编号 = str(学位证书编号[0])
            else:
                学位证书编号 = ""
            最后工作单位 = tree.xpath("/html/body/div/div[11]/table/td[15]/text()")
            if 最后工作单位:
                最后工作单位 = str(最后工作单位[0])
            else:
                最后工作单位 = ""
            最后工作省市 = tree.xpath("/html/body/div/div[11]/table/td[16]/text()")
            if 最后工作省市:
                最后工作省市 = str(最后工作省市[0])
            else:
                最后工作省市 = ""
            报考前户口所在省份 = tree.xpath("/html/body/div/div[11]/table/td[17]/text()")
            if 报考前户口所在省份:
                报考前户口所在省份 = str(报考前户口所在省份[0])
            else:
                报考前户口所在省份 = ""
            离校方式 = tree.xpath("/html/body/div/div[13]/table/td[1]/text()")
            if 离校方式:
                离校方式 = str(离校方式[0])
            else:
                离校方式 = ""
            英语分级 = tree.xpath("/html/body/div/div[13]/table/td[6]/text()")
            if 英语分级:
                英语分级 = str(英语分级[0])
            else:
                英语分级 = ""
            转博分类 = tree.xpath("/html/body/div/div[13]/table/td[7]/text()")
            if 转博分类:
                转博分类 = str(转博分类[0])
            else:
                转博分类 = ""
            硕士阶段学号 = tree.xpath("/html/body/div/div[13]/table/td[8]/text()")
            if 硕士阶段学号:
                硕士阶段学号 = str(硕士阶段学号[0])
            else:
                硕士阶段学号 = ""
            备注 = tree.xpath("/html/body/div/div[13]/table/tr/td[1]/text()")
            if 备注:
                备注 = str(备注[0])
            else:
                备注 = ""
            # 执行sql语句，写入数据库 Execute SQL statement and write to database
            insertSql = 'insert into Postgraduate(学号,姓名,姓名拼音,性别,出生日期,证件类型,证件号码,民族,政治面貌,录取类别,所在校区,年级,国籍,籍贯,入学日期,学制,学生类别,培养层次,院系,一级学科,专业,考试方式,学习形式,导师姓名,副导师姓名,导师指导小组成员姓名,定向委培单位所在省,定向委培或在职单位,外语语种,专项计划,生源地,生源地码,是否有学籍,是否在校,毕业状态,毕业时间,毕业类型,乘车目的地,是否在职,异动信息,是否国防生,是否保留学籍,思想政治表现,在校联系电话,手机,电子邮箱,是否在校住宿,宿舍号码,宿舍电话,住宿地址,目前所在地,银行卡号,入学奖学金,婚姻状况,家庭联系电话,家庭通讯地址,家庭邮政编码,家庭主要成员,监护人1姓名,监护人1证件类型,监护人1证件号码,监护人2姓名,监护人2证件类型,监护人2证件号码,个人简历,准考证号,考生来源,入学前最后学历,入校前最后学位,入学前毕业时间,毕业学校,毕业专业名称,毕业专业代码,毕业证书编号,学位证书编号,最后工作单位,最后工作省市,报考前户口所在省份,离校方式,英语分级,转博分类,硕士阶段学号,备注) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            conn.execute(insertSql, (学号,姓名,姓名拼音,性别,出生日期,证件类型,证件号码,民族,政治面貌,录取类别,所在校区,年级,国籍,籍贯,入学日期,学制,学生类别,培养层次,院系,一级学科,专业,考试方式,学习形式,导师姓名,副导师姓名,导师指导小组成员姓名,定向委培单位所在省,定向委培或在职单位,外语语种,专项计划,生源地,生源地码,是否有学籍,是否在校,毕业状态,毕业时间,毕业类型,乘车目的地,是否在职,异动信息,是否国防生,是否保留学籍,思想政治表现,在校联系电话,手机,电子邮箱,是否在校住宿,宿舍号码,宿舍电话,住宿地址,目前所在地,银行卡号,入学奖学金,婚姻状况,家庭联系电话,家庭通讯地址,家庭邮政编码,家庭主要成员,监护人1姓名,监护人1证件类型,监护人1证件号码,监护人2姓名,监护人2证件类型,监护人2证件号码,个人简历,准考证号,考生来源,入学前最后学历,入校前最后学位,入学前毕业时间,毕业学校,毕业专业名称,毕业专业代码,毕业证书编号,学位证书编号,最后工作单位,最后工作省市,报考前户口所在省份,离校方式,英语分级,转博分类,硕士阶段学号,备注))
            conn.commit()
            # succeed in adding into the sqlite database
            print(file_name+"成功添加进数据库！")