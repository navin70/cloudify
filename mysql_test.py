import	mysql.connector
from credentials import get_mysql_creds
creds = get_mysql_creds()
cnx = mysql.connector.connect(**creds)
cursor = cnx.cursor()
print cnx

add_data = ("INSERT INTO image_data "
		"(image_id, image_name, cloud_image_id, parent_cloud)"
		"VALUES (%s, %s, %s, %s)")
data_test = ('123123213123','bingo','123123213','Openstack')

cursor.execute (add_data, data_test)
cnx.commit()
cursor.close()
cnx.close()
