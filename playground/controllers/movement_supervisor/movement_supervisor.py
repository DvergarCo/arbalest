"""movement_supervisor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Supervisor

# create the Robot instance.
sv = Supervisor()

# get the time step of the current world.
timestep = int(sv.getBasicTimeStep())

subject = sv.getFromDef("kedi"); # note that kedi is the DEF value, not name!
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while sv.step(timestep) != -1:
    position=subject.getPosition()
    print(position)


# Enter here exit cleanup code.
