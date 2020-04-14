# -*- coding:utf-8 -*-

import pdb
import wmi

conn = wmi.connect_server(server="192.168.0.100", user="administrator",
                          password="Passw0rd", namespace=r"root\virtualization\v2")
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_SystemDevice")  # OK

# (Pdb) print(objs[0])                
# instance of Msvm_SystemDevice
# {
#         GroupComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"WIN-667A0LKMU6R\"";
#         PartComponent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Memory.CreationClassName=\"Msvm_Memory\",DeviceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\Aggregate\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
# };



# for obj in objs:
# print(obj)
# print(obj.groupcomponent.split(":")[0])
# print(obj.groupcomponent.split(":")[1])
# print(obj.groupcomponent.split(":")[1].split(',')[0])
# print(obj.groupcomponent.split(":")[1].split(',')[1])
# print(obj.partcomponent.split(":")[0])
# print(obj.partcomponent.split(":")[1])
# print(obj.partcomponent.split(":")[1].split(",")[0])
# print(obj.partcomponent.split(":")[1].split(",")[1])
# print(obj.partcomponent.split(":")[1].split(",")[2])
# print(obj.partcomponent.split(":")[1].split(",")[3])

# print(set([obj.groupcomponent.split(":")[0] for obj in objs]))
# # {'\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2'}

# print(set([obj.groupcomponent.split(",")[0] for obj in objs]))
# {
#     'Msvm_ComputerSystem.CreationClassName="Msvm_ComputerSystem"',
#     'Msvm_VirtualEthernetSwitch.CreationClassName="Msvm_VirtualEthernetSwitch"',
#     'Msvm_VirtualFcSwitch.CreationClassName="Msvm_VirtualFcSwitch"'
# }

# print(set([obj.groupcomponent.split(":")[1].split(',')[1] for obj in objs]))
# print(set([obj.groupcomponent.split(",")[1] for obj in objs]))
# {
#     'Name="E0198D60-8825-4FF1-A7C2-A8956152B443"',
#     'Name="411F1781-13E9-48FB-B6BA-6AF626438696"',
#     'Name="B549384C-525D-4B89-B218-79B854A42F56"',
#     'Name="78D861EC-60B6-4365-92E3-F905CCC292F7"',
#     'Name="A643F674-31C2-445B-8F68-5AC8ABFA072E"',
#     'Name="WIN-667A0LKMU6R"',
#     'Name="A1576C71-F505-4D1B-9B78-2CFD971B0F31"',
#     'Name="50FEBE89-6E35-4456-8536-85E8E34A529B"'
# }

# print(set([obj.partcomponent.split(":")[0] for obj in objs]))
# # {'\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2'}

