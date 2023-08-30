


import schedule
import time

from secrets_and_config import *

from register_classes import register_classes


job_error_count = 0
def run_job():
    global job_error_count
    try:
        register_classes()
    except:
        print("JOB ERRORED ABORTING")
        job_error_count += 1
        print(job_error_count)


print(f"Program set, will run about every {SECS_TO_WAIT_IN_BETWEEN_RUNS} seconds")
print("Currently there is no auto-stopping once detected, so you will need to check in periodically on CUNYFIRST and stop the program then")
print("Leave this program running in the background, stop the program by pressing control + C in the terminal")

time.sleep(5)
register_classes()

schedule.every(SECS_TO_WAIT_IN_BETWEEN_RUNS).seconds.do(register_classes)

while True:
    schedule.run_pending()

    # print(schedule.get_jobs())
    time.sleep(1)


"""
Potential todos
    - count down timer to next run
    - automatically stop once the run succeeds (or option for this)
    - run browser in the background instead of on screen (check if selenium supports this)

    - bundle into an executable or a pip package so people who don't like the terminal can use (as practice for other scripts I might write)
    - replace config.py with command line arguments maybe

video from freecodecamp where he makes a selenium userbot https://www.youtube.com/watch?v=j7VZsCCnptM (didn't watch before making)
    

"""