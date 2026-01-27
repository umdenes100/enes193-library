from machine import Pin, PWM, time_pulse_us
import time

class Tank:
    def __init__(self):
        # Motor Control Pins
        self.pwma = PWM(Pin(14), freq=1000)  # A = Right motors
        self.pwmb = PWM(Pin(13), freq=1000)  # B = Left motors
        self.pwma.duty(0)
        self.pwmb.duty(0)
        self.ain1 = Pin(23, Pin.OUT)
        self.bin1 = Pin(12, Pin.OUT)
        self.stby = Pin(26, Pin.OUT)
        self.stby.on()
        
        # Ultrasonic Pins
        self.echo = Pin(16, Pin.IN)
        self.trig = Pin(5, Pin.OUT)
        
        # Servo Pins
        self.servo1 = PWM(Pin(18, Pin.OUT), freq=50)
        self.set_servo(90)
        

    def set_right_PWM(self, speed):
        self.ain1.value(1 if speed > 0 else 0)
        self.pwma.duty(min(abs(speed), 1023))

    def set_left_PWM(self, speed):
        self.bin1.value(1 if speed > 0 else 0)
        self.pwmb.duty(min(abs(speed), 1023))

    def turn_off_motors(self):
        self.pwma.duty(0)
        self.pwmb.duty(0)
        
    def read_distance_sensor(self):
        pulse_time = self.__send_pulse()
        cms = (pulse_time / 2) / 29.1
        if cms < 0:
            return -1
        return cms
    
    def set_servo(self, angle):
        duty = self.__angle_to_duty(angle)
        self.servo1.duty_u16(duty)
    
    def __angle_to_duty(self, angle):
        # Convert angle (0-180) to a duty cycle value
        min_us = 550
        max_us = 2400
        # Calculate pulse width in microseconds
        pulse_us = min_us + (max_us - min_us) * angle / 180
        # Convert microseconds to duty cycle (0-65535 for 16-bit PWM)
        duty = int(pulse_us * 65535 / 20000)
        return duty
    
    def __send_pulse(self):    
        self.trig.value(0) # Stabilize the sensor
        time.sleep_us(5)
        self.trig.value(1)
        # Send a 10us pulse.
        time.sleep_us(10)
        self.trig.value(0)
        try:
            pulse_time = time_pulse_us(self.echo, 1, 30000)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

Tank = Tank()