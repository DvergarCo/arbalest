"""4wheel_diff_drive controller."""

from robotUprising import invaderBot

bot = invaderBot()

kb = bot.robot.getKeyboard()
kb.enable(bot.timestep)

while bot.doTimeStep():
    current_key = kb.getKey()
    
    if current_key == -1:
        bot.setMotors(0, 0)
    if current_key == ord('W'):
        bot.setMotors(10,10)
    if current_key == ord('S'):
        bot.setMotors(-10,-10)
    if current_key == ord('A'):
        bot.setMotors(10,-10)
    if current_key == ord('D'):
        bot.setMotors(-10,10)

print("Closing...")
