"""4wheel_diff_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Robot
from websocket_server import WebsocketServer
from threading import Thread

PORTBASE = 9000

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	global lastMsg
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))

def setupWebsockets(port):
    try:
        print("Trying a websocket on port %d..." %port)
        server = WebsocketServer(port)
        server.set_fn_new_client(new_client)
        server.set_fn_client_left(client_left)
        server.set_fn_message_received(message_received)
        t = Thread(target=server.run_forever, args=())
        t.start()
        
        print("Success!")
        return True
    except:
        return False

def setup_motors(robot, motor_names):
    return [robot.getMotor(motor_name) for motor_name in motor_names]    
    
def setMotors(inp, motors):
    mult = 1 if inp > 0 else -1
    for motor in motors:
        motor.setPosition(mult*float('+inf'))
        motor.setVelocity(inp)

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
    for x in range(10): # funny way to find the first available port :)
        if (setupWebsockets(PORTBASE + x)):
            break
    
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

        keyboard_controls(keyboard, (m_fl, m_rl, m_fr, m_rr),
                          {"W": (10, 10, 10, 10),
                           "S": (-10, -10, -10, -10), 
                           "A": (10, 10, -10, -10),
                           "D": (-10, -10, 10, 10)})

        
        # Enter here functions to send actuator commands, like:
        #  led.set(1)
    print("Closing...")
    # Enter here exit cleanup code.
