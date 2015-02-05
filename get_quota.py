#!/usr/bin/python
import sys
import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
creds = get_nova_creds()
nova = nvclient.Client(**creds)
quota = nova.quotas.get("tenant")
print ("Max Cores =",quota.cores)
print ("Max RAM=",quota.ram)
print ("Max Fixed Ips = ",quota.fixed_ips)
print ("Max Floating Ips =",quota.floating_ips)
print ("Max security_groups =",quota.security_groups)
print ("Max security_group_rules =",quota.security_group_rules)
print ("Max security_groups_members =",quota.server_group_members)
print ("Max server_groups =",quota.server_groups)
print ("Max injected_file_content_bytes =",quota.injected_file_content_bytes)
print ("Max injected_file_path_bytes = ",quota.injected_file_path_bytes)
print ("Max injected_files =",quota.injected_files)
print ("Max Instances = ",quota.instances)
print ("Max key_pairs=",quota.key_pairs)
print ("Max Metadata Items=",quota.metadata_items)

