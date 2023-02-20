import time
import schedule
def me():
    print("HEllo")
def job():
    print("perfect at day!")
schedule.every(2).seconds.do(me)
#schedule.every().day.at("8:47:00").do(me)
schedule.every().day.at("21:04").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
if __name__=="__main__":
    me()
