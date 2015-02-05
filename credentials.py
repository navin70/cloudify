#!/usr/bin/env python
import os

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d
def get_mysql_creds():
    d = {}
    d['user'] = 'cloudify'
    d['password'] = 'Y@mahafz16'
    d['host'] = 'localhost'
    d['database'] = 'cloud'
    return d
def get_glance_creds():

    keystone = get_keysone_creds()
    glance_endpoint = keystone.service_catalog.url_for(service_type='image')
    glance_creds = str(token="keystone.auth_token")
    d = ["glance_endpoint","glance_creds"]
    return d
