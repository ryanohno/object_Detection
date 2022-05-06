from datetime import datetime
import sys

result = (datetime.today().strftime('%Y-%m-%d %H:%M'))
print(result, file=open("/home/pi/Desktop/current_time.txt","w"))
