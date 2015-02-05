import	mysql.connector
from credentials import get_mysql_creds
import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
from gen_rand_no import rand_with_N_digits
from credentials import get_keystone_creds
creds = get_keystone_creds()
dbcreds = get_mysql_creds()
cnx = mysql.connector.connect(**dbcreds)
keystone = ksclient.Client(**creds)
cursor = cnx.cursor()

glance_endpoint = keystone.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
images = glance.images.list()
images = list(images)


add_image_data = ("INSERT  INTO image_data "
		"(image_id, image_name, cloud_image_id, parent_cloud, image_status, image_state)"
		"VALUES (%(image_id)s, %(image_name)s, %(cloud_image_id)s, %(parent_cloud)s, %(status)s, 'available')")



#def delete_dup(string):
#	 query = "DELETE FROM image_data WHERE parent_cloud=%s"
#	 cursor.execute(query, (string,))

#cloud = str("Openstack")
#delete_dup(cloud)



j = 0
for i in images:
	image_dict = images[j]
	image_data = {
	'cloud_image_id': image_dict['id'],
	'image_id' 	: rand_with_N_digits(10),
	'image_name' 	: image_dict['name'],
	'parent_cloud'	:  str('Openstack'),
	'status'	: image_dict['status'],
	}

	cursor.execute(add_image_data,image_data)
	j = j+1

	print image_data


# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()	
	

