# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_SystemExportSettingData") #OK 
for obj in objs: 
    print(obj)


# instance of Msvm_SystemExportSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemExportSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };

# instance of Msvm_SystemExportSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemExportSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };

# instance of Msvm_SystemExportSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemExportSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
# };