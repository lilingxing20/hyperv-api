# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

vms_obj = client.query("Select * from Msvm_ComputerSystem")
for vm in vms_obj: 
    print(vm)

## CreationClassName: Msvm_ComputerSystem
## Caption: '宿主计算机系统', '虚拟机'
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