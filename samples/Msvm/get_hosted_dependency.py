# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_HostedDependency") #OK 
for obj in objs: 
    print(obj)

# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\2\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\3\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\5\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\6\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\8\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\9\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\10\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\11\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\12\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\13\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\14\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\15\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\16\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\17\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\18\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\19\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\20\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\21\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\22\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\23\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\2\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\3\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\5\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\6\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\7\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\8\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\9\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\10\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\11\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\12\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\13\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\14\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\15\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\16\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\17\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\18\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\19\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\20\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\21\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\22\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_NumaNode.CreationClassName=\"Msvm_NumaNode\",NodeID=\"Microsoft:PhysicalNode\\\\1\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Processor.CreationClassName=\"Msvm_Processor\",DeviceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\23\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_HostedDependency
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"WIN-667A0LKMU6R\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
# };
