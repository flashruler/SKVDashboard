import requests
import pandas as pd 
from itertools import zip_longest

def getMatchSchedule(event,server):
    matches=requests.get("http://"+server+"/api/v1/events/"+event+"/matches/").json()
    for x in matches["matches"]:
        x['league']=event
    
    return matches["matches"]

def generateCSV(interleavedSchedule):
    df=pd.DataFrame.from_dict(interleavedSchedule)
    #data cleanup
    df=df.drop(columns=['time'])
    print(df)

#probably the most broken function here
# def interleaverOld(active,server):
#     schedules=[]
#     interleavedSchedule=[]
#     maxMatchNum=0
#     for x in active:
#         schedules.append(getMatchSchedule(x,server))
#     for x in schedules:
#         if len(x)>maxMatchNum:
#             maxMatchNum=len(x)
#     #yikes, to fix in the future
#     for x in range(maxMatchNum):
#         for i in schedules:
#             try:
#                 for j in range(len(i)):
#                     if i[j]["matchNumber"]==x+1:
#                         interleavedSchedule.append(i[j])
                    
#             except IndexError:
#                 pass
#             continue


#     generateCSV(interleavedSchedule)
#     return interleavedSchedule

def interleaver(active,server):
    schedules=[]
    interleavedSchedule = []
    for x in active:
            schedules.append(getMatchSchedule(x,server))
    b = list(zip_longest(*schedules))
    for l in b:
        interleavedSchedule.extend(l)
    interleavedSchedule = [i for i in interleavedSchedule if i is not None]
    return interleavedSchedule

