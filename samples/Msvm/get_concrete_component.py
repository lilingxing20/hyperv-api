# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_ConcreteComponent") #OK 
for obj in objs: 
    print(obj)


# PS D:\vscode> & C:/Python38/python.exe d:/vscode/python/hyperv/Msvm/get_concrete_component.py

# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\Aggregate\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };

# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\Aggregate\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\3\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\6\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\8\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\2\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\5\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskDrive.CreationClassName=\"Msvm_DiskDrive\",DeviceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:5F07AFDD-5851-415D-BEEF-BB46641A022D\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:27592149-0E67-4569-98FB-585586928ED8\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\2\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\3\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\5\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\6\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\8\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\9\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\10\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\11\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\12\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\13\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\14\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\15\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\16\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\17\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\18\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\19\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\20\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\21\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\22\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\23\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\2\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\3\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\5\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\6\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\8\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\9\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\10\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\11\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\12\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\13\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\14\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\15\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\16\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\17\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\18\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\19\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\20\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\21\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\22\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ConcreteComponent
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\23\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };