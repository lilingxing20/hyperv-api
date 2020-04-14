# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("SELECT * FROM Msvm_ExternalEthernetPort") #ok
for o in objs: 
    print(o)

# (Pdb) set([o.CreationClassName for o in objs])
# {'Msvm_ExternalEthernetPort'}
# (Pdb) print(objs[0])                           

# instance of Msvm_ExternalEthernetPort
# {
#         ActiveMaximumTransmissionUnit = "1500";
#         AdditionalAvailability = NULL;
#         AutoSense = TRUE;
#         Availability = NULL;
#         AvailableRequestedStates = NULL;
#         Capabilities = NULL;
#         CapabilityDescriptions = NULL;
#         Caption = "以太网端口";
#         CommunicationStatus = NULL;
#         CreationClassName = "Msvm_ExternalEthernetPort";
#         Description = "Microsoft 外部以太网端口";
#         DetailedStatus = NULL;
#         DeviceID = "Microsoft:{4397B43B-CA80-47D9-ACEE-C9061CED70F0}";
#         ElementName = "Broadcom NetXtreme Gigabit Ethernet #8";
#         EnabledCapabilities = NULL;
#         EnabledDefault = 2;
#         EnabledState = 2;
#         ErrorCleared = NULL;
#         ErrorDescription = NULL;
#         FullDuplex = TRUE;
#         HealthState = 5;
#         IdentifyingDescriptions = NULL;
#         InstallDate = NULL;
#         InstanceID = NULL;
#         IsBound = FALSE;
#         LastErrorCode = NULL;
#         LinkTechnology = 2;
#         MaxDataSize = 1500;
#         MaxQuiesceTime = NULL;
#         MaxSpeed = "1000000000";
#         Name = "Broadcom NetXtreme Gigabit Ethernet #8";
#         NetworkAddresses = NULL;
#         OperatingStatus = NULL;
#         OperationalStatus = {2};
#         OtherEnabledCapabilities = NULL;
#         OtherEnabledState = NULL;
#         OtherIdentifyingInfo = NULL;
#         OtherLinkTechnology = NULL;
#         OtherNetworkPortType = NULL;
#         OtherPortType = NULL;
#         PermanentAddress = "000AF79B1EB7";
#         PortNumber = 0;
#         PortType = 53;
#         PowerManagementCapabilities = NULL;
#         PowerManagementSupported = NULL;
#         PowerOnHours = NULL;
#         PrimaryStatus = NULL;
#         RequestedSpeed = "1000000000";
#         RequestedState = 12;
#         Speed = "1000000000";
#         Status = "OK";
#         StatusDescriptions = {"确定"};
#         StatusInfo = NULL;
#         SupportedMaximumTransmissionUnit = "1500";
#         SystemCreationClassName = "Msvm_ComputerSystem";
#         SystemName = "WIN-667A0LKMU6R";
#         TimeOfLastStateChange = NULL;
#         TotalPowerOnHours = NULL;
#         TransitioningToState = NULL;
#         UsageRestriction = 4;
# };