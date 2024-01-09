import requests
#generate keys for FTC Scorekeeper
def generateKey(name,server):
    res=requests.post("http://"+server+"/api/v1/keyrequest/?name="+name).json()
    key=res["key"]
    return key
#Checks if key is active
def keyCheck(keys):
    keyCheck=requests.get("http://localhost/api/v1/keycheck/?=", headers={"Authorization": keys}).json()
    return keyCheck["active"]