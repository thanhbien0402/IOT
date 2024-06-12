import time
import serial.tools.list_ports

def modbus_crc(message):
    crc = 0xFFFF
    for n in range(len(message)):
        if crc & 1:
            crc >>= 1
            crc ^= 0xA001
        else:
            crc >>= 1
    return [crc & 0xFF, (crc >> 8) & 0xFF]

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0,N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
    return commPort

port_name = getPort
print(port_name)

try:
    ser = serial.Serial(port=port_name, baudrate=9600)
    print("Open successfully")
except:
    print("cannot open port")

relay1_ON = [1,6,0,0,0,255]
relay1_OFF = [1,6,0,0,0,0]

relay2_ON = [2,6,0,0,0,255]
relay2_OFF = [2,6,0,0,0,0]

relay3_ON = [3,6,0,0,0,255]
relay3_OFF = [3,6,0,0,0,0]

relay4_ON = [4,6,0,0,0,255]
relay4_OFF = [4,6,0,0,0,0]

relay5_ON = [5,6,0,0,0,255]
relay5_OFF = [5,6,0,0,0,0]

relay6_ON = [6,6,0,0,0,255]
relay6_OFF = [6,6,0,0,0,0]

relay7_ON = [7,6,0,0,0,255]
relay7_OFF = [7,6,0,0,0,0]

relay8_ON = [8,6,0,0,0,255]
relay8_OFF = [8,6,0,0,0,0]

def write_relays(id, state):
    if id == 1:
        if state == 1:
            ser.write(modbus_crc(relay1_ON))
        elif state == 0:
            ser.write(modbus_crc(relay1_OFF))
    elif id == 2:
        if state == 1:
            ser.write(modbus_crc(relay2_ON))
        elif state == 0:
            ser.write(modbus_crc(relay2_OFF))
    elif id == 3:
        if state == 1:
            ser.write(modbus_crc(relay3_ON))
        elif state == 0:
            ser.write(modbus_crc(relay3_OFF))
    elif id == 4:
        if state == 1:
            ser.write(modbus_crc(relay4_ON))
        elif state == 0:
            ser.write(modbus_crc(relay4_OFF))
    elif id == 5:
        if state == 1:
            ser.write(modbus_crc(relay5_ON))
        elif state == 0:
            ser.write(modbus_crc(relay5_OFF))
    elif id == 6:
        if state == 1:
            ser.write(modbus_crc(relay6_ON))
        elif state == 0:
            ser.write(modbus_crc(relay6_OFF))
    elif id == 7:
        if state == 1:
            ser.write(modbus_crc(relay7_ON))
        elif state == 0:
            ser.write(modbus_crc(relay7_OFF))
    elif id == 8:
        if state == 1:
            ser.write(modbus_crc(relay8_ON))
        elif state == 0:
            ser.write(modbus_crc(relay8_OFF))
    time.sleep(1)
    print(serial_read_data(ser))

def serial_read_data(ser):
    byte_to_read = ser.inWaiting()
    if byte_to_read > 0:
        out = ser.read(byte_to_read)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

soil_temperature = [1,3,0,6,0,1]

def read_temperature():
    serial_read_data(ser)
    ser.write(modbus_crc(soil_temperature))
    time.sleep(1)
    result = serial_read_data(ser)/100
    print("temperature: ",result)
    return result

soil_humidity = [1,3,0,7,0,1]

def read_humidity():
    serial_read_data(ser)
    ser.write(modbus_crc(soil_humidity))
    time.sleep(1)
    result = serial_read_data(ser)/100
    print("Humidity: ", result)
    return result

