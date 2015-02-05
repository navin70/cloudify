#!/usr/bin/python
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
creds = get_nova_creds()
nova = nvclient.Client(**creds)
list = nova.servers.list()
print list
