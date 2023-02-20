#!ALERT!!Run these scipt in <C:\Windows\System32>
import schedule
import os
import time
print("Savdhan!Your pc shutdoen at 21:18")
def shutdown():
    #os.system("shutdown /s/t/1")#these is for shutdown USE r for Restart
    os.system("shutdown /s /t 1")
schedule.every().day.at("22:02").do(shutdown)
while True:
    schedule.run_pending()
    time.sleep(1)
if __name__=="__main__":
    shutdown()