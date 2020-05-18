#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Tue 12 May 2020 04:02:19 PM CST
File Name   : test_pywinrm_1.py
Description : 
'''

import winrm

hostname='172.30.126.231'
# hostname='WIN-OJ3IKT2C0C9'
username='administrator'
password='Passw0rd'
cmd='hostname'

wintest = winrm.Session('http://'+hostname+':5985/wsman',auth=(username,password))
ret = wintest.run_cmd(cmd)
print("ret:", ret)
print("std_out:", ret.std_out.decode())
print("std_err:", ret.std_err)


"""
[root@lixx ~]# pip install pywinrm
[root@lixx ~]# python test_pywinrm_1.py
('ret:', <Response code 0, out "WIN-OJ3IKT2C0C9
", err "">)
('std_out:', u'WIN-OJ3IKT2C0C9\r\n')
('std_err:', '')
"""
