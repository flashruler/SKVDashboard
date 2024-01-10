import requests
from reloading import reloading

@reloading
def pollEvents(server):
    events = requests.get("http://"+server+"/api/v1/events/").json()
    eventCodes=events["eventCodes"]
    return eventCodes

@reloading
def retrieveActiveMatch(event,server):
    match = {}
    query=requests.get("http://"+server+"/api/v1/events/"+event+"/matches/active/").json()
    match=query["matches"]
    return match

@reloading
def getActiveEvents(event,server):
    activeEvents=[]
    for x in event:
        event= requests.get("http://"+server+"/api/v1/events/"+x).json()
        if(event["status"]=="Qualifications"):
            activeEvents.append(x)
    return activeEvents

@reloading
def determineActiveLeague(eventCodes,server):
    active=""
    for x in eventCodes:
        activeMatch=retrieveActiveMatch(x,server)
        try: 
            if activeMatch and activeMatch[0]["matchState"]!= "UNPLAYED" and activeMatch[0]["matchState"]!= "REVIEW" :
                active=retrieveActiveMatch(x,server)[0]
        except IndexError:
            pass
        continue
    return active

@reloading
def getActiveTournamentMatch(active,interleavedSchedule):
    for x in interleavedSchedule:
        try:
            if x["red"]==active["red"] and x["blue"]==active["blue"]:
                print("Tournament Match is: " + str(interleavedSchedule.index(x)+1))
                return interleavedSchedule.index(x)+1
        except TypeError:
            pass
        continue


    
