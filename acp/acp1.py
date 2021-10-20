import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np
GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troykaVoltage = 17
comparator = 4
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def bin2dec(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]
def num2pins(pins, value):
    GPIO.output(pins, bin2dec(value))
def adc():

    value = 0
    direction =  1

    for i in range(8):
        delta=2**(8-i-1)
        value += delta*direction
        num2pins(leds, value)
        time.sleep(0.001)
        if(GPIO.input(comparator)==0):
            direction = -1
        else:
            direction = 1
    return value
list_Time = []
list_Voltage = []
list_Napr = [] 
schet = 0
try:
    GPIO.output(troykaVoltage, 1)
    time_begin = time.time()
    while  adc()< 252:
        schet+=1 
        list_Time.append =(time.time()-time_begin)
        list_Napr.append =(adc())
        Voltage = adc()*3.3/256
        list_Voltage.append(Voltage)
        time.sleep(0.01)
    
    GPIO.output(troykaVoltage,0)
    while adc()>0:
        schet+=1
        list_Time.append = (time.time()-time_begin)
        list_Napr.append = (adc())
        Voltage = adc()*3.3/256
        list_Voltage.append =(Voltage)
        time.sleep(0.01)
    time_end = time.time()
    work_time = time_end-time_begin
    work_time_str = str(work_time)
    chastota = schet/work_time
    chastota_str = str(chastota)
    period = work_time/schet
    period_str = str(period) 
    list_Napr_str =[str(item) for item in list_Napr] 
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(list_Napr_str))
    outfile.close()

    with open("setting.txt", "w") as settingfile:
        settingfile.write("Chastota = ")
        settingfile.write(chastota_str + "\n")
        settingfile.write("Period = ")
        settingfile.write(period_str+"\n")
        settingfile.write("Work time = ")
        settingfile.write(work_time)
    settingfile.close()

    plt.plot(list_Time, list_Voltage, 'r-')
    plt.title('Зависимость напряжения  от времени')
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.show()
finally:
    GPIO.cleanup()



