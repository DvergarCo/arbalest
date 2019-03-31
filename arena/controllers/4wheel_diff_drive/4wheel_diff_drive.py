"""4wheel_diff_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Robot

#from bluetooth import *

def setup_bluetooth():
    try:
        server_sock=BluetoothSocket( RFCOMM )
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        print("Waiting for connection on RFCOMM channel %d" % port)

        cli_sck, client_info = server_sock.accept()
        print("Accepted connection from ", client_info)
        cli_sck.setblocking(0)

        return cli_sck
    except NameError:
        # Bluetooth module not loaded.
        return None

def setup_motors(robot, motor_names):
    return [robot.getMotor(motor_name) for motor_name in motor_names]    
    
def setMotors(inp, motors):
    mult = 1 if inp > 0 else -1
    for motor in motors:
        motor.setPosition(mult*float('+inf'))
        motor.setVelocity(inp)

def remoteFunc(cli_sck, l_motors, r_motors):
    try:
        data = cli_sck.recv(1024)
        if len(data) == 0: pass
#       print("received [%s]" % data)
        if data[0] == 'w':
            setMotors(10, r_motors)
        if data[0] == 's':
            setMotors(-10, r_motors)
        if data[0] == '0':
            setMotors(0, r_motors)
            
        if data[0] == 'u':
            setMotors(10, l_motors)
        if data[0] == 'j':
            setMotors(-10, l_motors)
        if data[0] == 'o':
            setMotors(0, l_motors)
    except IOError:
        pass

def keyboard_controls(keyboard, motors, keys_speeds):
    """Keyboard controls for the robot.
    
    Params:
    keyboard (Keyboard) -- A Webots keyboard instance.
    motors (tuple) -- tuple containing all available motors.
    keys_speeds (dict) -- keyboard_key (str) -> (speed per motor).
    """
    current_key = keyboard.getKey()
    if current_key == -1:
        setMotors(0, motors)
        return
    for kb_key, speeds in keys_speeds.items():
        if (current_key == ord(kb_key)):
            for i, speed in enumerate(speeds):
                setMotors(speed, [motors[i]])
            break

if __name__ == "__main__":
    cli_sck = setup_bluetooth()
    
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    keyboard = robot.getKeyboard()
    keyboard.enable(timestep)
    (m_fl, m_fr, m_rl, m_rr) = setup_motors(robot, ["front_left", "front_right", "rear_left", "rear_right"])
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()

        # Process sensor data here.

        #remoteFunc(cli_sck, (m_fl, m_rl), (m_fr, m_rr))
        keyboard_controls(keyboard, (m_fl, m_rl, m_fr, m_rr),
                          {"W": (10, 10, 10, 10),
                           "S": (-10, -10, -10, -10), 
                           "A": (10, 10, -10, -10),
                           "D": (-10, -10, 10, 10)})

        # Enter here functions to send actuator commands, like:
        #  led.set(1)
    print("Closing...")
    # Enter here exit cleanup code.
