import datetime
import schedule
import time
def file_append():
    file=open(r'F:\python_Marvallous\scheduling\task.txt','a')
    file.write(f'{datetime.datetime.now()}-the script ran\n')
#schedule.every(1).minutes.do(file_append)
# schedule.every(2).seconds.do(file_append)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
if __name__=="__main__":
    file_append()
