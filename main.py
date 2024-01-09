from api import generateKey, keyCheck
from tournamentSchedule import pollEvents,getActiveEvents
from interleaver import interleaver
from tournamentSchedule import retrieveTournamentMatch, retrieveActiveMatch, determineActiveLeague

isActive=False

key=generateKey("SDFTCController","localhost")
while not isActive:
    print("Key is not Active! Activate on FTC Scorekeeper Dashboard")
    isActive=keyCheck(key)
    input("Press Enter to check key")
else:
    print("Key is Active!")
while isActive:
    query=input("What are you trying to do? Enter a number 1. Load events 2. Show Active Events 3. Generate Interleaved Schedule")
    match query:
        case "1":
            liveEvents= pollEvents("localhost")
            print(liveEvents)
        case "2":
            activeLeagues=getActiveEvents(liveEvents,"localhost")
            print(activeLeagues)
        case "3":
            interleavedSchedule=interleaver(activeLeagues,"localhost")
        case "4":
            activeLeague=determineActiveLeague(activeLeagues,"localhost")
            print(activeLeague)