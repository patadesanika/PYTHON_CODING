import time
import schedule 
def call_me(): 
  print("I am invoked")
# schedule.every(1).minutes.do(call_me)

# while True: #here yours schedule is going to excuted
#   schedule.run_pending()
#   time.sleep(1)
if __name__=="__main__":
  
  call_me()