# print(set([obj.partcomponent.split(":")[1].split(",")[0] for obj in objs]))
# {
#     'Msvm_VideoHead.CreationClassName="Msvm_VideoHead"',
#     'Msvm_ExternalFcPort.CreationClassName="Msvm_ExternalFcPort"',
#     'Msvm_DiskDrive.CreationClassName="Msvm_DiskDrive"',
#     'Msvm_S3DisplayController.CreationClassName="Msvm_S3DisplayController"',
#     'Msvm_GuestServiceInterfaceComponent.CreationClassName="Msvm_GuestServiceInterfaceComponent"',
#     'Msvm_RdvComponent.CreationClassName="Msvm_RdvComponent"',
#     'Msvm_LogicalDisk.CreationClassName="Msvm_LogicalDisk"',
#     'Msvm_InternalEthernetPort.CreationClassName="Msvm_InternalEthernetPort"',
#     'Msvm_VssComponent.CreationClassName="Msvm_VssComponent"',
#     'Msvm_KvpExchangeComponent.CreationClassName="Msvm_KvpExchangeComponent"',
#     'Msvm_ShutdownComponent.CreationClassName="Msvm_ShutdownComponent"',
#     'Msvm_Keyboard.CreationClassName="Msvm_Keyboard"',
#     'Msvm_EthernetSwitchPort.CreationClassName="Msvm_EthernetSwitchPort"',
#     'Msvm_FcSwitchPort.CreationClassName="Msvm_FcSwitchPort"',
#     'Msvm_SyntheticEthernetPort.CreationClassName="Msvm_SyntheticEthernetPort"',
#     'Msvm_PS2Mouse.CreationClassName="Msvm_PS2Mouse"',
#     'Msvm_ExternalEthernetPort.CreationClassName="Msvm_ExternalEthernetPort"',
#     'Msvm_DVDDrive.CreationClassName="Msvm_DVDDrive"',
#     'Msvm_SyntheticDisplayController.CreationClassName="Msvm_SyntheticDisplayController"',
#     'Msvm_DisketteController.CreationClassName="Msvm_DisketteController"',
#     'Msvm_SCSIProtocolController.CreationClassName="Msvm_SCSIProtocolController"',
#     'Msvm_Memory.CreationClassName="Msvm_Memory"',
#     'Msvm_TimeSyncComponent.CreationClassName="Msvm_TimeSyncComponent"',
#     'Msvm_SerialPort.CreationClassName="Msvm_SerialPort"',
#     'Msvm_Processor.CreationClassName="Msvm_Processor"',
#     'Msvm_IDEController.CreationClassName="Msvm_IDEController"',
#     'Msvm_SyntheticMouse.CreationClassName="Msvm_SyntheticMouse"',
#     'Msvm_HeartbeatComponent.CreationClassName="Msvm_HeartbeatComponent"',
#     'Msvm_DisketteDrive.CreationClassName="Msvm_DisketteDrive"',
#     'Msvm_SerialController.CreationClassName="Msvm_SerialController"'
# }

