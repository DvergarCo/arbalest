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

blueScore = 0
redScore = 0

def makeball(x, y):
    #root = robot.getRoot()
    root = robot.getFromDef("BALLS")
    root = root.getField("children")
    root.importMFNode(0, "../../protos/floorball.wbo")
    newball = root.getMFNode(0)
    pos = newball.getField("translation")
    pos.setSFVec3f([x,1,y])

def showScore():
    global redScore, blueScore
    robot.setLabel(0, "Red " + str(redScore) , 0, 0, 0.2, 0xff0000, 0)
    robot.setLabel(1, "Blue " + str(blueScore) , 0, 0.1, 0.2, 0x0000ff, 0)
    

def killball():
    global redScore, blueScore
    root = robot.getFromDef("BALLS")
    root = root.getField("children")
    
    ballCount = root.getCount()
    
    for ballidx in range(ballCount):
        ball = root.getMFNode(ballidx)
        pos = ball.getPosition()
        
        x = pos[0]
        y = pos[2]
        
        if x<-1.55 and y>1:
            blueScore += 1
            root.removeMF(ballidx)
            return
        
        if x>1 and y<-1.55:
            redScore += 1
            root.removeMF(ballidx)
            return

prevBallTime = 0

def ballmaker():
    global prevBallTime
    
    root = robot.getFromDef("BALLS")
    root = root.getField("children")
    
    ballCount = root.getCount()
    
    currentTime = robot.getTime()
    
    if currentTime-prevBallTime>10 and ballCount < 30:
        makeball(1.5, 1.2) # add how many you want!
        makeball(1.2, 1.5) # add how many you want!
        prevBallTime = currentTime

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    """if len(ballList) < 4:
        makeball()"""
    
    killball()
    showScore()
    ballmaker()
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  led.set(1)
    pass

# Enter here exit cleanup code.
