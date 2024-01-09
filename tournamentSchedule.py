import requests
def pollEvents(server):
    events = requests.get("http://"+server+"/api/v1/events/").json()
    eventCodes=events["eventCodes"]
    liveEvents=[]
    return eventCodes

def retrieveActiveMatch(event,server):
    match = {}
    query=requests.get("http://"+server+"/api/v1/events/"+event+"/matches/active/").json()
    match=query["matches"]
    return match

def getActiveEvents(event,server):
    activeEvents=[]
    for x in event:
        event= requests.get("http://"+server+"/api/v1/events/"+x).json()
        if(event["status"]=="Qualifications"):
            activeEvents.append(x)
    return activeEvents

def retrieveTournamentMatch(match,interleavedSchedule):
    matchNumber=0
    isActive=False
    for x in interleavedSchedule:
        if match["red"]==x["red"] and match["blue"]==x["blue"]:
            matchNumber=interleavedSchedule.index(x)+1

        if match["matchState"]!="unplayed":
            isActive=True

    return matchNumber,isActive

def determineActiveLeague(eventCodes,server):
    for x in eventCodes:
        activeMatch=retrieveActiveMatch(x,server)
        if activeMatch and activeMatch[0]["matchState"]!= "UNPLAYED" or activeMatch[0]["matchState"]!= "REVIEW":
            print(retrieveActiveMatch(x,server))
