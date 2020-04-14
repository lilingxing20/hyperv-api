# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_ElementSettingData") #OK 
for obj in objs: 
    print(obj)

# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementService.CreationClassName=\"Msvm_VirtualSystemManagementService\",Name=\"vmms\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementServiceSettingData.InstanceID=\"Microsoft:WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationService.CreationClassName=\"Msvm_VirtualSystemMigrationService\",Name=\"migrationwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationServiceSettingData.InstanceID=\"Microsoft:WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationService.CreationClassName=\"Msvm_ReplicationService\",Name=\"replicasvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationServiceSettingData.InstanceID=\"Microsoft:WIN-667A0LKMU6R\\\\HVR\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricServiceSettingData.InstanceID=\"Microsoft:WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TerminalService.CreationClassName=\"Msvm_TerminalService\",Name=\"termsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TerminalServiceSettingData.InstanceID=\"Microsoft:WIN-667A0LKMU6R\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 2;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\\\\HVR\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskMergeSettingData.InstanceID=\"Microsoft:4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 2;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\HVR\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskMergeSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = NULL;
#         IsDefault = NULL;
#         IsNext = NULL;
#         ManagedElement = NULL;
#         SettingData = NULL;
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = NULL;
#         IsDefault = NULL;
#         IsNext = NULL;
#         ManagedElement = NULL;
#         SettingData = NULL;
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_GuestServiceInterfaceComponent.CreationClassName=\"Msvm_GuestServiceInterfaceComponent\",DeviceID=\"Microsoft:6C09BB55-D683-4DA0-8931-C9BF705F6480\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_GuestServiceInterfaceComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\6C09BB55-D683-4DA0-8931-C9BF705F6480\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_HeartbeatComponent.CreationClassName=\"Msvm_HeartbeatComponent\",DeviceID=\"Microsoft:84EAAE65-2F2E-45F5-9BB5-0E857DC8EB47\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_HeartbeatComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\84EAAE65-2F2E-45F5-9BB5-0E857DC8EB47\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_KvpExchangeComponent.CreationClassName=\"Msvm_KvpExchangeComponent\",DeviceID=\"Microsoft:2A34B1C2-FD73-4043-8A5B-DD2159BC743F\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_KvpExchangeComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\2A34B1C2-FD73-4043-8A5B-DD2159BC743F\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ShutdownComponent.CreationClassName=\"Msvm_ShutdownComponent\",DeviceID=\"Microsoft:9F8233AC-BE49-4C79-8EE3-E7E1985B2077\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ShutdownComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\9F8233AC-BE49-4C79-8EE3-E7E1985B2077\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TimeSyncComponent.CreationClassName=\"Msvm_TimeSyncComponent\",DeviceID=\"Microsoft:2497F4DE-E9FA-4204-80E4-4B75C46419C0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TimeSyncComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\2497F4DE-E9FA-4204-80E4-4B75C46419C0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VssComponent.CreationClassName=\"Msvm_VssComponent\",DeviceID=\"Microsoft:5CED1297-4598-4915-A5FC-AD21BB4D02A4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VssComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\5CED1297-4598-4915-A5FC-AD21BB4D02A4\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_RdvComponent.CreationClassName=\"Msvm_RdvComponent\",DeviceID=\"Microsoft:6C5ADDB9-A11A-4E8E-84CB-E6208201DB63\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_RdvComponentSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\6C5ADDB9-A11A-4E8E-84CB-E6208201DB63\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\5CA08FA7-17F5-4F1E-A719-5104ECE99A5B\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\A3B6C664-3E69-4229-B688-A75358526ECF\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\A3B6C664-3E69-4229-B688-A75358526ECF\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\A3B6C664-3E69-4229-B688-A75358526ECF\\\\C\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\A3B6C664-3E69-4229-B688-A75358526ECF\\\\C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";  
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 2;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\HVR\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_DiskMergeSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\DE6CDC86-E1FB-4940-801B-C3C1A26C4DA4\\\\Keyboard\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\655BC5C5-A784-46B7-81BC-E26328F7EB0E\\\\Mouse\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\8F0D2762-0B00-4E04-AF4F-19010527CB93\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = NULL;
#         IsDefault = NULL;
#         IsNext = NULL;
#         ManagedElement = NULL;
#         SettingData = NULL;
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = NULL;
#         IsDefault = NULL;
#         IsNext = NULL;
#         ManagedElement = NULL;
#         SettingData = NULL;
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\0\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\D\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_StorageAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\83F8638B-8DCA-4152-9EDA-2CA8B33039B4\\\\1\\\\0\\\\L\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\58F75A6D-D949-4320-99E1-A2A2576D581C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F3CF6965-E8D3-44A9-9B7D-A04245EA7525\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_GuestServiceInterfaceComponent.CreationClassName=\"Msvm_GuestServiceInterfaceComponent\",DeviceID=\"Microsoft:6C09BB55-D683-4DA0-8931-C9BF705F6480\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_GuestServiceInterfaceComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\6C09BB55-D683-4DA0-8931-C9BF705F6480\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_HeartbeatComponent.CreationClassName=\"Msvm_HeartbeatComponent\",DeviceID=\"Microsoft:84EAAE65-2F2E-45F5-9BB5-0E857DC8EB47\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_HeartbeatComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\84EAAE65-2F2E-45F5-9BB5-0E857DC8EB47\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_KvpExchangeComponent.CreationClassName=\"Msvm_KvpExchangeComponent\",DeviceID=\"Microsoft:2A34B1C2-FD73-4043-8A5B-DD2159BC743F\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_KvpExchangeComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\2A34B1C2-FD73-4043-8A5B-DD2159BC743F\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ShutdownComponent.CreationClassName=\"Msvm_ShutdownComponent\",DeviceID=\"Microsoft:9F8233AC-BE49-4C79-8EE3-E7E1985B2077\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ShutdownComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\9F8233AC-BE49-4C79-8EE3-E7E1985B2077\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TimeSyncComponent.CreationClassName=\"Msvm_TimeSyncComponent\",DeviceID=\"Microsoft:2497F4DE-E9FA-4204-80E4-4B75C46419C0\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_TimeSyncComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\2497F4DE-E9FA-4204-80E4-4B75C46419C0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VssComponent.CreationClassName=\"Msvm_VssComponent\",DeviceID=\"Microsoft:5CED1297-4598-4915-A5FC-AD21BB4D02A4\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VssComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\5CED1297-4598-4915-A5FC-AD21BB4D02A4\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_RdvComponent.CreationClassName=\"Msvm_RdvComponent\",DeviceID=\"Microsoft:6C5ADDB9-A11A-4E8E-84CB-E6208201DB63\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_RdvComponentSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\6C5ADDB9-A11A-4E8E-84CB-E6208201DB63\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_SyntheticEthernetPortSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\\\\C\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\F28E3C2A-7A2D-44F5-8D15-6FBC98D3466C\\\\C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\39F5E639-4697-4214-A1E2-6605AE65645F\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourceAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\39F5E639-4697-4214-A1E2-6605AE65645F\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MemorySettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\4764334d-e001-4176-82ee-5594ec9b530e\"";  
# };


