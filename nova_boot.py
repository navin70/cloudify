#!/usr/bin/python
import sys
import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
creds = get_nova_creds()
nova = nvclient.Client(**creds)
if not nova.keypairs.findall(name="cloudify"):
    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
        nova.keypairs.create(name="mykey", public_key=fpubkey.read())
image = nova.images.find(name="cirros")
flavor = nova.flavors.find(name="m1.tiny")
print image
instance = nova.servers.create(name=str(sys.argv[1]), image=image, flavor=flavor, key_name="cloudify",userdata=/tmp/app)

# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    print "status: %s" % status
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print "status: %s" % status
