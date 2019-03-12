"""4wheel_diff_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  led = robot.getLED('ledname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

m_fl = robot.getMotor('front_left')
m_fr = robot.getMotor('front_right')
m_rl = robot.getMotor('rear_left')
m_rr = robot.getMotor('rear_right')
print(dir(robot))
print(dir(m_fl))

m_fl.setPosition(9999999) # there must be a better way!
m_rl.setPosition(9999999)
m_fl.setVelocity(10)
m_rl.setVelocity(10)

m_fr.setPosition(9999999)
m_rr.setPosition(9999999)
m_fr.setVelocity(5)
m_rr.setVelocity(5)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  led.set(1)
    pass

# Enter here exit cleanup code.
