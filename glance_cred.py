import keystoneclient.v2_0.client as ksclient
import glanceclient
creds = get_keystone_creds()
keystone = ksclient.Client(**creds)
glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                   endpoint_type='publicURL')
glance = glanceclient.Client('2',glance_endpoint, token=keystone.auth_token)
