import requests
# r=requests.get("https://imgs.xkcd.com/comics/python.png")
# print(r)
# print(r.status_code)
# f=open("D:\pyth_config\sample.png","wb")
# f.write(r.content)
# # print(r.content)
# f.close()


#passing argument to request module
import json
# parm={"page":2,"count":4}
# r=requests.get("http://httpbin.org/get",params=parm)
# print(r)
# print(r.status_code)
# print(r.text,type(r.text))
# print(json.loads(r.text))
# print(r.json())


parm={"username":"correy","password":"9564"}
r=requests.post("http://httpbin.org/post",data=parm)
print(r.text)
print(r.status_code)

