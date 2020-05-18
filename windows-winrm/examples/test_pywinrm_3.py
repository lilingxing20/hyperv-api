#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Fri 15 May 2020 04:47:28 PM CST
File Name   : test_pywinrm_3.py
Description : 
'''

from base64 import b64encode
from winrm.protocol import Protocol

p = Protocol(
    # endpoint='https://10.10.10.231:5986/wsman',
    endpoint='http://172.30.126.231:5985/wsman',
    transport='ntlm',
    # username=r'win\administrator',
    username='win\\administrator',
    password='Passw0rd',
    server_cert_validation='ignore')

cmd='hostname'
cmd='get-scvmhost'
encoded_ps = b64encode(cmd.encode('utf_16_le')).decode('ascii')
cmd2 = 'powershell -encodedcommand {0}'.format(encoded_ps)

# cmd='powershell -encodedcommand get-scvmhost'
shell_id = p.open_shell()
# command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
command_id = p.run_command(shell_id, cmd2, [])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
print(std_out)
print(std_err)
print(status_code)
