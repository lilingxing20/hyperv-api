# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_SystemTerminalConnection") #OK 
for obj in objs: 
    print(obj)

# (Pdb) objs = client.query("SELECT * FROM Msvm_SystemTerminalConnection")
# (Pdb) print(objs[0])
#
# instance of Msvm_SystemTerminalConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TerminalConnection.ConnectionID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\1\"";
# };
