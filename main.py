from api import generateKey
from tournamentSchedule import pollEvents,getActiveEvents
from interleaver import interleaver
from tournamentSchedule import getActiveTournamentMatch, retrieveActiveMatch, determineActiveLeague

isActive=True

key=generateKey("SDFTCController","192.168.4.52")

print("Key is not Active! Activate on FTC Scorekeeper Dashboard")


while isActive:
    query=input("What are you trying to do? Enter a number 1. Load events 2. Show Active Events 3. Generate Interleaved Schedule 4. Find Active Match Data 5. Find Tournament Match   --->   ")
    match query:
        case "1":
            liveEvents= pollEvents("192.168.4.52")
            print(liveEvents)
        case "2":
            activeLeagues=getActiveEvents(liveEvents,"192.168.4.52")
            print(activeLeagues)
        case "3":
            interleavedSchedule=interleaver(activeLeagues,"192.168.4.52")
        case "4":
            activeLeague=determineActiveLeague(activeLeagues,"192.168.4.52")
            print(activeLeague)
        case "5":
            tournamentMatch=getActiveTournamentMatch(activeLeague,interleavedSchedule)
            print(tournamentMatch)