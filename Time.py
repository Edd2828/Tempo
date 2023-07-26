import datetime
import time

current_time = datetime.datetime.utcnow()
test = datetime.timedelta(
    days=0,
    seconds=0,
    microseconds=0, 
    milliseconds=0, 
    minutes=0, 
    hours=1, 
    weeks=0

)

print(current_time+test)

'''
while True:
    time.sleep(1)
    current_time = datetime.datetime.utcnow()
    print(current_time)
'''