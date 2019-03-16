"""4wheel_diff_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Robot

from bluetooth import *


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

print("Waiting for connection on RFCOMM channel %d" % port)

cli_sck, client_info = server_sock.accept()
print("Accepted connection from ", client_info)
cli_sck.setblocking(0)

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

def setLeft(inp):
    if inp>0:
        m_fl.setPosition(float('+inf')) # there must be a better way!
        m_rl.setPosition(float('+inf'))
    else:
        m_fl.setPosition(-float('+inf')) # there must be a better way!
        m_rl.setPosition(-float('+inf'))
    
    m_fl.setVelocity(inp)
    m_rl.setVelocity(inp)
    
def setRight(inp):
    if inp>0:
        m_fr.setPosition(float('+inf')) # there must be a better way!
        m_rr.setPosition(float('+inf'))
    else:
        m_fr.setPosition(-float('+inf')) # there must be a better way!
        m_rr.setPosition(-float('+inf'))
    
    m_fr.setVelocity(inp)
    m_rr.setVelocity(inp)


def remoteFunc():
    try:
        data = cli_sck.recv(1024)
        if len(data) == 0: pass
#        print("received [%s]" % data)
        if data[0] == 'w':
            setRight(10)
        if data[0] == 's':
            setRight(-10)
        if data[0] == '0':
            setRight(0)
            
        if data[0] == 'u':
            setLeft(10)
        if data[0] == 'j':
            setLeft(-10)
        if data[0] == 'o':
            setLeft(0)
            
        
    except IOError:
        pass


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    remoteFunc()
    # Enter here functions to send actuator commands, like:
    #  led.set(1)
    pass

# Enter here exit cleanup code.
