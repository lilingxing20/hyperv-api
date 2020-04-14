# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_SystemBios") #OK 
for obj in objs: 
    print(obj)


# instance of Msvm_SystemBIOS
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BIOSElement.Name=\"BIOS\",SoftwareElementID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\AC6B8DC1-3257-4A70-B1B2-A9C9215659AD\",SoftwareElementState=2,TargetOperatingSystem=0,Version=\"09.00.06\"";
# };

# instance of Msvm_SystemBIOS
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BIOSElement.Name=\"BIOS\",SoftwareElementID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\AC6B8DC1-3257-4A70-B1B2-A9C9215659AD\",SoftwareElementState=2,TargetOperatingSystem=0,Version=\"09.00.06\"";
# };