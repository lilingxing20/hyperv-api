# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_SettingsDefineState") #OK 
for obj in objs: 
    print(obj)




# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Keyboard.CreationClassName=\"Msvm_Keyboard\",DeviceID=\"Microsoft:DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_PS2Mouse.CreationClassName=\"Msvm_PS2Mouse\",DeviceID=\"Microsoft:655BC5C5-A784-46B7-81BC-E26328F7EB0E\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_S3DisplayController.CreationClassName=\"Msvm_S3DisplayController\",DeviceID=\"Microsoft:7D80D3DB-61EE-4879-8879-5609F1100AD0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\7D80D3DB-61EE-4879-8879-5609F1100AD0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteController.CreationClassName=\"Msvm_DisketteController\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteDrive.CreationClassName=\"Msvm_DisketteDrive\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialController.CreationClassName=\"Msvm_SerialController\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialPort.CreationClassName=\"Msvm_SerialPort\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialPort.CreationClassName=\"Msvm_SerialPort\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\1\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_IDEController.CreationClassName=\"Msvm_IDEController\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_IDEController.CreationClassName=\"Msvm_IDEController\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DVDDrive.CreationClassName=\"Msvm_DVDDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticMouse.CreationClassName=\"Msvm_SyntheticMouse\",DeviceID=\"Microsoft:58F75A6D-D949-4320-99E1-A2A2576D581C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticDisplayController.CreationClassName=\"Msvm_SyntheticDisplayController\",DeviceID=\"Microsoft:F3CF6965-E8D3-44A9-9B7D-A04245EA7525\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SCSIProtocolController.CreationClassName=\"Msvm_SCSIProtocolController\",DeviceID=\"Microsoft:5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPort.CreationClassName=\"Msvm_SyntheticEthernetPort\",DeviceID=\"Microsoft:A3B6C664-3E69-4229-B688-A75358526ECF\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\A3B6C664-3E69-4229-B688-A75358526ECF\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334D-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";  
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Keyboard.CreationClassName=\"Msvm_Keyboard\",DeviceID=\"Microsoft:DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_PS2Mouse.CreationClassName=\"Msvm_PS2Mouse\",DeviceID=\"Microsoft:655BC5C5-A784-46B7-81BC-E26328F7EB0E\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_S3DisplayController.CreationClassName=\"Msvm_S3DisplayController\",DeviceID=\"Microsoft:7D80D3DB-61EE-4879-8879-5609F1100AD0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\7D80D3DB-61EE-4879-8879-5609F1100AD0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteController.CreationClassName=\"Msvm_DisketteController\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DisketteDrive.CreationClassName=\"Msvm_DisketteDrive\",DeviceID=\"Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialController.CreationClassName=\"Msvm_SerialController\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialPort.CreationClassName=\"Msvm_SerialPort\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SerialPort.CreationClassName=\"Msvm_SerialPort\",DeviceID=\"Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\1\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_IDEController.CreationClassName=\"Msvm_IDEController\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LogicalDisk.CreationClassName=\"Msvm_LogicalDisk\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_IDEController.CreationClassName=\"Msvm_IDEController\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DVDDrive.CreationClassName=\"Msvm_DVDDrive\",DeviceID=\"Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticMouse.CreationClassName=\"Msvm_SyntheticMouse\",DeviceID=\"Microsoft:58F75A6D-D949-4320-99E1-A2A2576D581C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticDisplayController.CreationClassName=\"Msvm_SyntheticDisplayController\",DeviceID=\"Microsoft:F3CF6965-E8D3-44A9-9B7D-A04245EA7525\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPort.CreationClassName=\"Msvm_SyntheticEthernetPort\",DeviceID=\"Microsoft:F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SCSIProtocolController.CreationClassName=\"Msvm_SCSIProtocolController\",DeviceID=\"Microsoft:39F5E639-4697-4214-A1E2-6605AE65645F\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\39F5E639-4697-4214-A1E2-6605AE65645F\\\\0\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334D-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";  
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Synth3dVideoPool.InstanceID=\"Microsoft:06FF76FA-2D58-4BAF-9F8D-455773824F37\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\06FF76FA-2D58-4BAF-9F8D-455773824F37\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:146C56A0-3546-469B-9737-FCBCF82428F4\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\146C56A0-3546-469B-9737-FCBCF82428F4\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcPortAllocationSettingData.InstanceID=\"Microsoft:Pool\\\\698F2285-28DC-4438-A147-82D7432C5254\\\\146C56A0-3546-469B-9737-FCBCF82428F4\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\698F2285-28DC-4438-A147-82D7432C5254\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:19839BFF-6F04-4B24-B4B5-1AFCCBE729DE\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\19839BFF-6F04-4B24-B4B5-1AFCCBE729DE\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\353B3BE8-310C-4CF4-839E-4E1B14616136\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\4764334E-E001-4176-82EE-5594EC9B530E\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4EA4F71F-16E6-4250-99A8-A2315332CC64\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\4EA4F71F-16E6-4250-99A8-A2315332CC64\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:78AA0C27-B2BD-45BA-83D1-5F2A8C4C6656\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\78AA0C27-B2BD-45BA-83D1-5F2A8C4C6656\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\7951A5ED-8DC5-42D7-AA8C-9F14C54CEB84\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\BDE5D4D6-E450-46D2-B925-976CA3E989B4\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D45268DA-37C5-44da-B827-B0C55CCB3BDC\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\D45268DA-37C5-44DA-B827-B0C55CCB3BDC\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:DACDCF3F-6F67-4EB8-A4D0-5D93B48A2468\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\DACDCF3F-6F67-4EB8-A4D0-5D93B48A2468\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolSettingData.InstanceID=\"Microsoft:Pool\\\\F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitch.CreationClassName=\"Msvm_VirtualEthernetSwitch\",Name=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitchSettingData.InstanceID=\"Microsoft:50FEBE89-6E35-4456-8536-85E8E34A529B\"";
# };


# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitch.CreationClassName=\"Msvm_VirtualEthernetSwitch\",Name=\"78D861EC-60B6-4365-92E3-F905CCC292F7\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitchSettingData.InstanceID=\"Microsoft:78D861EC-60B6-4365-92E3-F905CCC292F7\"";
# };

# instance of Msvm_SettingsDefineState
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitch.CreationClassName=\"Msvm_VirtualEthernetSwitch\",Name=\"A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualEthernetSwitchSettingData.InstanceID=\"Microsoft:A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
# };


# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualFcSwitch.CreationClassName=\"Msvm_VirtualFcSwitch\",Name=\"E0198D60-8825-4FF1-A7C2-A8956152B443\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualFcSwitchSettingData.InstanceID=\"Microsoft:E0198D60-8825-4FF1-A7C2-A8956152B443\"";
# };


# instance of Msvm_SettingsDefineState
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualFcSwitch.CreationClassName=\"Msvm_VirtualFcSwitch\",Name=\"411F1781-13E9-48FB-B6BA-6AF626438696\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualFcSwitchSettingData.InstanceID=\"Microsoft:411F1781-13E9-48FB-B6BA-6AF626438696\"";
# };