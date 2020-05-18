# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from CIM_ComputerSystem")
for o in objs: 
    print(o)


# (Pdb) set([o.CreationClassName for o in objs])
# {'Msvm_VirtualEthernetSwitch', 'Msvm_VirtualFcSwitch', 'Msvm_ComputerSystem'}


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


# instance of Msvm_VirtualFcSwitch
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟 FibreChannel 交换机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_VirtualFcSwitch";
#         Dedicated = {38};
#         Description = "Microsoft 虚拟 FibreChannel 交换机";
#         DetailedStatus = NULL;
#         ElementName = "Microsoft Virtual FibreChannel Switch";
#         EnabledDefault = 2;
#         EnabledState = 5;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = NULL;
#         InstanceID = NULL;
#         Name = "E0198D60-8825-4FF1-A7C2-A8956152B443";
#         NameFormat = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         RequestedState = 12;
#         ResetCapability = 5;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastStateChange = "20200403061332.000000-000";
#         TransitioningToState = NULL;
# };


# instance of Msvm_ComputerSystem
# {
#         AvailableRequestedStates = NULL;
#         Caption = "宿主计算机系统";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_ComputerSystem";
#         Dedicated = NULL;
#         Description = "Microsoft 宿主计算机系统";
#         DetailedStatus = NULL;
#         ElementName = "WIN-667A0LKMU6R";
#         EnabledDefault = 2;
#         EnabledState = 2;
#         EnhancedSessionModeState = NULL;
#         FailedOverReplicationType = NULL;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = NULL;
#         InstanceID = NULL;
#         LastApplicationConsistentReplicationTime = NULL;
#         LastReplicationTime = NULL;
#         LastReplicationType = NULL;
#         LastSuccessfulBackupTime = NULL;
#         Name = "WIN-667A0LKMU6R";
#         NameFormat = NULL;
#         NumberOfNumaNodes = 2;
#         OnTimeInMilliseconds = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         ProcessID = NULL;
#         ReplicationHealth = NULL;
#         ReplicationMode = NULL;
#         ReplicationState = NULL;
#         RequestedState = 12;
#         ResetCapability = 1;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastConfigurationChange = NULL;
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


# instance of Msvm_VirtualFcSwitch
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟 FibreChannel 交换机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_VirtualFcSwitch";
#         Dedicated = {38};
#         Description = "Microsoft 虚拟 FibreChannel 交换机";
#         DetailedStatus = NULL;
#         ElementName = "Microsoft Virtual FibreChannel Switch";
#         EnabledDefault = 2;
#         EnabledState = 5;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = NULL;
#         InstanceID = NULL;
#         Name = "411F1781-13E9-48FB-B6BA-6AF626438696";
#         NameFormat = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         RequestedState = 12;
#         ResetCapability = 5;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         TimeOfLastStateChange = "20200403061332.000000-000";
#         TransitioningToState = NULL;
# };


# instance of Msvm_ComputerSystem
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_ComputerSystem";
#         Dedicated = NULL;
#         Description = "Microsoft 虚拟机";
#         DetailedStatus = NULL;
#         ElementName = "centos7";
#         EnabledDefault = 3;
#         EnabledState = 3;
#         EnhancedSessionModeState = 3;
#         FailedOverReplicationType = 0;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = "16010101000000.000000-000";
#         InstanceID = NULL;
#         LastApplicationConsistentReplicationTime = "16010101000000.000000-000";
#         LastReplicationTime = "16010101000000.000000-000";
#         LastReplicationType = 0;
#         LastSuccessfulBackupTime = NULL;
#         Name = "4EA7033C-356C-4EBA-9F77-1A3399CFCD72";
#         NameFormat = NULL;
#         NumberOfNumaNodes = 1;
#         OnTimeInMilliseconds = "0";
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         ProcessID = NULL;
#         ReplicationHealth = 0;
#         ReplicationMode = 0;
#         ReplicationState = 0;
#         RequestedState = 12;
#         ResetCapability = 1;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"正常运行"};
#         TimeOfLastConfigurationChange = "20200330022238.631038-000";
#         TimeOfLastStateChange = "20200403061332.261705-000";
#         TransitioningToState = NULL;
# };


# instance of Msvm_ComputerSystem
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_ComputerSystem";
#         Dedicated = NULL;
#         Description = "Microsoft 虚拟机";
#         DetailedStatus = NULL;
#         ElementName = "instance-000019c7";
#         EnabledDefault = 6;
#         EnabledState = 9;
#         EnhancedSessionModeState = 3;
#         FailedOverReplicationType = 0;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = "16010101000000.000000-000";
#         InstanceID = NULL;
#         LastApplicationConsistentReplicationTime = "16010101000000.000000-000";
#         LastReplicationTime = "16010101000000.000000-000";
#         LastReplicationType = 0;
#         LastSuccessfulBackupTime = NULL;
#         Name = "A1576C71-F505-4D1B-9B78-2CFD971B0F31";
#         NameFormat = NULL;
#         NumberOfNumaNodes = 1;
#         OnTimeInMilliseconds = "72835398";
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         ProcessID = 5748;
#         ReplicationHealth = 0;
#         ReplicationMode = 0;
#         ReplicationState = 0;
#         RequestedState = 12;
#         ResetCapability = 1;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"正常运行"};
#         TimeOfLastConfigurationChange = "20200404022732.584553-000";
#         TimeOfLastStateChange = "20200404022732.584553-000";
#         TransitioningToState = NULL;
# };


# instance of Msvm_ComputerSystem
# {
#         AvailableRequestedStates = NULL;
#         Caption = "虚拟机";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_ComputerSystem";
#         Dedicated = NULL;
#         Description = "Microsoft 虚拟机";
#         DetailedStatus = NULL;
#         ElementName = "testdiff";
#         EnabledDefault = 2;
#         EnabledState = 2;
#         EnhancedSessionModeState = 3;
#         FailedOverReplicationType = 0;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = "20200330023308.105545-000";
#         InstanceID = NULL;
#         LastApplicationConsistentReplicationTime = "16010101000000.000000-000";
#         LastReplicationTime = "16010101000000.000000-000";
#         LastReplicationType = 0;
#         LastSuccessfulBackupTime = NULL;
#         Name = "B549384C-525D-4B89-B218-79B854A42F56";
#         NameFormat = NULL;
#         NumberOfNumaNodes = 1;
#         OnTimeInMilliseconds = "74849569";
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherDedicatedDescriptions = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         PowerManagementCapabilities = NULL;
#         PrimaryOwnerContact = NULL;
#         PrimaryOwnerName = NULL;
#         PrimaryStatus = NULL;
#         ProcessID = 4920;
#         ReplicationHealth = 0;
#         ReplicationMode = 0;
#         ReplicationState = 0;
#         RequestedState = 12;
#         ResetCapability = 1;
#         Roles = NULL;
#         Status = "OK";
#         StatusDescriptions = {"正常运行"};
#         TimeOfLastConfigurationChange = "20200413144805.569671-000";
#         TimeOfLastStateChange = "20200413144805.569671-000";
#         TransitioningToState = NULL;
# };