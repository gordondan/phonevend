#!/usr/bin/python
from azure.servicebus import ServiceBusService, Message, Queue
from time import sleep
import RPi.GPIO as io

# switches pins to GPIO numbers, not pin number on Pi
io.setmode(io.BCM)
in_pin1  = 27
in_pin2  = 20
in_pin3  = 2
in_pin4  = 3
in_pin5  = 4
in_pin6  = 14
in_pin7  = 15
in_pin8  = 17
in_pin9  = 18
in_pin10 = 22
in_pin11 = 23
in_pin12 = 24

io.setup(in_pin1, io.OUT)
io.setup(in_pin2, io.OUT)
io.setup(in_pin3, io.OUT)
io.setup(in_pin4, io.OUT)
io.setup(in_pin5, io.OUT)
io.setup(in_pin6, io.OUT)
io.setup(in_pin7, io.OUT)
io.setup(in_pin8, io.OUT)
io.setup(in_pin9, io.OUT)
io.setup(in_pin10, io.OUT)
io.setup(in_pin11, io.OUT)
io.setup(in_pin12, io.OUT)

def trigger1() :
    io.output(in_pin1,True)
    sleep(.5)
    io.output(in_pin1, False)

def trigger2() :
    io.output(in_pin2,True)
    sleep(.5)
    io.output(in_pin2, False)

def trigger3() :
    io.output(in_pin3,True)
    sleep(.5)
    io.output(in_pin3, False)

def trigger4() :
    io.output(in_pin4,True)
    sleep(.5)
    io.output(in_pin4, False)

def trigger5() :
    io.output(in_pin5,True)
    sleep(.5)
    io.output(in_pin5, False)

def trigger6() :
    io.output(in_pin6,True)
    sleep(.5)
    io.output(in_pin6, False)

def trigger7() :
    io.output(in_pin7,True)
    sleep(.5)
    io.output(in_pin7, False)

def trigger8() :
    io.output(in_pin8,True)
    sleep(.5)
    io.output(in_pin8, False)

def trigger9() :
    io.output(in_pin9,True)
    sleep(.5)
    io.output(in_pin9, False)

def trigger10() :
    io.output(in_pin10,True)
    sleep(.5)
    io.output(in_pin10, False)

def trigger11() :
    io.output(in_pin11,True)
    sleep(.5)
    io.output(in_pin11, False)

def trigger12() :
    io.output(in_pin12,True)
    sleep(.5)
    io.output(in_pin12, False)

def stop() :
    io.output(in_pin1,  False)
    io.output(in_pin2,  False)
    io.output(in_pin3,  False)
    io.output(in_pin4,  False)
    io.output(in_pin5,  False)
    io.output(in_pin6,  False)
    io.output(in_pin7,  False)
    io.output(in_pin8,  False)
    io.output(in_pin9,  False)
    io.output(in_pin10, False)
    io.output(in_pin11, False)
    io.output(in_pin12, False)
    
bus_service = ServiceBusService(
    service_namespace='appcandy-ns',
    shared_access_key_name='MachineListen',
    shared_access_key_value='OLYoVII6DU85jRQ70F06aHhX3wJwoTq+LC7WiW0zO6Q=')

dog = 1
print("dog " + str(dog))
while (dog < 4) :
    msg = bus_service.receive_queue_message('appcandy', peek_lock=False)
    print(msg.body)

    # get the number from the return message
    #number = str(msg.body[len(msg.body)-1])
    number = int(msg.body[-1:])
    print ('number is: ' + str(number) + ' len: ' + str(len(msg.body)) )
    #NOTE: we may need to do a different check for pins 10, 11, 12
    print ('lets go')
    # set the correct pin high
    if number == 1  :
        print ("I would do trigger 1")
        trigger1()
    elif number == 2  :
        trigger2()
    elif number == 3  :
        trigger3()
    elif number == 4  :
        trigger4()
    elif number == 5  :
        trigger5()
    elif number == 6  :
        trigger6()
    elif number == 7  :
        trigger7()
    elif number == 8  :
        trigger8()
    elif number == 9  :
        trigger9()
    elif number == 10 :
        trigger10()
    elif number == 11 :
        trigger11()
    elif number == 12 :
        trigger12()



