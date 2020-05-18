#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Fri 15 May 2020 05:34:17 PM CST
File Name   : test_pywinrm_4.py
Description : 
'''

import winrm


hostname = '172.30.126.231'
#hostname = 'WIN-OJ3IKT2C0C9'
# username = 'win\\administrator'
username = r'win\administrator'
password = 'Passw0rd'

## 管理员（administrator）用户环境命令
cmd = 'hostname'
script1 = """hostname
pwd"""
script2 = 'hostname; pwd'

## 域控用户（win\administrator）环境命令
# cmd = 'get-scvmhost'

## 使用管理员（administrator）用户时, 默认 transport = 'plaintext'
# wintest = winrm.Session('https://'+hostname+':5986/wsman', auth=(username,password))
wintest = winrm.Session('http://'+hostname+':5985/wsman', auth=(username,password))

## 使用域控用户 win\administrator时，设置 transport='ntlm'
# wintest = winrm.Session('https://'+hostname+':5986/wsman', auth=(username,password))
wintest = winrm.Session('http://'+hostname+':5985/wsman', auth=(username,password), transport='ntlm')

## 运行doc命令
# ret = wintest.run_cmd(cmd)

## 运行PowerShell脚本
# ret = wintest.run_ps(script1)
ret = wintest.run_ps(script2)

print(ret)
print(ret.std_out.decode())
print(ret.std_err)
