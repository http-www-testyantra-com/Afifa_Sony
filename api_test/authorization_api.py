import requests
import json
parm={"username":"correy","password":"testing"}
r=requests.post("http://httpbin.org/basic-auth/sadf/234",auth=('sadf','234'))
print(r.text)
print(r.status_code)