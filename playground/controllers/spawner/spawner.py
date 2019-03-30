"""spawner controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Supervisor

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  led = robot.getLED('ledname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)


def makeball():
    #root = robot.getRoot()
    root = robot.getFromDef("BALLS")
    root = root.getField("children")
    root.importMFNode(0, "../../protos/importable.wbo")
    newball = root.getMFNode(0)

def killball():
    root = robot.getFromDef("BALLS")
    root = root.getField("children")
    
    ballCount = root.getCount()
    
    for ballidx in range(ballCount):
        ball = root.getMFNode(ballidx)
        pos = ball.getPosition()
        
        x = pos[0]
        y = pos[2]
        
        
        if abs(x) > 1.5 and abs(y) > 1.5: # if the ball is near one of the corners
            root.removeMF(ballidx)
            makeball()
        

makeball() # add how many you want!


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    """if len(ballList) < 4:
        makeball()"""
    
    killball()
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  led.set(1)
    pass

# Enter here exit cleanup code.
