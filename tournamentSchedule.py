import requests
def pollEvents(server):
    events = requests.get("http://"+server+"/api/v1/events/").json()
    eventCodes=events["eventCodes"]
    liveEvents=[]
    return eventCodes

def getActiveEvents(eventCodes,server):
    activeEvents=[]
    for x in eventCodes:
        event= requests.get("http://"+server+"/api/v1/events/"+x).json()
        if(event["status"]=="Qualifications"):
            activeEvents.append(x)
    return activeEvents
