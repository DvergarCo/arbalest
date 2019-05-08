"""Wrapper for the Webots controls.

Using this will make it easier to run the same code on a Pi later.
"""

from controller import Robot

class RobotWrapper():
    """Wrapper for Webots."""

    def __init__(self):
        self.robot = Robot()

    def getBasicTimeStep(self):
        return self.robot.getBasicTimeStep()

    def getKeyboard(self):
        return self.robot.getKeyboard()

    def step(timestep):
        return self.robot.step(timestep)

    def getMotor(motorname):
        return self.robot.getMotor(motorname)

def get_robot():
    return Robot()