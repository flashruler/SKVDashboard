import requests
import pandas as pd 
def getMatchSchedule(event,server):
    matches=requests.get("http://"+server+"/api/v1/events/"+event+"/matches/").json()
    for x in matches["matches"]:
        x['league']=event
    
    return matches["matches"]

def generateCSV(interleavedSchedule):
    df=pd.DataFrame.from_dict(interleavedSchedule)
    #data cleanup
    df.drop(["finished","time","matchState"], axis=1)

    print(df)

def interleaver(active,server):
    schedules=[]
    interleavedSchedule=[]
    maxMatchNum=0
    for x in active:
        schedules.append(getMatchSchedule(x,server))
    for x in schedules:
        if len(x)>maxMatchNum:
            maxMatchNum=len(x)
    for x in range(maxMatchNum):
        for i in schedules:
            try:
                for j in range(len(i)):
                    if i[j]["matchNumber"]==x+1:
                        interleavedSchedule.append(i[j])
                    
            except IndexError:
                pass
            continue


    generateCSV(interleavedSchedule)
    return interleavedSchedule