# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("SELECT * FROM CIM_ActiveConnection")
for obj in objs: 
    print(obj)


# instance of Msvm_FcActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcEndpoint.CreationClassName=\"Msvm_FcEndpoint\",Name=\"Microsoft:C157E0B2-904B-4F94-A86D-E1443A1C47AD\",SystemCreationClassName=\"Msvm_VirtualFcSwitch\",SystemName=\"E0198D60-8825-4FF1-A7C2-A8956152B443\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcEndpoint.CreationClassName=\"Msvm_FcEndpoint\",Name=\"Microsoft:07B22F66-1053-4FD6-A4A2-B11226C4DC01\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_FcActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcEndpoint.CreationClassName=\"Msvm_FcEndpoint\",Name=\"Microsoft:730CE612-ECCA-4701-B705-5F45915436BB\",SystemCreationClassName=\"Msvm_VirtualFcSwitch\",SystemName=\"411F1781-13E9-48FB-B6BA-6AF626438696\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcEndpoint.CreationClassName=\"Msvm_FcEndpoint\",Name=\"Microsoft:68A4C814-CD53-4071-A479-C67E8C75B474\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:8DF9951B-A383-4094-92EF-88144B98208B\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:{1E19508F-DFEC-4AAE-A4F3-1838985F472E}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:E4DACE35-149A-4D9E-AF89-E37649B4AAC5\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:{89F6CBF3-43BF-462B-A728-E7F2742A54CF}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:65768F90-E8F6-4A29-8C85-5176A9FE2F2B\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"78D861EC-60B6-4365-92E3-F905CCC292F7\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:{D92B05D7-7C34-4D27-93C7-51BFE6D200A5}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:B6D42B40-79FE-49B7-A23E-9D90117A1947\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:{F18E14AA-0193-4857-BAFF-C531E73FC7A6}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:EE33772E-42E3-4E4F-8635-E8AA74323E56\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:{291B7538-6BAD-4506-B816-470934CDD75F}\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:5F07AFDD-5851-415D-BEEF-BB46641A022D\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:f28e3c2a-7a2d-44f5-8d15-6fbc98d3466c\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"b549384c-525d-4b89-b218-79b854a42f56\"";
#         IsUnidirectional = FALSE;
# };


# instance of Msvm_ActiveConnection
# {
#         Antecedent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:27592149-0E67-4569-98FB-585586928ED8\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         Dependent = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_LANEndpoint.CreationClassName=\"Msvm_LANEndpoint\",Name=\"Microsoft:a3b6c664-3e69-4229-b688-a75358526ecf\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"a1576c71-f505-4d1b-9b78-2cfd971b0f31\"";
#         IsUnidirectional = FALSE;
# };