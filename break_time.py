
import webbrowser
import time
import datetime


url = "https://www.youtube.com/watch?v=SXiSVQZLje8&list=PLQxmXJiUdQOXBrb1e1Q1NA-ejL81uRDvK&index=103"

#print "The program started on: ", datetime.datetime.now()

total_breaks = 3
break_ct = 0
while (break_ct < total_breaks):
    time.sleep(5)
    print "The program started on: ", datetime.datetime.now()
    webbrowser.open_new(url)
   # print "The program started on: ", datetime.datetime.now()
    break_ct += 1
