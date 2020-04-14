# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_AffectedStorageJobElement") #OK 
for obj in objs: 
    print(obj)


# 重置虚拟机操作
# PS D:\vscode> & C:/Python38/python.exe d:/vscode/python/hyperv/Msvm/get_affected_job_element.py

# instance of Msvm_AffectedJobElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ConcreteJob.InstanceID=\"7758B7D5-BEF6-49F7-9E8E-69E308DDD118\"";
#         ElementEffects = {0};
#         OtherElementEffectsDescriptions = {};
# };