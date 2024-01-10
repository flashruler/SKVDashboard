import requests
from reloading import reloading

@reloading
def generateKey(name,server):
    res=requests.post("http://"+server+"/api/v1/keyrequest/?name="+name)
    res=res.json()
    key=res["key"]
    return key

@reloading
def keyCheck(keys):
    keyCheck=requests.get("http://localhost/api/v1/keycheck/?=", headers={"Authorization": keys})
    keyCheck=keyCheck.json()
    return keyCheck["active"]