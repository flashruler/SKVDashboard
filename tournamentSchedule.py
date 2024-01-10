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


def determineActiveLeague(eventCodes,server):
    active=""
    for x in eventCodes:
        activeMatch=retrieveActiveMatch(x,server)
        try: 
            match activeMatch[0]["matchState"]:
                case "UNPLAYED": 
                    active="unplayed"
                case "REVIEW":
                    active="review"
                case "AUTONOMOUS":
                    active=retrieveActiveMatch(x,server)[0]
                case "TELEOP":
                    active=retrieveActiveMatch(x,server)[0]
            # if activeMatch and activeMatch[0]["matchState"]!= "UNPLAYED":
            #     active=retrieveActiveMatch(x,server)[0]
        except IndexError:
            pass
        continue
    print(active)
    return active

def getActiveTournamentMatch(active,interleavedSchedule):
    activeTournamentMatch=0
    for x in interleavedSchedule:
        if active["red"]==x["red"] and active["blue"]==x["blue"]:
            activeTournamentMatch=interleavedSchedule.index(x)+1
    return activeTournamentMatch




    
