#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/15'
import os

content={"c":"","root_path":os.path.dirname(__file__)}

def get_files(path):
    root_path = os.path.join(content["root_path"],*path)
    files = os.listdir(root_path)
    j = []
    for f in files:
        i=[]
        if (f in ['venv','.idea',"__pycache__",'to_init_porject.py']):
            continue
        if f.endswith(".pyc"):
            continue
        i.extend(path)
        i.append(f)
        j.append(i)
    return j

def mk_files(content,file):
    root_path = os.path.join(content["root_path"],*file)
    with  open(root_path,'r',encoding="utf-8") as f :
        # f.readline()
        c = f.read()

        c = c.replace('"""',"'''")
        c = c.replace('\\', "\\\\")

        content['c'] += '''
content = """{}"""
os_tool.mkfile(root_path,*{}, content=content)

        '''.format(c,file)

def mk_dirs(content,dir):
    content['c'] += """
os_tool.mkdir(os.path.join(root_path,*{}))""".format(dir)
    files = get_files(dir)
    for f in files:
        s = os.path.join(content["root_path"],*f)
        if os.path.isdir(s):
            mk_dirs(content,f)
        else:
            mk_files(content,f)

def mk_project(content):
    content["c"] += """#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tools import os_tool
import os
############################
# 初始化工程目录
############################
root_path = os_tool.get_root_path()

    """
    files = get_files(["./"])
    for f in files:
        s= os.path.join(content["root_path"],*f)
        if os.path.isdir(s):
            mk_dirs(content,f)
        else:
            mk_files(content,f)




if __name__ == '__main__':
    mk_project(content)
    with open("init_project.py",'w',encoding='utf-8') as f :
        f.write(content['c'])