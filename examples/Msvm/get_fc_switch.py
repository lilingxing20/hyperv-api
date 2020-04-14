# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_VirtualFcSwitch") #OK 
for obj in objs: 
    print(obj)


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