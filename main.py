
import time

from secrets_and_config import *

from register_classes import register_classes


job_error_count = 0
def run_job():
    global job_error_count
    try:
        register_classes()
    except:
        job_error_count += 1
        print(f"JOB ERRORED ABORTING  - {job_error_count} jobs failed so far")


print(f"Program set, will run about every {SECS_TO_WAIT_IN_BETWEEN_RUNS} seconds")
print("Currently there is no auto-stopping once detected, so you will need to check in periodically on CUNYFIRST and stop the program then")
print("Leave this program running in the background, stop the program by pressing control + C in the terminal")

times_run = 0
count = 5
while True:
    time.sleep(1)

    print(f"\r> {count} seconds till next run. run {times_run} times so far, failed {job_error_count} times   ", end='')

    count -= 1
    if count <= 0:
        success = run_job()
        count = SECS_TO_WAIT_IN_BETWEEN_RUNS
        times_run += 1
        if success:
            print("SEEMS TO HAVE SUCCEEDED")
            SECS_TO_WAIT_IN_BETWEEN_RUNS = 3600
            # break
    


"""
Potential todos
    - count down timer to next run
    - automatically stop once the run succeeds (or option for this)
    - run browser in the background instead of on screen (check if selenium supports this)

    - bundle into an executable or a pip package so people who don't like the terminal can use (as practice for other scripts I might write)
    - replace config.py with command line arguments maybe

video from freecodecamp where he makes a selenium userbot https://www.youtube.com/watch?v=j7VZsCCnptM (didn't watch before making)
    

"""