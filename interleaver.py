import requests
import pandas as pd 
import numpy as np
from itertools import zip_longest
from reloading import reloading

def getMatchSchedule(event,server):
    matches=requests.get("http://"+server+"/api/v1/events/"+event+"/matches/").json()
    for x in matches["matches"]:
        x['league']=event
    
    return matches["matches"]

@reloading
def generateCSV(interleavedSchedule):
    dfRaw=pd.DataFrame.from_dict(interleavedSchedule)
    df=dfRaw
    #data cleanup
    df=df.drop(columns=['time','matchState','finished','matchNumber'])
    df2=pd.json_normalize(df['red'])
    df2.rename(columns={'team1': 'Red Team 1', 'team2': 'Red Team 2'}, inplace=True)
    df2.drop(['isTeam1Surrogate','isTeam2Surrogate'], axis=1, inplace=True)
    df3=pd.json_normalize(df['blue'])
    df3.drop(['isTeam1Surrogate','isTeam2Surrogate'], axis=1, inplace=True)
    df3.rename(columns={'team1': 'Blue Team 1', 'team2': 'Blue Team 2'}, inplace=True)
    df.drop(['red','blue'], axis=1, inplace=True)
    df3=pd.concat([df2,df3],axis=1)
    df=pd.concat([df,df3],axis=1)
    df['field']=np.where(df.index%2==0, 'A', 'B') 
    field=df.pop('field')
    matchName=df.pop('matchName')
    df.insert(0, 'Tournament Match', range(1, 1 + len(df)))
    df.insert(1, 'Field', field)
    df.insert(3, 'Match', matchName)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    df.to_csv(r'dftocsv.csv', sep='\t', encoding='utf-8', header='true')
    return dfRaw

def interleaver(active,server):
    schedules=[]
    interleavedSchedule = []
    for x in active:
            schedules.append(getMatchSchedule(x,server))
    b = list(zip_longest(*schedules))
    for l in b:
        interleavedSchedule.extend(l)
    interleavedSchedule = [i for i in interleavedSchedule if i is not None]
    df= generateCSV(interleavedSchedule)
    return df

