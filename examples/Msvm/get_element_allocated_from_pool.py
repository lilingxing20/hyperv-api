# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_ElementAllocatedFromPool") #OK 
for obj in objs:
    print(obj)

# PS D:\vscode> & C:/Python38/python.exe d:/vscode/python/hyperv/Msvm/get_element_allocated_from_pool.py

# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:DACDCF3F-6F67-4eb8-A4D0-5D93B48A2468\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteDrive.CreationClassName=\"Msvm_DisketteDrive\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DVDDrive.CreationClassName=\"Msvm_DVDDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticMouse.CreationClassName=\"Msvm_SyntheticMouse\",DeviceID=\"Microsoft:58F75A6D-D949-4320-99E1-A2A2576D581C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D45268DA-37C5-44da-B827-B0C55CCB3BDC\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticDisplayController.CreationClassName=\"Msvm_SyntheticDisplayController\",DeviceID=\"Microsoft:F3CF6965-E8D3-44A9-9B7D-A04245EA7525\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SCSIProtocolController.CreationClassName=\"Msvm_SCSIProtocolController\",DeviceID=\"Microsoft:5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:6A45335D-4C3A-44b7-B61F-C9808BBDF8ED\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPort.CreationClassName=\"Msvm_SyntheticEthernetPort\",DeviceID=\"Microsoft:A3B6C664-3E69-4229-B688-A75358526ECF\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334D-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:DACDCF3F-6F67-4eb8-A4D0-5D93B48A2468\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteDrive.CreationClassName=\"Msvm_DisketteDrive\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DVDDrive.CreationClassName=\"Msvm_DVDDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticMouse.CreationClassName=\"Msvm_SyntheticMouse\",DeviceID=\"Microsoft:58F75A6D-D949-4320-99E1-A2A2576D581C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D45268DA-37C5-44da-B827-B0C55CCB3BDC\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticDisplayController.CreationClassName=\"Msvm_SyntheticDisplayController\",DeviceID=\"Microsoft:F3CF6965-E8D3-44A9-9B7D-A04245EA7525\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:6A45335D-4C3A-44b7-B61F-C9808BBDF8ED\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPort.CreationClassName=\"Msvm_SyntheticEthernetPort\",DeviceID=\"Microsoft:F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SCSIProtocolController.CreationClassName=\"Msvm_SCSIProtocolController\",DeviceID=\"Microsoft:39F5E639-4697-4214-A1E2-6605AE65645F\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334D-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementAllocatedFromPool
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:146C56A0-3546-469B-9737-FCBCF82428F4\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
# };