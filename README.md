# ENES193 Library

### Package Download and Installation 
In this section, you will download the package and upload it to your microcontroller through Thonny IDE. 
1) To download the package, click the green  **<> Code** drop down at the top of the page. Then click **Download ZIP**.
2) Open Thonny and navigate to **Tools > Manage packages...**
3) Using **Install from local file**, find the file on your computer and upload it to your device.

### Usage
`from enes193.tank import tank` -> import tank functions

`from enes193 import Enes193` -> import vision system functions

To use the package, you have to direct the compiler to include it in your code. Add it manually by typing the above at the very top of your file.

## Tank Library
### Functions

`tank.turn_off_motors()` sets the pwm of both motors to 0.

`tank.set_left_PWM(pwm)` sets motors on left speeds to specified pwm (pwm: -1023 to 1023).

`tank.set_right_PWM(pwm)` sets motors right speeds to specified pwm (pwm: -1023 to 1023).

`tank.read_distance_sensor()` reads and returns distance in centimeters.

`tank.set_servo(deg)` sets servo motor to specified angle (deg: 0-180).

## ENES193 Library (Vision System Communication)
### Functions
### Enes193.begin()
`Enes193.begin(team_name: str, team_type: str, aruco_id: int, room_num: int)`
**Example:**`Enes193.begin("LTFs", "FIRE", 105, 1116)`
Establishes communication with the Vision System and allows for the use of all other enes100 commands
- team_name: Name of the team that will show up in the Vision System
- team_type: Type of mission your team is running.
	- Valid Mission Types: `'CRASH_SITE'`, `'DATA'`, `'MATERIAL'`, `'FIRE'`, `'WATER'`, `'SEED'`
- aruco_id: ID of your Aruco Marker
- room_num: The number of the classroom in which you are located (1116 or 1120)

### Enes193.x and similar
The Aruco Marker has 4 values
- x: x-coordinate of the Aruco Marker (from 0.0 to 4.0), -1 if aruco is not visible
- y: y-coordinate of the Aruco Marker (From 0.0 to 2.0), -1 if aruco is not visible
- theta: angle of the Aruco Marker (from -pi radians to pi radians), -1 if aruco is not visible
- visibility: whether the ArUco marker is visible (true or false)

These values can be queried by using the following commands:
- `Enes193.x`
- `Enes193.y`
- `Enes193.theta`
- `Enes193.is_visible`

Enes193.get variants will make sure you get the latest data available to you about your OTV's location. There is no need to save these as a separate variable.

### Enes193.is_connected()
`Enes193.is_connected()`

Returns true if the ESP8266 is connected to the Vision System, false otherwise. Note: enes100.begin will not return until this function is true.

### Enes193.print()
`Enes193.print(message: str)`

Sends a message to the vision system with a new line. Any messages sent after will be printed in a new line below the ' println'

### Enes193.mission()
`Enes193.mission(type: str, message: str*)`

Sends value for a mission objective.
- type: what type of mission call you are sending
- message: mission value associated with the mission type.

All the definitions defined in the Enes100 package correlate to an integer. To save you the trouble, you can call the uppercase definition like 'LENGTH' for Crash Site teams or 'MATERIAL_TYPE' for Material Identification teams.

*For some mission calls below, the value i will denote an integer value. In that case, i should be an int NOT a str.

Valid calls for **DATA**:
- `Enes193.mission(CYCLE, i)` i is the duty cycle percent (ex. 10, 30, 50, 70, 90)
- `Enes193.mission(MAGNETISM, MAGNETIC)`
- `Enes193.mission(MAGNETISM, NOT_MAGNETIC)`

Valid calls for **MATERIAL**:
- `Enes193.mission(WEIGHT, HEAVY)`
- `Enes193.mission(WEIGHT, MEDIUM)`
- `Enes193.mission(WEIGHT, LIGHT)`
- `Enes193.mission(MATERIAL_TYPE, FOAM)`
- `Enes193.mission(MATERIAL_TYPE, PLASTIC)`

Valid calls for **FIRE**:
- `Enes193.mission(NUM_CANDLES, i)` i is an integer (0, 1, 2, 3, 4, 5)
- `Enes193.mission(TOPOGRAPHY, TOP_A)`
- `Enes193.mission(TOPOGRAPHY, TOP_B)`
- `Enes193.mission(TOPOGRAPHY, TOP_C)`

Valid calls for **WATER**:
- `Enes193.mission(DEPTH, i)` i is in mm
- `Enes193.mission(WATER_TYPE, FRESH_UNPOLLUTED)`
- `Enes193.mission(WATER_TYPE, FRESH_POLLUTED)`


