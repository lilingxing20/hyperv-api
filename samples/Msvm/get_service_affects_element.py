# -*- coding:utf-8 -*-

import wmi 

conn = wmi.connect_server(server="192.168.0.100", user="administrator", password="Passw0rd", namespace=r"root\virtualization\v2") 
client = wmi.WMI(wmi=conn)

objs = client.query("Select * from  Msvm_ServiceAffectsElement") #OK 
for obj in objs: 
    print(obj)



# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_Synth3dVideoPool.InstanceID=\"Microsoft:06FF76FA-2D58-4BAF-9F8D-455773824F37\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:118C3BE5-0D31-4804-85F0-5C6074ABEA8F\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:146C56A0-3546-469B-9737-FCBCF82428F4\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:698F2285-28DC-4438-A147-82D7432C5254\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:19839BFF-6F04-4B24-B4B5-1AFCCBE729DE\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:353B3BE8-310C-4cf4-839E-4E1B14616136\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4764334E-E001-4176-82EE-5594EC9B530E\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:4EA4F71F-16E6-4250-99A8-A2315332CC64\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:6A45335D-4C3A-44B7-B61F-C9808BBDF8ED\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:70BB60D2-A9D3-46AA-B654-3DE53004B4F8\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:72027ECE-E44A-446E-AF2B-8D8C4B8A2279\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:78AA0C27-B2BD-45BA-83D1-5F2A8C4C6656\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:7951A5ED-8DC5-42d7-AA8C-9F14C54CEB84\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ProcessorPool.InstanceID=\"Microsoft:B637F347-6A0E-4DEC-AF52-BD70CB80A21D\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:bde5d4d6-e450-46d2-b925-976ca3e989b4\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D45268DA-37C5-44da-B827-B0C55CCB3BDC\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:D92D268E-9AA8-49DD-8C7D-821CEFB5F597\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:DACDCF3F-6F67-4EB8-A4D0-5D93B48A2468\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePool.InstanceID=\"Microsoft:F6293891-F32F-4930-B2DB-1A8961D9CB75\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ResourcePoolConfigurationService.CreationClassName=\"Msvm_ResourcePoolConfigurationService\",Name=\"poolcfgsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:04BDF59E-580D-4441-8828-FFFE44472D2D\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:04BDF59E-580D-4441-8828-FFFE44472D2E\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:394DCE66-458F-4895-AE56-41D7C9602A49\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:394DCE66-458F-4895-AE56-41D7C9602A4A\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:3C215D49-078B-4D9F-8E2E-0C844642D3BB\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:3C215D49-078B-4D9F-8E2E-0C844642D3BC\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:3F6F1051-C8FC-47EF-9821-C07240848748\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:3F6F1051-C8FC-47EF-9821-C07240848749\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:534FA8D7-9875-4FAB-BAA6-2424DF29B31E\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:72544D55-3035-41DA-B9D7-6C5A39BF8F35\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:7A9EB0A9-28CF-4216-A6CA-F8DE74A5D4A3\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:8F5001D9-CAB4-4F85-AC1E-887FBBB07641\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:942103D7-A125-4F19-B734-97AEDBF81995\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:A4BCA0D9-C27D-4BC8-A7E3-7ED13C89E373\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:A6C250B0-867B-4CE7-9C47-A4F00AA6BB15\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:A6C250B0-867B-4CE7-9C47-A4F00AA6BB16\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:A9DFBC22-E05F-438D-9405-22E2078353D6\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:AD29978B-AAB6-44AE-81CD-0609BF929F18\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:AD29978B-AAB6-44AE-81CD-0609BF929F19\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:FF85EA46-9933-4436-BE5D-C96827399966\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_AggregationMetricDefinition.Id=\"Microsoft:FF85EA46-9933-4436-BE5D-C96827399967\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_BaseMetricDefinition.Id=\"Microsoft:FFD2C1DC-091E-4F2A-95F7-75994CE92046\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_MetricService.CreationClassName=\"Msvm_MetricService\",Name=\"metricsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationService.CreationClassName=\"Msvm_VirtualSystemMigrationService\",Name=\"migrationwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationService.CreationClassName=\"Msvm_ReplicationService\",Name=\"replicasvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementService.CreationClassName=\"Msvm_VirtualSystemManagementService\",Name=\"vmms\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"4EA7033C-356C-4EBA-9F77-1A3399CFCD72\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSnapshotService.CreationClassName=\"Msvm_VirtualSystemSnapshotService\",Name=\"vssnapsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationService.CreationClassName=\"Msvm_VirtualSystemMigrationService\",Name=\"migrationwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationService.CreationClassName=\"Msvm_ReplicationService\",Name=\"replicasvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementService.CreationClassName=\"Msvm_VirtualSystemManagementService\",Name=\"vmms\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"A1576C71-F505-4D1B-9B78-2CFD971B0F31\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSnapshotService.CreationClassName=\"Msvm_VirtualSystemSnapshotService\",Name=\"vssnapsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemMigrationService.CreationClassName=\"Msvm_VirtualSystemMigrationService\",Name=\"migrationwmi\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ReplicationService.CreationClassName=\"Msvm_ReplicationService\",Name=\"replicasvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemManagementService.CreationClassName=\"Msvm_VirtualSystemManagementService\",Name=\"vmms\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_ComputerSystem.CreationClassName=\"Msvm_ComputerSystem\",Name=\"B549384C-525D-4B89-B218-79B854A42F56\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSnapshotService.CreationClassName=\"Msvm_VirtualSystemSnapshotService\",Name=\"vssnapsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:5C39A06A-464C-4BC1-9A6C-A13833CE5267\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSnapshotService.CreationClassName=\"Msvm_VirtualSystemSnapshotService\",Name=\"vssnapsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };


# instance of Msvm_ServiceAffectsElement
# {
#         AffectedElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSettingData.InstanceID=\"Microsoft:A3E95F27-94D5-4243-8700-6F92145BD27C\"";
#         AffectingElement = "\\\\WIN-667A0LKMU6R\\root\\virtualization\\v2:Msvm_VirtualSystemSnapshotService.CreationClassName=\"Msvm_VirtualSystemSnapshotService\",Name=\"vssnapsvc\",SystemCreationClassName=\"Msvm_ComputerSystem\",SystemName=\"WIN-667A0LKMU6R\"";
#         ElementEffects = {5};
#         OtherElementEffectsDescriptions = {};
# };