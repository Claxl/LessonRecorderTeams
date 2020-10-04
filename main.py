from datetime import datetime
from subprocess import call
import time
# datetime object containing current date and time
def record():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%A %H:%M")
    print("date and time =", dt_string)
    x = dt_string.split(" ",1);
    print(x[0]);
    lesson = ["Monday","Tuesday","Wednesday","Thursday","Friday"];
    timeLesson = {}
    timeLesson["Monday"] = "9:00","11:15"
    timeLesson["Tuesday"] = "9:00","11:15","14:30"
    timeLesson["Wednesday"] = "9:00"
    timeLesson["Thursday"] = "9:00","11:15","14:30"
    timeLesson["Friday"] = "11:15"
    # print(timeLesson);
    print(x[1])
    if x[0] in lesson:
        print("LESSON DAY")
        if x[1] in timeLesson[x[0]]:
            print("START RECORD!!!")
            dir = "C:/Program Files/obs-studio/bin/64bit"
            cmdline = "obs64.exe --startrecording"
            call("start cmd /c "+cmdline, cwd = dir,shell=True)#change ip with nordvpn
        else :
            print("NOT YET")
    else:
        print("FREE DAY")
        
if __name__=="__main__":
    print("Starting...")
    while(1):
        time.sleep(60)
        print("Checking...")
        record()
    
