import requests#used to get the info from website 
from sense_hat import SenseHat#used to talk to sense hat 
import time #link

from datetime import datetime,time#used to insure only runs on the specified times
print("Initiating Code")

link ="https://pastebin.com/raw/gUUa97wg"
f=requests.get(link)#reads the webpage
sense=SenseHat()#makes sensehat
def fullblock(color): 
  red= color#need to be 3 numbers (,,#)

  color_array = [red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red,
         red,red,red,red,red,red,red,red]
  return color_array
#used to record the time between checking website
count = 60 
wait = 2 
print("Iniating Code")

def comm(ReCommq):
  sense.show_message("",[0,0,0])

while(true):#need to insert a sleep or standby function
  f=requests.get(link)#reads the webpage

  while "RED" in f.text:#checks for red alert issue
    f=requests.get(link)#reads the webpage
    sense.set_pixels(fullblock((255,0,0)))
    time.sleep(wait)
    info = f.text.replace("RED"," ")
    sense.show_message(info, text_colour = [255,0,0])
    
  while "GREEN" in f.text:
    f=requests.get(link)#reads the webpage
    sense.set_pixels(fullblock((0,255,0)))
    time.sleep(wait)
    message = f.text.replace("GREEN"," ")
    sense.show_message(message, text_colour = [0,255,0])
  if(f.text=="Error with this ID!"):
    print("\n"*3,"Error Reading Web Page","\n"*3)
    break
  else:
    print(f.text)
    sense.show_message(f.text, text_colour = [0,0,255])
  time.sleep(2)
