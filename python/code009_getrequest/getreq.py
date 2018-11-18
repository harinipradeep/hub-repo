import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
r=requests.get('https://github.com/harinipradeep/hub-repo',
auth=('harinipradeep27@gmail.com','hpghub@27'))
print "Status Code: "+str(r.status_code)
print r.json
