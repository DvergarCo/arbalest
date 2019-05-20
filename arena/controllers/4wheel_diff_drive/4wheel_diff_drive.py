"""4wheel_diff_drive controller."""

from robotUprising import invaderBot

from websocket import create_connection
import time

bot = invaderBot()
bot.setup()

connected = False
while(connected == False):
    time.sleep(0.25)
    try:
        ws = create_connection("ws://localhost:9000")
        connected = True
    except:
        connected = False
        
while bot.doTimeStep():
    
    message = ws.recv()
    (left, right) = message.split("|")
    left = float(left)
    right = float(right)
    left *= 10
    right *= 10
    bot.setMotors(left, right)

print("Closing...")
ws.close()
    
