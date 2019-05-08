"""4wheel_diff_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Robot
from threading import Thread
from websocket import create_connection

import sys
import threading
import time
import math


def setup_motors(robot, motor_names):
    return [robot.getMotor(motor_name) for motor_name in motor_names]


def setMotors(inp, motors):
    mult = 1 if inp > 0 else -1
    for motor in motors:
        motor.setPosition(mult*float('+inf'))
        motor.setVelocity(inp)


def setAllMotors(speeds):
    global m_fl, m_fr, m_rl, m_rr
    motors = (m_fl, m_rl, m_fr, m_rr)
    for i, speed in enumerate(speeds):
        setMotors(speed, [motors[i]])


def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))


if __name__ == "__main__":
    global m_fl, m_fr, m_rl, m_rr

    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    (m_fl, m_fr, m_rl, m_rr) = setup_motors(
        robot, ["front_left", "front_right", "rear_left", "rear_right"])

    # Hack way to connect to the server safely
    connected = False
    while(connected == False):
        time.sleep(0.25)
        try:
            ws = create_connection("ws://localhost:9000")
            connected = True
        except:
            connected = False

    ws.send("NEW ROBOT")

    while robot.step(timestep) != -1:

        message = ws.recv()
        (left, right) = message.split("|")
        left = float(left)
        right = float(right)
        left *= 10
        right *= 10
        setAllMotors((left, left, right, right))

    print("Closing...")
    ws.close()
    # Enter here exit cleanup code.
