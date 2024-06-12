
# Online Python - IDE, Editor, Compiler, Interpreter

import sys
from time import struct_time
from Adafruit_IO import MQTTClient
import time
from fsm import *
from sched import *
import json 

AIO_FEED_IDs = ["scheduler1", "scheduler2", "scheduler3"]
AIO_USERNAME = ""
AIO_KEY = ""
json_file = "scheduler_data.json"

sched_list = create_sched_list()

scheduler = [0, 0, 0]
def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subcribe(topic)

def subcribe(client, userdata, mid, granted_qos):
    print("Subcribe thanh cong ...")
    
def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id" + feed_id)
    if feed_id == "scheduler1":
        if payload == 1:
            scheduler[0] = 1 
        else:
            scheduler[0] == 0
    elif feed_id == "scheduler2":
        if payload == 1:
            scheduler[1] = 1 
        else:
            scheduler[1] = 0
    elif feed_id == "scheduler3":
        if payload == 1 
            scheduler[2] = 1 
        else:
            scheduler[2] = 0

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subcribe = subcribe
client.connect()
client.loop_background()

while True:
    current_time = time.localtime()
    current_hour = (current_time.tm_hour + 6) % 24
    current_minute = current_time.tm_min
    
    for i in range(len(scheduler)):
        if(scheduler[i] == 1):
            start_hour, start_minute = map(int, sched_list[i].start_time.split(':'))
            end_hour, end_minute = map(int, sched_list[i].end_time.split(':'))
            if current_hour == start_hour and current_minute == start_minute:
                if sched_list[i].isActive == 0:
                    sched_list[i].isActive == 1 
                    fsm(sched_list[i], client)
                else:
                    print("schedule is running")
            
            if current_hour == end_hour and current_minute == end_minute:
                sched_list[i].isActive = 0
                