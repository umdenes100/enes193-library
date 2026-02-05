from enes193.tank import tank
import time

# Forward (0 < PWM < 1023)
tank.set_right_PWM(150)
tank.set_left_PWM(150)
time.sleep(3)

# Backward (-1023 < PWM < 0)
tank.set_right_PWM(-300)
tank.set_left_PWM(-300)
time.sleep(3)

# Spin in place: right forward, left backward or vice versa
tank.set_right_PWM(300)
tank.set_left_PWM(-300)
time.sleep(3)

# Stop motors
tank.turn_off_motors()
# Ultrasonics
dist = tank.read_distance_sensor()
print(dist)
time.sleep(0.5)

# Servo (set in degrees: 0-180)
tank.set_servo(0) # right
time.sleep(1)
tank.set_servo(90) # forward
time.sleep(1)
tank.set_servo(180) # left

