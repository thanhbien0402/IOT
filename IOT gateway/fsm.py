
# Online Python - IDE, Editor, Compiler, Interpreter

import time 
from rs485 import *
from 
from Adafruit_IO import MQTT client

IDLE = 0
MIXER1 = 1 
MIXER2 = 2 
MIXER3 = 3 
PUMP_IN = 4
SELECTOR = 5
PUMP_OUT = 6
NEXT_CYCLE = 7 
STOP = 8 

WAIT_TIME = 10

status = IDLE
cycle = 0 
count = 0 

def fsm(sched, client):
    global status, cycle, count
    if status == IDLE:
        print("idling")
        status = MIXER1
        count = sched.flow1
        print("cycle: " + str(cycle))
        print("mixer1")
        write_relays(1,1) 
        publish_noti(client, sche.id)
    elif status == MIXER1:
        if count <= 0:
            write_relays(1,0)
            count = sched.flow2
            status = MIXER2 
            print("mixer2")
            write_relays(2,1)
            publish_noti(client, sched.id)
    elif status == MIXER2:
        if count <= 0:
            write_relays(2,0)
            count = sched.flow3
            status = MIXER3 
            print("mixer3")
            write_relays(3,1)
            publish_noti(client, sched.id)
    elif status == MIXER3:
        if count <= 0: 
            write_relays(3,0) 
            count = WAIT_TIME
            status = PUMP_IN
            print("pump in")
            write_relays(7,1)
            publish_noti(client, sched.id)
    elif status == PUMP_IN:
        if count <= 0:
            write_relays(7,0)
            print("select area")
            if(sched.area == -1):
                select_area(sched.area % 3)
            else:
                select_area(sche.area)
    elif status == SELECTOR:
        count = WAIT_TIME
        status = PUMP_OUT
        print("pump out")
        write_relays(8,1)
        publish_noti(client, sched.id)
    elif status == PUMP_OUT:
        if count <= 0:
            write_relays(8,0)
            status = NEXT_CYCLE
            print("next cycle")
            publish_noti(client, sched.id)
    elif status == NEXT_CYCLE:
        cycle = cycle + 1
        if cycle >= sched.cycle:
            print("finish")
            status = STOP
            publish_noti(client, sched.id)
        else:
            status = MIXER1
            print("cycle" + str(cycle))
            print("mixer1")
            write_relays(1,1)
            publish_noti(client, sched.id)
    count = count - 1 
    
    
def select_area(area):
    if area == 0 :
        print("area 0")
        write_relays(4,1)
        write_relays(5,0)
        write_relays(6,0)
    elif area == 1 : 
        print("area 1")
        write_relays(4,0)
        write_relays(5,1)
        write_relays(6,0)
    elif area == 2:
        print("area 2")
        write_relays(4,0)
        write_relays(5,0)
        write_relays(6,1)
     
def publish_noti(client, id ):
    global status, cycle
    message = f"{id},{cycle},{status}"
    client.publish("id_noti", message)

