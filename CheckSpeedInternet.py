''' Check and save information about Internet speed from download and upload '''

import time
from datetime import datetime
import speedtest   # pip install speedtest-cli
import os

def check_file(file):
    # if the file does not exist, create a file with headers
    if not os.path.isfile(file):
        with open(file,"a+") as f:
            f.write("Date,Time,Download,Upload\n")
    return file

def check_speed(n):
    while n != 0:
        file = check_file("Files/checkspeed.csv")
        date_check = datetime.now().strftime("%d-%m-%Y")
        time_check = datetime.now().strftime("%H:%M")

        print(f"Checking speed on {date_check} at {time_check}h")
        s = speedtest.Speedtest()
        download = round(s.download() / (10**6), 2) # Mbps
        upload = round(s.upload() / (10**6), 2) # Mbps

        with open(file,"a+") as f:
            f.write(str(date_check) + "," + str(time_check) + "," + str(download) + "," + str(upload) + "\n")
        n -= 1
        # Wait the interval in seconds to check again
        time.sleep(3600)

if __name__ == "__main__":
   check_speed(10) # will check the speed 10 times
