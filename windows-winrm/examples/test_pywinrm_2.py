#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Tue 12 May 2020 04:02:19 PM CST
File Name   : test_pywinrm_2.py
Description : 
'''


from winrm.protocol import Protocol


p = Protocol(
    #endpoint='https://172.30.126.231:5986/wsman',
    endpoint='http://172.30.126.231:5985/wsman',
    transport='ntlm',
    username=r'win\administrator',
    #username=r'administrator',
    password='Passw0rd',
    #server_cert_validation='ignore'
    )

shell_id = p.open_shell()
#command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
command_id = p.run_command(shell_id, 'Get-SCVMHost', [])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
print(std_out)
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
