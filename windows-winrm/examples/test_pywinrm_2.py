#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Tue 12 May 2020 04:02:19 PM CST
File Name   : test_pywinrm_2.py
Description : 
'''

from __future__ import unicode_literals
from base64 import b64encode
from winrm.protocol import Protocol


p = Protocol(
    #endpoint='https://172.30.126.231:5986/wsman',
    endpoint='http://172.30.126.231:5985/wsman',
    transport='ntlm',
    username=r'win\administrator',
    #username=r'administrator',
    password='Passw0rd',
    server_cert_validation='ignore'
    )

shell_id = p.open_shell()
#command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
script='ls'
encoded_ps = b64encode(script.encode('utf_16_le')).decode('utf-8')
p.run_command(shell_id, 'chcp 65001', [])
command_id = p.run_command(shell_id, 'powershell -encodedcommand {0}'.format(encoded_ps), [])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
print(std_out.decode('utf-8'))
print(std_err)
print(status_code)


"""
[root@lixx ~]# pip install pywinrm
[root@lixx ~]# python test_pywinrm_2.py
('ret:', <Response code 0, out "WIN-OJ3IKT2C0C9
", err "">)
('std_out:', u'WIN-OJ3IKT2C0C9\r\n')
('std_err:', '')
"""
