# -*- coding: utf-8 -*-
import urllib3
import urllib
import time
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "CD6RZlJuI8PostJBrrnkvGngb-gnSJbs"
secret = "lHp0GrPsZvxMHdgYUtEiAExZ_JFPKia4"
filepath = r"image\myself.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)
print("data: ", data)

http_body = ''
for item in data:
	# print(type(item).__name__)
	if type(item).__name__ == \
			'str':
		http_body=http_body + '\r\n' + item
	else:
		http_body=http_body + '\r\n' + item.decode("utf-8")

# http_body='\r\n'.join(data)
#buld http request
req=urllib3.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#post data to server
	resp = urllib3.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print(qrcont)

except urllib3.HTTPError as e:
    print(e.read())