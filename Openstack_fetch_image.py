from credentials import get_keystone_creds
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient
creds = get_keystone_creds()
keystone = ksclient.Client(**creds)
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
image = glance.images.list()
print list(image)
