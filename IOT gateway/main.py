import sys
from Adafruit_IO import MQTTClient
import time
import random
# from simple_ai import *
from uart import *

AIO_FEED_ID = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "HCrystalH"
# AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed id: " + feed_id)
    if feed_id =="nutnhan1":  
        if payload == "1":
            writeData("Bat")
        else:
            writeData("Tat")
    
    if feed_id =="nutnhan2":
        if payload == "2":
            writeData("Bat")
        else:
            writeData("Tat")

### Uncomment to run 

# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()



counter = 10 
# counter_ai = 5  
# ai_result =""
previous_result =""
while True:
    
    counter = counter - 1
    if counter <=0:
        counter = 120
        #TO DO 
        # print("Random data is publishing ... ")
        # temp = random.randint(20,50)
        # client.publish("temperature", temp)
        # humi = random.randint(0,100)
        # client.publish("humidity",humi)
        # light = random.randint(0,100)
        # client.publish("cambien3",light)
    
    
    counter_ai = counter_ai - 1
    # if counter_ai <=0:
    #     counter_ai = 10
    #     previous_result = ai_result
    #     ai_result = image_detector()
    #     print("AI Output: ",ai_result)
    #     if previous_result != ai_result:
    #         client.publish("AI", ai_result)
    
    readSerial(client)
    time.sleep(1)
    # # Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)

    # # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
    #     break