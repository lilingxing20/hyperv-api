# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_VirtualEthernetSwitch") #OK 
for obj in objs: 
    print(obj)


# instance of Msvm_VirtualEthernetSwitch
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟交换机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_VirtualEthernetSwitch";
#         Dedicated = {38};
#         Description = "Microsoft 虚拟交换机";
#         DetailedStatus = NULL;
#         ElementName = "br127";
#         EnabledDefault = 2;
#         EnabledState = 5;
#         HealthState = 5;
#         IdentifyingDescriptions = {"虚拟交换机扩展微型端口适配器 ID"};
#         InstallDate = NULL;
#         InstanceID = NULL;
#         MaxIOVOffloads = 0;
#         MaxVMQOffloads = 0;
#         Name = "50FEBE89-6E35-4456-8536-85E8E34A529B";
#         NameFormat = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = {"{CA7AB5E3-8F75-4DC0-9941-45796C2951E9}"};
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         RequestedState = 12;
#         ResetCapability = 5;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastStateChange = NULL;
#         TransitioningToState = NULL;
# };


# instance of Msvm_VirtualEthernetSwitch
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟交换机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_VirtualEthernetSwitch";
#         Dedicated = {38};
#         Description = "Microsoft 虚拟交换机";
#         DetailedStatus = NULL;
#         ElementName = "br-vlan";
#         EnabledDefault = 2;
#         EnabledState = 5;
#         HealthState = 5;
#         IdentifyingDescriptions = {"虚拟交换机扩展微型端口适配器 ID"};
#         InstallDate = NULL;
#         InstanceID = NULL;
#         MaxIOVOffloads = 0;
#         MaxVMQOffloads = 0;
#         Name = "78D861EC-60B6-4365-92E3-F905CCC292F7";
#         NameFormat = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = {"{5BD83BBB-4B72-44B9-BEB5-7AE6AEB6D8B6}"};
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         RequestedState = 12;
#         ResetCapability = 5;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastStateChange = NULL;
#         TransitioningToState = NULL;
# };


# instance of Msvm_VirtualEthernetSwitch
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟交换机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_VirtualEthernetSwitch";
#         Dedicated = {38};
#         Description = "Microsoft 虚拟交换机";
#         DetailedStatus = NULL;
#         ElementName = "Broadcom NetXtreme Gigabit Ethernet - Virtual Switch";
#         EnabledDefault = 2;
#         EnabledState = 5;
#         HealthState = 5;
#         IdentifyingDescriptions = {"虚拟交换机扩展微型端口适配器 ID"};
#         InstallDate = NULL;
#         InstanceID = NULL;
#         MaxIOVOffloads = 0;
#         MaxVMQOffloads = 0;
#         Name = "A643F674-31C2-445B-8F68-5AC8ABFA072E";
#         NameFormat = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = {"{A6E7122B-DE96-4989-B22B-9E99FD624D9B}"};
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         RequestedState = 12;
#         ResetCapability = 5;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastStateChange = NULL;
#         TransitioningToState = NULL;
# };
