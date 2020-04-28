#!/bin/python
# -*- coding:utf-8 -*-

import wmi

conn = wmi.WMI(moniker='//./Root/Microsoft/Windows/Storage')

volumes = conn.MSFT_Volume()
for idx, volume in enumerate(volumes, 1):
    partitions = volume.associators(wmi_result_class='MSFT_Partition')
    for partition in partitions:
        (ret_val, _, size_max, _) = partition.GetSupportedSize()
        # print(partition)
        # print(ret_val, size_max)

        partition_size = partition.Size
        partition_num = partition.PartitionNumber
        print('The partition "%s" current size %s .' %
              (partition_num, partition_size))
        if size_max > partition_size:
            print('Extending partition "%(partition_number)s" '
                  'to %(size)s bytes' %
                  {'partition_number': partition.PartitionNumber,
                   'size': size_max})
        # 调整大小
        (ret_val, _) = partition.Resize(size_max)
        if ret_val:
            print("Resize failed with error: %s" % ret_val)
