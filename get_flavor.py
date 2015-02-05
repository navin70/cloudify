#!/usr/bin/python
import sys
import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
creds = get_nova_creds()
nova = nvclient.Client(**creds)
profile  = nova.flavors.list
print profile["Flavor"]