# instance of Msvm_ElementSettingData
# {
#         IsCurrent = 1;
#         IsDefault = 1;
#         IsNext = 0;
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\b637f346-6a0e-4dec-af52-bd70cb80a21d\\\\0\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:8DF9951B-A383-4094-92EF-88144B98208B\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:50FEBE89-6E35-4456-8536-85E8E34A529B\\\\8DF9951B-A383-4094-92EF-88144B98208B\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:B6D42B40-79FE-49B7-A23E-9D90117A1947\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:50FEBE89-6E35-4456-8536-85E8E34A529B\\\\B6D42B40-79FE-49B7-A23E-9D90117A1947\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:65768F90-E8F6-4A29-8C85-5176A9FE2F2B\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"78D861EC-60B6-4365-92E3-F905CCC292F7\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:78D861EC-60B6-4365-92E3-F905CCC292F7\\\\65768F90-E8F6-4A29-8C85-5176A9FE2F2B\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:E4DACE35-149A-4D9E-AF89-E37649B4AAC5\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:A643F674-31C2-445B-8F68-5AC8ABFA072E\\\\E4DACE35-149A-4D9E-AF89-E37649B4AAC5\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:EE33772E-42E3-4E4F-8635-E8AA74323E56\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"A643F674-31C2-445B-8F68-5AC8ABFA072E\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:A643F674-31C2-445B-8F68-5AC8ABFA072E\\\\EE33772E-42E3-4E4F-8635-E8AA74323E56\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:5F07AFDD-5851-415D-BEEF-BB46641A022D\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:B549384C-525D-4B89-B218-79B854A42F56\\\\f28e3c2a-7a2d-44f5-8d15-6fbc98d3466c\\\\C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetSwitchPort.CreationClassName=\"Msvm_EthernetSwitchPort\",DeviceID=\"Microsoft:27592149-0E67-4569-98FB-585586928ED8\",SystemCreationClassName=\"Msvm_VirtualEthernetSwitch\",SystemName=\"50FEBE89-6E35-4456-8536-85E8E34A529B\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_EthernetPortAllocationSettingData.InstanceID=\"Microsoft:A1576C71-F505-4D1B-9B78-2CFD971B0F31\\\\a3b6c664-3e69-4229-b688-a75358526ecf\\\\C\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcSwitchPort.CreationClassName=\"Msvm_FcSwitchPort\",DeviceID=\"Microsoft:C157E0B2-904B-4F94-A86D-E1443A1C47AD\",SystemCreationClassName=\"Msvm_VirtualFcSwitch\",SystemName=\"E0198D60-8825-4FF1-A7C2-A8956152B443\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcPortAllocationSettingData.InstanceID=\"Microsoft:E0198D60-8825-4FF1-A7C2-A8956152B443\\\\C157E0B2-904B-4F94-A86D-E1443A1C47AD\"";
# };


# instance of Msvm_ElementSettingData
# {
#         ManagedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcSwitchPort.CreationClassName=\"Msvm_FcSwitchPort\",DeviceID=\"Microsoft:730CE612-ECCA-4701-B705-5F45915436BB\",SystemCreationClassName=\"Msvm_VirtualFcSwitch\",SystemName=\"411F1781-13E9-48FB-B6BA-6AF626438696\"";
#         SettingData = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_FcPortAllocationSettingData.InstanceID=\"Microsoft:411F1781-13E9-48FB-B6BA-6AF626438696\\\\730CE612-ECCA-4701-B705-5F45915436BB\"";
# };