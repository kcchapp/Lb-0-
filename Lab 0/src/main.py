'''!
@file       main.py
@brief      sets up LED pins on nucleo and creates isosceles triangle wave
@details    This program uses built-in PYB board commands to control inputs 
            and outputs of pin connections. After enabling the LED pin on the 
            board, we can control the brightness.
            
@author     Jeremy Baechler
@author     Kendall Chappell
@author     Matthew Wimberley
@date       06-Jan-2022
'''

import utime #to use built in computer time

def led_setup():
    '''!
    @brief      instantiates board pins, timers, and channels
    '''
    
    global ch1
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=20000)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0) 
    #PWM channel is inverted, so when pin reads low, light will shine

def led_brightness(bright):
    '''!
    @brief      sets LED pulse width brightness to local variable bright
    @param      emits the LED brightness as a percentage 
    '''
    
    ch1.pulse_width_percent(bright)

    
if __name__ == '__main__':
    
    current_time = utime.ticks_us() #instantiates current time outside of loop
    led_setup()
    
    while True:
        new_time = utime.ticks_us()
        diff = utime.ticks_diff(new_time, current_time)/1000000 #us to s
        if diff >= 0 and diff < 5:
            bright = 20*(diff)
            led_brightness(bright)
        elif diff >=5 and diff < 10:
            bright = 100 - 20 * (diff - 5)
            led_brightness(bright)
        else:
            current_time = utime.ticks_us()
        print(bright, diff) #testing line to affirm our values follow a triangle pattern
            