# print(set([obj.partcomponent.split(",")[1] for obj in objs]))
# {
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\7"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\20"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\4"',
# 	'DeviceID="Microsoft:{89F6CBF3-43BF-462B-A728-E7F2742A54CF}"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\18"',
# 	'DeviceID="Microsoft:730CE612-ECCA-4701-B705-5F45915436BB"',
# 	'DeviceID="Microsoft:{D92B05D7-7C34-4D27-93C7-51BFE6D200A5}"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\13"',
# 	'DeviceID="Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\0"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\8"',
# 	'DeviceID="Microsoft:7D80D3DB-61EE-4879-8879-5609F1100AD0"',
# 	'DeviceID="Microsoft:84EAAE65-2F2E-45F5-9BB5-0E857DC8EB47"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\9"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\6"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\15"',
# 	'DeviceID="Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\19"',
# 	'DeviceID="Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\2"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\23"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\16"',
# 	'DeviceID="Microsoft:{BD5A0381-FBB6-4EDA-900A-4EEBEF76748F}"',
# 	'DeviceID="Microsoft:68A4C814-CD53-4071-A479-C67E8C75B474"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\1"',
# 	'DeviceID="Microsoft:2A34B1C2-FD73-4043-8A5B-DD2159BC743F"',
# 	'DeviceID="Microsoft:A3B6C664-3E69-4229-B688-A75358526ECF"',
# 	'DeviceID="Microsoft:{291B7538-6BAD-4506-B816-470934CDD75F}"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L"',
# 	'DeviceID="Microsoft:5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\15"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\9"',
# 	'DeviceID="Microsoft:9F8233AC-BE49-4C79-8EE3-E7E1985B2077"',
# 	'DeviceID="Microsoft:{758ECB8C-8694-4751-8710-FFF0188D29EE}"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\18"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\4"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\2"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\17"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\22"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\11"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\5"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\22"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0"',
# 	'DeviceID="Microsoft:{4397B43B-CA80-47D9-ACEE-C9061CED70F0}"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\8"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1"',
# 	'DeviceID="Microsoft:8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0"',
# 	'DeviceID="Microsoft:655BC5C5-A784-46B7-81BC-E26328F7EB0E"',
# 	'DeviceID="Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\Aggregate"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\19"',
# 	'DeviceID="Microsoft:B6D42B40-79FE-49B7-A23E-9D90117A1947"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\0"',
# 	'DeviceID="Microsoft:{1E19508F-DFEC-4AAE-A4F3-1838985F472E}"',
# 	'DeviceID="Microsoft:4764334D-E001-4176-82EE-5594EC9B530E\\\\0"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\14"',
# 	'DeviceID="Microsoft:EE33772E-42E3-4E4F-8635-E8AA74323E56"',
# 	'DeviceID="Microsoft:39F5E639-4697-4214-A1E2-6605AE65645F\\\\0"',
# 	'DeviceID="Microsoft:5F07AFDD-5851-415D-BEEF-BB46641A022D"',
# 	'DeviceID="Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\\\\1"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\3"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\10"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\5"',
# 	'DeviceID="Microsoft:6C09BB55-D683-4DA0-8931-C9BF705F6480"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\6"',
# 	'DeviceID="Microsoft:65768F90-E8F6-4A29-8C85-5176A9FE2F2B"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\6"',
# 	'DeviceID="Microsoft:DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\7"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\1"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\21"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\23"',
# 	'DeviceID="Microsoft:F3CF6965-E8D3-44A9-9B7D-A04245EA7525"',
# 	'DeviceID="Microsoft:E4DACE35-149A-4D9E-AF89-E37649B4AAC5"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\4"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\20"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\14"',
# 	'DeviceID="Microsoft:58F75A6D-D949-4320-99E1-A2A2576D581C"',
# 	'DeviceID="Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\\\\1"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\17"',
# 	'DeviceID="Microsoft:F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\12"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\0"',
# 	'DeviceID="Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\1"',
# 	'DeviceID="Microsoft:b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0"',
# 	'DeviceID="Microsoft:{F18E14AA-0193-4857-BAFF-C531E73FC7A6}"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\3"',
# 	'DeviceID="Microsoft:{EB473ADB-0B3E-4748-A9CF-BCC641982C61}"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\16"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\21"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\3"',
# 	'DeviceID="Microsoft:83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\10"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\12"',
# 	'DeviceID="Microsoft:07B22F66-1053-4FD6-A4A2-B11226C4DC01"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\7"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\11"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\2"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\1\\\\8"',
# 	'DeviceID="Microsoft:27592149-0E67-4569-98FB-585586928ED8"',
# 	'DeviceID="Microsoft:5CED1297-4598-4915-A5FC-AD21BB4D02A4"',
# 	'DeviceID="Microsoft:8DF9951B-A383-4094-92EF-88144B98208B"',
# 	'DeviceID="Microsoft:2497F4DE-E9FA-4204-80E4-4B75C46419C0"',
# 	'DeviceID="Microsoft:8E3A359F-559A-4B6A-98A9-1690A6100ED7\\\\0"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\5"',
# 	'DeviceID="Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\\\\0\\\\13"',
# 	'DeviceID="Microsoft:C157E0B2-904B-4F94-A86D-E1443A1C47AD"',
# 	'DeviceID="Microsoft:{683922E8-DE84-4348-AAC4-597112DD14BC}"',
# 	'DeviceID="Microsoft:6C5ADDB9-A11A-4E8E-84CB-E6208201DB63"'
# }


# print(set([obj.partcomponent.split(",")[2] for obj in objs])) 
# {
# 	'SystemCreationClassName="Msvm_VirtualFcSwitch"',
# 	'SystemCreationClassName="Msvm_ComputerSystem"',
# 	'SystemCreationClassName="Msvm_VirtualEthernetSwitch"'
# }

# print(set([obj.partcomponent.split(",")[3] for obj in objs]))
# {
# 	'SystemName="A643F674-31C2-445B-8F68-5AC8ABFA072E"',
# 	'SystemName="78D861EC-60B6-4365-92E3-F905CCC292F7"',
# 	'SystemName="A1576C71-F505-4D1B-9B78-2CFD971B0F31"',
# 	'SystemName="50FEBE89-6E35-4456-8536-85E8E34A529B"',
# 	'SystemName="E0198D60-8825-4FF1-A7C2-A8956152B443"',
# 	'SystemName="B549384C-525D-4B89-B218-79B854A42F56"',
# 	'SystemName="WIN-667A0LKMU6R"',
# 	'SystemName="411F1781-13E9-48FB-B6BA-6AF626438696"'
# }

