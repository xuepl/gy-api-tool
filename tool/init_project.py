#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tool import os_tool
import os
############################
# 初始化工程目录
############################
root_path = os_tool.get_root_path()

    
content = """# allure report
reports/html/
reports/xml/

# pycharm
.idea/                                                                                        
# Byte-compiled / optimized / DLL files                                                       
__pycache__/                                                                                  
*.py[cod]                                                                                     
*$py.class                                                                                    
                                                                                              
# C extensions                                                                                
*.so                                                                                          
                                                                                              
# Distribution / packaging                                                                    
.Python                                                                                       
build/                                                                                        
develop-eggs/                                                                                 
dist/                                                                                         
downloads/                                                                                    
eggs/                                                                                         
.eggs/                                                                                        
lib/                                                                                          
lib64/                                                                                        
parts/                                                                                        
sdist/                                                                                        
var/                                                                                          
wheels/                                                                                       
*.egg-info/                                                                                   
.installed.cfg                                                                                
*.egg                                                                                         
MANIFEST                                                                                      
                                                                                              
# PyInstaller                                                                                 
#  Usually these files are written by a python script from a template                         
#  before PyInstaller builds the exe, so as to inject date/other infos into it.               
*.manifest                                                                                    
*.spec                                                                                        
                                                                                              
# Installer logs                                                                              
pip-log.txt                                                                                   
pip-delete-this-directory.txt                                                                 
                                                                                              
# Unit test / coverage reports                                                                
htmlcov/                                                                                      
.tox/                                                                                         
.coverage                                                                                     
.coverage.*                                                                                   
.cache                                                                                        
nosetests.xml                                                                                 
coverage.xml                                                                                  
*.cover                                                                                       
.hypothesis/                                                                                  
.pytest_cache/                                                                                
                                                                                              
# Translations                                                                                
*.mo                                                                                          
*.pot                                                                                         
                                                                                              
# Django stuff:                                                                               
*.log                                                                                         
local_settings.py                                                                             
db.sqlite3                                                                                    
                                                                                              
# Flask stuff:                                                                                
instance/                                                                                     
.webassets-cache                                                                              
                                                                                              
# Scrapy stuff:                                                                               
.scrapy                                                                                       
                                                                                              
# Sphinx documentation                                                                        
docs/_build/                                                                                  
                                                                                              
# PyBuilder                                                                                   
target/                                                                                       
                                                                                              
# Jupyter Notebook                                                                            
.ipynb_checkpoints                                                                            
                                                                                              
# pyenv                                                                                       
.python-version                                                                               
                                                                                              
# celery beat schedule file                                                                   
celerybeat-schedule                                                                           
                                                                                              
# SageMath parsed files                                                                       
*.sage.py                                                                                     
                                                                                              
# Environments                                                                                
.env                                                                                          
.venv                                                                                         
env/                                                                                          
venv/                                                                                         
ENV/                                                                                          
env.bak/                                                                                      
venv.bak/                                                                                     
                                                                                              
# Spyder project settings                                                                     
.spyderproject                                                                                
.spyproject                                                                                   
                                                                                              
# Rope project settings                                                                       
.ropeproject                                                                                  
                                                                                              
# mkdocs documentation                                                                        
/site                                                                                         
                                                                                              
# mypy                                                                                        
.mypy_cache/                                                                                  
"""
os_tool.mkfile(root_path,*['./', '.gitignore'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'config']))
content = """# API_URL="http://api.yansl.com:8084"
API_URL="http://api.yansl.com:8084"
GY_DB_QA = {
    'host': 'qa.guoyasoft.com',
    'port': 3306,
    'db': 'guoya_virtual_mall_1811',
    'user': 'root',
    'passwd': 'Guoya006',
    'charset': 'utf8'
}

GY_EMAIL_QA = {
    'on_off': 'on',  # 邮件是否发生，on发送，off不发送
    'mail_host': 'smtp.126.com',  # 设置服务器
    'mail_user': 'wuling1105@126.com',  # 用户名
    'mail_pass': '126shouquanma',  # 口令
    'sender': 'wuling1105@126.com',
    'mail_port': 25,
    'receivers': ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
}
"""
os_tool.mkfile(root_path,*['./', 'config', 'conf.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/16 9:08"""
os_tool.mkfile(root_path,*['./', 'config', '__init__.py'], content=content)

        
content = """# -*- coding:utf-8 -*-																		
# Author : 小吴老师                                                                        
# Data ：2019/7/12 7:41                                                                    
from tools.os import shell_tool
import pytest
                                                                                           
if __name__ == '__main__':                                                                 
    # 修改成要执行的测试用例                                                               
    test_case = './test_case/test_hello.py'
                                                                                           
    xml_report_path = './reports/xml/'                                                     
    html_report_path = './reports/html/'                                                   
                                                                                           
    pytest.main(['-s', '-q', '--alluredir',                                                
                 xml_report_path, test_case])                                              
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    shell_tool.invoke(cmd1)
"""
os_tool.mkfile(root_path,*['./', 'run.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'test_case']))
content = """import pytest                                               
                                                            
                                                            
@pytest.fixture(scope='session')                            
def pub_data():
    data = {'token':'asdfasdfjsldkfjlsxllkj'}               
    return data                                             


@pytest.fixture(scope='session')                            
def pub_list():                                             
    data = ['张三','zhangsan',30,'男','aaa123']             
    return data                                             


@pytest.fixture(scope='session')                            
def pub_var():                                              
    token = 'xxxxsdfsdfjkllwklewe'                          
    return token                                            

@pytest.fixture(scope='session',autouse=True)
def aaa(pytestconfig):
    print(pytestconfig.invocation_dir)"""
os_tool.mkfile(root_path,*['./', 'test_case', 'conftest.py'], content=content)

        
content = """#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools.api import request_tool
'''
文件名 和方法名要以test_
类名Test
'''


def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "xuepl123",
  "userName": "xuepl123"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    print(r.headers)




def test_get_params(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"phone":'18103909786'}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_get_file(pub_data):
    file_name = "e:\\\\sku.xlsx" # 下载文件地址
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"pridCode":'4l300'}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "9999"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"rw") as f :
        f.write(r.content)

def test_post_file(pub_data):
    file_name = "e:\\\\sku.xls" # 下载文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)




"""
os_tool.mkfile(root_path,*['./', 'test_case', 'test_hello.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/16 9:08"""
os_tool.mkfile(root_path,*['./', 'test_case', '__init__.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'tools']))
os_tool.mkdir(os.path.join(root_path,*['./', 'tools', 'api']))
content = """'''
封装request
'''

import requests

from tools.report import log_tool
from tools.report.decorators_tool import logs, datas
import time


@datas
@logs
def request(*args,**kwargs):
    '''
    Get请求
    :param url:
    :param data:
    :param header:
    :return:
    '''
    try:
        response = requests.request(*args,**kwargs)
    except requests.RequestException as e:
        log_tool.error('%s%s' % ('Exception url: ', kwargs['url']))
        log_tool.error(e)
        return ()
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ',kwargs['url']))
        return ()
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response


@datas
@logs
def post_request(*args,**kwargs):
    '''
    Post请求
    :param url:
    :param data:
    :param header:
    :return:
    '''

    try:
        response = requests.post(*args,**kwargs)

    except requests.RequestException as e:
        log_tool.error('%s%s' % ('RequestException url: ',kwargs['url']))
        log_tool.error(e)
        return ()

    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', kwargs['url']))
        log_tool.error(e)
        return ()

    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)

    return response

@datas
@logs
def post_request_multipart(*args,**kwargs):
    '''
    提交Multipart/form-data 格式的Post请求
    :param url:
    :param data:
    :param header:
    :param file_parm:
    :param file:
    :param type:
    :return:
    '''

    response = requests.post(*args,**kwargs)
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)

    return response

@datas
@logs
def put_request(*args,**kwargs):
    '''
    Put请求
    :param url:
    :param data:
    :param header:
    :return:
    '''

    try:

        response = requests.put(*args,**kwargs)
    except requests.RequestException as e:
        log_tool.error('%s%s' % ('RequestException url: ', kwargs['url']))
        log_tool.error(e)
        return ()

    except Exception as e:
        print('%s%s' % ('Exception url: ', kwargs['url']))
        print(e)
        return ()

    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)

    return response

def down_big_file(srcUrl, localFile):
    print('%s\\n --->>>\\n  %s' % (srcUrl, localFile))
    startTime = time.time()
    with requests.get(srcUrl, stream=True) as r:
        contentLength = int(r.headers['content-length'])
        line = 'content-length: %dB/ %.2fKB/ %.2fMB'
        line = line % (contentLength, contentLength / 1024, contentLength / 1024 / 1024)
        print(line)
        print('正在下载中..............')
        downSize = 0
        with open(localFile, 'wb') as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                downSize += len(chunk)
                line = '%d KB/s - %.2f MB， 共 %.2f MB'
                line = line % (
                downSize / 1024 / (time.time() - startTime), downSize / 1024 / 1024, contentLength / 1024 / 1024)
                print(line, end='\\r')
                if downSize >= contentLength:
                    break
        timeCost = time.time() - startTime
        line = '共耗时: %.2f s, 平均速度: %.2f KB/s'
        line = line % (timeCost, downSize / 1024 / timeCost)
        print(line)
"""
os_tool.mkfile(root_path,*['./', 'tools', 'api', 'request_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-api-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:23"""
os_tool.mkfile(root_path,*['./', 'tools', 'api', '__init__.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'tools', 'data']))
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/10 6:26

import configparser
import os


class ConfigTool:

    def __init__(self):
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)).replace('\\\\','/')
        file_path = '/config/config.ini'
        file_name = root_path + file_path
        print(file_name)
        self.config = configparser.ConfigParser()
        print(file_name)
        self.config.read(file_name)

    def get_conf(self,section,option):
        return self.config.get(section,option)


    def get_api_url(self,section):
        protocal = self.get_conf(section, 'protocal')
        host = self.get_conf(section, 'host')
        port = self.get_conf(section, 'port')

        url = protocal + '://' + host + ':' + port
        return url

    def get_db_dict(self,section):
        db_dict = dict()
        db_dict['host'] = self.get_conf(section, 'host')
        db_dict['port'] = int(self.get_conf(section, 'port'))
        db_dict['db'] = self.get_conf(section, 'db')
        db_dict['user'] = self.get_conf(section, 'user')
        db_dict['passwd'] = self.get_conf(section, 'passwd')
        db_dict['charset'] = self.get_conf(section, 'charset')
        print(type(db_dict))
        print(db_dict)
        return  db_dict
"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'config_tool.py'], content=content)

        
content = """import xlrd
import xlwt
from tools.os import os_tool


def write_excel(file_name,data_title,data_list,encoding='utf-8'):
    # 创建workbook和sheet对象 注意Workbook的开头W要大写
    workbook = xlwt.Workbook(encoding=encoding)
    # 添加一个名为sheet1的表
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    # 向表头写入数据
    for i in range(len(data_title)):
        sheet1.write(0, i, data_title[i])

    # 向sheet写入数据
    for i in range(len(data_list)):
        for j in range(4):
            sheet1.write(i + 1, j, data_list[i][j])

    # 保存数据到‘Workbook2.xls’文件中
    workbook.save(file_name)
    print('创建execel完成！')

def _get_excel_dict(file):
    data = []
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    # print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    # print(sheet1)
    # print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in range(1, sheet1.nrows):
        # l.append(sheet1.row_values(i))
        d = {}
        for j in range(sheet1.ncols):
            d[sheet1.row_values(0)[j]] = sheet1.row_values(i)[j]
        data.append(d)
    # print(l)
    return data


def _get_excel_list(file):
    data = []  # 声明变量
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格sheet
    for i in range(1, sheet1.nrows):  # 循环行
        data.append(sheet1.row_values(i))  # 获取每行内容 并 添加进l
    return data

def _get_excel_ids(excel_list):
    ids_list = []
    for i in range(len(excel_list)):
        # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
        ids_pop = excel_list[i].pop(0)
        # 将ids_pop添加到 ids_list 里面
        ids_list.append(ids_pop)
    return ids_list

def get_test_case(file):
    root_path = os_tool.get_root_path()
    data = {}
    case_list=_get_excel_list(root_path+file)
    case_ids=_get_excel_ids(case_list)
    data[0]=case_ids
    data[1]=case_list
    return data

if __name__ == '__main__':
    data = get_test_case("C:/softwareData/PycharmProjects/s00-wuling/documents/user/注册接口sign_up.xlsx")
    print(data[0])
    print(data[1])
"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'excel_tool.py'], content=content)

        
content = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/12'
import random
import re

from tools.data import random_tool
from tools.data.make_info import make_info


en = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
num = [ str(i) for i in range(10)]
zf = list(str(bytes([0x60, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d,
                                  0x2e, 0x2f, 0x3c, 0x3e, 0x3f, 0x40, 0x5b, 0x5c, 0x5d, 0x5e, 0x5f, 0x7b, 0x7c, 0x7d,
                                  0x7e, 0x60])))
zw = [bytes.fromhex(f'{head:x}{body:x}').decode('gb2312') for head in range(0xb0, 0xf7,0x01) for body in range(0xa1, 0xf9,0x01)]
def get_length(s):
    length = 1
    l = s.split(",")
    if (len(l) == 1):
        length = int(l[0])
    elif (len(l) == 2 and (l[0] != '' or l[1] != '')):
        if (l[0] != '' and l[1] != ''):
            length = random.randint(int(l[0]), int(l[1]))

        elif (l[0] == ''):
            length = random.randint(1, int(l[1]))
        else:
            length = random.randint(int(l[0]), 9999)
    else:
        pass
    return length
def get_str(length,ll):
    l = []
    limits = ll[0]
    if (limits.find("字母") != -1):
        l += en
    if (limits.find("数字") != -1):
        l += num
    if (limits.find("特殊字符") != -1):
        l += zf
    if (limits.find("中文") != -1):
        l += zw
    value = ''
    if (len(l) != 0):
        for i in range(length):
            value +=  l[random.randint(0, len(l) - 1)]
    if len(ll) == 2:
        value = ll[1] + value
    return value

def replace_data(s):
    value = ""
    s_l = s.split(" ")
    if(s_l[1].find('字符') != -1 or s_l[1].find('string') != -1):
        s_l[2] = s_l[2].replace('，',',')
        length = get_length(s_l[2])
        value = get_str(length,s_l[3:])
    elif (s_l[1].find("地址") != -1):
        value = random_tool.random_addr()
    elif (s_l[1].find("手机") != -1):
        value = random_tool.random_tell()
    elif (s_l[1].find("邮箱") != -1):
        value = random_tool.random_email()
    elif (s_l[1].find("姓名") != -1):
        value = random_tool.random_name()
    elif (s_l[1].find("数字") != -1):
        s_l[2] = s_l[2].replace('，', ',')
        value = get_length(s_l[2])
    elif (s_l[1].find("身份证") != -1):
        value = make_info()["身份证号"]
    else:
        value = None
    return value


def get_json_data(dic,pa,d):
    for key in pa:
        path = pa[key].strip()
        if(not path.startswith("$")):
            print("请输入正确的jsonpath")
            return
        p_list = path.split('.')
        n_list = []
        for p in p_list:
            if (p.find('[') != -1):
                start = p.index('[')
                end = p.index(']')
                n_list.append(p[:start])
                n_list.append(p[start+1:end])
                try:
                    if(p[end+1:] != ''):
                        n_list.append(p[end+1:])
                except:
                    pass
            else:
                n_list.append(p)

        for i in n_list[1:]:
            if(i.isdigit()):
                dic=dic[int(i)]
            else:
                dic = dic[i]
        d[key] = dic

def replace_str(s,data):
    r = re.compile(r"\\${(.*?)}")
    s_l = r.findall(s)
    for l in s_l:
        s = s.replace("${"+l+"}",data[l])
    return s


def index_dic(d,data):
    if(isinstance(d,dict)):
        for key in d:
            if (isinstance(d[key], str)):
                try:
                    d[key] = replace_str(d[key],data)
                except:
                    pass
                if (d[key].find("自动生成") != -1):
                    d[key] = replace_data(d[key].strip())
                    print(d)
            else:
                index_dic(d[key],data)
    elif(isinstance(d,list)):
        for i in range(len(d)):
            if (isinstance(d[i], str)):
                d[i] = d[i].strip()
                if(d[i].startswith("$") and d[i].endswith("}")):
                    try:
                        d[i] = data[d[i][2:-1]]
                    except:
                        pass
                if (d[i].startswith("自动生成")):
                    d[i] = replace_data(d[i])
            else:
                index_dic(d[i], data)
    else:
        pass
    return d

if __name__ == '__main__':
     data = {"token":"sssssss"}
     s = "fff${token}${token}ddd"
     s = replace_str(s,data)
     print(s)"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'json_path_tool.py'], content=content)

        
content = """#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import time

shengdic = {'11': '北京市', '12': '天津市', '13': '河北省', '14': '山西省', '15': '内蒙古自治区', '21': '辽宁省', '22': '吉林省', '23': '黑龙江省', '31': '上海市', '32': '江苏省', '33': '浙江省', '34': '安徽省', '35': '福建省', '36': '江西省', '37': '山东省', '41': '河南省', '42': '湖北省', '43': '湖南省', '44': '广东省', '45': '广西壮族自治区', '46': '海南省', '50': '重庆市', '51': '四川省', '52': '贵州省', '53': '云南省', '54': '西藏自治区', '61': '陕西省', '62': '甘肃省', '63': '青海省', '64': '宁夏回族自治区', '65': '新疆维吾尔自治区'}
shidic = {'1101': '市辖区', '1102': '县', '1201': '市辖区', '1202': '县', '1301': '石家庄市', '1302': '唐山市', '1303': '秦皇岛市', '1304': '邯郸市', '1305': '邢台市', '1306': '保定市', '1307': '张家口市', '1308': '承德市', '1309': '沧州市', '1310': '廊坊市', '1311': '衡水市', '1401': '太原市', '1402': '大同市', '1403': '阳泉市', '1404': '长治市', '1405': '晋城市', '1406': '朔州市', '1407': '晋中市', '1408': '运城市', '1409': '忻州市', '1410': '临汾市', '1411': '吕梁市', '1501': '呼和浩特市', '1502': '包头市', '1503': '乌海市', '1504': '赤峰市', '1505': '通辽市', '1506': '鄂尔多斯市', '1507': '呼伦贝尔市', '1508': '巴彦淖尔市', '1509': '乌兰察布市', '1522': '兴安盟', '1525': '锡林郭勒盟', '1529': '阿拉善盟', '2101': '沈阳市', '2102': '大连市', '2103': '鞍山市', '2104': '抚顺市', '2105': '本溪市', '2106': '丹东市', '2107': '锦州市', '2108': '营口市', '2109': '阜新市', '2110': '辽阳市', '2111': '盘锦市', '2112': '铁岭市', '2113': '朝阳市', '2114': '葫芦岛市', '2201': '长春市', '2202': '吉林市', '2203': '四平市', '2204': '辽源市', '2205': '通化市', '2206': '白山市', '2207': '松原市', '2208': '白城市', '2224': '延边朝鲜族自治州', '2301': '哈尔滨市', '2302': '齐齐哈尔市', '2303': '鸡西市', '2304': '鹤岗市', '2305': '双鸭山市', '2306': '大庆市', '2307': '伊春市', '2308': '佳木斯市', '2309': '七台河市', '2310': '牡丹江市', '2311': '黑河市', '2312': '绥化市', '2327': '大兴安岭地区', '3101': '市辖区', '3102': '县', '3201': '南京市', '3202': '无锡市', '3203': '徐州市', '3204': '常州市', '3205': '苏州市', '3206': '南通市', '3207': '连云港市', '3208': '淮安市', '3209': '盐城市', '3210': '扬州市', '3211': '镇江市', '3212': '泰州市', '3213': '宿迁市', '3301': '杭州市', '3302': '宁波市', '3303': '温州市', '3304': '嘉兴市', '3305': '湖州市', '3306': '绍兴市', '3307': '金华市', '3308': '衢州市', '3309': '舟山市', '3310': '台州市', '3311': '丽水市', '3401': '合肥市', '3402': '芜湖市', '3403': '蚌埠市', '3404': '淮南市', '3405': '马鞍山市', '3406': '淮北市', '3407': '铜陵市', '3408': '安庆市', '3410': '黄山市', '3411': '滁州市', '3412': '阜阳市', '3413': '宿州市', '3415': '六安市', '3416': '亳州市', '3417': '池州市', '3418': '宣城市', '3501': '福州市', '3502': '厦门市', '3503': '莆田市', '3504': '三明市', '3505': '泉州市', '3506': '漳州市', '3507': '南平市', '3508': '龙岩市', '3509': '宁德市', '3601': '南昌市', '3602': '景德镇市', '3603': '萍乡市', '3604': '九江市', '3605': '新余市', '3606': '鹰潭市', '3607': '赣州市', '3608': '吉安市', '3609': '宜春市', '3610': '抚州市', '3611': '上饶市', '3701': '济南市', '3702': '青岛市', '3703': '淄博市', '3704': '枣庄市', '3705': '东营市', '3706': '烟台市', '3707': '潍坊市', '3708': '济宁市', '3709': '泰安市', '3710': '威海市', '3711': '日照市', '3712': '莱芜市', '3713': '临沂市', '3714': '德州市', '3715': '聊城市', '3716': '滨州市', '3717': '菏泽市', '4101': '郑州市', '4102': '开封市', '4103': '洛阳市', '4104': '平顶山市', '4105': '安阳市', '4106': '鹤壁市', '4107': '新乡市', '4108': '焦作市', '4109': '濮阳市', '4110': '许昌市', '4111': '漯河市', '4112': '三门峡市', '4113': '南阳市', '4114': '商丘市', '4115': '信阳市', '4116': '周口市', '4117': '驻马店市', '4190': '省直辖县级行政区划', '4201': '武汉市', '4202': '黄石市', '4203': '十堰市', '4205': '宜昌市', '4206': '襄阳市', '4207': '鄂州市', '4208': '荆门市', '4209': '孝感市', '4210': '荆州市', '4211': '黄冈市', '4212': '咸宁市', '4213': '随州市', '4228': '恩施土家族苗族自治州', '4290': '省直辖县级行政区划', '4301': '长沙市', '4302': '株洲市', '4303': '湘潭市', '4304': '衡阳市', '4305': '邵阳市', '4306': '岳阳市', '4307': '常德市', '4308': '张家界市', '4309': '益阳市', '4310': '郴州市', '4311': '永州市', '4312': '怀化市', '4313': '娄底市', '4331': '湘西土家族苗族自治州', '4401': '广州市', '4402': '韶关市', '4403': '深圳市', '4404': '珠海市', '4405': '汕头市', '4406': '佛山市', '4407': '江门市', '4408': '湛江市', '4409': '茂名市', '4412': '肇庆市', '4413': '惠州市', '4414': '梅州市', '4415': '汕尾市', '4416': '河源市', '4417': '阳江市', '4418': '清远市', '4419': '东莞市', '4420': '中山市', '4451': '潮州市', '4452': '揭阳市', '4453': '云浮市', '4501': '南宁市', '4502': '柳州市', '4503': '桂林市', '4504': '梧州市', '4505': '北海市', '4506': '防城港市', '4507': '钦州市', '4508': '贵港市', '4509': '玉林市', '4510': '百色市', '4511': '贺州市', '4512': '河池市', '4513': '来宾市', '4514': '崇左市', '4601': '海口市', '4602': '三亚市', '4603': '三沙市', '4690': '省直辖县级行政区划', '5001': '市辖区', '5002': '县', '5101': '成都市', '5103': '自贡市', '5104': '攀枝花市', '5105': '泸州市', '5106': '德阳市', '5107': '绵阳市', '5108': '广元市', '5109': '遂宁市', '5110': '内江市', '5111': '乐山市', '5113': '南充市', '5114': '眉山市', '5115': '宜宾市', '5116': '广安市', '5117': '达州市', '5118': '雅安市', '5119': '巴中市', '5120': '资阳市', '5132': '阿坝藏族羌族自治州', '5133': '甘孜藏族自治州', '5134': '凉山彝族自治州', '5201': '贵阳市', '5202': '六盘水市', '5203': '遵义市', '5204': '安顺市', '5205': '毕节市', '5206': '铜仁市', '5223': '黔西南布依族苗族自治州', '5226': '黔东南苗族侗族自治州', '5227': '黔南布依族苗族自治州', '5301': '昆明市', '5303': '曲靖市', '5304': '玉溪市', '5305': '保山市', '5306': '昭通市', '5307': '丽江市', '5308': '普洱市', '5309': '临沧市', '5323': '楚雄彝族自治州', '5325': '红河哈尼族彝族自治州', '5326': '文山壮族苗族自治州', '5328': '西双版纳傣族自治州', '5329': '大理白族自治州', '5331': '德宏傣族景颇族自治州', '5333': '怒江傈僳族自治州', '5334': '迪庆藏族自治州', '5401': '拉萨市', '5421': '昌都地区', '5422': '山南地区', '5423': '日喀则地区', '5424': '那曲地区', '5425': '阿里地区', '5426': '林芝地区', '6101': '西安市', '6102': '铜川市', '6103': '宝鸡市', '6104': '咸阳市', '6105': '渭南市', '6106': '延安市', '6107': '汉中市', '6108': '榆林市', '6109': '安康市', '6110': '商洛市', '6201': '兰州市', '6202': '嘉峪关市', '6203': '金昌市', '6204': '白银市', '6205': '天水市', '6206': '武威市', '6207': '张掖市', '6208': '平凉市', '6209': '酒泉市', '6210': '庆阳市', '6211': '定西市', '6212': '陇南市', '6229': '临夏回族自治州', '6230': '甘南藏族自治州', '6301': '西宁市', '6321': '海东地区', '6322': '海北藏族自治州', '6323': '黄南藏族自治州', '6325': '海南藏族自治州', '6326': '果洛藏族自治州', '6327': '玉树藏族自治州', '6328': '海西蒙古族藏族自治州', '6401': '银川市', '6402': '石嘴山市', '6403': '吴忠市', '6404': '固原市', '6405': '中卫市', '6501': '乌鲁木齐市', '6502': '克拉玛依市', '6521': '吐鲁番地区', '6522': '哈密地区', '6523': '昌吉回族自治州', '6527': '博尔塔拉蒙古自治州', '6528': '巴音郭楞蒙古自治州', '6529': '阿克苏地区', '6530': '克孜勒苏柯尔克孜自治州', '6531': '喀什地区', '6532': '和田地区', '6540': '伊犁哈萨克自治州', '6542': '塔城地区', '6543': '阿勒泰地区', '6590': '自治区直辖县级行政区划'}
qudic = {'110101': '东城区', '110102': '西城区', '110105': '朝阳区', '110106': '丰台区', '110107': '石景山区', '110108': '海淀区', '110109': '门头沟区', '110111': '房山区', '110112': '通州区', '110113': '顺义区', '110114': '昌平区', '110115': '大兴区', '110116': '怀柔区', '110117': '平谷区', '110228': '密云县', '110229': '延庆县', '120101': '和平区', '120102': '河东区', '120103': '河西区', '120104': '南开区', '120105': '河北区', '120106': '红桥区', '120110': '东丽区', '120111': '西青区', '120112': '津南区', '120113': '北辰区', '120114': '武清区', '120115': '宝坻区', '120116': '滨海新区', '120221': '宁河县', '120223': '静海县', '120225': '蓟县', '130101': '市辖区', '130102': '长安区', '130103': '桥东区', '130104': '桥西区', '130105': '新华区', '130107': '井陉矿区', '130108': '裕华区', '130121': '井陉县', '130123': '正定县', '130124': '栾城县', '130125': '行唐县', '130126': '灵寿县', '130127': '高邑县', '130128': '深泽县', '130129': '赞皇县', '130130': '无极县', '130131': '平山县', '130132': '元氏县', '130133': '赵县', '130181': '辛集市', '130182': '藁城市', '130183': '晋州市', '130184': '新乐市', '130185': '鹿泉市', '130201': '市辖区', '130202': '路南区', '130203': '路北区', '130204': '古冶区', '130205': '开平区', '130207': '丰南区', '130208': '丰润区', '130209': '曹妃甸区', '130223': '滦县', '130224': '滦南县', '130225': '乐亭县', '130227': '迁西县', '130229': '玉田县', '130281': '遵化市', '130283': '迁安市', '130301': '市辖区', '130302': '海港区', '130303': '山海关区', '130304': '北戴河区', '130321': '青龙满族自治县', '130322': '昌黎县', '130323': '抚宁县', '130324': '卢龙县', '130401': '市辖区', '130402': '邯山区', '130403': '丛台区', '130404': '复兴区', '130406': '峰峰矿区', '130421': '邯郸县', '130423': '临漳县', '130424': '成安县', '130425': '大名县', '130426': '涉县', '130427': '磁县', '130428': '肥乡县', '130429': '永年县', '130430': '邱县', '130431': '鸡泽县', '130432': '广平县', '130433': '馆陶县', '130434': '魏县', '130435': '曲周县', '130481': '武安市', '130501': '市辖区', '130502': '桥东区', '130503': '桥西区', '130521': '邢台县', '130522': '临城县', '130523': '内丘县', '130524': '柏乡县', '130525': '隆尧县', '130526': '任县', '130527': '南和县', '130528': '宁晋县', '130529': '巨鹿县', '130530': '新河县', '130531': '广宗县', '130532': '平乡县', '130533': '威县', '130534': '清河县', '130535': '临西县', '130581': '南宫市', '130582': '沙河市', '130601': '市辖区', '130602': '新市区', '130603': '北市区', '130604': '南市区', '130621': '满城县', '130622': '清苑县', '130623': '涞水县', '130624': '阜平县', '130625': '徐水县', '130626': '定兴县', '130627': '唐县', '130628': '高阳县', '130629': '容城县', '130630': '涞源县', '130631': '望都县', '130632': '安新县', '130633': '易县', '130634': '曲阳县', '130635': '蠡县', '130636': '顺平县', '130637': '博野县', '130638': '雄县', '130681': '涿州市', '130682': '定州市', '130683': '安国市', '130684': '高碑店市', '130701': '市辖区', '130702': '桥东区', '130703': '桥西区', '130705': '宣化区', '130706': '下花园区', '130721': '宣化县', '130722': '张北县', '130723': '康保县', '130724': '沽源县', '130725': '尚义县', '130726': '蔚县', '130727': '阳原县', '130728': '怀安县', '130729': '万全县', '130730': '怀来县', '130731': '涿鹿县', '130732': '赤城县', '130733': '崇礼县', '130801': '市辖区', '130802': '双桥区', '130803': '双滦区', '130804': '鹰手营子矿区', '130821': '承德县', '130822': '兴隆县', '130823': '平泉县', '130824': '滦平县', '130825': '隆化县', '130826': '丰宁满族自治县', '130827': '宽城满族自治县', '130828': '围场满族蒙古族自治县', '130901': '市辖区', '130902': '新华区', '130903': '运河区', '130921': '沧县', '130922': '青县', '130923': '东光县', '130924': '海兴县', '130925': '盐山县', '130926': '肃宁县', '130927': '南皮县', '130928': '吴桥县', '130929': '献县', '130930': '孟村回族自治县', '130981': '泊头市', '130982': '任丘市', '130983': '黄骅市', '130984': '河间市', '131001': '市辖区', '131002': '安次区', '131003': '广阳区', '131022': '固安县', '131023': '永清县', '131024': '香河县', '131025': '大城县', '131026': '文安县', '131028': '大厂回族自治县', '131081': '霸州市', '131082': '三河市', '131101': '市辖区', '131102': '桃城区', '131121': '枣强县', '131122': '武邑县', '131123': '武强县', '131124': '饶阳县', '131125': '安平县', '131126': '故城县', '131127': '景县', '131128': '阜城县', '131181': '冀州市', '131182': '深州市', '140101': '市辖区', '140105': '小店区', '140106': '迎泽区', '140107': '杏花岭区', '140108': '尖草坪区', '140109': '万柏林区', '140110': '晋源区', '140121': '清徐县', '140122': '阳曲县', '140123': '娄烦县', '140181': '古交市', '140201': '市辖区', '140202': '城区', '140203': '矿区', '140211': '南郊区', '140212': '新荣区', '140221': '阳高县', '140222': '天镇县', '140223': '广灵县', '140224': '灵丘县', '140225': '浑源县', '140226': '左云县', '140227': '大同县', '140301': '市辖区', '140302': '城区', '140303': '矿区', '140311': '郊区', '140321': '平定县', '140322': '盂县', '140401': '市辖区', '140402': '城区', '140411': '郊区', '140421': '长治县', '140423': '襄垣县', '140424': '屯留县', '140425': '平顺县', '140426': '黎城县', '140427': '壶关县', '140428': '长子县', '140429': '武乡县', '140430': '沁县', '140431': '沁源县', '140481': '潞城市', '140501': '市辖区', '140502': '城区', '140521': '沁水县', '140522': '阳城县', '140524': '陵川县', '140525': '泽州县', '140581': '高平市', '140601': '市辖区', '140602': '朔城区', '140603': '平鲁区', '140621': '山阴县', '140622': '应县', '140623': '右玉县', '140624': '怀仁县', '140701': '市辖区', '140702': '榆次区', '140721': '榆社县', '140722': '左权县', '140723': '和顺县', '140724': '昔阳县', '140725': '寿阳县', '140726': '太谷县', '140727': '祁县', '140728': '平遥县', '140729': '灵石县', '140781': '介休市', '140801': '市辖区', '140802': '盐湖区', '140821': '临猗县', '140822': '万荣县', '140823': '闻喜县', '140824': '稷山县', '140825': '新绛县', '140826': '绛县', '140827': '垣曲县', '140828': '夏县', '140829': '平陆县', '140830': '芮城县', '140881': '永济市', '140882': '河津市', '140901': '市辖区', '140902': '忻府区', '140921': '定襄县', '140922': '五台县', '140923': '代县', '140924': '繁峙县', '140925': '宁武县', '140926': '静乐县', '140927': '神池县', '140928': '五寨县', '140929': '岢岚县', '140930': '河曲县', '140931': '保德县', '140932': '偏关县', '140981': '原平市', '141001': '市辖区', '141002': '尧都区', '141021': '曲沃县', '141022': '翼城县', '141023': '襄汾县', '141024': '洪洞县', '141025': '古县', '141026': '安泽县', '141027': '浮山县', '141028': '吉县', '141029': '乡宁县', '141030': '大宁县', '141031': '隰县', '141032': '永和县', '141033': '蒲县', '141034': '汾西县', '141081': '侯马市', '141082': '霍州市', '141101': '市辖区', '141102': '离石区', '141121': '文水县', '141122': '交城县', '141123': '兴县', '141124': '临县', '141125': '柳林县', '141126': '石楼县', '141127': '岚县', '141128': '方山县', '141129': '中阳县', '141130': '交口县', '141181': '孝义市', '141182': '汾阳市', '150101': '市辖区', '150102': '新城区', '150103': '回民区', '150104': '玉泉区', '150105': '赛罕区', '150121': '土默特左旗', '150122': '托克托县', '150123': '和林格尔县', '150124': '清水河县', '150125': '武川县', '150201': '市辖区', '150202': '东河区', '150203': '昆都仑区', '150204': '青山区', '150205': '石拐区', '150206': '白云鄂博矿区', '150207': '九原区', '150221': '土默特右旗', '150222': '固阳县', '150223': '达尔罕茂明安联合旗', '150301': '市辖区', '150302': '海勃湾区', '150303': '海南区', '150304': '乌达区', '150401': '市辖区', '150402': '红山区', '150403': '元宝山区', '150404': '松山区', '150421': '阿鲁科尔沁旗', '150422': '巴林左旗', '150423': '巴林右旗', '150424': '林西县', '150425': '克什克腾旗', '150426': '翁牛特旗', '150428': '喀喇沁旗', '150429': '宁城县', '150430': '敖汉旗', '150501': '市辖区', '150502': '科尔沁区', '150521': '科尔沁左翼中旗', '150522': '科尔沁左翼后旗', '150523': '开鲁县', '150524': '库伦旗', '150525': '奈曼旗', '150526': '扎鲁特旗', '150581': '霍林郭勒市', '150601': '市辖区', '150602': '东胜区', '150621': '达拉特旗', '150622': '准格尔旗', '150623': '鄂托克前旗', '150624': '鄂托克旗', '150625': '杭锦旗', '150626': '乌审旗', '150627': '伊金霍洛旗', '150701': '市辖区', '150702': '海拉尔区', '150721': '阿荣旗', '150722': '莫力达瓦达斡尔族自治旗', '150723': '鄂伦春自治旗', '150724': '鄂温克族自治旗', '150725': '陈巴尔虎旗', '150726': '新巴尔虎左旗', '150727': '新巴尔虎右旗', '150781': '满洲里市', '150782': '牙克石市', '150783': '扎兰屯市', '150784': '额尔古纳市', '150785': '根河市', '150801': '市辖区', '150802': '临河区', '150821': '五原县', '150822': '磴口县', '150823': '乌拉特前旗', '150824': '乌拉特中旗', '150825': '乌拉特后旗', '150826': '杭锦后旗', '150901': '市辖区', '150902': '集宁区', '150921': '卓资县', '150922': '化德县', '150923': '商都县', '150924': '兴和县', '150925': '凉城县', '150926': '察哈尔右翼前旗', '150927': '察哈尔右翼中旗', '150928': '察哈尔右翼后旗', '150929': '四子王旗', '150981': '丰镇市', '152201': '乌兰浩特市', '152202': '阿尔山市', '152221': '科尔沁右翼前旗', '152222': '科尔沁右翼中旗', '152223': '扎赉特旗', '152224': '突泉县', '152501': '二连浩特市', '152502': '锡林浩特市', '152522': '阿巴嘎旗', '152523': '苏尼特左旗', '152524': '苏尼特右旗', '152525': '东乌珠穆沁旗', '152526': '西乌珠穆沁旗', '152527': '太仆寺旗', '152528': '镶黄旗', '152529': '正镶白旗', '152530': '正蓝旗', '152531': '多伦县', '152921': '阿拉善左旗', '152922': '阿拉善右旗', '152923': '额济纳旗', '210101': '市辖区', '210102': '和平区', '210103': '沈河区', '210104': '大东区', '210105': '皇姑区', '210106': '铁西区', '210111': '苏家屯区', '210112': '东陵区', '210113': '沈北新区', '210114': '于洪区', '210122': '辽中县', '210123': '康平县', '210124': '法库县', '210181': '新民市', '210201': '市辖区', '210202': '中山区', '210203': '西岗区', '210204': '沙河口区', '210211': '甘井子区', '210212': '旅顺口区', '210213': '金州区', '210224': '长海县', '210281': '瓦房店市', '210282': '普兰店市', '210283': '庄河市', '210301': '市辖区', '210302': '铁东区', '210303': '铁西区', '210304': '立山区', '210311': '千山区', '210321': '台安县', '210323': '岫岩满族自治县', '210381': '海城市', '210401': '市辖区', '210402': '新抚区', '210403': '东洲区', '210404': '望花区', '210411': '顺城区', '210421': '抚顺县', '210422': '新宾满族自治县', '210423': '清原满族自治县', '210501': '市辖区', '210502': '平山区', '210503': '溪湖区', '210504': '明山区', '210505': '南芬区', '210521': '本溪满族自治县', '210522': '桓仁满族自治县', '210601': '市辖区', '210602': '元宝区', '210603': '振兴区', '210604': '振安区', '210624': '宽甸满族自治县', '210681': '东港市', '210682': '凤城市', '210701': '市辖区', '210702': '古塔区', '210703': '凌河区', '210711': '太和区', '210726': '黑山县', '210727': '义县', '210781': '凌海市', '210782': '北镇市', '210801': '市辖区', '210802': '站前区', '210803': '西市区', '210804': '鲅鱼圈区', '210811': '老边区', '210881': '盖州市', '210882': '大石桥市', '210901': '市辖区', '210902': '海州区', '210903': '新邱区', '210904': '太平区', '210905': '清河门区', '210911': '细河区', '210921': '阜新蒙古族自治县', '210922': '彰武县', '211001': '市辖区', '211002': '白塔区', '211003': '文圣区', '211004': '宏伟区', '211005': '弓长岭区', '211011': '太子河区', '211021': '辽阳县', '211081': '灯塔市', '211101': '市辖区', '211102': '双台子区', '211103': '兴隆台区', '211121': '大洼县', '211122': '盘山县', '211201': '市辖区', '211202': '银州区', '211204': '清河区', '211221': '铁岭县', '211223': '西丰县', '211224': '昌图县', '211281': '调兵山市', '211282': '开原市', '211301': '市辖区', '211302': '双塔区', '211303': '龙城区', '211321': '朝阳县', '211322': '建平县', '211324': '喀喇沁左翼蒙古族自治县', '211381': '北票市', '211382': '凌源市', '211401': '市辖区', '211402': '连山区', '211403': '龙港区', '211404': '南票区', '211421': '绥中县', '211422': '建昌县', '211481': '兴城市', '220101': '市辖区', '220102': '南关区', '220103': '宽城区', '220104': '朝阳区', '220105': '二道区', '220106': '绿园区', '220112': '双阳区', '220122': '农安县', '220181': '九台市', '220182': '榆树市', '220183': '德惠市', '220201': '市辖区', '220202': '昌邑区', '220203': '龙潭区', '220204': '船营区', '220211': '丰满区', '220221': '永吉县', '220281': '蛟河市', '220282': '桦甸市', '220283': '舒兰市', '220284': '磐石市', '220301': '市辖区', '220302': '铁西区', '220303': '铁东区', '220322': '梨树县', '220323': '伊通满族自治县', '220381': '公主岭市', '220382': '双辽市', '220401': '市辖区', '220402': '龙山区', '220403': '西安区', '220421': '东丰县', '220422': '东辽县', '220501': '市辖区', '220502': '东昌区', '220503': '二道江区', '220521': '通化县', '220523': '辉南县', '220524': '柳河县', '220581': '梅河口市', '220582': '集安市', '220601': '市辖区', '220602': '浑江区', '220605': '江源区', '220621': '抚松县', '220622': '靖宇县', '220623': '长白朝鲜族自治县', '220681': '临江市', '220701': '市辖区', '220702': '宁江区', '220721': '前郭尔罗斯蒙古族自治县', '220722': '长岭县', '220723': '乾安县', '220724': '扶余县', '220801': '市辖区', '220802': '洮北区', '220821': '镇赉县', '220822': '通榆县', '220881': '洮南市', '220882': '大安市', '222401': '延吉市', '222402': '图们市', '222403': '敦化市', '222404': '珲春市', '222405': '龙井市', '222406': '和龙市', '222424': '汪清县', '222426': '安图县', '230101': '市辖区', '230102': '道里区', '230103': '南岗区', '230104': '道外区', '230108': '平房区', '230109': '松北区', '230110': '香坊区', '230111': '呼兰区', '230112': '阿城区', '230123': '依兰县', '230124': '方正县', '230125': '宾县', '230126': '巴彦县', '230127': '木兰县', '230128': '通河县', '230129': '延寿县', '230182': '双城市', '230183': '尚志市', '230184': '五常市', '230201': '市辖区', '230202': '龙沙区', '230203': '建华区', '230204': '铁锋区', '230205': '昂昂溪区', '230206': '富拉尔基区', '230207': '碾子山区', '230208': '梅里斯达斡尔族区', '230221': '龙江县', '230223': '依安县', '230224': '泰来县', '230225': '甘南县', '230227': '富裕县', '230229': '克山县', '230230': '克东县', '230231': '拜泉县', '230281': '讷河市', '230301': '市辖区', '230302': '鸡冠区', '230303': '恒山区', '230304': '滴道区', '230305': '梨树区', '230306': '城子河区', '230307': '麻山区', '230321': '鸡东县', '230381': '虎林市', '230382': '密山市', '230401': '市辖区', '230402': '向阳区', '230403': '工农区', '230404': '南山区', '230405': '兴安区', '230406': '东山区', '230407': '兴山区', '230421': '萝北县', '230422': '绥滨县', '230501': '市辖区', '230502': '尖山区', '230503': '岭东区', '230505': '四方台区', '230506': '宝山区', '230521': '集贤县', '230522': '友谊县', '230523': '宝清县', '230524': '饶河县', '230601': '市辖区', '230602': '萨尔图区', '230603': '龙凤区', '230604': '让胡路区', '230605': '红岗区', '230606': '大同区', '230621': '肇州县', '230622': '肇源县', '230623': '林甸县', '230624': '杜尔伯特蒙古族自治县', '230701': '市辖区', '230702': '伊春区', '230703': '南岔区', '230704': '友好区', '230705': '西林区', '230706': '翠峦区', '230707': '新青区', '230708': '美溪区', '230709': '金山屯区', '230710': '五营区', '230711': '乌马河区', '230712': '汤旺河区', '230713': '带岭区', '230714': '乌伊岭区', '230715': '红星区', '230716': '上甘岭区', '230722': '嘉荫县', '230781': '铁力市', '230801': '市辖区', '230803': '向阳区', '230804': '前进区', '230805': '东风区', '230811': '郊区', '230822': '桦南县', '230826': '桦川县', '230828': '汤原县', '230833': '抚远县', '230881': '同江市', '230882': '富锦市', '230901': '市辖区', '230902': '新兴区', '230903': '桃山区', '230904': '茄子河区', '230921': '勃利县', '231001': '市辖区', '231002': '东安区', '231003': '阳明区', '231004': '爱民区', '231005': '西安区', '231024': '东宁县', '231025': '林口县', '231081': '绥芬河市', '231083': '海林市', '231084': '宁安市', '231085': '穆棱市', '231101': '市辖区', '231102': '爱辉区', '231121': '嫩江县', '231123': '逊克县', '231124': '孙吴县', '231181': '北安市', '231182': '五大连池市', '231201': '市辖区', '231202': '北林区', '231221': '望奎县', '231222': '兰西县', '231223': '青冈县', '231224': '庆安县', '231225': '明水县', '231226': '绥棱县', '231281': '安达市', '231282': '肇东市', '231283': '海伦市', '232721': '呼玛县', '232722': '塔河县', '232723': '漠河县', '310101': '黄浦区', '310104': '徐汇区', '310105': '长宁区', '310106': '静安区', '310107': '普陀区', '310108': '闸北区', '310109': '虹口区', '310110': '杨浦区', '310112': '闵行区', '310113': '宝山区', '310114': '嘉定区', '310115': '浦东新区', '310116': '金山区', '310117': '松江区', '310118': '青浦区', '310120': '奉贤区', '310230': '崇明县', '320101': '市辖区', '320102': '玄武区', '320103': '白下区', '320104': '秦淮区', '320105': '建邺区', '320106': '鼓楼区', '320107': '下关区', '320111': '浦口区', '320113': '栖霞区', '320114': '雨花台区', '320115': '江宁区', '320116': '六合区', '320124': '溧水县', '320125': '高淳县', '320201': '市辖区', '320202': '崇安区', '320203': '南长区', '320204': '北塘区', '320205': '锡山区', '320206': '惠山区', '320211': '滨湖区', '320281': '江阴市', '320282': '宜兴市', '320301': '市辖区', '320302': '鼓楼区', '320303': '云龙区', '320305': '贾汪区', '320311': '泉山区', '320312': '铜山区', '320321': '丰县', '320322': '沛县', '320324': '睢宁县', '320381': '新沂市', '320382': '邳州市', '320401': '市辖区', '320402': '天宁区', '320404': '钟楼区', '320405': '戚墅堰区', '320411': '新北区', '320412': '武进区', '320481': '溧阳市', '320482': '金坛市', '320501': '市辖区', '320505': '虎丘区', '320506': '吴中区', '320507': '相城区', '320508': '姑苏区', '320509': '吴江区', '320581': '常熟市', '320582': '张家港市', '320583': '昆山市', '320585': '太仓市', '320601': '市辖区', '320602': '崇川区', '320611': '港闸区', '320612': '通州区', '320621': '海安县', '320623': '如东县', '320681': '启东市', '320682': '如皋市', '320684': '海门市', '320701': '市辖区', '320703': '连云区', '320705': '新浦区', '320706': '海州区', '320721': '赣榆县', '320722': '东海县', '320723': '灌云县', '320724': '灌南县', '320801': '市辖区', '320802': '清河区', '320803': '淮安区', '320804': '淮阴区', '320811': '清浦区', '320826': '涟水县', '320829': '洪泽县', '320830': '盱眙县', '320831': '金湖县', '320901': '市辖区', '320902': '亭湖区', '320903': '盐都区', '320921': '响水县', '320922': '滨海县', '320923': '阜宁县', '320924': '射阳县', '320925': '建湖县', '320981': '东台市', '320982': '大丰市', '321001': '市辖区', '321002': '广陵区', '321003': '邗江区', '321012': '江都区', '321023': '宝应县', '321081': '仪征市', '321084': '高邮市', '321101': '市辖区', '321102': '京口区', '321111': '润州区', '321112': '丹徒区', '321181': '丹阳市', '321182': '扬中市', '321183': '句容市', '321201': '市辖区', '321202': '海陵区', '321203': '高港区', '321281': '兴化市', '321282': '靖江市', '321283': '泰兴市', '321284': '姜堰市', '321301': '市辖区', '321302': '宿城区', '321311': '宿豫区', '321322': '沭阳县', '321323': '泗阳县', '321324': '泗洪县', '330101': '市辖区', '330102': '上城区', '330103': '下城区', '330104': '江干区', '330105': '拱墅区', '330106': '西湖区', '330108': '滨江区', '330109': '萧山区', '330110': '余杭区', '330122': '桐庐县', '330127': '淳安县', '330182': '建德市', '330183': '富阳市', '330185': '临安市', '330201': '市辖区', '330203': '海曙区', '330204': '江东区', '330205': '江北区', '330206': '北仑区', '330211': '镇海区', '330212': '鄞州区', '330225': '象山县', '330226': '宁海县', '330281': '余姚市', '330282': '慈溪市', '330283': '奉化市', '330301': '市辖区', '330302': '鹿城区', '330303': '龙湾区', '330304': '瓯海区', '330322': '洞头县', '330324': '永嘉县', '330326': '平阳县', '330327': '苍南县', '330328': '文成县', '330329': '泰顺县', '330381': '瑞安市', '330382': '乐清市', '330401': '市辖区', '330402': '南湖区', '330411': '秀洲区', '330421': '嘉善县', '330424': '海盐县', '330481': '海宁市', '330482': '平湖市', '330483': '桐乡市', '330501': '市辖区', '330502': '吴兴区', '330503': '南浔区', '330521': '德清县', '330522': '长兴县', '330523': '安吉县', '330601': '市辖区', '330602': '越城区', '330621': '绍兴县', '330624': '新昌县', '330681': '诸暨市', '330682': '上虞市', '330683': '嵊州市', '330701': '市辖区', '330702': '婺城区', '330703': '金东区', '330723': '武义县', '330726': '浦江县', '330727': '磐安县', '330781': '兰溪市', '330782': '义乌市', '330783': '东阳市', '330784': '永康市', '330801': '市辖区', '330802': '柯城区', '330803': '衢江区', '330822': '常山县', '330824': '开化县', '330825': '龙游县', '330881': '江山市', '330901': '市辖区', '330902': '定海区', '330903': '普陀区', '330921': '岱山县', '330922': '嵊泗县', '331001': '市辖区', '331002': '椒江区', '331003': '黄岩区', '331004': '路桥区', '331021': '玉环县', '331022': '三门县', '331023': '天台县', '331024': '仙居县', '331081': '温岭市', '331082': '临海市', '331101': '市辖区', '331102': '莲都区', '331121': '青田县', '331122': '缙云县', '331123': '遂昌县', '331124': '松阳县', '331125': '云和县', '331126': '庆元县', '331127': '景宁畲族自治县', '331181': '龙泉市', '340101': '市辖区', '340102': '瑶海区', '340103': '庐阳区', '340104': '蜀山区', '340111': '包河区', '340121': '长丰县', '340122': '肥东县', '340123': '肥西县', '340124': '庐江县', '340181': '巢湖市', '340201': '市辖区', '340202': '镜湖区', '340203': '弋江区', '340207': '鸠江区', '340208': '三山区', '340221': '芜湖县', '340222': '繁昌县', '340223': '南陵县', '340225': '无为县', '340301': '市辖区', '340302': '龙子湖区', '340303': '蚌山区', '340304': '禹会区', '340311': '淮上区', '340321': '怀远县', '340322': '五河县', '340323': '固镇县', '340401': '市辖区', '340402': '大通区', '340403': '田家庵区', '340404': '谢家集区', '340405': '八公山区', '340406': '潘集区', '340421': '凤台县', '340501': '市辖区', '340503': '花山区', '340504': '雨山区', '340506': '博望区', '340521': '当涂县', '340522': '含山县', '340523': '和县', '340601': '市辖区', '340602': '杜集区', '340603': '相山区', '340604': '烈山区', '340621': '濉溪县', '340701': '市辖区', '340702': '铜官山区', '340703': '狮子山区', '340711': '郊区', '340721': '铜陵县', '340801': '市辖区', '340802': '迎江区', '340803': '大观区', '340811': '宜秀区', '340822': '怀宁县', '340823': '枞阳县', '340824': '潜山县', '340825': '太湖县', '340826': '宿松县', '340827': '望江县', '340828': '岳西县', '340881': '桐城市', '341001': '市辖区', '341002': '屯溪区', '341003': '黄山区', '341004': '徽州区', '341021': '歙县', '341022': '休宁县', '341023': '黟县', '341024': '祁门县', '341101': '市辖区', '341102': '琅琊区', '341103': '南谯区', '341122': '来安县', '341124': '全椒县', '341125': '定远县', '341126': '凤阳县', '341181': '天长市', '341182': '明光市', '341201': '市辖区', '341202': '颍州区', '341203': '颍东区', '341204': '颍泉区', '341221': '临泉县', '341222': '太和县', '341225': '阜南县', '341226': '颍上县', '341282': '界首市', '341301': '市辖区', '341302': '埇桥区', '341321': '砀山县', '341322': '萧县', '341323': '灵璧县', '341324': '泗县', '341501': '市辖区', '341502': '金安区', '341503': '裕安区', '341521': '寿县', '341522': '霍邱县', '341523': '舒城县', '341524': '金寨县', '341525': '霍山县', '341601': '市辖区', '341602': '谯城区', '341621': '涡阳县', '341622': '蒙城县', '341623': '利辛县', '341701': '市辖区', '341702': '贵池区', '341721': '东至县', '341722': '石台县', '341723': '青阳县', '341801': '市辖区', '341802': '宣州区', '341821': '郎溪县', '341822': '广德县', '341823': '泾县', '341824': '绩溪县', '341825': '旌德县', '341881': '宁国市', '350101': '市辖区', '350102': '鼓楼区', '350103': '台江区', '350104': '仓山区', '350105': '马尾区', '350111': '晋安区', '350121': '闽侯县', '350122': '连江县', '350123': '罗源县', '350124': '闽清县', '350125': '永泰县', '350128': '平潭县', '350181': '福清市', '350182': '长乐市', '350201': '市辖区', '350203': '思明区', '350205': '海沧区', '350206': '湖里区', '350211': '集美区', '350212': '同安区', '350213': '翔安区', '350301': '市辖区', '350302': '城厢区', '350303': '涵江区', '350304': '荔城区', '350305': '秀屿区', '350322': '仙游县', '350401': '市辖区', '350402': '梅列区', '350403': '三元区', '350421': '明溪县', '350423': '清流县', '350424': '宁化县', '350425': '大田县', '350426': '尤溪县', '350427': '沙县', '350428': '将乐县', '350429': '泰宁县', '350430': '建宁县', '350481': '永安市', '350501': '市辖区', '350502': '鲤城区', '350503': '丰泽区', '350504': '洛江区', '350505': '泉港区', '350521': '惠安县', '350524': '安溪县', '350525': '永春县', '350526': '德化县', '350527': '金门县', '350581': '石狮市', '350582': '晋江市', '350583': '南安市', '350601': '市辖区', '350602': '芗城区', '350603': '龙文区', '350622': '云霄县', '350623': '漳浦县', '350624': '诏安县', '350625': '长泰县', '350626': '东山县', '350627': '南靖县', '350628': '平和县', '350629': '华安县', '350681': '龙海市', '350701': '市辖区', '350702': '延平区', '350721': '顺昌县', '350722': '浦城县', '350723': '光泽县', '350724': '松溪县', '350725': '政和县', '350781': '邵武市', '350782': '武夷山市', '350783': '建瓯市', '350784': '建阳市', '350801': '市辖区', '350802': '新罗区', '350821': '长汀县', '350822': '永定县', '350823': '上杭县', '350824': '武平县', '350825': '连城县', '350881': '漳平市', '350901': '市辖区', '350902': '蕉城区', '350921': '霞浦县', '350922': '古田县', '350923': '屏南县', '350924': '寿宁县', '350925': '周宁县', '350926': '柘荣县', '350981': '福安市', '350982': '福鼎市', '360101': '市辖区', '360102': '东湖区', '360103': '西湖区', '360104': '青云谱区', '360105': '湾里区', '360111': '青山湖区', '360121': '南昌县', '360122': '新建县', '360123': '安义县', '360124': '进贤县', '360201': '市辖区', '360202': '昌江区', '360203': '珠山区', '360222': '浮梁县', '360281': '乐平市', '360301': '市辖区', '360302': '安源区', '360313': '湘东区', '360321': '莲花县', '360322': '上栗县', '360323': '芦溪县', '360401': '市辖区', '360402': '庐山区', '360403': '浔阳区', '360421': '九江县', '360423': '武宁县', '360424': '修水县', '360425': '永修县', '360426': '德安县', '360427': '星子县', '360428': '都昌县', '360429': '湖口县', '360430': '彭泽县', '360481': '瑞昌市', '360482': '共青城市', '360501': '市辖区', '360502': '渝水区', '360521': '分宜县', '360601': '市辖区', '360602': '月湖区', '360622': '余江县', '360681': '贵溪市', '360701': '市辖区', '360702': '章贡区', '360721': '赣县', '360722': '信丰县', '360723': '大余县', '360724': '上犹县', '360725': '崇义县', '360726': '安远县', '360727': '龙南县', '360728': '定南县', '360729': '全南县', '360730': '宁都县', '360731': '于都县', '360732': '兴国县', '360733': '会昌县', '360734': '寻乌县', '360735': '石城县', '360781': '瑞金市', '360782': '南康市', '360801': '市辖区', '360802': '吉州区', '360803': '青原区', '360821': '吉安县', '360822': '吉水县', '360823': '峡江县', '360824': '新干县', '360825': '永丰县', '360826': '泰和县', '360827': '遂川县', '360828': '万安县', '360829': '安福县', '360830': '永新县', '360881': '井冈山市', '360901': '市辖区', '360902': '袁州区', '360921': '奉新县', '360922': '万载县', '360923': '上高县', '360924': '宜丰县', '360925': '靖安县', '360926': '铜鼓县', '360981': '丰城市', '360982': '樟树市', '360983': '高安市', '361001': '市辖区', '361002': '临川区', '361021': '南城县', '361022': '黎川县', '361023': '南丰县', '361024': '崇仁县', '361025': '乐安县', '361026': '宜黄县', '361027': '金溪县', '361028': '资溪县', '361029': '东乡县', '361030': '广昌县', '361101': '市辖区', '361102': '信州区', '361121': '上饶县', '361122': '广丰县', '361123': '玉山县', '361124': '铅山县', '361125': '横峰县', '361126': '弋阳县', '361127': '余干县', '361128': '鄱阳县', '361129': '万年县', '361130': '婺源县', '361181': '德兴市', '370101': '市辖区', '370102': '历下区', '370103': '市中区', '370104': '槐荫区', '370105': '天桥区', '370112': '历城区', '370113': '长清区', '370124': '平阴县', '370125': '济阳县', '370126': '商河县', '370181': '章丘市', '370201': '市辖区', '370202': '市南区', '370203': '市北区', '370205': '四方区', '370211': '黄岛区', '370212': '崂山区', '370213': '李沧区', '370214': '城阳区', '370281': '胶州市', '370282': '即墨市', '370283': '平度市', '370284': '胶南市', '370285': '莱西市', '370301': '市辖区', '370302': '淄川区', '370303': '张店区', '370304': '博山区', '370305': '临淄区', '370306': '周村区', '370321': '桓台县', '370322': '高青县', '370323': '沂源县', '370401': '市辖区', '370402': '市中区', '370403': '薛城区', '370404': '峄城区', '370405': '台儿庄区', '370406': '山亭区', '370481': '滕州市', '370501': '市辖区', '370502': '东营区', '370503': '河口区', '370521': '垦利县', '370522': '利津县', '370523': '广饶县', '370601': '市辖区', '370602': '芝罘区', '370611': '福山区', '370612': '牟平区', '370613': '莱山区', '370634': '长岛县', '370681': '龙口市', '370682': '莱阳市', '370683': '莱州市', '370684': '蓬莱市', '370685': '招远市', '370686': '栖霞市', '370687': '海阳市', '370701': '市辖区', '370702': '潍城区', '370703': '寒亭区', '370704': '坊子区', '370705': '奎文区', '370724': '临朐县', '370725': '昌乐县', '370781': '青州市', '370782': '诸城市', '370783': '寿光市', '370784': '安丘市', '370785': '高密市', '370786': '昌邑市', '370801': '市辖区', '370802': '市中区', '370811': '任城区', '370826': '微山县', '370827': '鱼台县', '370828': '金乡县', '370829': '嘉祥县', '370830': '汶上县', '370831': '泗水县', '370832': '梁山县', '370881': '曲阜市', '370882': '兖州市', '370883': '邹城市', '370901': '市辖区', '370902': '泰山区', '370911': '岱岳区', '370921': '宁阳县', '370923': '东平县', '370982': '新泰市', '370983': '肥城市', '371001': '市辖区', '371002': '环翠区', '371081': '文登市', '371082': '荣成市', '371083': '乳山市', '371101': '市辖区', '371102': '东港区', '371103': '岚山区', '371121': '五莲县', '371122': '莒县', '371201': '市辖区', '371202': '莱城区', '371203': '钢城区', '371301': '市辖区', '371302': '兰山区', '371311': '罗庄区', '371312': '河东区', '371321': '沂南县', '371322': '郯城县', '371323': '沂水县', '371324': '苍山县', '371325': '费县', '371326': '平邑县', '371327': '莒南县', '371328': '蒙阴县', '371329': '临沭县', '371401': '市辖区', '371402': '德城区', '371421': '陵县', '371422': '宁津县', '371423': '庆云县', '371424': '临邑县', '371425': '齐河县', '371426': '平原县', '371427': '夏津县', '371428': '武城县', '371481': '乐陵市', '371482': '禹城市', '371501': '市辖区', '371502': '东昌府区', '371521': '阳谷县', '371522': '莘县', '371523': '茌平县', '371524': '东阿县', '371525': '冠县', '371526': '高唐县', '371581': '临清市', '371601': '市辖区', '371602': '滨城区', '371621': '惠民县', '371622': '阳信县', '371623': '无棣县', '371624': '沾化县', '371625': '博兴县', '371626': '邹平县', '371701': '市辖区', '371702': '牡丹区', '371721': '曹县', '371722': '单县', '371723': '成武县', '371724': '巨野县', '371725': '郓城县', '371726': '鄄城县', '371727': '定陶县', '371728': '东明县', '410101': '市辖区', '410102': '中原区', '410103': '二七区', '410104': '管城回族区', '410105': '金水区', '410106': '上街区', '410108': '惠济区', '410122': '中牟县', '410181': '巩义市', '410182': '荥阳市', '410183': '新密市', '410184': '新郑市', '410185': '登封市', '410201': '市辖区', '410202': '龙亭区', '410203': '顺河回族区', '410204': '鼓楼区', '410205': '禹王台区', '410211': '金明区', '410221': '杞县', '410222': '通许县', '410223': '尉氏县', '410224': '开封县', '410225': '兰考县', '410301': '市辖区', '410302': '老城区', '410303': '西工区', '410304': '瀍河回族区', '410305': '涧西区', '410306': '吉利区', '410311': '洛龙区', '410322': '孟津县', '410323': '新安县', '410324': '栾川县', '410325': '嵩县', '410326': '汝阳县', '410327': '宜阳县', '410328': '洛宁县', '410329': '伊川县', '410381': '偃师市', '410401': '市辖区', '410402': '新华区', '410403': '卫东区', '410404': '石龙区', '410411': '湛河区', '410421': '宝丰县', '410422': '叶县', '410423': '鲁山县', '410425': '郏县', '410481': '舞钢市', '410482': '汝州市', '410501': '市辖区', '410502': '文峰区', '410503': '北关区', '410505': '殷都区', '410506': '龙安区', '410522': '安阳县', '410523': '汤阴县', '410526': '滑县', '410527': '内黄县', '410581': '林州市', '410601': '市辖区', '410602': '鹤山区', '410603': '山城区', '410611': '淇滨区', '410621': '浚县', '410622': '淇县', '410701': '市辖区', '410702': '红旗区', '410703': '卫滨区', '410704': '凤泉区', '410711': '牧野区', '410721': '新乡县', '410724': '获嘉县', '410725': '原阳县', '410726': '延津县', '410727': '封丘县', '410728': '长垣县', '410781': '卫辉市', '410782': '辉县市', '410801': '市辖区', '410802': '解放区', '410803': '中站区', '410804': '马村区', '410811': '山阳区', '410821': '修武县', '410822': '博爱县', '410823': '武陟县', '410825': '温县', '410882': '沁阳市', '410883': '孟州市', '410901': '市辖区', '410902': '华龙区', '410922': '清丰县', '410923': '南乐县', '410926': '范县', '410927': '台前县', '410928': '濮阳县', '411001': '市辖区', '411002': '魏都区', '411023': '许昌县', '411024': '鄢陵县', '411025': '襄城县', '411081': '禹州市', '411082': '长葛市', '411101': '市辖区', '411102': '源汇区', '411103': '郾城区', '411104': '召陵区', '411121': '舞阳县', '411122': '临颍县', '411201': '市辖区', '411202': '湖滨区', '411221': '渑池县', '411222': '陕县', '411224': '卢氏县', '411281': '义马市', '411282': '灵宝市', '411301': '市辖区', '411302': '宛城区', '411303': '卧龙区', '411321': '南召县', '411322': '方城县', '411323': '西峡县', '411324': '镇平县', '411325': '内乡县', '411326': '淅川县', '411327': '社旗县', '411328': '唐河县', '411329': '新野县', '411330': '桐柏县', '411381': '邓州市', '411401': '市辖区', '411402': '梁园区', '411403': '睢阳区', '411421': '民权县', '411422': '睢县', '411423': '宁陵县', '411424': '柘城县', '411425': '虞城县', '411426': '夏邑县', '411481': '永城市', '411501': '市辖区', '411502': '浉河区', '411503': '平桥区', '411521': '罗山县', '411522': '光山县', '411523': '新县', '411524': '商城县', '411525': '固始县', '411526': '潢川县', '411527': '淮滨县', '411528': '息县', '411601': '市辖区', '411602': '川汇区', '411621': '扶沟县', '411622': '西华县', '411623': '商水县', '411624': '沈丘县', '411625': '郸城县', '411626': '淮阳县', '411627': '太康县', '411628': '鹿邑县', '411681': '项城市', '411701': '市辖区', '411702': '驿城区', '411721': '西平县', '411722': '上蔡县', '411723': '平舆县', '411724': '正阳县', '411725': '确山县', '411726': '泌阳县', '411727': '汝南县', '411728': '遂平县', '411729': '新蔡县', '419001': '济源市', '420101': '市辖区', '420102': '江岸区', '420103': '江汉区', '420104': '硚口区', '420105': '汉阳区', '420106': '武昌区', '420107': '青山区', '420111': '洪山区', '420112': '东西湖区', '420113': '汉南区', '420114': '蔡甸区', '420115': '江夏区', '420116': '黄陂区', '420117': '新洲区', '420201': '市辖区', '420202': '黄石港区', '420203': '西塞山区', '420204': '下陆区', '420205': '铁山区', '420222': '阳新县', '420281': '大冶市', '420301': '市辖区', '420302': '茅箭区', '420303': '张湾区', '420321': '郧县', '420322': '郧西县', '420323': '竹山县', '420324': '竹溪县', '420325': '房县', '420381': '丹江口市', '420501': '市辖区', '420502': '西陵区', '420503': '伍家岗区', '420504': '点军区', '420505': '猇亭区', '420506': '夷陵区', '420525': '远安县', '420526': '兴山县', '420527': '秭归县', '420528': '长阳土家族自治县', '420529': '五峰土家族自治县', '420581': '宜都市', '420582': '当阳市', '420583': '枝江市', '420601': '市辖区', '420602': '襄城区', '420606': '樊城区', '420607': '襄州区', '420624': '南漳县', '420625': '谷城县', '420626': '保康县', '420682': '老河口市', '420683': '枣阳市', '420684': '宜城市', '420701': '市辖区', '420702': '梁子湖区', '420703': '华容区', '420704': '鄂城区', '420801': '市辖区', '420802': '东宝区', '420804': '掇刀区', '420821': '京山县', '420822': '沙洋县', '420881': '钟祥市', '420901': '市辖区', '420902': '孝南区', '420921': '孝昌县', '420922': '大悟县', '420923': '云梦县', '420981': '应城市', '420982': '安陆市', '420984': '汉川市', '421001': '市辖区', '421002': '沙市区', '421003': '荆州区', '421022': '公安县', '421023': '监利县', '421024': '江陵县', '421081': '石首市', '421083': '洪湖市', '421087': '松滋市', '421101': '市辖区', '421102': '黄州区', '421121': '团风县', '421122': '红安县', '421123': '罗田县', '421124': '英山县', '421125': '浠水县', '421126': '蕲春县', '421127': '黄梅县', '421181': '麻城市', '421182': '武穴市', '421201': '市辖区', '421202': '咸安区', '421221': '嘉鱼县', '421222': '通城县', '421223': '崇阳县', '421224': '通山县', '421281': '赤壁市', '421301': '市辖区', '421303': '曾都区', '421321': '随县', '421381': '广水市', '422801': '恩施市', '422802': '利川市', '422822': '建始县', '422823': '巴东县', '422825': '宣恩县', '422826': '咸丰县', '422827': '来凤县', '422828': '鹤峰县', '429004': '仙桃市', '429005': '潜江市', '429006': '天门市', '429021': '神农架林区', '430101': '市辖区', '430102': '芙蓉区', '430103': '天心区', '430104': '岳麓区', '430105': '开福区', '430111': '雨花区', '430112': '望城区', '430121': '长沙县', '430124': '宁乡县', '430181': '浏阳市', '430201': '市辖区', '430202': '荷塘区', '430203': '芦淞区', '430204': '石峰区', '430211': '天元区', '430221': '株洲县', '430223': '攸县', '430224': '茶陵县', '430225': '炎陵县', '430281': '醴陵市', '430301': '市辖区', '430302': '雨湖区', '430304': '岳塘区', '430321': '湘潭县', '430381': '湘乡市', '430382': '韶山市', '430401': '市辖区', '430405': '珠晖区', '430406': '雁峰区', '430407': '石鼓区', '430408': '蒸湘区', '430412': '南岳区', '430421': '衡阳县', '430422': '衡南县', '430423': '衡山县', '430424': '衡东县', '430426': '祁东县', '430481': '耒阳市', '430482': '常宁市', '430501': '市辖区', '430502': '双清区', '430503': '大祥区', '430511': '北塔区', '430521': '邵东县', '430522': '新邵县', '430523': '邵阳县', '430524': '隆回县', '430525': '洞口县', '430527': '绥宁县', '430528': '新宁县', '430529': '城步苗族自治县', '430581': '武冈市', '430601': '市辖区', '430602': '岳阳楼区', '430603': '云溪区', '430611': '君山区', '430621': '岳阳县', '430623': '华容县', '430624': '湘阴县', '430626': '平江县', '430681': '汨罗市', '430682': '临湘市', '430701': '市辖区', '430702': '武陵区', '430703': '鼎城区', '430721': '安乡县', '430722': '汉寿县', '430723': '澧县', '430724': '临澧县', '430725': '桃源县', '430726': '石门县', '430781': '津市市', '430801': '市辖区', '430802': '永定区', '430811': '武陵源区', '430821': '慈利县', '430822': '桑植县', '430901': '市辖区', '430902': '资阳区', '430903': '赫山区', '430921': '南县', '430922': '桃江县', '430923': '安化县', '430981': '沅江市', '431001': '市辖区', '431002': '北湖区', '431003': '苏仙区', '431021': '桂阳县', '431022': '宜章县', '431023': '永兴县', '431024': '嘉禾县', '431025': '临武县', '431026': '汝城县', '431027': '桂东县', '431028': '安仁县', '431081': '资兴市', '431101': '市辖区', '431102': '零陵区', '431103': '冷水滩区', '431121': '祁阳县', '431122': '东安县', '431123': '双牌县', '431124': '道县', '431125': '江永县', '431126': '宁远县', '431127': '蓝山县', '431128': '新田县', '431129': '江华瑶族自治县', '431201': '市辖区', '431202': '鹤城区', '431221': '中方县', '431222': '沅陵县', '431223': '辰溪县', '431224': '溆浦县', '431225': '会同县', '431226': '麻阳苗族自治县', '431227': '新晃侗族自治县', '431228': '芷江侗族自治县', '431229': '靖州苗族侗族自治县', '431230': '通道侗族自治县', '431281': '洪江市', '431301': '市辖区', '431302': '娄星区', '431321': '双峰县', '431322': '新化县', '431381': '冷水江市', '431382': '涟源市', '433101': '吉首市', '433122': '泸溪县', '433123': '凤凰县', '433124': '花垣县', '433125': '保靖县', '433126': '古丈县', '433127': '永顺县', '433130': '龙山县', '440101': '市辖区', '440103': '荔湾区', '440104': '越秀区', '440105': '海珠区', '440106': '天河区', '440111': '白云区', '440112': '黄埔区', '440113': '番禺区', '440114': '花都区', '440115': '南沙区', '440116': '萝岗区', '440183': '增城市', '440184': '从化市', '440201': '市辖区', '440203': '武江区', '440204': '浈江区', '440205': '曲江区', '440222': '始兴县', '440224': '仁化县', '440229': '翁源县', '440232': '乳源瑶族自治县', '440233': '新丰县', '440281': '乐昌市', '440282': '南雄市', '440301': '市辖区', '440303': '罗湖区', '440304': '福田区', '440305': '南山区', '440306': '宝安区', '440307': '龙岗区', '440308': '盐田区', '440401': '市辖区', '440402': '香洲区', '440403': '斗门区', '440404': '金湾区', '440501': '市辖区', '440507': '龙湖区', '440511': '金平区', '440512': '濠江区', '440513': '潮阳区', '440514': '潮南区', '440515': '澄海区', '440523': '南澳县', '440601': '市辖区', '440604': '禅城区', '440605': '南海区', '440606': '顺德区', '440607': '三水区', '440608': '高明区', '440701': '市辖区', '440703': '蓬江区', '440704': '江海区', '440705': '新会区', '440781': '台山市', '440783': '开平市', '440784': '鹤山市', '440785': '恩平市', '440801': '市辖区', '440802': '赤坎区', '440803': '霞山区', '440804': '坡头区', '440811': '麻章区', '440823': '遂溪县', '440825': '徐闻县', '440881': '廉江市', '440882': '雷州市', '440883': '吴川市', '440901': '市辖区', '440902': '茂南区', '440903': '茂港区', '440923': '电白县', '440981': '高州市', '440982': '化州市', '440983': '信宜市', '441201': '市辖区', '441202': '端州区', '441203': '鼎湖区', '441223': '广宁县', '441224': '怀集县', '441225': '封开县', '441226': '德庆县', '441283': '高要市', '441284': '四会市', '441301': '市辖区', '441302': '惠城区', '441303': '惠阳区', '441322': '博罗县', '441323': '惠东县', '441324': '龙门县', '441401': '市辖区', '441402': '梅江区', '441421': '梅县', '441422': '大埔县', '441423': '丰顺县', '441424': '五华县', '441426': '平远县', '441427': '蕉岭县', '441481': '兴宁市', '441501': '市辖区', '441502': '城区', '441521': '海丰县', '441523': '陆河县', '441581': '陆丰市', '441601': '市辖区', '441602': '源城区', '441621': '紫金县', '441622': '龙川县', '441623': '连平县', '441624': '和平县', '441625': '东源县', '441701': '市辖区', '441702': '江城区', '441721': '阳西县', '441723': '阳东县', '441781': '阳春市', '441801': '市辖区', '441802': '清城区', '441821': '佛冈县', '441823': '阳山县', '441825': '连山壮族瑶族自治县', '441826': '连南瑶族自治县', '441827': '清新县', '441881': '英德市', '441882': '连州市', '445101': '市辖区', '445102': '湘桥区', '445121': '潮安县', '445122': '饶平县', '445201': '市辖区', '445202': '榕城区', '445221': '揭东县', '445222': '揭西县', '445224': '惠来县', '445281': '普宁市', '445301': '市辖区', '445302': '云城区', '445321': '新兴县', '445322': '郁南县', '445323': '云安县', '445381': '罗定市', '450101': '市辖区', '450102': '兴宁区', '450103': '青秀区', '450105': '江南区', '450107': '西乡塘区', '450108': '良庆区', '450109': '邕宁区', '450122': '武鸣县', '450123': '隆安县', '450124': '马山县', '450125': '上林县', '450126': '宾阳县', '450127': '横县', '450201': '市辖区', '450202': '城中区', '450203': '鱼峰区', '450204': '柳南区', '450205': '柳北区', '450221': '柳江县', '450222': '柳城县', '450223': '鹿寨县', '450224': '融安县', '450225': '融水苗族自治县', '450226': '三江侗族自治县', '450301': '市辖区', '450302': '秀峰区', '450303': '叠彩区', '450304': '象山区', '450305': '七星区', '450311': '雁山区', '450321': '阳朔县', '450322': '临桂县', '450323': '灵川县', '450324': '全州县', '450325': '兴安县', '450326': '永福县', '450327': '灌阳县', '450328': '龙胜各族自治县', '450329': '资源县', '450330': '平乐县', '450331': '荔浦县', '450332': '恭城瑶族自治县', '450401': '市辖区', '450403': '万秀区', '450404': '蝶山区', '450405': '长洲区', '450421': '苍梧县', '450422': '藤县', '450423': '蒙山县', '450481': '岑溪市', '450501': '市辖区', '450502': '海城区', '450503': '银海区', '450512': '铁山港区', '450521': '合浦县', '450601': '市辖区', '450602': '港口区', '450603': '防城区', '450621': '上思县', '450681': '东兴市', '450701': '市辖区', '450702': '钦南区', '450703': '钦北区', '450721': '灵山县', '450722': '浦北县', '450801': '市辖区', '450802': '港北区', '450803': '港南区', '450804': '覃塘区', '450821': '平南县', '450881': '桂平市', '450901': '市辖区', '450902': '玉州区', '450921': '容县', '450922': '陆川县', '450923': '博白县', '450924': '兴业县', '450981': '北流市', '451001': '市辖区', '451002': '右江区', '451021': '田阳县', '451022': '田东县', '451023': '平果县', '451024': '德保县', '451025': '靖西县', '451026': '那坡县', '451027': '凌云县', '451028': '乐业县', '451029': '田林县', '451030': '西林县', '451031': '隆林各族自治县', '451101': '市辖区', '451102': '八步区', '451121': '昭平县', '451122': '钟山县', '451123': '富川瑶族自治县', '451201': '市辖区', '451202': '金城江区', '451221': '南丹县', '451222': '天峨县', '451223': '凤山县', '451224': '东兰县', '451225': '罗城仫佬族自治县', '451226': '环江毛南族自治县', '451227': '巴马瑶族自治县', '451228': '都安瑶族自治县', '451229': '大化瑶族自治县', '451281': '宜州市', '451301': '市辖区', '451302': '兴宾区', '451321': '忻城县', '451322': '象州县', '451323': '武宣县', '451324': '金秀瑶族自治县', '451381': '合山市', '451401': '市辖区', '451402': '江洲区', '451421': '扶绥县', '451422': '宁明县', '451423': '龙州县', '451424': '大新县', '451425': '天等县', '451481': '凭祥市', '460101': '市辖区', '460105': '秀英区', '460106': '龙华区', '460107': '琼山区', '460108': '美兰区', '460201': '市辖区', '460321': '西沙群岛', '460322': '南沙群岛', '460323': '中沙群岛的岛礁及其海域', '469001': '五指山市', '469002': '琼海市', '469003': '儋州市', '469005': '文昌市', '469006': '万宁市', '469007': '东方市', '469021': '定安县', '469022': '屯昌县', '469023': '澄迈县', '469024': '临高县', '469025': '白沙黎族自治县', '469026': '昌江黎族自治县', '469027': '乐东黎族自治县', '469028': '陵水黎族自治县', '469029': '保亭黎族苗族自治县', '469030': '琼中黎族苗族自治县', '500101': '万州区', '500102': '涪陵区', '500103': '渝中区', '500104': '大渡口区', '500105': '江北区', '500106': '沙坪坝区', '500107': '九龙坡区', '500108': '南岸区', '500109': '北碚区', '500110': '綦江区', '500111': '大足区', '500112': '渝北区', '500113': '巴南区', '500114': '黔江区', '500115': '长寿区', '500116': '江津区', '500117': '合川区', '500118': '永川区', '500119': '南川区', '500223': '潼南县', '500224': '铜梁县', '500226': '荣昌县', '500227': '璧山县', '500228': '梁平县', '500229': '城口县', '500230': '丰都县', '500231': '垫江县', '500232': '武隆县', '500233': '忠县', '500234': '开县', '500235': '云阳县', '500236': '奉节县', '500237': '巫山县', '500238': '巫溪县', '500240': '石柱土家族自治县', '500241': '秀山土家族苗族自治县', '500242': '酉阳土家族苗族自治县', '500243': '彭水苗族土家族自治县', '510101': '市辖区', '510104': '锦江区', '510105': '青羊区', '510106': '金牛区', '510107': '武侯区', '510108': '成华区', '510112': '龙泉驿区', '510113': '青白江区', '510114': '新都区', '510115': '温江区', '510121': '金堂县', '510122': '双流县', '510124': '郫县', '510129': '大邑县', '510131': '蒲江县', '510132': '新津县', '510181': '都江堰市', '510182': '彭州市', '510183': '邛崃市', '510184': '崇州市', '510301': '市辖区', '510302': '自流井区', '510303': '贡井区', '510304': '大安区', '510311': '沿滩区', '510321': '荣县', '510322': '富顺县', '510401': '市辖区', '510402': '东区', '510403': '西区', '510411': '仁和区', '510421': '米易县', '510422': '盐边县', '510501': '市辖区', '510502': '江阳区', '510503': '纳溪区', '510504': '龙马潭区', '510521': '泸县', '510522': '合江县', '510524': '叙永县', '510525': '古蔺县', '510601': '市辖区', '510603': '旌阳区', '510623': '中江县', '510626': '罗江县', '510681': '广汉市', '510682': '什邡市', '510683': '绵竹市', '510701': '市辖区', '510703': '涪城区', '510704': '游仙区', '510722': '三台县', '510723': '盐亭县', '510724': '安县', '510725': '梓潼县', '510726': '北川羌族自治县', '510727': '平武县', '510781': '江油市', '510801': '市辖区', '510802': '利州区', '510811': '元坝区', '510812': '朝天区', '510821': '旺苍县', '510822': '青川县', '510823': '剑阁县', '510824': '苍溪县', '510901': '市辖区', '510903': '船山区', '510904': '安居区', '510921': '蓬溪县', '510922': '射洪县', '510923': '大英县', '511001': '市辖区', '511002': '市中区', '511011': '东兴区', '511024': '威远县', '511025': '资中县', '511028': '隆昌县', '511101': '市辖区', '511102': '市中区', '511111': '沙湾区', '511112': '五通桥区', '511113': '金口河区', '511123': '犍为县', '511124': '井研县', '511126': '夹江县', '511129': '沐川县', '511132': '峨边彝族自治县', '511133': '马边彝族自治县', '511181': '峨眉山市', '511301': '市辖区', '511302': '顺庆区', '511303': '高坪区', '511304': '嘉陵区', '511321': '南部县', '511322': '营山县', '511323': '蓬安县', '511324': '仪陇县', '511325': '西充县', '511381': '阆中市', '511401': '市辖区', '511402': '东坡区', '511421': '仁寿县', '511422': '彭山县', '511423': '洪雅县', '511424': '丹棱县', '511425': '青神县', '511501': '市辖区', '511502': '翠屏区', '511503': '南溪区', '511521': '宜宾县', '511523': '江安县', '511524': '长宁县', '511525': '高县', '511526': '珙县', '511527': '筠连县', '511528': '兴文县', '511529': '屏山县', '511601': '市辖区', '511602': '广安区', '511621': '岳池县', '511622': '武胜县', '511623': '邻水县', '511681': '华蓥市', '511701': '市辖区', '511702': '通川区', '511721': '达县', '511722': '宣汉县', '511723': '开江县', '511724': '大竹县', '511725': '渠县', '511781': '万源市', '511801': '市辖区', '511802': '雨城区', '511803': '名山区', '511822': '荥经县', '511823': '汉源县', '511824': '石棉县', '511825': '天全县', '511826': '芦山县', '511827': '宝兴县', '511901': '市辖区', '511902': '巴州区', '511921': '通江县', '511922': '南江县', '511923': '平昌县', '512001': '市辖区', '512002': '雁江区', '512021': '安岳县', '512022': '乐至县', '512081': '简阳市', '513221': '汶川县', '513222': '理县', '513223': '茂县', '513224': '松潘县', '513225': '九寨沟县', '513226': '金川县', '513227': '小金县', '513228': '黑水县', '513229': '马尔康县', '513230': '壤塘县', '513231': '阿坝县', '513232': '若尔盖县', '513233': '红原县', '513321': '康定县', '513322': '泸定县', '513323': '丹巴县', '513324': '九龙县', '513325': '雅江县', '513326': '道孚县', '513327': '炉霍县', '513328': '甘孜县', '513329': '新龙县', '513330': '德格县', '513331': '白玉县', '513332': '石渠县', '513333': '色达县', '513334': '理塘县', '513335': '巴塘县', '513336': '乡城县', '513337': '稻城县', '513338': '得荣县', '513401': '西昌市', '513422': '木里藏族自治县', '513423': '盐源县', '513424': '德昌县', '513425': '会理县', '513426': '会东县', '513427': '宁南县', '513428': '普格县', '513429': '布拖县', '513430': '金阳县', '513431': '昭觉县', '513432': '喜德县', '513433': '冕宁县', '513434': '越西县', '513435': '甘洛县', '513436': '美姑县', '513437': '雷波县', '520101': '市辖区', '520102': '南明区', '520103': '云岩区', '520111': '花溪区', '520112': '乌当区', '520113': '白云区', '520114': '小河区', '520121': '开阳县', '520122': '息烽县', '520123': '修文县', '520181': '清镇市', '520201': '钟山区', '520203': '六枝特区', '520221': '水城县', '520222': '盘县', '520301': '市辖区', '520302': '红花岗区', '520303': '汇川区', '520321': '遵义县', '520322': '桐梓县', '520323': '绥阳县', '520324': '正安县', '520325': '道真仡佬族苗族自治县', '520326': '务川仡佬族苗族自治县', '520327': '凤冈县', '520328': '湄潭县', '520329': '余庆县', '520330': '习水县', '520381': '赤水市', '520382': '仁怀市', '520401': '市辖区', '520402': '西秀区', '520421': '平坝县', '520422': '普定县', '520423': '镇宁布依族苗族自治县', '520424': '关岭布依族苗族自治县', '520425': '紫云苗族布依族自治县', '520502': '七星关区', '520521': '大方县', '520522': '黔西县', '520523': '金沙县', '520524': '织金县', '520525': '纳雍县', '520526': '威宁彝族回族苗族自治县', '520527': '赫章县', '520602': '碧江区', '520603': '万山区', '520621': '江口县', '520622': '玉屏侗族自治县', '520623': '石阡县', '520624': '思南县', '520625': '印江土家族苗族自治县', '520626': '德江县', '520627': '沿河土家族自治县', '520628': '松桃苗族自治县', '522301': '兴义市', '522322': '兴仁县', '522323': '普安县', '522324': '晴隆县', '522325': '贞丰县', '522326': '望谟县', '522327': '册亨县', '522328': '安龙县', '522601': '凯里市', '522622': '黄平县', '522623': '施秉县', '522624': '三穗县', '522625': '镇远县', '522626': '岑巩县', '522627': '天柱县', '522628': '锦屏县', '522629': '剑河县', '522630': '台江县', '522631': '黎平县', '522632': '榕江县', '522633': '从江县', '522634': '雷山县', '522635': '麻江县', '522636': '丹寨县', '522701': '都匀市', '522702': '福泉市', '522722': '荔波县', '522723': '贵定县', '522725': '瓮安县', '522726': '独山县', '522727': '平塘县', '522728': '罗甸县', '522729': '长顺县', '522730': '龙里县', '522731': '惠水县', '522732': '三都水族自治县', '530101': '市辖区', '530102': '五华区', '530103': '盘龙区', '530111': '官渡区', '530112': '西山区', '530113': '东川区', '530114': '呈贡区', '530122': '晋宁县', '530124': '富民县', '530125': '宜良县', '530126': '石林彝族自治县', '530127': '嵩明县', '530128': '禄劝彝族苗族自治县', '530129': '寻甸回族彝族自治县', '530181': '安宁市', '530301': '市辖区', '530302': '麒麟区', '530321': '马龙县', '530322': '陆良县', '530323': '师宗县', '530324': '罗平县', '530325': '富源县', '530326': '会泽县', '530328': '沾益县', '530381': '宣威市', '530402': '红塔区', '530421': '江川县', '530422': '澄江县', '530423': '通海县', '530424': '华宁县', '530425': '易门县', '530426': '峨山彝族自治县', '530427': '新平彝族傣族自治县', '530428': '元江哈尼族彝族傣族自治县', '530501': '市辖区', '530502': '隆阳区', '530521': '施甸县', '530522': '腾冲县', '530523': '龙陵县', '530524': '昌宁县', '530601': '市辖区', '530602': '昭阳区', '530621': '鲁甸县', '530622': '巧家县', '530623': '盐津县', '530624': '大关县', '530625': '永善县', '530626': '绥江县', '530627': '镇雄县', '530628': '彝良县', '530629': '威信县', '530630': '水富县', '530701': '市辖区', '530702': '古城区', '530721': '玉龙纳西族自治县', '530722': '永胜县', '530723': '华坪县', '530724': '宁蒗彝族自治县', '530801': '市辖区', '530802': '思茅区', '530821': '宁洱哈尼族彝族自治县', '530822': '墨江哈尼族自治县', '530823': '景东彝族自治县', '530824': '景谷傣族彝族自治县', '530825': '镇沅彝族哈尼族拉祜族自治县', '530826': '江城哈尼族彝族自治县', '530827': '孟连傣族拉祜族佤族自治县', '530828': '澜沧拉祜族自治县', '530829': '西盟佤族自治县', '530901': '市辖区', '530902': '临翔区', '530921': '凤庆县', '530922': '云县', '530923': '永德县', '530924': '镇康县', '530925': '双江拉祜族佤族布朗族傣族自治县', '530926': '耿马傣族佤族自治县', '530927': '沧源佤族自治县', '532301': '楚雄市', '532322': '双柏县', '532323': '牟定县', '532324': '南华县', '532325': '姚安县', '532326': '大姚县', '532327': '永仁县', '532328': '元谋县', '532329': '武定县', '532331': '禄丰县', '532501': '个旧市', '532502': '开远市', '532503': '蒙自市', '532523': '屏边苗族自治县', '532524': '建水县', '532525': '石屏县', '532526': '弥勒县', '532527': '泸西县', '532528': '元阳县', '532529': '红河县', '532530': '金平苗族瑶族傣族自治县', '532531': '绿春县', '532532': '河口瑶族自治县', '532601': '文山市', '532622': '砚山县', '532623': '西畴县', '532624': '麻栗坡县', '532625': '马关县', '532626': '丘北县', '532627': '广南县', '532628': '富宁县', '532801': '景洪市', '532822': '勐海县', '532823': '勐腊县', '532901': '大理市', '532922': '漾濞彝族自治县', '532923': '祥云县', '532924': '宾川县', '532925': '弥渡县', '532926': '南涧彝族自治县', '532927': '巍山彝族回族自治县', '532928': '永平县', '532929': '云龙县', '532930': '洱源县', '532931': '剑川县', '532932': '鹤庆县', '533102': '瑞丽市', '533103': '芒市', '533122': '梁河县', '533123': '盈江县', '533124': '陇川县', '533321': '泸水县', '533323': '福贡县', '533324': '贡山独龙族怒族自治县', '533325': '兰坪白族普米族自治县', '533421': '香格里拉县', '533422': '德钦县', '533423': '维西傈僳族自治县', '540101': '市辖区', '540102': '城关区', '540121': '林周县', '540122': '当雄县', '540123': '尼木县', '540124': '曲水县', '540125': '堆龙德庆县', '540126': '达孜县', '540127': '墨竹工卡县', '542121': '昌都县', '542122': '江达县', '542123': '贡觉县', '542124': '类乌齐县', '542125': '丁青县', '542126': '察雅县', '542127': '八宿县', '542128': '左贡县', '542129': '芒康县', '542132': '洛隆县', '542133': '边坝县', '542221': '乃东县', '542222': '扎囊县', '542223': '贡嘎县', '542224': '桑日县', '542225': '琼结县', '542226': '曲松县', '542227': '措美县', '542228': '洛扎县', '542229': '加查县', '542231': '隆子县', '542232': '错那县', '542233': '浪卡子县', '542301': '日喀则市', '542322': '南木林县', '542323': '江孜县', '542324': '定日县', '542325': '萨迦县', '542326': '拉孜县', '542327': '昂仁县', '542328': '谢通门县', '542329': '白朗县', '542330': '仁布县', '542331': '康马县', '542332': '定结县', '542333': '仲巴县', '542334': '亚东县', '542335': '吉隆县', '542336': '聂拉木县', '542337': '萨嘎县', '542338': '岗巴县', '542421': '那曲县', '542422': '嘉黎县', '542423': '比如县', '542424': '聂荣县', '542425': '安多县', '542426': '申扎县', '542427': '索县', '542428': '班戈县', '542429': '巴青县', '542430': '尼玛县', '542521': '普兰县', '542522': '札达县', '542523': '噶尔县', '542524': '日土县', '542525': '革吉县', '542526': '改则县', '542527': '措勤县', '542621': '林芝县', '542622': '工布江达县', '542623': '米林县', '542624': '墨脱县', '542625': '波密县', '542626': '察隅县', '542627': '朗县', '610101': '市辖区', '610102': '新城区', '610103': '碑林区', '610104': '莲湖区', '610111': '灞桥区', '610112': '未央区', '610113': '雁塔区', '610114': '阎良区', '610115': '临潼区', '610116': '长安区', '610122': '蓝田县', '610124': '周至县', '610125': '户县', '610126': '高陵县', '610201': '市辖区', '610202': '王益区', '610203': '印台区', '610204': '耀州区', '610222': '宜君县', '610301': '市辖区', '610302': '渭滨区', '610303': '金台区', '610304': '陈仓区', '610322': '凤翔县', '610323': '岐山县', '610324': '扶风县', '610326': '眉县', '610327': '陇县', '610328': '千阳县', '610329': '麟游县', '610330': '凤县', '610331': '太白县', '610401': '市辖区', '610402': '秦都区', '610403': '杨陵区', '610404': '渭城区', '610422': '三原县', '610423': '泾阳县', '610424': '乾县', '610425': '礼泉县', '610426': '永寿县', '610427': '彬县', '610428': '长武县', '610429': '旬邑县', '610430': '淳化县', '610431': '武功县', '610481': '兴平市', '610501': '市辖区', '610502': '临渭区', '610521': '华县', '610522': '潼关县', '610523': '大荔县', '610524': '合阳县', '610525': '澄城县', '610526': '蒲城县', '610527': '白水县', '610528': '富平县', '610581': '韩城市', '610582': '华阴市', '610601': '市辖区', '610602': '宝塔区', '610621': '延长县', '610622': '延川县', '610623': '子长县', '610624': '安塞县', '610625': '志丹县', '610626': '吴起县', '610627': '甘泉县', '610628': '富县', '610629': '洛川县', '610630': '宜川县', '610631': '黄龙县', '610632': '黄陵县', '610701': '市辖区', '610702': '汉台区', '610721': '南郑县', '610722': '城固县', '610723': '洋县', '610724': '西乡县', '610725': '勉县', '610726': '宁强县', '610727': '略阳县', '610728': '镇巴县', '610729': '留坝县', '610730': '佛坪县', '610801': '市辖区', '610802': '榆阳区', '610821': '神木县', '610822': '府谷县', '610823': '横山县', '610824': '靖边县', '610825': '定边县', '610826': '绥德县', '610827': '米脂县', '610828': '佳县', '610829': '吴堡县', '610830': '清涧县', '610831': '子洲县', '610901': '市辖区', '610902': '汉滨区', '610921': '汉阴县', '610922': '石泉县', '610923': '宁陕县', '610924': '紫阳县', '610925': '岚皋县', '610926': '平利县', '610927': '镇坪县', '610928': '旬阳县', '610929': '白河县', '611001': '市辖区', '611002': '商州区', '611021': '洛南县', '611022': '丹凤县', '611023': '商南县', '611024': '山阳县', '611025': '镇安县', '611026': '柞水县', '620101': '市辖区', '620102': '城关区', '620103': '七里河区', '620104': '西固区', '620105': '安宁区', '620111': '红古区', '620121': '永登县', '620122': '皋兰县', '620123': '榆中县', '620201': '市辖区', '620301': '市辖区', '620302': '金川区', '620321': '永昌县', '620401': '市辖区', '620402': '白银区', '620403': '平川区', '620421': '靖远县', '620422': '会宁县', '620423': '景泰县', '620501': '市辖区', '620502': '秦州区', '620503': '麦积区', '620521': '清水县', '620522': '秦安县', '620523': '甘谷县', '620524': '武山县', '620525': '张家川回族自治县', '620601': '市辖区', '620602': '凉州区', '620621': '民勤县', '620622': '古浪县', '620623': '天祝藏族自治县', '620701': '市辖区', '620702': '甘州区', '620721': '肃南裕固族自治县', '620722': '民乐县', '620723': '临泽县', '620724': '高台县', '620725': '山丹县', '620801': '市辖区', '620802': '崆峒区', '620821': '泾川县', '620822': '灵台县', '620823': '崇信县', '620824': '华亭县', '620825': '庄浪县', '620826': '静宁县', '620901': '市辖区', '620902': '肃州区', '620921': '金塔县', '620922': '瓜州县', '620923': '肃北蒙古族自治县', '620924': '阿克塞哈萨克族自治县', '620981': '玉门市', '620982': '敦煌市', '621001': '市辖区', '621002': '西峰区', '621021': '庆城县', '621022': '环县', '621023': '华池县', '621024': '合水县', '621025': '正宁县', '621026': '宁县', '621027': '镇原县', '621101': '市辖区', '621102': '安定区', '621121': '通渭县', '621122': '陇西县', '621123': '渭源县', '621124': '临洮县', '621125': '漳县', '621126': '岷县', '621201': '市辖区', '621202': '武都区', '621221': '成县', '621222': '文县', '621223': '宕昌县', '621224': '康县', '621225': '西和县', '621226': '礼县', '621227': '徽县', '621228': '两当县', '622901': '临夏市', '622921': '临夏县', '622922': '康乐县', '622923': '永靖县', '622924': '广河县', '622925': '和政县', '622926': '东乡族自治县', '622927': '积石山保安族东乡族撒拉族自治县', '623001': '合作市', '623021': '临潭县', '623022': '卓尼县', '623023': '舟曲县', '623024': '迭部县', '623025': '玛曲县', '623026': '碌曲县', '623027': '夏河县', '630101': '市辖区', '630102': '城东区', '630103': '城中区', '630104': '城西区', '630105': '城北区', '630121': '大通回族土族自治县', '630122': '湟中县', '630123': '湟源县', '632121': '平安县', '632122': '民和回族土族自治县', '632123': '乐都县', '632126': '互助土族自治县', '632127': '化隆回族自治县', '632128': '循化撒拉族自治县', '632221': '门源回族自治县', '632222': '祁连县', '632223': '海晏县', '632224': '刚察县', '632321': '同仁县', '632322': '尖扎县', '632323': '泽库县', '632324': '河南蒙古族自治县', '632521': '共和县', '632522': '同德县', '632523': '贵德县', '632524': '兴海县', '632525': '贵南县', '632621': '玛沁县', '632622': '班玛县', '632623': '甘德县', '632624': '达日县', '632625': '久治县', '632626': '玛多县', '632721': '玉树县', '632722': '杂多县', '632723': '称多县', '632724': '治多县', '632725': '囊谦县', '632726': '曲麻莱县', '632801': '格尔木市', '632802': '德令哈市', '632821': '乌兰县', '632822': '都兰县', '632823': '天峻县', '640101': '市辖区', '640104': '兴庆区', '640105': '西夏区', '640106': '金凤区', '640121': '永宁县', '640122': '贺兰县', '640181': '灵武市', '640201': '市辖区', '640202': '大武口区', '640205': '惠农区', '640221': '平罗县', '640301': '市辖区', '640302': '利通区', '640303': '红寺堡区', '640323': '盐池县', '640324': '同心县', '640381': '青铜峡市', '640401': '市辖区', '640402': '原州区', '640422': '西吉县', '640423': '隆德县', '640424': '泾源县', '640425': '彭阳县', '640501': '市辖区', '640502': '沙坡头区', '640521': '中宁县', '640522': '海原县', '650101': '市辖区', '650102': '天山区', '650103': '沙依巴克区', '650104': '新市区', '650105': '水磨沟区', '650106': '头屯河区', '650107': '达坂城区', '650109': '米东区', '650121': '乌鲁木齐县', '650201': '市辖区', '650202': '独山子区', '650203': '克拉玛依区', '650204': '白碱滩区', '650205': '乌尔禾区', '652101': '吐鲁番市', '652122': '鄯善县', '652123': '托克逊县', '652201': '哈密市', '652222': '巴里坤哈萨克自治县', '652223': '伊吾县', '652301': '昌吉市', '652302': '阜康市', '652323': '呼图壁县', '652324': '玛纳斯县', '652325': '奇台县', '652327': '吉木萨尔县', '652328': '木垒哈萨克自治县', '652701': '博乐市', '652722': '精河县', '652723': '温泉县', '652801': '库尔勒市', '652822': '轮台县', '652823': '尉犁县', '652824': '若羌县', '652825': '且末县', '652826': '焉耆回族自治县', '652827': '和静县', '652828': '和硕县', '652829': '博湖县', '652901': '阿克苏市', '652922': '温宿县', '652923': '库车县', '652924': '沙雅县', '652925': '新和县', '652926': '拜城县', '652927': '乌什县', '652928': '阿瓦提县', '652929': '柯坪县', '653001': '阿图什市', '653022': '阿克陶县', '653023': '阿合奇县', '653024': '乌恰县', '653101': '喀什市', '653121': '疏附县', '653122': '疏勒县', '653123': '英吉沙县', '653124': '泽普县', '653125': '莎车县', '653126': '叶城县', '653127': '麦盖提县', '653128': '岳普湖县', '653129': '伽师县', '653130': '巴楚县', '653131': '塔什库尔干塔吉克自治县', '653201': '和田市', '653221': '和田县', '653222': '墨玉县', '653223': '皮山县', '653224': '洛浦县', '653225': '策勒县', '653226': '于田县', '653227': '民丰县', '654002': '伊宁市', '654003': '奎屯市', '654021': '伊宁县', '654022': '察布查尔锡伯自治县', '654023': '霍城县', '654024': '巩留县', '654025': '新源县', '654026': '昭苏县', '654027': '特克斯县', '654028': '尼勒克县', '654201': '塔城市', '654202': '乌苏市', '654221': '额敏县', '654223': '沙湾县', '654224': '托里县', '654225': '裕民县', '654226': '和布克赛尔蒙古自治县', '654301': '阿勒泰市', '654321': '布尔津县', '654322': '富蕴县', '654323': '福海县', '654324': '哈巴河县', '654325': '青河县', '654326': '吉木乃县', '659001': '石河子市', '659002': '阿拉尔市', '659003': '图木舒克市', '659004': '五家渠市'}

area_dict = {'110101': '东城区', '110102': '西城区', '110105': '朝阳区', '110106': '丰台区', '110107': '石景山区', '110108': '海淀区', '110109': '门头沟区', '110111': '房山区', '110112': '通州区', '110113': '顺义区', '110114': '昌平区', '110115': '大兴区', '110116': '怀柔区', '110117': '平谷区', '110228': '密云县', '110229': '延庆县', '120101': '和平区', '120102': '河东区', '120103': '河西区', '120104': '南开区', '120105': '河北区', '120106': '红桥区', '120110': '东丽区', '120111': '西青区', '120112': '津南区', '120113': '北辰区', '120114': '武清区', '120115': '宝坻区', '120116': '滨海新区', '120221': '宁河县', '120223': '静海县', '120225': '蓟县', '130101': '市辖区', '130102': '长安区', '130103': '桥东区', '130104': '桥西区', '130105': '新华区', '130107': '井陉矿区', '130108': '裕华区', '130121': '井陉县', '130123': '正定县', '130124': '栾城县', '130125': '行唐县', '130126': '灵寿县', '130127': '高邑县', '130128': '深泽县', '130129': '赞皇县', '130130': '无极县', '130131': '平山县', '130132': '元氏县', '130133': '赵县', '130181': '辛集市', '130182': '藁城市', '130183': '晋州市', '130184': '新乐市', '130185': '鹿泉市', '130201': '市辖区', '130202': '路南区', '130203': '路北区', '130204': '古冶区', '130205': '开平区', '130207': '丰南区', '130208': '丰润区', '130209': '曹妃甸区', '130223': '滦县', '130224': '滦南县', '130225': '乐亭县', '130227': '迁西县', '130229': '玉田县', '130281': '遵化市', '130283': '迁安市', '130301': '市辖区', '130302': '海港区', '130303': '山海关区', '130304': '北戴河区', '130321': '青龙满族自治县', '130322': '昌黎县', '130323': '抚宁县', '130324': '卢龙县', '130401': '市辖区', '130402': '邯山区', '130403': '丛台区', '130404': '复兴区', '130406': '峰峰矿区', '130421': '邯郸县', '130423': '临漳县', '130424': '成安县', '130425': '大名县', '130426': '涉县', '130427': '磁县', '130428': '肥乡县', '130429': '永年县', '130430': '邱县', '130431': '鸡泽县', '130432': '广平县', '130433': '馆陶县', '130434': '魏县', '130435': '曲周县', '130481': '武安市', '130501': '市辖区', '130502': '桥东区', '130503': '桥西区', '130521': '邢台县', '130522': '临城县', '130523': '内丘县', '130524': '柏乡县', '130525': '隆尧县', '130526': '任县', '130527': '南和县', '130528': '宁晋县', '130529': '巨鹿县', '130530': '新河县', '130531': '广宗县', '130532': '平乡县', '130533': '威县', '130534': '清河县', '130535': '临西县', '130581': '南宫市', '130582': '沙河市', '130601': '市辖区', '130602': '新市区', '130603': '北市区', '130604': '南市区', '130621': '满城县', '130622': '清苑县', '130623': '涞水县', '130624': '阜平县', '130625': '徐水县', '130626': '定兴县', '130627': '唐县', '130628': '高阳县', '130629': '容城县', '130630': '涞源县', '130631': '望都县', '130632': '安新县', '130633': '易县', '130634': '曲阳县', '130635': '蠡县', '130636': '顺平县', '130637': '博野县', '130638': '雄县', '130681': '涿州市', '130682': '定州市', '130683': '安国市', '130684': '高碑店市', '130701': '市辖区', '130702': '桥东区', '130703': '桥西区', '130705': '宣化区', '130706': '下花园区', '130721': '宣化县', '130722': '张北县', '130723': '康保县', '130724': '沽源县', '130725': '尚义县', '130726': '蔚县', '130727': '阳原县', '130728': '怀安县', '130729': '万全县', '130730': '怀来县', '130731': '涿鹿县', '130732': '赤城县', '130733': '崇礼县', '130801': '市辖区', '130802': '双桥区', '130803': '双滦区', '130804': '鹰手营子矿区', '130821': '承德县', '130822': '兴隆县', '130823': '平泉县', '130824': '滦平县', '130825': '隆化县', '130826': '丰宁满族自治县', '130827': '宽城满族自治县', '130828': '围场满族蒙古族自治县', '130901': '市辖区', '130902': '新华区', '130903': '运河区', '130921': '沧县', '130922': '青县', '130923': '东光县', '130924': '海兴县', '130925': '盐山县', '130926': '肃宁县', '130927': '南皮县', '130928': '吴桥县', '130929': '献县', '130930': '孟村回族自治县', '130981': '泊头市', '130982': '任丘市', '130983': '黄骅市', '130984': '河间市', '131001': '市辖区', '131002': '安次区', '131003': '广阳区', '131022': '固安县', '131023': '永清县', '131024': '香河县', '131025': '大城县', '131026': '文安县', '131028': '大厂回族自治县', '131081': '霸州市', '131082': '三河市', '131101': '市辖区', '131102': '桃城区', '131121': '枣强县', '131122': '武邑县', '131123': '武强县', '131124': '饶阳县', '131125': '安平县', '131126': '故城县', '131127': '景县', '131128': '阜城县', '131181': '冀州市', '131182': '深州市', '140101': '市辖区', '140105': '小店区', '140106': '迎泽区', '140107': '杏花岭区', '140108': '尖草坪区', '140109': '万柏林区', '140110': '晋源区', '140121': '清徐县', '140122': '阳曲县', '140123': '娄烦县', '140181': '古交市', '140201': '市辖区', '140202': '城区', '140203': '矿区', '140211': '南郊区', '140212': '新荣区', '140221': '阳高县', '140222': '天镇县', '140223': '广灵县', '140224': '灵丘县', '140225': '浑源县', '140226': '左云县', '140227': '大同县', '140301': '市辖区', '140302': '城区', '140303': '矿区', '140311': '郊区', '140321': '平定县', '140322': '盂县', '140401': '市辖区', '140402': '城区', '140411': '郊区', '140421': '长治县', '140423': '襄垣县', '140424': '屯留县', '140425': '平顺县', '140426': '黎城县', '140427': '壶关县', '140428': '长子县', '140429': '武乡县', '140430': '沁县', '140431': '沁源县', '140481': '潞城市', '140501': '市辖区', '140502': '城区', '140521': '沁水县', '140522': '阳城县', '140524': '陵川县', '140525': '泽州县', '140581': '高平市', '140601': '市辖区', '140602': '朔城区', '140603': '平鲁区', '140621': '山阴县', '140622': '应县', '140623': '右玉县', '140624': '怀仁县', '140701': '市辖区', '140702': '榆次区', '140721': '榆社县', '140722': '左权县', '140723': '和顺县', '140724': '昔阳县', '140725': '寿阳县', '140726': '太谷县', '140727': '祁县', '140728': '平遥县', '140729': '灵石县', '140781': '介休市', '140801': '市辖区', '140802': '盐湖区', '140821': '临猗县', '140822': '万荣县', '140823': '闻喜县', '140824': '稷山县', '140825': '新绛县', '140826': '绛县', '140827': '垣曲县', '140828': '夏县', '140829': '平陆县', '140830': '芮城县', '140881': '永济市', '140882': '河津市', '140901': '市辖区', '140902': '忻府区', '140921': '定襄县', '140922': '五台县', '140923': '代县', '140924': '繁峙县', '140925': '宁武县', '140926': '静乐县', '140927': '神池县', '140928': '五寨县', '140929': '岢岚县', '140930': '河曲县', '140931': '保德县', '140932': '偏关县', '140981': '原平市', '141001': '市辖区', '141002': '尧都区', '141021': '曲沃县', '141022': '翼城县', '141023': '襄汾县', '141024': '洪洞县', '141025': '古县', '141026': '安泽县', '141027': '浮山县', '141028': '吉县', '141029': '乡宁县', '141030': '大宁县', '141031': '隰县', '141032': '永和县', '141033': '蒲县', '141034': '汾西县', '141081': '侯马市', '141082': '霍州市', '141101': '市辖区', '141102': '离石区', '141121': '文水县', '141122': '交城县', '141123': '兴县', '141124': '临县', '141125': '柳林县', '141126': '石楼县', '141127': '岚县', '141128': '方山县', '141129': '中阳县', '141130': '交口县', '141181': '孝义市', '141182': '汾阳市', '150101': '市辖区', '150102': '新城区', '150103': '回民区', '150104': '玉泉区', '150105': '赛罕区', '150121': '土默特左旗', '150122': '托克托县', '150123': '和林格尔县', '150124': '清水河县', '150125': '武川县', '150201': '市辖区', '150202': '东河区', '150203': '昆都仑区', '150204': '青山区', '150205': '石拐区', '150206': '白云鄂博矿区', '150207': '九原区', '150221': '土默特右旗', '150222': '固阳县', '150223': '达尔罕茂明安联合旗', '150301': '市辖区', '150302': '海勃湾区', '150303': '海南区', '150304': '乌达区', '150401': '市辖区', '150402': '红山区', '150403': '元宝山区', '150404': '松山区', '150421': '阿鲁科尔沁旗', '150422': '巴林左旗', '150423': '巴林右旗', '150424': '林西县', '150425': '克什克腾旗', '150426': '翁牛特旗', '150428': '喀喇沁旗', '150429': '宁城县', '150430': '敖汉旗', '150501': '市辖区', '150502': '科尔沁区', '150521': '科尔沁左翼中旗', '150522': '科尔沁左翼后旗', '150523': '开鲁县', '150524': '库伦旗', '150525': '奈曼旗', '150526': '扎鲁特旗', '150581': '霍林郭勒市', '150601': '市辖区', '150602': '东胜区', '150621': '达拉特旗', '150622': '准格尔旗', '150623': '鄂托克前旗', '150624': '鄂托克旗', '150625': '杭锦旗', '150626': '乌审旗', '150627': '伊金霍洛旗', '150701': '市辖区', '150702': '海拉尔区', '150721': '阿荣旗', '150722': '莫力达瓦达斡尔族自治旗', '150723': '鄂伦春自治旗', '150724': '鄂温克族自治旗', '150725': '陈巴尔虎旗', '150726': '新巴尔虎左旗', '150727': '新巴尔虎右旗', '150781': '满洲里市', '150782': '牙克石市', '150783': '扎兰屯市', '150784': '额尔古纳市', '150785': '根河市', '150801': '市辖区', '150802': '临河区', '150821': '五原县', '150822': '磴口县', '150823': '乌拉特前旗', '150824': '乌拉特中旗', '150825': '乌拉特后旗', '150826': '杭锦后旗', '150901': '市辖区', '150902': '集宁区', '150921': '卓资县', '150922': '化德县', '150923': '商都县', '150924': '兴和县', '150925': '凉城县', '150926': '察哈尔右翼前旗', '150927': '察哈尔右翼中旗', '150928': '察哈尔右翼后旗', '150929': '四子王旗', '150981': '丰镇市', '152201': '乌兰浩特市', '152202': '阿尔山市', '152221': '科尔沁右翼前旗', '152222': '科尔沁右翼中旗', '152223': '扎赉特旗', '152224': '突泉县', '152501': '二连浩特市', '152502': '锡林浩特市', '152522': '阿巴嘎旗', '152523': '苏尼特左旗', '152524': '苏尼特右旗', '152525': '东乌珠穆沁旗', '152526': '西乌珠穆沁旗', '152527': '太仆寺旗', '152528': '镶黄旗', '152529': '正镶白旗', '152530': '正蓝旗', '152531': '多伦县', '152921': '阿拉善左旗', '152922': '阿拉善右旗', '152923': '额济纳旗', '210101': '市辖区', '210102': '和平区', '210103': '沈河区', '210104': '大东区', '210105': '皇姑区', '210106': '铁西区', '210111': '苏家屯区', '210112': '东陵区', '210113': '沈北新区', '210114': '于洪区', '210122': '辽中县', '210123': '康平县', '210124': '法库县', '210181': '新民市', '210201': '市辖区', '210202': '中山区', '210203': '西岗区', '210204': '沙河口区', '210211': '甘井子区', '210212': '旅顺口区', '210213': '金州区', '210224': '长海县', '210281': '瓦房店市', '210282': '普兰店市', '210283': '庄河市', '210301': '市辖区', '210302': '铁东区', '210303': '铁西区', '210304': '立山区', '210311': '千山区', '210321': '台安县', '210323': '岫岩满族自治县', '210381': '海城市', '210401': '市辖区', '210402': '新抚区', '210403': '东洲区', '210404': '望花区', '210411': '顺城区', '210421': '抚顺县', '210422': '新宾满族自治县', '210423': '清原满族自治县', '210501': '市辖区', '210502': '平山区', '210503': '溪湖区', '210504': '明山区', '210505': '南芬区', '210521': '本溪满族自治县', '210522': '桓仁满族自治县', '210601': '市辖区', '210602': '元宝区', '210603': '振兴区', '210604': '振安区', '210624': '宽甸满族自治县', '210681': '东港市', '210682': '凤城市', '210701': '市辖区', '210702': '古塔区', '210703': '凌河区', '210711': '太和区', '210726': '黑山县', '210727': '义县', '210781': '凌海市', '210782': '北镇市', '210801': '市辖区', '210802': '站前区', '210803': '西市区', '210804': '鲅鱼圈区', '210811': '老边区', '210881': '盖州市', '210882': '大石桥市', '210901': '市辖区', '210902': '海州区', '210903': '新邱区', '210904': '太平区', '210905': '清河门区', '210911': '细河区', '210921': '阜新蒙古族自治县', '210922': '彰武县', '211001': '市辖区', '211002': '白塔区', '211003': '文圣区', '211004': '宏伟区', '211005': '弓长岭区', '211011': '太子河区', '211021': '辽阳县', '211081': '灯塔市', '211101': '市辖区', '211102': '双台子区', '211103': '兴隆台区', '211121': '大洼县', '211122': '盘山县', '211201': '市辖区', '211202': '银州区', '211204': '清河区', '211221': '铁岭县', '211223': '西丰县', '211224': '昌图县', '211281': '调兵山市', '211282': '开原市', '211301': '市辖区', '211302': '双塔区', '211303': '龙城区', '211321': '朝阳县', '211322': '建平县', '211324': '喀喇沁左翼蒙古族自治县', '211381': '北票市', '211382': '凌源市', '211401': '市辖区', '211402': '连山区', '211403': '龙港区', '211404': '南票区', '211421': '绥中县', '211422': '建昌县', '211481': '兴城市', '220101': '市辖区', '220102': '南关区', '220103': '宽城区', '220104': '朝阳区', '220105': '二道区', '220106': '绿园区', '220112': '双阳区', '220122': '农安县', '220181': '九台市', '220182': '榆树市', '220183': '德惠市', '220201': '市辖区', '220202': '昌邑区', '220203': '龙潭区', '220204': '船营区', '220211': '丰满区', '220221': '永吉县', '220281': '蛟河市', '220282': '桦甸市', '220283': '舒兰市', '220284': '磐石市', '220301': '市辖区', '220302': '铁西区', '220303': '铁东区', '220322': '梨树县', '220323': '伊通满族自治县', '220381': '公主岭市', '220382': '双辽市', '220401': '市辖区', '220402': '龙山区', '220403': '西安区', '220421': '东丰县', '220422': '东辽县', '220501': '市辖区', '220502': '东昌区', '220503': '二道江区', '220521': '通化县', '220523': '辉南县', '220524': '柳河县', '220581': '梅河口市', '220582': '集安市', '220601': '市辖区', '220602': '浑江区', '220605': '江源区', '220621': '抚松县', '220622': '靖宇县', '220623': '长白朝鲜族自治县', '220681': '临江市', '220701': '市辖区', '220702': '宁江区', '220721': '前郭尔罗斯蒙古族自治县', '220722': '长岭县', '220723': '乾安县', '220724': '扶余县', '220801': '市辖区', '220802': '洮北区', '220821': '镇赉县', '220822': '通榆县', '220881': '洮南市', '220882': '大安市', '222401': '延吉市', '222402': '图们市', '222403': '敦化市', '222404': '珲春市', '222405': '龙井市', '222406': '和龙市', '222424': '汪清县', '222426': '安图县', '230101': '市辖区', '230102': '道里区', '230103': '南岗区', '230104': '道外区', '230108': '平房区', '230109': '松北区', '230110': '香坊区', '230111': '呼兰区', '230112': '阿城区', '230123': '依兰县', '230124': '方正县', '230125': '宾县', '230126': '巴彦县', '230127': '木兰县', '230128': '通河县', '230129': '延寿县', '230182': '双城市', '230183': '尚志市', '230184': '五常市', '230201': '市辖区', '230202': '龙沙区', '230203': '建华区', '230204': '铁锋区', '230205': '昂昂溪区', '230206': '富拉尔基区', '230207': '碾子山区', '230208': '梅里斯达斡尔族区', '230221': '龙江县', '230223': '依安县', '230224': '泰来县', '230225': '甘南县', '230227': '富裕县', '230229': '克山县', '230230': '克东县', '230231': '拜泉县', '230281': '讷河市', '230301': '市辖区', '230302': '鸡冠区', '230303': '恒山区', '230304': '滴道区', '230305': '梨树区', '230306': '城子河区', '230307': '麻山区', '230321': '鸡东县', '230381': '虎林市', '230382': '密山市', '230401': '市辖区', '230402': '向阳区', '230403': '工农区', '230404': '南山区', '230405': '兴安区', '230406': '东山区', '230407': '兴山区', '230421': '萝北县', '230422': '绥滨县', '230501': '市辖区', '230502': '尖山区', '230503': '岭东区', '230505': '四方台区', '230506': '宝山区', '230521': '集贤县', '230522': '友谊县', '230523': '宝清县', '230524': '饶河县', '230601': '市辖区', '230602': '萨尔图区', '230603': '龙凤区', '230604': '让胡路区', '230605': '红岗区', '230606': '大同区', '230621': '肇州县', '230622': '肇源县', '230623': '林甸县', '230624': '杜尔伯特蒙古族自治县', '230701': '市辖区', '230702': '伊春区', '230703': '南岔区', '230704': '友好区', '230705': '西林区', '230706': '翠峦区', '230707': '新青区', '230708': '美溪区', '230709': '金山屯区', '230710': '五营区', '230711': '乌马河区', '230712': '汤旺河区', '230713': '带岭区', '230714': '乌伊岭区', '230715': '红星区', '230716': '上甘岭区', '230722': '嘉荫县', '230781': '铁力市', '230801': '市辖区', '230803': '向阳区', '230804': '前进区', '230805': '东风区', '230811': '郊区', '230822': '桦南县', '230826': '桦川县', '230828': '汤原县', '230833': '抚远县', '230881': '同江市', '230882': '富锦市', '230901': '市辖区', '230902': '新兴区', '230903': '桃山区', '230904': '茄子河区', '230921': '勃利县', '231001': '市辖区', '231002': '东安区', '231003': '阳明区', '231004': '爱民区', '231005': '西安区', '231024': '东宁县', '231025': '林口县', '231081': '绥芬河市', '231083': '海林市', '231084': '宁安市', '231085': '穆棱市', '231101': '市辖区', '231102': '爱辉区', '231121': '嫩江县', '231123': '逊克县', '231124': '孙吴县', '231181': '北安市', '231182': '五大连池市', '231201': '市辖区', '231202': '北林区', '231221': '望奎县', '231222': '兰西县', '231223': '青冈县', '231224': '庆安县', '231225': '明水县', '231226': '绥棱县', '231281': '安达市', '231282': '肇东市', '231283': '海伦市', '232721': '呼玛县', '232722': '塔河县', '232723': '漠河县', '310101': '黄浦区', '310104': '徐汇区', '310105': '长宁区', '310106': '静安区', '310107': '普陀区', '310108': '闸北区', '310109': '虹口区', '310110': '杨浦区', '310112': '闵行区', '310113': '宝山区', '310114': '嘉定区', '310115': '浦东新区', '310116': '金山区', '310117': '松江区', '310118': '青浦区', '310120': '奉贤区', '310230': '崇明县', '320101': '市辖区', '320102': '玄武区', '320103': '白下区', '320104': '秦淮区', '320105': '建邺区', '320106': '鼓楼区', '320107': '下关区', '320111': '浦口区', '320113': '栖霞区', '320114': '雨花台区', '320115': '江宁区', '320116': '六合区', '320124': '溧水县', '320125': '高淳县', '320201': '市辖区', '320202': '崇安区', '320203': '南长区', '320204': '北塘区', '320205': '锡山区', '320206': '惠山区', '320211': '滨湖区', '320281': '江阴市', '320282': '宜兴市', '320301': '市辖区', '320302': '鼓楼区', '320303': '云龙区', '320305': '贾汪区', '320311': '泉山区', '320312': '铜山区', '320321': '丰县', '320322': '沛县', '320324': '睢宁县', '320381': '新沂市', '320382': '邳州市', '320401': '市辖区', '320402': '天宁区', '320404': '钟楼区', '320405': '戚墅堰区', '320411': '新北区', '320412': '武进区', '320481': '溧阳市', '320482': '金坛市', '320501': '市辖区', '320505': '虎丘区', '320506': '吴中区', '320507': '相城区', '320508': '姑苏区', '320509': '吴江区', '320581': '常熟市', '320582': '张家港市', '320583': '昆山市', '320585': '太仓市', '320601': '市辖区', '320602': '崇川区', '320611': '港闸区', '320612': '通州区', '320621': '海安县', '320623': '如东县', '320681': '启东市', '320682': '如皋市', '320684': '海门市', '320701': '市辖区', '320703': '连云区', '320705': '新浦区', '320706': '海州区', '320721': '赣榆县', '320722': '东海县', '320723': '灌云县', '320724': '灌南县', '320801': '市辖区', '320802': '清河区', '320803': '淮安区', '320804': '淮阴区', '320811': '清浦区', '320826': '涟水县', '320829': '洪泽县', '320830': '盱眙县', '320831': '金湖县', '320901': '市辖区', '320902': '亭湖区', '320903': '盐都区', '320921': '响水县', '320922': '滨海县', '320923': '阜宁县', '320924': '射阳县', '320925': '建湖县', '320981': '东台市', '320982': '大丰市', '321001': '市辖区', '321002': '广陵区', '321003': '邗江区', '321012': '江都区', '321023': '宝应县', '321081': '仪征市', '321084': '高邮市', '321101': '市辖区', '321102': '京口区', '321111': '润州区', '321112': '丹徒区', '321181': '丹阳市', '321182': '扬中市', '321183': '句容市', '321201': '市辖区', '321202': '海陵区', '321203': '高港区', '321281': '兴化市', '321282': '靖江市', '321283': '泰兴市', '321284': '姜堰市', '321301': '市辖区', '321302': '宿城区', '321311': '宿豫区', '321322': '沭阳县', '321323': '泗阳县', '321324': '泗洪县', '330101': '市辖区', '330102': '上城区', '330103': '下城区', '330104': '江干区', '330105': '拱墅区', '330106': '西湖区', '330108': '滨江区', '330109': '萧山区', '330110': '余杭区', '330122': '桐庐县', '330127': '淳安县', '330182': '建德市', '330183': '富阳市', '330185': '临安市', '330201': '市辖区', '330203': '海曙区', '330204': '江东区', '330205': '江北区', '330206': '北仑区', '330211': '镇海区', '330212': '鄞州区', '330225': '象山县', '330226': '宁海县', '330281': '余姚市', '330282': '慈溪市', '330283': '奉化市', '330301': '市辖区', '330302': '鹿城区', '330303': '龙湾区', '330304': '瓯海区', '330322': '洞头县', '330324': '永嘉县', '330326': '平阳县', '330327': '苍南县', '330328': '文成县', '330329': '泰顺县', '330381': '瑞安市', '330382': '乐清市', '330401': '市辖区', '330402': '南湖区', '330411': '秀洲区', '330421': '嘉善县', '330424': '海盐县', '330481': '海宁市', '330482': '平湖市', '330483': '桐乡市', '330501': '市辖区', '330502': '吴兴区', '330503': '南浔区', '330521': '德清县', '330522': '长兴县', '330523': '安吉县', '330601': '市辖区', '330602': '越城区', '330621': '绍兴县', '330624': '新昌县', '330681': '诸暨市', '330682': '上虞市', '330683': '嵊州市', '330701': '市辖区', '330702': '婺城区', '330703': '金东区', '330723': '武义县', '330726': '浦江县', '330727': '磐安县', '330781': '兰溪市', '330782': '义乌市', '330783': '东阳市', '330784': '永康市', '330801': '市辖区', '330802': '柯城区', '330803': '衢江区', '330822': '常山县', '330824': '开化县', '330825': '龙游县', '330881': '江山市', '330901': '市辖区', '330902': '定海区', '330903': '普陀区', '330921': '岱山县', '330922': '嵊泗县', '331001': '市辖区', '331002': '椒江区', '331003': '黄岩区', '331004': '路桥区', '331021': '玉环县', '331022': '三门县', '331023': '天台县', '331024': '仙居县', '331081': '温岭市', '331082': '临海市', '331101': '市辖区', '331102': '莲都区', '331121': '青田县', '331122': '缙云县', '331123': '遂昌县', '331124': '松阳县', '331125': '云和县', '331126': '庆元县', '331127': '景宁畲族自治县', '331181': '龙泉市', '340101': '市辖区', '340102': '瑶海区', '340103': '庐阳区', '340104': '蜀山区', '340111': '包河区', '340121': '长丰县', '340122': '肥东县', '340123': '肥西县', '340124': '庐江县', '340181': '巢湖市', '340201': '市辖区', '340202': '镜湖区', '340203': '弋江区', '340207': '鸠江区', '340208': '三山区', '340221': '芜湖县', '340222': '繁昌县', '340223': '南陵县', '340225': '无为县', '340301': '市辖区', '340302': '龙子湖区', '340303': '蚌山区', '340304': '禹会区', '340311': '淮上区', '340321': '怀远县', '340322': '五河县', '340323': '固镇县', '340401': '市辖区', '340402': '大通区', '340403': '田家庵区', '340404': '谢家集区', '340405': '八公山区', '340406': '潘集区', '340421': '凤台县', '340501': '市辖区', '340503': '花山区', '340504': '雨山区', '340506': '博望区', '340521': '当涂县', '340522': '含山县', '340523': '和县', '340601': '市辖区', '340602': '杜集区', '340603': '相山区', '340604': '烈山区', '340621': '濉溪县', '340701': '市辖区', '340702': '铜官山区', '340703': '狮子山区', '340711': '郊区', '340721': '铜陵县', '340801': '市辖区', '340802': '迎江区', '340803': '大观区', '340811': '宜秀区', '340822': '怀宁县', '340823': '枞阳县', '340824': '潜山县', '340825': '太湖县', '340826': '宿松县', '340827': '望江县', '340828': '岳西县', '340881': '桐城市', '341001': '市辖区', '341002': '屯溪区', '341003': '黄山区', '341004': '徽州区', '341021': '歙县', '341022': '休宁县', '341023': '黟县', '341024': '祁门县', '341101': '市辖区', '341102': '琅琊区', '341103': '南谯区', '341122': '来安县', '341124': '全椒县', '341125': '定远县', '341126': '凤阳县', '341181': '天长市', '341182': '明光市', '341201': '市辖区', '341202': '颍州区', '341203': '颍东区', '341204': '颍泉区', '341221': '临泉县', '341222': '太和县', '341225': '阜南县', '341226': '颍上县', '341282': '界首市', '341301': '市辖区', '341302': '埇桥区', '341321': '砀山县', '341322': '萧县', '341323': '灵璧县', '341324': '泗县', '341501': '市辖区', '341502': '金安区', '341503': '裕安区', '341521': '寿县', '341522': '霍邱县', '341523': '舒城县', '341524': '金寨县', '341525': '霍山县', '341601': '市辖区', '341602': '谯城区', '341621': '涡阳县', '341622': '蒙城县', '341623': '利辛县', '341701': '市辖区', '341702': '贵池区', '341721': '东至县', '341722': '石台县', '341723': '青阳县', '341801': '市辖区', '341802': '宣州区', '341821': '郎溪县', '341822': '广德县', '341823': '泾县', '341824': '绩溪县', '341825': '旌德县', '341881': '宁国市', '350101': '市辖区', '350102': '鼓楼区', '350103': '台江区', '350104': '仓山区', '350105': '马尾区', '350111': '晋安区', '350121': '闽侯县', '350122': '连江县', '350123': '罗源县', '350124': '闽清县', '350125': '永泰县', '350128': '平潭县', '350181': '福清市', '350182': '长乐市', '350201': '市辖区', '350203': '思明区', '350205': '海沧区', '350206': '湖里区', '350211': '集美区', '350212': '同安区', '350213': '翔安区', '350301': '市辖区', '350302': '城厢区', '350303': '涵江区', '350304': '荔城区', '350305': '秀屿区', '350322': '仙游县', '350401': '市辖区', '350402': '梅列区', '350403': '三元区', '350421': '明溪县', '350423': '清流县', '350424': '宁化县', '350425': '大田县', '350426': '尤溪县', '350427': '沙县', '350428': '将乐县', '350429': '泰宁县', '350430': '建宁县', '350481': '永安市', '350501': '市辖区', '350502': '鲤城区', '350503': '丰泽区', '350504': '洛江区', '350505': '泉港区', '350521': '惠安县', '350524': '安溪县', '350525': '永春县', '350526': '德化县', '350527': '金门县', '350581': '石狮市', '350582': '晋江市', '350583': '南安市', '350601': '市辖区', '350602': '芗城区', '350603': '龙文区', '350622': '云霄县', '350623': '漳浦县', '350624': '诏安县', '350625': '长泰县', '350626': '东山县', '350627': '南靖县', '350628': '平和县', '350629': '华安县', '350681': '龙海市', '350701': '市辖区', '350702': '延平区', '350721': '顺昌县', '350722': '浦城县', '350723': '光泽县', '350724': '松溪县', '350725': '政和县', '350781': '邵武市', '350782': '武夷山市', '350783': '建瓯市', '350784': '建阳市', '350801': '市辖区', '350802': '新罗区', '350821': '长汀县', '350822': '永定县', '350823': '上杭县', '350824': '武平县', '350825': '连城县', '350881': '漳平市', '350901': '市辖区', '350902': '蕉城区', '350921': '霞浦县', '350922': '古田县', '350923': '屏南县', '350924': '寿宁县', '350925': '周宁县', '350926': '柘荣县', '350981': '福安市', '350982': '福鼎市', '360101': '市辖区', '360102': '东湖区', '360103': '西湖区', '360104': '青云谱区', '360105': '湾里区', '360111': '青山湖区', '360121': '南昌县', '360122': '新建县', '360123': '安义县', '360124': '进贤县', '360201': '市辖区', '360202': '昌江区', '360203': '珠山区', '360222': '浮梁县', '360281': '乐平市', '360301': '市辖区', '360302': '安源区', '360313': '湘东区', '360321': '莲花县', '360322': '上栗县', '360323': '芦溪县', '360401': '市辖区', '360402': '庐山区', '360403': '浔阳区', '360421': '九江县', '360423': '武宁县', '360424': '修水县', '360425': '永修县', '360426': '德安县', '360427': '星子县', '360428': '都昌县', '360429': '湖口县', '360430': '彭泽县', '360481': '瑞昌市', '360482': '共青城市', '360501': '市辖区', '360502': '渝水区', '360521': '分宜县', '360601': '市辖区', '360602': '月湖区', '360622': '余江县', '360681': '贵溪市', '360701': '市辖区', '360702': '章贡区', '360721': '赣县', '360722': '信丰县', '360723': '大余县', '360724': '上犹县', '360725': '崇义县', '360726': '安远县', '360727': '龙南县', '360728': '定南县', '360729': '全南县', '360730': '宁都县', '360731': '于都县', '360732': '兴国县', '360733': '会昌县', '360734': '寻乌县', '360735': '石城县', '360781': '瑞金市', '360782': '南康市', '360801': '市辖区', '360802': '吉州区', '360803': '青原区', '360821': '吉安县', '360822': '吉水县', '360823': '峡江县', '360824': '新干县', '360825': '永丰县', '360826': '泰和县', '360827': '遂川县', '360828': '万安县', '360829': '安福县', '360830': '永新县', '360881': '井冈山市', '360901': '市辖区', '360902': '袁州区', '360921': '奉新县', '360922': '万载县', '360923': '上高县', '360924': '宜丰县', '360925': '靖安县', '360926': '铜鼓县', '360981': '丰城市', '360982': '樟树市', '360983': '高安市', '361001': '市辖区', '361002': '临川区', '361021': '南城县', '361022': '黎川县', '361023': '南丰县', '361024': '崇仁县', '361025': '乐安县', '361026': '宜黄县', '361027': '金溪县', '361028': '资溪县', '361029': '东乡县', '361030': '广昌县', '361101': '市辖区', '361102': '信州区', '361121': '上饶县', '361122': '广丰县', '361123': '玉山县', '361124': '铅山县', '361125': '横峰县', '361126': '弋阳县', '361127': '余干县', '361128': '鄱阳县', '361129': '万年县', '361130': '婺源县', '361181': '德兴市', '370101': '市辖区', '370102': '历下区', '370103': '市中区', '370104': '槐荫区', '370105': '天桥区', '370112': '历城区', '370113': '长清区', '370124': '平阴县', '370125': '济阳县', '370126': '商河县', '370181': '章丘市', '370201': '市辖区', '370202': '市南区', '370203': '市北区', '370205': '四方区', '370211': '黄岛区', '370212': '崂山区', '370213': '李沧区', '370214': '城阳区', '370281': '胶州市', '370282': '即墨市', '370283': '平度市', '370284': '胶南市', '370285': '莱西市', '370301': '市辖区', '370302': '淄川区', '370303': '张店区', '370304': '博山区', '370305': '临淄区', '370306': '周村区', '370321': '桓台县', '370322': '高青县', '370323': '沂源县', '370401': '市辖区', '370402': '市中区', '370403': '薛城区', '370404': '峄城区', '370405': '台儿庄区', '370406': '山亭区', '370481': '滕州市', '370501': '市辖区', '370502': '东营区', '370503': '河口区', '370521': '垦利县', '370522': '利津县', '370523': '广饶县', '370601': '市辖区', '370602': '芝罘区', '370611': '福山区', '370612': '牟平区', '370613': '莱山区', '370634': '长岛县', '370681': '龙口市', '370682': '莱阳市', '370683': '莱州市', '370684': '蓬莱市', '370685': '招远市', '370686': '栖霞市', '370687': '海阳市', '370701': '市辖区', '370702': '潍城区', '370703': '寒亭区', '370704': '坊子区', '370705': '奎文区', '370724': '临朐县', '370725': '昌乐县', '370781': '青州市', '370782': '诸城市', '370783': '寿光市', '370784': '安丘市', '370785': '高密市', '370786': '昌邑市', '370801': '市辖区', '370802': '市中区', '370811': '任城区', '370826': '微山县', '370827': '鱼台县', '370828': '金乡县', '370829': '嘉祥县', '370830': '汶上县', '370831': '泗水县', '370832': '梁山县', '370881': '曲阜市', '370882': '兖州市', '370883': '邹城市', '370901': '市辖区', '370902': '泰山区', '370911': '岱岳区', '370921': '宁阳县', '370923': '东平县', '370982': '新泰市', '370983': '肥城市', '371001': '市辖区', '371002': '环翠区', '371081': '文登市', '371082': '荣成市', '371083': '乳山市', '371101': '市辖区', '371102': '东港区', '371103': '岚山区', '371121': '五莲县', '371122': '莒县', '371201': '市辖区', '371202': '莱城区', '371203': '钢城区', '371301': '市辖区', '371302': '兰山区', '371311': '罗庄区', '371312': '河东区', '371321': '沂南县', '371322': '郯城县', '371323': '沂水县', '371324': '苍山县', '371325': '费县', '371326': '平邑县', '371327': '莒南县', '371328': '蒙阴县', '371329': '临沭县', '371401': '市辖区', '371402': '德城区', '371421': '陵县', '371422': '宁津县', '371423': '庆云县', '371424': '临邑县', '371425': '齐河县', '371426': '平原县', '371427': '夏津县', '371428': '武城县', '371481': '乐陵市', '371482': '禹城市', '371501': '市辖区', '371502': '东昌府区', '371521': '阳谷县', '371522': '莘县', '371523': '茌平县', '371524': '东阿县', '371525': '冠县', '371526': '高唐县', '371581': '临清市', '371601': '市辖区', '371602': '滨城区', '371621': '惠民县', '371622': '阳信县', '371623': '无棣县', '371624': '沾化县', '371625': '博兴县', '371626': '邹平县', '371701': '市辖区', '371702': '牡丹区', '371721': '曹县', '371722': '单县', '371723': '成武县', '371724': '巨野县', '371725': '郓城县', '371726': '鄄城县', '371727': '定陶县', '371728': '东明县', '410101': '市辖区', '410102': '中原区', '410103': '二七区', '410104': '管城回族区', '410105': '金水区', '410106': '上街区', '410108': '惠济区', '410122': '中牟县', '410181': '巩义市', '410182': '荥阳市', '410183': '新密市', '410184': '新郑市', '410185': '登封市', '410201': '市辖区', '410202': '龙亭区', '410203': '顺河回族区', '410204': '鼓楼区', '410205': '禹王台区', '410211': '金明区', '410221': '杞县', '410222': '通许县', '410223': '尉氏县', '410224': '开封县', '410225': '兰考县', '410301': '市辖区', '410302': '老城区', '410303': '西工区', '410304': '瀍河回族区', '410305': '涧西区', '410306': '吉利区', '410311': '洛龙区', '410322': '孟津县', '410323': '新安县', '410324': '栾川县', '410325': '嵩县', '410326': '汝阳县', '410327': '宜阳县', '410328': '洛宁县', '410329': '伊川县', '410381': '偃师市', '410401': '市辖区', '410402': '新华区', '410403': '卫东区', '410404': '石龙区', '410411': '湛河区', '410421': '宝丰县', '410422': '叶县', '410423': '鲁山县', '410425': '郏县', '410481': '舞钢市', '410482': '汝州市', '410501': '市辖区', '410502': '文峰区', '410503': '北关区', '410505': '殷都区', '410506': '龙安区', '410522': '安阳县', '410523': '汤阴县', '410526': '滑县', '410527': '内黄县', '410581': '林州市', '410601': '市辖区', '410602': '鹤山区', '410603': '山城区', '410611': '淇滨区', '410621': '浚县', '410622': '淇县', '410701': '市辖区', '410702': '红旗区', '410703': '卫滨区', '410704': '凤泉区', '410711': '牧野区', '410721': '新乡县', '410724': '获嘉县', '410725': '原阳县', '410726': '延津县', '410727': '封丘县', '410728': '长垣县', '410781': '卫辉市', '410782': '辉县市', '410801': '市辖区', '410802': '解放区', '410803': '中站区', '410804': '马村区', '410811': '山阳区', '410821': '修武县', '410822': '博爱县', '410823': '武陟县', '410825': '温县', '410882': '沁阳市', '410883': '孟州市', '410901': '市辖区', '410902': '华龙区', '410922': '清丰县', '410923': '南乐县', '410926': '范县', '410927': '台前县', '410928': '濮阳县', '411001': '市辖区', '411002': '魏都区', '411023': '许昌县', '411024': '鄢陵县', '411025': '襄城县', '411081': '禹州市', '411082': '长葛市', '411101': '市辖区', '411102': '源汇区', '411103': '郾城区', '411104': '召陵区', '411121': '舞阳县', '411122': '临颍县', '411201': '市辖区', '411202': '湖滨区', '411221': '渑池县', '411222': '陕县', '411224': '卢氏县', '411281': '义马市', '411282': '灵宝市', '411301': '市辖区', '411302': '宛城区', '411303': '卧龙区', '411321': '南召县', '411322': '方城县', '411323': '西峡县', '411324': '镇平县', '411325': '内乡县', '411326': '淅川县', '411327': '社旗县', '411328': '唐河县', '411329': '新野县', '411330': '桐柏县', '411381': '邓州市', '411401': '市辖区', '411402': '梁园区', '411403': '睢阳区', '411421': '民权县', '411422': '睢县', '411423': '宁陵县', '411424': '柘城县', '411425': '虞城县', '411426': '夏邑县', '411481': '永城市', '411501': '市辖区', '411502': '浉河区', '411503': '平桥区', '411521': '罗山县', '411522': '光山县', '411523': '新县', '411524': '商城县', '411525': '固始县', '411526': '潢川县', '411527': '淮滨县', '411528': '息县', '411601': '市辖区', '411602': '川汇区', '411621': '扶沟县', '411622': '西华县', '411623': '商水县', '411624': '沈丘县', '411625': '郸城县', '411626': '淮阳县', '411627': '太康县', '411628': '鹿邑县', '411681': '项城市', '411701': '市辖区', '411702': '驿城区', '411721': '西平县', '411722': '上蔡县', '411723': '平舆县', '411724': '正阳县', '411725': '确山县', '411726': '泌阳县', '411727': '汝南县', '411728': '遂平县', '411729': '新蔡县', '419001': '济源市', '420101': '市辖区', '420102': '江岸区', '420103': '江汉区', '420104': '硚口区', '420105': '汉阳区', '420106': '武昌区', '420107': '青山区', '420111': '洪山区', '420112': '东西湖区', '420113': '汉南区', '420114': '蔡甸区', '420115': '江夏区', '420116': '黄陂区', '420117': '新洲区', '420201': '市辖区', '420202': '黄石港区', '420203': '西塞山区', '420204': '下陆区', '420205': '铁山区', '420222': '阳新县', '420281': '大冶市', '420301': '市辖区', '420302': '茅箭区', '420303': '张湾区', '420321': '郧县', '420322': '郧西县', '420323': '竹山县', '420324': '竹溪县', '420325': '房县', '420381': '丹江口市', '420501': '市辖区', '420502': '西陵区', '420503': '伍家岗区', '420504': '点军区', '420505': '猇亭区', '420506': '夷陵区', '420525': '远安县', '420526': '兴山县', '420527': '秭归县', '420528': '长阳土家族自治县', '420529': '五峰土家族自治县', '420581': '宜都市', '420582': '当阳市', '420583': '枝江市', '420601': '市辖区', '420602': '襄城区', '420606': '樊城区', '420607': '襄州区', '420624': '南漳县', '420625': '谷城县', '420626': '保康县', '420682': '老河口市', '420683': '枣阳市', '420684': '宜城市', '420701': '市辖区', '420702': '梁子湖区', '420703': '华容区', '420704': '鄂城区', '420801': '市辖区', '420802': '东宝区', '420804': '掇刀区', '420821': '京山县', '420822': '沙洋县', '420881': '钟祥市', '420901': '市辖区', '420902': '孝南区', '420921': '孝昌县', '420922': '大悟县', '420923': '云梦县', '420981': '应城市', '420982': '安陆市', '420984': '汉川市', '421001': '市辖区', '421002': '沙市区', '421003': '荆州区', '421022': '公安县', '421023': '监利县', '421024': '江陵县', '421081': '石首市', '421083': '洪湖市', '421087': '松滋市', '421101': '市辖区', '421102': '黄州区', '421121': '团风县', '421122': '红安县', '421123': '罗田县', '421124': '英山县', '421125': '浠水县', '421126': '蕲春县', '421127': '黄梅县', '421181': '麻城市', '421182': '武穴市', '421201': '市辖区', '421202': '咸安区', '421221': '嘉鱼县', '421222': '通城县', '421223': '崇阳县', '421224': '通山县', '421281': '赤壁市', '421301': '市辖区', '421303': '曾都区', '421321': '随县', '421381': '广水市', '422801': '恩施市', '422802': '利川市', '422822': '建始县', '422823': '巴东县', '422825': '宣恩县', '422826': '咸丰县', '422827': '来凤县', '422828': '鹤峰县', '429004': '仙桃市', '429005': '潜江市', '429006': '天门市', '429021': '神农架林区', '430101': '市辖区', '430102': '芙蓉区', '430103': '天心区', '430104': '岳麓区', '430105': '开福区', '430111': '雨花区', '430112': '望城区', '430121': '长沙县', '430124': '宁乡县', '430181': '浏阳市', '430201': '市辖区', '430202': '荷塘区', '430203': '芦淞区', '430204': '石峰区', '430211': '天元区', '430221': '株洲县', '430223': '攸县', '430224': '茶陵县', '430225': '炎陵县', '430281': '醴陵市', '430301': '市辖区', '430302': '雨湖区', '430304': '岳塘区', '430321': '湘潭县', '430381': '湘乡市', '430382': '韶山市', '430401': '市辖区', '430405': '珠晖区', '430406': '雁峰区', '430407': '石鼓区', '430408': '蒸湘区', '430412': '南岳区', '430421': '衡阳县', '430422': '衡南县', '430423': '衡山县', '430424': '衡东县', '430426': '祁东县', '430481': '耒阳市', '430482': '常宁市', '430501': '市辖区', '430502': '双清区', '430503': '大祥区', '430511': '北塔区', '430521': '邵东县', '430522': '新邵县', '430523': '邵阳县', '430524': '隆回县', '430525': '洞口县', '430527': '绥宁县', '430528': '新宁县', '430529': '城步苗族自治县', '430581': '武冈市', '430601': '市辖区', '430602': '岳阳楼区', '430603': '云溪区', '430611': '君山区', '430621': '岳阳县', '430623': '华容县', '430624': '湘阴县', '430626': '平江县', '430681': '汨罗市', '430682': '临湘市', '430701': '市辖区', '430702': '武陵区', '430703': '鼎城区', '430721': '安乡县', '430722': '汉寿县', '430723': '澧县', '430724': '临澧县', '430725': '桃源县', '430726': '石门县', '430781': '津市市', '430801': '市辖区', '430802': '永定区', '430811': '武陵源区', '430821': '慈利县', '430822': '桑植县', '430901': '市辖区', '430902': '资阳区', '430903': '赫山区', '430921': '南县', '430922': '桃江县', '430923': '安化县', '430981': '沅江市', '431001': '市辖区', '431002': '北湖区', '431003': '苏仙区', '431021': '桂阳县', '431022': '宜章县', '431023': '永兴县', '431024': '嘉禾县', '431025': '临武县', '431026': '汝城县', '431027': '桂东县', '431028': '安仁县', '431081': '资兴市', '431101': '市辖区', '431102': '零陵区', '431103': '冷水滩区', '431121': '祁阳县', '431122': '东安县', '431123': '双牌县', '431124': '道县', '431125': '江永县', '431126': '宁远县', '431127': '蓝山县', '431128': '新田县', '431129': '江华瑶族自治县', '431201': '市辖区', '431202': '鹤城区', '431221': '中方县', '431222': '沅陵县', '431223': '辰溪县', '431224': '溆浦县', '431225': '会同县', '431226': '麻阳苗族自治县', '431227': '新晃侗族自治县', '431228': '芷江侗族自治县', '431229': '靖州苗族侗族自治县', '431230': '通道侗族自治县', '431281': '洪江市', '431301': '市辖区', '431302': '娄星区', '431321': '双峰县', '431322': '新化县', '431381': '冷水江市', '431382': '涟源市', '433101': '吉首市', '433122': '泸溪县', '433123': '凤凰县', '433124': '花垣县', '433125': '保靖县', '433126': '古丈县', '433127': '永顺县', '433130': '龙山县', '440101': '市辖区', '440103': '荔湾区', '440104': '越秀区', '440105': '海珠区', '440106': '天河区', '440111': '白云区', '440112': '黄埔区', '440113': '番禺区', '440114': '花都区', '440115': '南沙区', '440116': '萝岗区', '440183': '增城市', '440184': '从化市', '440201': '市辖区', '440203': '武江区', '440204': '浈江区', '440205': '曲江区', '440222': '始兴县', '440224': '仁化县', '440229': '翁源县', '440232': '乳源瑶族自治县', '440233': '新丰县', '440281': '乐昌市', '440282': '南雄市', '440301': '市辖区', '440303': '罗湖区', '440304': '福田区', '440305': '南山区', '440306': '宝安区', '440307': '龙岗区', '440308': '盐田区', '440401': '市辖区', '440402': '香洲区', '440403': '斗门区', '440404': '金湾区', '440501': '市辖区', '440507': '龙湖区', '440511': '金平区', '440512': '濠江区', '440513': '潮阳区', '440514': '潮南区', '440515': '澄海区', '440523': '南澳县', '440601': '市辖区', '440604': '禅城区', '440605': '南海区', '440606': '顺德区', '440607': '三水区', '440608': '高明区', '440701': '市辖区', '440703': '蓬江区', '440704': '江海区', '440705': '新会区', '440781': '台山市', '440783': '开平市', '440784': '鹤山市', '440785': '恩平市', '440801': '市辖区', '440802': '赤坎区', '440803': '霞山区', '440804': '坡头区', '440811': '麻章区', '440823': '遂溪县', '440825': '徐闻县', '440881': '廉江市', '440882': '雷州市', '440883': '吴川市', '440901': '市辖区', '440902': '茂南区', '440903': '茂港区', '440923': '电白县', '440981': '高州市', '440982': '化州市', '440983': '信宜市', '441201': '市辖区', '441202': '端州区', '441203': '鼎湖区', '441223': '广宁县', '441224': '怀集县', '441225': '封开县', '441226': '德庆县', '441283': '高要市', '441284': '四会市', '441301': '市辖区', '441302': '惠城区', '441303': '惠阳区', '441322': '博罗县', '441323': '惠东县', '441324': '龙门县', '441401': '市辖区', '441402': '梅江区', '441421': '梅县', '441422': '大埔县', '441423': '丰顺县', '441424': '五华县', '441426': '平远县', '441427': '蕉岭县', '441481': '兴宁市', '441501': '市辖区', '441502': '城区', '441521': '海丰县', '441523': '陆河县', '441581': '陆丰市', '441601': '市辖区', '441602': '源城区', '441621': '紫金县', '441622': '龙川县', '441623': '连平县', '441624': '和平县', '441625': '东源县', '441701': '市辖区', '441702': '江城区', '441721': '阳西县', '441723': '阳东县', '441781': '阳春市', '441801': '市辖区', '441802': '清城区', '441821': '佛冈县', '441823': '阳山县', '441825': '连山壮族瑶族自治县', '441826': '连南瑶族自治县', '441827': '清新县', '441881': '英德市', '441882': '连州市', '445101': '市辖区', '445102': '湘桥区', '445121': '潮安县', '445122': '饶平县', '445201': '市辖区', '445202': '榕城区', '445221': '揭东县', '445222': '揭西县', '445224': '惠来县', '445281': '普宁市', '445301': '市辖区', '445302': '云城区', '445321': '新兴县', '445322': '郁南县', '445323': '云安县', '445381': '罗定市', '450101': '市辖区', '450102': '兴宁区', '450103': '青秀区', '450105': '江南区', '450107': '西乡塘区', '450108': '良庆区', '450109': '邕宁区', '450122': '武鸣县', '450123': '隆安县', '450124': '马山县', '450125': '上林县', '450126': '宾阳县', '450127': '横县', '450201': '市辖区', '450202': '城中区', '450203': '鱼峰区', '450204': '柳南区', '450205': '柳北区', '450221': '柳江县', '450222': '柳城县', '450223': '鹿寨县', '450224': '融安县', '450225': '融水苗族自治县', '450226': '三江侗族自治县', '450301': '市辖区', '450302': '秀峰区', '450303': '叠彩区', '450304': '象山区', '450305': '七星区', '450311': '雁山区', '450321': '阳朔县', '450322': '临桂县', '450323': '灵川县', '450324': '全州县', '450325': '兴安县', '450326': '永福县', '450327': '灌阳县', '450328': '龙胜各族自治县', '450329': '资源县', '450330': '平乐县', '450331': '荔浦县', '450332': '恭城瑶族自治县', '450401': '市辖区', '450403': '万秀区', '450404': '蝶山区', '450405': '长洲区', '450421': '苍梧县', '450422': '藤县', '450423': '蒙山县', '450481': '岑溪市', '450501': '市辖区', '450502': '海城区', '450503': '银海区', '450512': '铁山港区', '450521': '合浦县', '450601': '市辖区', '450602': '港口区', '450603': '防城区', '450621': '上思县', '450681': '东兴市', '450701': '市辖区', '450702': '钦南区', '450703': '钦北区', '450721': '灵山县', '450722': '浦北县', '450801': '市辖区', '450802': '港北区', '450803': '港南区', '450804': '覃塘区', '450821': '平南县', '450881': '桂平市', '450901': '市辖区', '450902': '玉州区', '450921': '容县', '450922': '陆川县', '450923': '博白县', '450924': '兴业县', '450981': '北流市', '451001': '市辖区', '451002': '右江区', '451021': '田阳县', '451022': '田东县', '451023': '平果县', '451024': '德保县', '451025': '靖西县', '451026': '那坡县', '451027': '凌云县', '451028': '乐业县', '451029': '田林县', '451030': '西林县', '451031': '隆林各族自治县', '451101': '市辖区', '451102': '八步区', '451121': '昭平县', '451122': '钟山县', '451123': '富川瑶族自治县', '451201': '市辖区', '451202': '金城江区', '451221': '南丹县', '451222': '天峨县', '451223': '凤山县', '451224': '东兰县', '451225': '罗城仫佬族自治县', '451226': '环江毛南族自治县', '451227': '巴马瑶族自治县', '451228': '都安瑶族自治县', '451229': '大化瑶族自治县', '451281': '宜州市', '451301': '市辖区', '451302': '兴宾区', '451321': '忻城县', '451322': '象州县', '451323': '武宣县', '451324': '金秀瑶族自治县', '451381': '合山市', '451401': '市辖区', '451402': '江洲区', '451421': '扶绥县', '451422': '宁明县', '451423': '龙州县', '451424': '大新县', '451425': '天等县', '451481': '凭祥市', '460101': '市辖区', '460105': '秀英区', '460106': '龙华区', '460107': '琼山区', '460108': '美兰区', '460201': '市辖区', '460321': '西沙群岛', '460322': '南沙群岛', '460323': '中沙群岛的岛礁及其海域', '469001': '五指山市', '469002': '琼海市', '469003': '儋州市', '469005': '文昌市', '469006': '万宁市', '469007': '东方市', '469021': '定安县', '469022': '屯昌县', '469023': '澄迈县', '469024': '临高县', '469025': '白沙黎族自治县', '469026': '昌江黎族自治县', '469027': '乐东黎族自治县', '469028': '陵水黎族自治县', '469029': '保亭黎族苗族自治县', '469030': '琼中黎族苗族自治县', '500101': '万州区', '500102': '涪陵区', '500103': '渝中区', '500104': '大渡口区', '500105': '江北区', '500106': '沙坪坝区', '500107': '九龙坡区', '500108': '南岸区', '500109': '北碚区', '500110': '綦江区', '500111': '大足区', '500112': '渝北区', '500113': '巴南区', '500114': '黔江区', '500115': '长寿区', '500116': '江津区', '500117': '合川区', '500118': '永川区', '500119': '南川区', '500223': '潼南县', '500224': '铜梁县', '500226': '荣昌县', '500227': '璧山县', '500228': '梁平县', '500229': '城口县', '500230': '丰都县', '500231': '垫江县', '500232': '武隆县', '500233': '忠县', '500234': '开县', '500235': '云阳县', '500236': '奉节县', '500237': '巫山县', '500238': '巫溪县', '500240': '石柱土家族自治县', '500241': '秀山土家族苗族自治县', '500242': '酉阳土家族苗族自治县', '500243': '彭水苗族土家族自治县', '510101': '市辖区', '510104': '锦江区', '510105': '青羊区', '510106': '金牛区', '510107': '武侯区', '510108': '成华区', '510112': '龙泉驿区', '510113': '青白江区', '510114': '新都区', '510115': '温江区', '510121': '金堂县', '510122': '双流县', '510124': '郫县', '510129': '大邑县', '510131': '蒲江县', '510132': '新津县', '510181': '都江堰市', '510182': '彭州市', '510183': '邛崃市', '510184': '崇州市', '510301': '市辖区', '510302': '自流井区', '510303': '贡井区', '510304': '大安区', '510311': '沿滩区', '510321': '荣县', '510322': '富顺县', '510401': '市辖区', '510402': '东区', '510403': '西区', '510411': '仁和区', '510421': '米易县', '510422': '盐边县', '510501': '市辖区', '510502': '江阳区', '510503': '纳溪区', '510504': '龙马潭区', '510521': '泸县', '510522': '合江县', '510524': '叙永县', '510525': '古蔺县', '510601': '市辖区', '510603': '旌阳区', '510623': '中江县', '510626': '罗江县', '510681': '广汉市', '510682': '什邡市', '510683': '绵竹市', '510701': '市辖区', '510703': '涪城区', '510704': '游仙区', '510722': '三台县', '510723': '盐亭县', '510724': '安县', '510725': '梓潼县', '510726': '北川羌族自治县', '510727': '平武县', '510781': '江油市', '510801': '市辖区', '510802': '利州区', '510811': '元坝区', '510812': '朝天区', '510821': '旺苍县', '510822': '青川县', '510823': '剑阁县', '510824': '苍溪县', '510901': '市辖区', '510903': '船山区', '510904': '安居区', '510921': '蓬溪县', '510922': '射洪县', '510923': '大英县', '511001': '市辖区', '511002': '市中区', '511011': '东兴区', '511024': '威远县', '511025': '资中县', '511028': '隆昌县', '511101': '市辖区', '511102': '市中区', '511111': '沙湾区', '511112': '五通桥区', '511113': '金口河区', '511123': '犍为县', '511124': '井研县', '511126': '夹江县', '511129': '沐川县', '511132': '峨边彝族自治县', '511133': '马边彝族自治县', '511181': '峨眉山市', '511301': '市辖区', '511302': '顺庆区', '511303': '高坪区', '511304': '嘉陵区', '511321': '南部县', '511322': '营山县', '511323': '蓬安县', '511324': '仪陇县', '511325': '西充县', '511381': '阆中市', '511401': '市辖区', '511402': '东坡区', '511421': '仁寿县', '511422': '彭山县', '511423': '洪雅县', '511424': '丹棱县', '511425': '青神县', '511501': '市辖区', '511502': '翠屏区', '511503': '南溪区', '511521': '宜宾县', '511523': '江安县', '511524': '长宁县', '511525': '高县', '511526': '珙县', '511527': '筠连县', '511528': '兴文县', '511529': '屏山县', '511601': '市辖区', '511602': '广安区', '511621': '岳池县', '511622': '武胜县', '511623': '邻水县', '511681': '华蓥市', '511701': '市辖区', '511702': '通川区', '511721': '达县', '511722': '宣汉县', '511723': '开江县', '511724': '大竹县', '511725': '渠县', '511781': '万源市', '511801': '市辖区', '511802': '雨城区', '511803': '名山区', '511822': '荥经县', '511823': '汉源县', '511824': '石棉县', '511825': '天全县', '511826': '芦山县', '511827': '宝兴县', '511901': '市辖区', '511902': '巴州区', '511921': '通江县', '511922': '南江县', '511923': '平昌县', '512001': '市辖区', '512002': '雁江区', '512021': '安岳县', '512022': '乐至县', '512081': '简阳市', '513221': '汶川县', '513222': '理县', '513223': '茂县', '513224': '松潘县', '513225': '九寨沟县', '513226': '金川县', '513227': '小金县', '513228': '黑水县', '513229': '马尔康县', '513230': '壤塘县', '513231': '阿坝县', '513232': '若尔盖县', '513233': '红原县', '513321': '康定县', '513322': '泸定县', '513323': '丹巴县', '513324': '九龙县', '513325': '雅江县', '513326': '道孚县', '513327': '炉霍县', '513328': '甘孜县', '513329': '新龙县', '513330': '德格县', '513331': '白玉县', '513332': '石渠县', '513333': '色达县', '513334': '理塘县', '513335': '巴塘县', '513336': '乡城县', '513337': '稻城县', '513338': '得荣县', '513401': '西昌市', '513422': '木里藏族自治县', '513423': '盐源县', '513424': '德昌县', '513425': '会理县', '513426': '会东县', '513427': '宁南县', '513428': '普格县', '513429': '布拖县', '513430': '金阳县', '513431': '昭觉县', '513432': '喜德县', '513433': '冕宁县', '513434': '越西县', '513435': '甘洛县', '513436': '美姑县', '513437': '雷波县', '520101': '市辖区', '520102': '南明区', '520103': '云岩区', '520111': '花溪区', '520112': '乌当区', '520113': '白云区', '520114': '小河区', '520121': '开阳县', '520122': '息烽县', '520123': '修文县', '520181': '清镇市', '520201': '钟山区', '520203': '六枝特区', '520221': '水城县', '520222': '盘县', '520301': '市辖区', '520302': '红花岗区', '520303': '汇川区', '520321': '遵义县', '520322': '桐梓县', '520323': '绥阳县', '520324': '正安县', '520325': '道真仡佬族苗族自治县', '520326': '务川仡佬族苗族自治县', '520327': '凤冈县', '520328': '湄潭县', '520329': '余庆县', '520330': '习水县', '520381': '赤水市', '520382': '仁怀市', '520401': '市辖区', '520402': '西秀区', '520421': '平坝县', '520422': '普定县', '520423': '镇宁布依族苗族自治县', '520424': '关岭布依族苗族自治县', '520425': '紫云苗族布依族自治县', '520502': '七星关区', '520521': '大方县', '520522': '黔西县', '520523': '金沙县', '520524': '织金县', '520525': '纳雍县', '520526': '威宁彝族回族苗族自治县', '520527': '赫章县', '520602': '碧江区', '520603': '万山区', '520621': '江口县', '520622': '玉屏侗族自治县', '520623': '石阡县', '520624': '思南县', '520625': '印江土家族苗族自治县', '520626': '德江县', '520627': '沿河土家族自治县', '520628': '松桃苗族自治县', '522301': '兴义市', '522322': '兴仁县', '522323': '普安县', '522324': '晴隆县', '522325': '贞丰县', '522326': '望谟县', '522327': '册亨县', '522328': '安龙县', '522601': '凯里市', '522622': '黄平县', '522623': '施秉县', '522624': '三穗县', '522625': '镇远县', '522626': '岑巩县', '522627': '天柱县', '522628': '锦屏县', '522629': '剑河县', '522630': '台江县', '522631': '黎平县', '522632': '榕江县', '522633': '从江县', '522634': '雷山县', '522635': '麻江县', '522636': '丹寨县', '522701': '都匀市', '522702': '福泉市', '522722': '荔波县', '522723': '贵定县', '522725': '瓮安县', '522726': '独山县', '522727': '平塘县', '522728': '罗甸县', '522729': '长顺县', '522730': '龙里县', '522731': '惠水县', '522732': '三都水族自治县', '530101': '市辖区', '530102': '五华区', '530103': '盘龙区', '530111': '官渡区', '530112': '西山区', '530113': '东川区', '530114': '呈贡区', '530122': '晋宁县', '530124': '富民县', '530125': '宜良县', '530126': '石林彝族自治县', '530127': '嵩明县', '530128': '禄劝彝族苗族自治县', '530129': '寻甸回族彝族自治县', '530181': '安宁市', '530301': '市辖区', '530302': '麒麟区', '530321': '马龙县', '530322': '陆良县', '530323': '师宗县', '530324': '罗平县', '530325': '富源县', '530326': '会泽县', '530328': '沾益县', '530381': '宣威市', '530402': '红塔区', '530421': '江川县', '530422': '澄江县', '530423': '通海县', '530424': '华宁县', '530425': '易门县', '530426': '峨山彝族自治县', '530427': '新平彝族傣族自治县', '530428': '元江哈尼族彝族傣族自治县', '530501': '市辖区', '530502': '隆阳区', '530521': '施甸县', '530522': '腾冲县', '530523': '龙陵县', '530524': '昌宁县', '530601': '市辖区', '530602': '昭阳区', '530621': '鲁甸县', '530622': '巧家县', '530623': '盐津县', '530624': '大关县', '530625': '永善县', '530626': '绥江县', '530627': '镇雄县', '530628': '彝良县', '530629': '威信县', '530630': '水富县', '530701': '市辖区', '530702': '古城区', '530721': '玉龙纳西族自治县', '530722': '永胜县', '530723': '华坪县', '530724': '宁蒗彝族自治县', '530801': '市辖区', '530802': '思茅区', '530821': '宁洱哈尼族彝族自治县', '530822': '墨江哈尼族自治县', '530823': '景东彝族自治县', '530824': '景谷傣族彝族自治县', '530825': '镇沅彝族哈尼族拉祜族自治县', '530826': '江城哈尼族彝族自治县', '530827': '孟连傣族拉祜族佤族自治县', '530828': '澜沧拉祜族自治县', '530829': '西盟佤族自治县', '530901': '市辖区', '530902': '临翔区', '530921': '凤庆县', '530922': '云县', '530923': '永德县', '530924': '镇康县', '530925': '双江拉祜族佤族布朗族傣族自治县', '530926': '耿马傣族佤族自治县', '530927': '沧源佤族自治县', '532301': '楚雄市', '532322': '双柏县', '532323': '牟定县', '532324': '南华县', '532325': '姚安县', '532326': '大姚县', '532327': '永仁县', '532328': '元谋县', '532329': '武定县', '532331': '禄丰县', '532501': '个旧市', '532502': '开远市', '532503': '蒙自市', '532523': '屏边苗族自治县', '532524': '建水县', '532525': '石屏县', '532526': '弥勒县', '532527': '泸西县', '532528': '元阳县', '532529': '红河县', '532530': '金平苗族瑶族傣族自治县', '532531': '绿春县', '532532': '河口瑶族自治县', '532601': '文山市', '532622': '砚山县', '532623': '西畴县', '532624': '麻栗坡县', '532625': '马关县', '532626': '丘北县', '532627': '广南县', '532628': '富宁县', '532801': '景洪市', '532822': '勐海县', '532823': '勐腊县', '532901': '大理市', '532922': '漾濞彝族自治县', '532923': '祥云县', '532924': '宾川县', '532925': '弥渡县', '532926': '南涧彝族自治县', '532927': '巍山彝族回族自治县', '532928': '永平县', '532929': '云龙县', '532930': '洱源县', '532931': '剑川县', '532932': '鹤庆县', '533102': '瑞丽市', '533103': '芒市', '533122': '梁河县', '533123': '盈江县', '533124': '陇川县', '533321': '泸水县', '533323': '福贡县', '533324': '贡山独龙族怒族自治县', '533325': '兰坪白族普米族自治县', '533421': '香格里拉县', '533422': '德钦县', '533423': '维西傈僳族自治县', '540101': '市辖区', '540102': '城关区', '540121': '林周县', '540122': '当雄县', '540123': '尼木县', '540124': '曲水县', '540125': '堆龙德庆县', '540126': '达孜县', '540127': '墨竹工卡县', '542121': '昌都县', '542122': '江达县', '542123': '贡觉县', '542124': '类乌齐县', '542125': '丁青县', '542126': '察雅县', '542127': '八宿县', '542128': '左贡县', '542129': '芒康县', '542132': '洛隆县', '542133': '边坝县', '542221': '乃东县', '542222': '扎囊县', '542223': '贡嘎县', '542224': '桑日县', '542225': '琼结县', '542226': '曲松县', '542227': '措美县', '542228': '洛扎县', '542229': '加查县', '542231': '隆子县', '542232': '错那县', '542233': '浪卡子县', '542301': '日喀则市', '542322': '南木林县', '542323': '江孜县', '542324': '定日县', '542325': '萨迦县', '542326': '拉孜县', '542327': '昂仁县', '542328': '谢通门县', '542329': '白朗县', '542330': '仁布县', '542331': '康马县', '542332': '定结县', '542333': '仲巴县', '542334': '亚东县', '542335': '吉隆县', '542336': '聂拉木县', '542337': '萨嘎县', '542338': '岗巴县', '542421': '那曲县', '542422': '嘉黎县', '542423': '比如县', '542424': '聂荣县', '542425': '安多县', '542426': '申扎县', '542427': '索县', '542428': '班戈县', '542429': '巴青县', '542430': '尼玛县', '542521': '普兰县', '542522': '札达县', '542523': '噶尔县', '542524': '日土县', '542525': '革吉县', '542526': '改则县', '542527': '措勤县', '542621': '林芝县', '542622': '工布江达县', '542623': '米林县', '542624': '墨脱县', '542625': '波密县', '542626': '察隅县', '542627': '朗县', '610101': '市辖区', '610102': '新城区', '610103': '碑林区', '610104': '莲湖区', '610111': '灞桥区', '610112': '未央区', '610113': '雁塔区', '610114': '阎良区', '610115': '临潼区', '610116': '长安区', '610122': '蓝田县', '610124': '周至县', '610125': '户县', '610126': '高陵县', '610201': '市辖区', '610202': '王益区', '610203': '印台区', '610204': '耀州区', '610222': '宜君县', '610301': '市辖区', '610302': '渭滨区', '610303': '金台区', '610304': '陈仓区', '610322': '凤翔县', '610323': '岐山县', '610324': '扶风县', '610326': '眉县', '610327': '陇县', '610328': '千阳县', '610329': '麟游县', '610330': '凤县', '610331': '太白县', '610401': '市辖区', '610402': '秦都区', '610403': '杨陵区', '610404': '渭城区', '610422': '三原县', '610423': '泾阳县', '610424': '乾县', '610425': '礼泉县', '610426': '永寿县', '610427': '彬县', '610428': '长武县', '610429': '旬邑县', '610430': '淳化县', '610431': '武功县', '610481': '兴平市', '610501': '市辖区', '610502': '临渭区', '610521': '华县', '610522': '潼关县', '610523': '大荔县', '610524': '合阳县', '610525': '澄城县', '610526': '蒲城县', '610527': '白水县', '610528': '富平县', '610581': '韩城市', '610582': '华阴市', '610601': '市辖区', '610602': '宝塔区', '610621': '延长县', '610622': '延川县', '610623': '子长县', '610624': '安塞县', '610625': '志丹县', '610626': '吴起县', '610627': '甘泉县', '610628': '富县', '610629': '洛川县', '610630': '宜川县', '610631': '黄龙县', '610632': '黄陵县', '610701': '市辖区', '610702': '汉台区', '610721': '南郑县', '610722': '城固县', '610723': '洋县', '610724': '西乡县', '610725': '勉县', '610726': '宁强县', '610727': '略阳县', '610728': '镇巴县', '610729': '留坝县', '610730': '佛坪县', '610801': '市辖区', '610802': '榆阳区', '610821': '神木县', '610822': '府谷县', '610823': '横山县', '610824': '靖边县', '610825': '定边县', '610826': '绥德县', '610827': '米脂县', '610828': '佳县', '610829': '吴堡县', '610830': '清涧县', '610831': '子洲县', '610901': '市辖区', '610902': '汉滨区', '610921': '汉阴县', '610922': '石泉县', '610923': '宁陕县', '610924': '紫阳县', '610925': '岚皋县', '610926': '平利县', '610927': '镇坪县', '610928': '旬阳县', '610929': '白河县', '611001': '市辖区', '611002': '商州区', '611021': '洛南县', '611022': '丹凤县', '611023': '商南县', '611024': '山阳县', '611025': '镇安县', '611026': '柞水县', '620101': '市辖区', '620102': '城关区', '620103': '七里河区', '620104': '西固区', '620105': '安宁区', '620111': '红古区', '620121': '永登县', '620122': '皋兰县', '620123': '榆中县', '620201': '市辖区', '620301': '市辖区', '620302': '金川区', '620321': '永昌县', '620401': '市辖区', '620402': '白银区', '620403': '平川区', '620421': '靖远县', '620422': '会宁县', '620423': '景泰县', '620501': '市辖区', '620502': '秦州区', '620503': '麦积区', '620521': '清水县', '620522': '秦安县', '620523': '甘谷县', '620524': '武山县', '620525': '张家川回族自治县', '620601': '市辖区', '620602': '凉州区', '620621': '民勤县', '620622': '古浪县', '620623': '天祝藏族自治县', '620701': '市辖区', '620702': '甘州区', '620721': '肃南裕固族自治县', '620722': '民乐县', '620723': '临泽县', '620724': '高台县', '620725': '山丹县', '620801': '市辖区', '620802': '崆峒区', '620821': '泾川县', '620822': '灵台县', '620823': '崇信县', '620824': '华亭县', '620825': '庄浪县', '620826': '静宁县', '620901': '市辖区', '620902': '肃州区', '620921': '金塔县', '620922': '瓜州县', '620923': '肃北蒙古族自治县', '620924': '阿克塞哈萨克族自治县', '620981': '玉门市', '620982': '敦煌市', '621001': '市辖区', '621002': '西峰区', '621021': '庆城县', '621022': '环县', '621023': '华池县', '621024': '合水县', '621025': '正宁县', '621026': '宁县', '621027': '镇原县', '621101': '市辖区', '621102': '安定区', '621121': '通渭县', '621122': '陇西县', '621123': '渭源县', '621124': '临洮县', '621125': '漳县', '621126': '岷县', '621201': '市辖区', '621202': '武都区', '621221': '成县', '621222': '文县', '621223': '宕昌县', '621224': '康县', '621225': '西和县', '621226': '礼县', '621227': '徽县', '621228': '两当县', '622901': '临夏市', '622921': '临夏县', '622922': '康乐县', '622923': '永靖县', '622924': '广河县', '622925': '和政县', '622926': '东乡族自治县', '622927': '积石山保安族东乡族撒拉族自治县', '623001': '合作市', '623021': '临潭县', '623022': '卓尼县', '623023': '舟曲县', '623024': '迭部县', '623025': '玛曲县', '623026': '碌曲县', '623027': '夏河县', '630101': '市辖区', '630102': '城东区', '630103': '城中区', '630104': '城西区', '630105': '城北区', '630121': '大通回族土族自治县', '630122': '湟中县', '630123': '湟源县', '632121': '平安县', '632122': '民和回族土族自治县', '632123': '乐都县', '632126': '互助土族自治县', '632127': '化隆回族自治县', '632128': '循化撒拉族自治县', '632221': '门源回族自治县', '632222': '祁连县', '632223': '海晏县', '632224': '刚察县', '632321': '同仁县', '632322': '尖扎县', '632323': '泽库县', '632324': '河南蒙古族自治县', '632521': '共和县', '632522': '同德县', '632523': '贵德县', '632524': '兴海县', '632525': '贵南县', '632621': '玛沁县', '632622': '班玛县', '632623': '甘德县', '632624': '达日县', '632625': '久治县', '632626': '玛多县', '632721': '玉树县', '632722': '杂多县', '632723': '称多县', '632724': '治多县', '632725': '囊谦县', '632726': '曲麻莱县', '632801': '格尔木市', '632802': '德令哈市', '632821': '乌兰县', '632822': '都兰县', '632823': '天峻县', '640101': '市辖区', '640104': '兴庆区', '640105': '西夏区', '640106': '金凤区', '640121': '永宁县', '640122': '贺兰县', '640181': '灵武市', '640201': '市辖区', '640202': '大武口区', '640205': '惠农区', '640221': '平罗县', '640301': '市辖区', '640302': '利通区', '640303': '红寺堡区', '640323': '盐池县', '640324': '同心县', '640381': '青铜峡市', '640401': '市辖区', '640402': '原州区', '640422': '西吉县', '640423': '隆德县', '640424': '泾源县', '640425': '彭阳县', '640501': '市辖区', '640502': '沙坡头区', '640521': '中宁县', '640522': '海原县', '650101': '市辖区', '650102': '天山区', '650103': '沙依巴克区', '650104': '新市区', '650105': '水磨沟区', '650106': '头屯河区', '650107': '达坂城区', '650109': '米东区', '650121': '乌鲁木齐县', '650201': '市辖区', '650202': '独山子区', '650203': '克拉玛依区', '650204': '白碱滩区', '650205': '乌尔禾区', '652101': '吐鲁番市', '652122': '鄯善县', '652123': '托克逊县', '652201': '哈密市', '652222': '巴里坤哈萨克自治县', '652223': '伊吾县', '652301': '昌吉市', '652302': '阜康市', '652323': '呼图壁县', '652324': '玛纳斯县', '652325': '奇台县', '652327': '吉木萨尔县', '652328': '木垒哈萨克自治县', '652701': '博乐市', '652722': '精河县', '652723': '温泉县', '652801': '库尔勒市', '652822': '轮台县', '652823': '尉犁县', '652824': '若羌县', '652825': '且末县', '652826': '焉耆回族自治县', '652827': '和静县', '652828': '和硕县', '652829': '博湖县', '652901': '阿克苏市', '652922': '温宿县', '652923': '库车县', '652924': '沙雅县', '652925': '新和县', '652926': '拜城县', '652927': '乌什县', '652928': '阿瓦提县', '652929': '柯坪县', '653001': '阿图什市', '653022': '阿克陶县', '653023': '阿合奇县', '653024': '乌恰县', '653101': '喀什市', '653121': '疏附县', '653122': '疏勒县', '653123': '英吉沙县', '653124': '泽普县', '653125': '莎车县', '653126': '叶城县', '653127': '麦盖提县', '653128': '岳普湖县', '653129': '伽师县', '653130': '巴楚县', '653131': '塔什库尔干塔吉克自治县', '653201': '和田市', '653221': '和田县', '653222': '墨玉县', '653223': '皮山县', '653224': '洛浦县', '653225': '策勒县', '653226': '于田县', '653227': '民丰县', '654002': '伊宁市', '654003': '奎屯市', '654021': '伊宁县', '654022': '察布查尔锡伯自治县', '654023': '霍城县', '654024': '巩留县', '654025': '新源县', '654026': '昭苏县', '654027': '特克斯县', '654028': '尼勒克县', '654201': '塔城市', '654202': '乌苏市', '654221': '额敏县', '654223': '沙湾县', '654224': '托里县', '654225': '裕民县', '654226': '和布克赛尔蒙古自治县', '654301': '阿勒泰市', '654321': '布尔津县', '654322': '富蕴县', '654323': '福海县', '654324': '哈巴河县', '654325': '青河县', '654326': '吉木乃县', '659001': '石河子市', '659002': '阿拉尔市', '659003': '图木舒克市', '659004': '五家渠市'}
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
'''
时间戳转字符串格式时间
'''
def stamp_to_timestr(time_stamp,time_format):
    time_array = time.localtime(time_stamp)
    return time.strftime(time_format, time_array)
'''
获取偏移时间
'''
def get_ago_later_stamp(years=0,months=0,days=0,minutes=0,seconds=0):
    now = datetime.datetime.now()
    # print(now)
    now += datetime.timedelta(days=days)
    now += datetime.timedelta(minutes=minutes)
    now += datetime.timedelta(seconds=seconds)
    time_str = str(now)[:-7]
    # print(time_str)
    time_tuple = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    time_list = list(time_tuple)
    year = int(months/12)
    years += year
    # print(years)
    if(months > 0):
        months %= 12
    else:
        months %= 12*-1

    # print(months)
    time_list[0] += years
    time_list[1] += months
    #return time.strftime('%Y-%m-%d %H:%M:%S',tuple(time_list))
    return time.mktime(tuple(time_list))


def timestr_to_stamp(time_str, time_format):
    time_array = time.strptime(time_str, time_format)
    time_stamp  = time.mktime(time_array)
    return time_stamp
def random_date():
    start = int(get_ago_later_stamp(years=-49))  # 生成开始时间戳
    end = int(get_ago_later_stamp(years=-18))  # 生成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中间随机取出一个
    date = stamp_to_timestr(t, "%Y%m%d")  # 将时间元组转成格式化字符串（1976-05-21）
    return date

def random_order():
    return str(random.randint(1, 999)).zfill(3)

def make_id():
    seventh='{0}{1}{2}'.format(random.choice(list(area_dict.keys())),random_date(),random_order())
    s = 0
    for i in range(len(seventh)):
        s += int(seventh[i]) * id_code_list[i]
    idnumber = seventh + str(check_code_list[s%11])
    return idnumber
def make_addr(di_num):
    addr=''
    addr += shengdic[di_num[:2]]
    if(shidic[di_num[:4]]=='县' or shidic[di_num[:4]]=='市辖区'):
        pass
    else:
        addr += shidic[di_num[:4]]
    addr+=qudic[di_num[:6]]

    return addr
def make_info():
    id_num = make_id()
    info_dic ={"身份证号":id_num}
    if int(id_num[14:-1]) % 2 == 0:
        sex = '女'
    else:
        sex='男'
    info_dic['性别'] = sex
    info_dic['地址'] = make_addr(id_num)
    return info_dic


"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'make_info.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/10 6:26

import pymysql

def connect(**db):
    conn = pymysql.connect(**db)
    return conn


def query_one(sql,db):
    print(type(db))
    conn = connect(**db)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        # 执行sql语句
        cursor.execute(sql)
        row = cursor.fetchone()
        return row
    except Exception as  e:
        # 如果执行sql语句出现问题，则执行回滚操作
        print(e)
    finally:
        # 不论try中的代码是否抛出异常，这里都会执行
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()
"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'mysql_tool.py'], content=content)

        
content = """    
# -*- coding:utf-8 -*-


import random
import string
from datetime import time

import pinyin


# 1. 定义“获取性别”函数，函数名：get_sex()
# 2. 随机0和1,0代表男，1代表女
# 3. 打印日志
#       性别：0-男
#       性别：1-女
# 4. 返回性别（数字）
def random_sex():
    sex = random.randint(0,1)
    if sex == 0:
        print('性别：0-男')
    else:
        print('性别：1-女')
    return sex

# 1. 定义函数，函数名：get_name()
# 2. 需要支持指定性别，参数名sex
# 3. 提供3个字符串：百家姓、适合男性的字、适合女性的字
# 4. 姓名由3个字组成：姓+名1+名2
#       姓：从百家姓字符串随机1个
#       名1：若为男生，从boys中选1个字
#           若为女生，从girls里选1个字
#       名2：先随机0或1,0不需要第3个字，1需要第3个字
#           若需要第3个字，男生从boys中选1个，女生从girls中选1个
# 5. 返回名字（第1个字+第2个字+第3个字）
def random_name(sex=-1):
    if sex == -1:
        sex = random.randint(0,1)

    first_name = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华" \\
                 "金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞" \\
                 "任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐" \\
                 "康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈" \\
                 "宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林" \\
                 "刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯咎管卢莫经房裘缪干解应宗宣丁" \\
                 "贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄魏加封芮" \\
                 "羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁" \\
                 "仇栾暴甘钭厉戎祖武符刘姜詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲台从鄂索" \\
                 "咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍" \\
                 "却璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼" \\
                 "容向古易慎戈廖庚终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚" \\
                 "越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相" \\
                 "查后江红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇" \\
                 "甫尉迟公羊澹台公冶宗政濮阳淳于仲孙太叔申屠公孙乐正轩辕令狐钟离" \\
                 "闾丘长孙慕容鲜于宇文司徒司空亓官司寇仉督子车颛孙端木巫马公西漆" \\
                 "雕乐正壤驷公良拓拔夹谷宰父谷粱晋楚阎法汝鄢涂钦段干百里东郭南门" \\
                 "呼延归海羊舌微生岳帅缑亢况后有琴梁丘左丘东门西门商牟佘佴伯赏南" \\
                 "宫墨哈谯笪年爱阳佟第五言福百家姓续"
    girl = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲" \\
           "真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎" \\
           "锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰" \\
           "韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸" \\
           "菲寒伊亚宜可姬舒影荔枝思丽";
    boy = "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国" \\
          "胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博" \\
          "诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固" \\
          "之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛" \\
          "雄琛钧冠策腾楠榕风航弘";

    first = random.choice(first_name)
    names = boy if sex == 0 else girl
    second = random.choice(names)
    has_third = random.randint(0,1)
    third = random.choice(names) if has_third == 1 else ''
    full_name = first+second+third
    print('姓名：'+full_name)
    return full_name

# 1. 定义函数，函数名：get_pwd()
# 2. 密码长度8位，由大写字母、小写字母和数字组成
# 3. 至少包含1个大写字母、1个小写字母，1个数字
# 4. 其余5个字母随便取
# 5. 返回密码
def random_pwd():
    src = string.ascii_letters+string.digits
    pwd_list = random.sample(src,5)
    pwd_list.extend(random.sample(string.digits,1))
    pwd_list.extend(random.sample(string.ascii_uppercase,1))
    pwd_list.extend(random.sample(string.ascii_lowercase,1))
    random.shuffle(pwd_list)
    pwd = ''.join(pwd_list)
    print('密码：'+pwd)
    return pwd


'''
# 1. 定义函数，函数名：get_tell()
# 2. 前三位为号段，如186/135，从有效号段列表取
# 3. 至少包含1个大写字母、1个小写字母，1个数字
# 4. 其余5个字母随便取
# 5. 返回密码
'''
def random_tell():
    tel_first = ['139', '138', '137', '136', '135', '134',
                 '159', '158', '157', '150', '151', '152', '147',
                 '188', '187','182', '183', '184', '178', '130', '131',
                 '132', '156', '155', '186', '185', '145', '176',
                 '133', '153', '189', '180', '181', '177', '173']
    first = random.choice(tel_first)
    second = str(random.randint(0, 9999) + 10000)[1:]
    third = str(random.randint(0, 9999) + 10000)[1:]

    tell_num = first + second + third
    print('电话:'+tell_num)
    return tell_num


'''
# 1. 定义函数，函数名：get_addr()
# 2. 地址组成：省份+地区+路名+门牌号+房间号（楼层+号数）
#              eg：地址：上海市金山区河南广场33号1202室
# 3. 门牌号取值范围：11-150号
# 4. 房间号：
#       楼层高度范围：1-20层，不需前补0
#       房间号范围：1-20室，两位前补0（比如3，则改成03）
#       示例：12层第3个房间，房间号：1203室
# 5. 返回地址
'''
def random_addr():
    province ='上海市'
    districts = ['黄浦区','徐汇区','长宁区','静安区','普陀区','虹口区',
                 '闸北区','杨浦区','闵行区','宝山区','青浦区','松江区','嘉定区','奉贤区','金山区','浦东新区']
    road_list = '重庆大厦','黑龙江路','十梅庵街','遵义路','湘潭街',\\
                '瑞金广场','仙山街','仙山东路','仙山西大厦','白沙河路',\\
                '赵红广场','机场路','民航街','长城南路','流亭立交桥',\\
                '虹桥广场','长城大厦','礼阳路','风岗街','中川路','白塔广场',\\
                '兴阳路','文阳街','绣城路','河城大厦','锦城广场','崇阳街',\\
                '华城路','康城街','正阳路','和阳广场','中城路','江城大厦',\\
                '顺城路','安城街','山城广场','春城街','国城路','泰城街',\\
                '德阳路','明阳大厦','春阳路','艳阳街','秋阳路','硕阳街',\\
                '青威高速','瑞阳街','丰海路','双元大厦','惜福镇街道',\\
                '夏庄街道','古庙工业园','中山街','太平路','广西街',\\
                '潍县广场','博山大厦','湖南路','济宁街','芝罘路',\\
                '易州广场','荷泽四路','荷泽二街','荷泽一路','荷泽三大厦',\\
                '观海二广场','广西支街','观海一路','济宁支街','莒县路',\\
                '平度广场','明水路','蒙阴大厦','青岛路','湖北街',\\
                '江宁广场','郯城街','天津路','保定街','安徽路',\\
                '河北大厦','黄岛路','北京街','莘县路','济南街',\\
                '宁阳广场','日照街','德县路','新泰大厦','荷泽路',\\
                '山西广场','沂水路','肥城街','兰山路','四方街','平原广场',\\
                '泗水大厦','浙江路','曲阜街','寿康路','河南广场','泰安路',\\
                '大沽街','红山峡支路','西陵峡一大厦','台西纬一广场',\\
                '台西纬四街','台西纬二路','西陵峡二街','西陵峡三路',\\
                '台西纬三广场','台西纬五路','明月峡大厦','青铜峡路',\\
                '台西二街','观音峡广场','瞿塘峡街','团岛二路','团岛一街',\\
                '台西三路','台西一大厦','郓城南路','团岛三街','刘家峡路',\\
                '西藏二街','西藏一广场','台西四街','三门峡路','城武支大厦',\\
                '红山峡路','郓城北广场','龙羊峡路','西陵峡街','台西五路',\\
                '团岛四街','石村广场','巫峡大厦','四川路','寿张街',\\
                '嘉祥路','南村广场','范县路','西康街','云南路','巨野大厦',\\
                '西江广场','鱼台街','单县路','定陶街','滕县路','钜野广场',\\
                '观城路','汶上大厦','朝城路','滋阳街','邹县广场','濮县街',\\
                '磁山路','汶水街','西藏路','城武大厦','团岛路','南阳街',\\
                '广州路','东平街','枣庄广场','贵州街','费县路','南海大厦',\\
                '登州路','文登广场','信号山支路','延安一街','信号山路',\\
                '兴安支街','福山支广场','红岛支大厦','莱芜二路','吴县一街',\\
                '金口三路','金口一广场','伏龙山路','鱼山支街','观象二路',\\
                '吴县二大厦','莱芜一广场','金口二街','海阳路','龙口街',\\
                '恒山路','鱼山广场','掖县路','福山大厦','红岛路','常州街',\\
                '大学广场','龙华街','齐河路','莱阳街','黄县路','张店大厦',\\
                '祚山路','苏州街','华山路','伏龙街','江苏广场','龙江街',\\
                '王村路','琴屿大厦','齐东路','京山广场','龙山路','牟平街',\\
                '延安三路','延吉街','南京广场','东海东大厦','银川西路',\\
                '海口街','山东路','绍兴广场','芝泉路','东海中街','宁夏路',\\
                '香港西大厦','隆德广场','扬州街','郧阳路','太平角一街',\\
                '宁国二支路','太平角二广场','天台东一路','太平角三大厦',\\
                '漳州路一路','漳州街二街','宁国一支广场','太平角六街',\\
                '太平角四路','天台东二街','太平角五路','宁国三大厦',\\
                '澳门三路','江西支街','澳门二路','宁国四街','大尧一广场',\\
                '咸阳支街','洪泽湖路','吴兴二大厦','澄海三路','天台一广场',\\
                '新湛二路','三明北街','新湛支路','湛山五街','泰州三广场',\\
                '湛山四大厦','闽江三路','澳门四街','南海支路','吴兴三广场',\\
                '三明南路','湛山二街','二轻新村镇','江南大厦','吴兴一广场',\\
                '珠海二街','嘉峪关路','高邮湖街','湛山三路','澳门六广场',\\
                '泰州二路','东海一大厦','天台二路','微山湖街','洞庭湖广场',\\
                '珠海支街','福州南路','澄海二街','泰州四路','香港中大厦',\\
                '澳门五路','新湛三街','澳门一路','正阳关街','宁武关广场',\\
                '闽江四街','新湛一路','宁国一大厦','王家麦岛','澳门七广场',\\
                '泰州一路','泰州六街','大尧二路','青大一街','闽江二广场',\\
                '闽江一大厦','屏东支路','湛山一街','东海西路',\\
                '徐家麦岛函谷关广场','大尧三路','晓望支街','秀湛二路',\\
                '逍遥三大厦','澳门九广场','泰州五街','澄海一路','澳门八街',\\
                '福州北路','珠海一广场','宁国二路','临淮关大厦','燕儿岛路',\\
                '紫荆关街','武胜关广场','逍遥一街','秀湛四路','居庸关街',\\
                '山海关路','鄱阳湖大厦','新湛路','漳州街','仙游路','花莲街'
    district = random.choice(districts)
    road = random.choice(road_list)
    no = str(random.randint(11,150))+'号'
    room = str(random.randint(1,20))+str(random.randint(100,120))[1:]+'室'
    addr = province+district+road+no+room
    print('地址：'+addr)
    return addr

'''
# 1. 定义函数，函数名：get_email()
# 2. 邮箱组成：
#       首字符：只能是字母（大写或小写）
#       其余字符：大写字母、小写字母、数字、下划线
#       邮箱后缀：主流邮箱服务商，如@126.com、@gmail.com、@qq.com等
# 3. 邮箱名长度：6-18位
# 4. 返回邮箱
'''
def random_email():
    email_suffix = ['@gmail.com','@yahoo.com','@msn.com','@hotmail.com',
                    '@aol.com','@ask.com','@live.com','@qq.com',
                    '@0355.net','@163.com','@163.net','@263.net',
                    '@3721.net','@yeah.net','@googlemail.com','@126.com',
                    '@sina.com','@sohu.com','@yahoo.com.cn']
    first = random.choice(string.ascii_letters)
    num = string.ascii_letters+string.digits+"_"
    length = random.randint(5,17)
    second = ''.join(map(str,random.sample(num,length)))
    third = random.choice(email_suffix)
    email = first+second+third
    print('邮箱：'+email)
    return email

def random_name_pinyin(name=''):
    if name == '':
        name = random_name()
    if len(name) == 2:
        name_pinyin = pinyin.get(name, format='strip')
    else:
        name_pinyin = pinyin.get(name[0],format='strip')+pinyin.get_initial(name[1:],delimiter="")
    print('姓名（拼音）：'+name_pinyin)
    return name_pinyin

def random_number(min=0,max=1,step=1):
    num = random.randrange(min,max,step)
    print('随机数：'+str(num))
    return num

# 随机字母
def random_str_abc(num):
    str =''
    for i in range(num):
        str=str+random.choice(string.ascii_letters)
    return str


# 中文
def random_chinese():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

# 常用汉字
def random_gbk_chines():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'random_tool.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/14 8:26

# 字典转字符串
def dic_to_str(dic):
    s = ''
    for key in dic:
        s+="{0}: {1}\\n".format(key,dic[key])
    return s"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'string_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-tools-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:52
import datetime

def get_now():
    date_time=str(datetime.datetime.now())[0:19]
    print(date_time)
    return date_time

def get_today():
    date=str(datetime.datetime.now())[0:10]
    print(date)
    return date

def get_time():
    time = str(datetime.datetime.now())[11:19]
    print(time)
    return time

if __name__ == '__main__':
    get_now()
    get_today()
    get_time()"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'time_tool.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 22:47
import yaml

def get_yaml(yaml_path):
    with open(yaml_path,'r',encoding='utf-8') as f:
        content =yaml.load(f.read(),Loader=yaml.FullLoader)
    return content"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', 'yaml_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-api-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:25"""
os_tool.mkfile(root_path,*['./', 'tools', 'data', '__init__.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'tools', 'os']))
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/11 18:31
import os
import shutil
import stat


def get_root_path():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)).replace('\\\\', '/')
    print(root_path)
    if root_path.find('venv') > 0:
        root_path=root_path[:root_path.find('venv')-1]
    return root_path+'/'

def deldir(dir):
    if os.path.exists(dir):
        for file in os.listdir(dir):
            file = os.path.join(dir, file)
            if os.path.isdir(file):
                print("remove dir", file)
                os.chmod(file, stat.S_IWRITE|stat.S_IWOTH)
                deldir(file)
            elif os.path.isfile(file) :
                print("remove file", file)
                os.chmod(file, stat.S_IWRITE|stat.S_IWOTH)
                os.remove(file)
        shutil.rmtree(dir,True)

def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)

def remove(path):
    is_exists = os.path.exists(path)
    if is_exists:
        os.remove(path)

def exists(file_or_path):
    is_exists = os.path.exists(file_or_path)
    return is_exists
#
# def copy_dir(source_path,target_path):
#     if not os.path.exists(target_path):
#         os.makedirs(target_path)
#
#     if os.path.exists(source_path):
#         # root 所指的是当前正在遍历的这个文件夹的本身的地址
#         # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
#         # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
#         for root, dirs, files in os.walk(source_path):
#             for file in files:
#                 src_file = os.path.join(root, file)
#                 shutil.copy(src_file, target_path)
#                 print(src_file)
#
#     print('copy files finished!')

def move(src_dir,target_dir):
    if not os.path.exists(target_dir):
        shutil.move(src_dir,target_dir)

def copy_dir(src_dir,target_dir):
    if not os.path.exists(target_dir):
        shutil.copytree(src_dir,target_dir)

def copy_file(src_file,target_dir):
    shutil.copy(src_file,target_dir)"""
os_tool.mkfile(root_path,*['./', 'tools', 'os', 'os_tool.py'], content=content)

        
content = """'''
封装执行shell语句方法
'''

import subprocess
from tools.report import log_tool


def invoke(cmd):
    try:
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        print(o)
        return o
    except Exception as e:
        log_tool.error('执行命令失败，请检查环境配置')
        log_tool.error(e)
        raise

"""
os_tool.mkfile(root_path,*['./', 'tools', 'os', 'shell_tool.py'], content=content)

        
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 18:56

import zipfile
import os


# zipfile解压
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\\\', '/')
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir): os.mkdir(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


if __name__ == '__main__':
    unzip_file('C:/softwareData/PycharmProjects/test-ui-1/chrom_driver/chromedriver_win32.zip',
               'C:/softwareData/PycharmProjects/test-ui-1/chrom_driver')
"""
os_tool.mkfile(root_path,*['./', 'tools', 'os', 'zip_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-api-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:30"""
os_tool.mkfile(root_path,*['./', 'tools', 'os', '__init__.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'tools', 'report']))
content = """'''
封装Assert方法

'''
from tools.report import log_tool
import json


def assert_in(body, expected_msg):
    '''
    验证response body中是否包含预期字符串
    :param body:
    :param expected_msg:
    :return:
    '''
    try:
        text = json.dumps(body, ensure_ascii=False)
        # print(text)
        assert expected_msg in text
        return True

    except:
        log_tool.error("不包含期望值, 期望值 是  %s" % expected_msg)
        raise


def assert_equal(body, expected_msg):
    '''
    验证response body中是否等于预期字符串
    :param body:
    :param expected_msg:
    :return:
    '''
    try:
        assert body == expected_msg
        return True
    except:
        log_tool.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
        raise


def assert_time(time, expected_time):
    '''
    验证response body响应时间小于预期最大响应时间,单位：毫秒
    :param body:
    :param expected_time:
    :return:
    '''
    try:
        assert time < expected_time
        return True

    except:
        log_tool.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
        raise


def assert_not_null(actual):
    '''
            验证实际结果不为null
            :param actual:
            :return:
            '''
    try:
        assert actual != ''
        return True

    except:
        log_tool.error("预期不为空，实际结果为空")
        raise
"""
os_tool.mkfile(root_path,*['./', 'tools', 'report', 'assert_tool.py'], content=content)

        
content = """import allure
import json
from tools.report import log_tool
from tools.data import string_tool
from tools.report import assert_tool
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf
from tools.data.json_path_tool import *

# log decorator
def logs(func):
    def _func(*args, **kwargs):
        r= func(*args, **kwargs)
        request = "-------------------request-------------" \\
                  "\\n{0}\\n{1}\\n{2}".format(r.url, string_tool.dic_to_str(r.request.headers), r.request.body)
        log_tool.info(request)
        response = "---------------response----------------" \\
                   "\\n{0}\\n{1}\\n{2}".format(r.status_code, string_tool.dic_to_str(r.headers), r.text)
        log_tool.info(response)
        allure.attach(request,'request',allure.attachment_type.TEXT)
        allure.attach(response, 'response', allure.attachment_type.TEXT)
        return r
    return _func



# screenshot decorator
def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)
        i = 1
        res = None
        while(i <= 3):
            try:
                res = func(*args, **kwargs)
                break
            except :
                if i == 3:
                    allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
                    raise
                i += 1
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
        return res
    return function


def is_empty(a):
    if isinstance(a,int) or not a:
        return True
    elif(isinstance(a,str) and len(a)==0):
        return True
    return False



def datas(func):
    def function(*args,**kwargs):
        data=kwargs.pop("pub_data")
        d = kwargs
        keys = list(kwargs.keys())
        for k in ['json_data','json']:
            if k in keys :
                keys.remove(k)
                value = d.pop(k)
                if (isinstance(value, str)):
                    d['json'] = json.loads(value)
                else:
                    d['json']=value
        with allure.step("第一步：获取url"):
            pass
        if 'uri' in keys:
            keys.remove('uri')
            value = d.pop('uri')
            d['url'] = value
        for k in ["feature",'story','tag','testcase','description','title','issue','link','mro','severity']:
            if k in keys:
                keys.remove(k)
                value = d.pop(k)
                if not is_empty(value)  and isinstance(value,list):
                    getattr(allure.dynamic, k)(*value)
                elif(not is_empty(value)  and isinstance(value,str)):
                    getattr(allure.dynamic, k)(value)
        with allure.step("第二步：准备测试数据"):pass
        try:
            index_dic(data, data)
            index_dic(d,data)
        except:
            pass
        if "url" not in keys:
            print("请输入正确的uri")
        if 'http://' not in d["url"]:
            d["url"] = conf.API_URL + d["url"]
        for s in ["status_code",'expect',"json_path"]:
            if s in keys:
                keys.remove(s)
                exec("{} = d.pop(s)".format(s))

            else:
                exec("{}=None".format(s))
        with allure.step("第三步：发送请求"):
            resp = func(*args,**kwargs)
        try:
            exec('''
if(len(json_path) != 0):
    for path in json_path:
        get_json_data(resp.json(),path,data)''')

        except:
            pass
        a = '''
if not is_empty(status_code):    
    # 判断响应码
    allure.attach("预期结果：{}\\\\n------------------------------------------------------\\\\n实际结果：{}".format(status_code, resp.status_code), "响应状态码断言", allure.attachment_type.TEXT)
    assert_tool.assert_equal(resp.status_code, status_code)
if not is_empty(expect):
    # 判断响应码
    allure.attach("预期结果：{}\\\\n------------------------------------------------------\\\\n实际结果：{}".format(expect, resp.text), "响应正文断言", allure.attachment_type.TEXT)
    assert_tool.assert_in(resp.text, expect)'''
        with allure.step("第四步：判断结果"):
            exec(a)

        return resp
    return function





"""
os_tool.mkfile(root_path,*['./', 'tools', 'report', 'decorators_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-tools-demo
# Creator: LudvikWoo
# Create time: 2019-09-18 00:26
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart



def test_send_text():
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com"  # 设置服务器
    mail_user = "wuling1105@126.com"  # 用户名
    mail_pass = "126shouquanma"  # 口令

    sender = 'wuling1105@126.com'
    receivers = ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('果芽软件自动代码', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ';'.join(receivers)

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def test_send_html():
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com"  # 设置服务器
    mail_user = "wuling1105@126.com"  # 用户名
    mail_pass = "126shouquanma"  # 口令

    sender = 'wuling1105@126.com'
    receivers = ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    mail_msg = '''
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.guoyasoft.com">这是一个链接</a></p>
    '''
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = ';'.join(receivers)

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def test_send_attach():
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com"  # 设置服务器
    mail_user = "wuling1105@126.com"  # 用户名
    mail_pass = "126shouquanma"  # 口令

    sender = 'wuling1105@126.com'
    receivers = ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ';'.join(receivers)
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    att2 = MIMEText(open('guoya.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    message.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
"""
os_tool.mkfile(root_path,*['./', 'tools', 'report', 'email_tool.py'], content=content)

        
content = """import logging
from logging.handlers import TimedRotatingFileHandler
from tools.os import os_tool

'''
封装log方法
'''
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
root_path =  '../../logs/'
os_tool.mkdir(root_path)

handler = TimedRotatingFileHandler(root_path + 'info.log',when = 'd',interval = 1,backupCount=30,encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


handler2 = TimedRotatingFileHandler(root_path + 'error.log',when = 'd',interval = 1,backupCount=30,encoding='utf-8')
handler2.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter)
logger.addHandler(handler2)

handler3 = logging.StreamHandler()
handler3.setLevel(logging.DEBUG)
formatter = logging.Formatter()
handler3.setFormatter(formatter)
logger.addHandler(handler3)


def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)

"""
os_tool.mkfile(root_path,*['./', 'tools', 'report', 'log_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-api-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:29"""
os_tool.mkfile(root_path,*['./', 'tools', 'report', '__init__.py'], content=content)

        
os_tool.mkdir(os.path.join(root_path,*['./', 'tools', 'security']))
content = """# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/21 14:53
import hashlib

def md5_passwd(str,key='123456'):
    #satl是盐值，默认是123456
    str=str+key
    md = hashlib.md5()  # 构造一个md5对象
    md.update(str.encode())
    res = md.hexdigest()
    return res
"""
os_tool.mkfile(root_path,*['./', 'tools', 'security', 'md5_tool.py'], content=content)

        
content = """# -*- coding: utf-8 -*- 
# Project: guoya-api-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:30"""
os_tool.mkfile(root_path,*['./', 'tools', 'security', '__init__.py'], content=content)

        
content = """import pytest


@pytest.fixture(scope="session")
def pub_data():
    data = {'token':'asdfasdfjsldkfjlsxllkj'}
    return data"""
os_tool.mkfile(root_path,*['./', 'tools', '__init__.py'], content=content)

        