from tank import Tank
import time

# Forward (0 < PWM < 1023)
Tank.set_right_PWM(150)
Tank.set_left_PWM(150)
time.sleep(3)

# Backward (-1023 < PWM < 0)
Tank.set_right_PWM(-300)
Tank.set_left_PWM(-300)
time.sleep(3)

# Spin in place: right forward, left backward or vice versa
Tank.set_right_PWM(300)
Tank.set_left_PWM(-300)
time.sleep(3)

# Stop motors
Tank.turn_off_motors()

# Ultrasonics
dist = Tank.read_distance_sensor()
print(dist)
time.sleep(0.5)

# Servo (set in degrees: 0-180)
Tank.set_servo(0) # right
time.sleep(1)
Tank.set_servo(90) # forward
time.sleep(1)
Tank.set_servo(180) # left


