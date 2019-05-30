"""4wheel_diff_drive controller."""

from robotUprising import invaderBot
import math

bot = invaderBot()

kb = bot.robot.getKeyboard()
kb.enable(bot.timestep)


while bot.doTimeStep():
    """current_key = kb.getKey()
    
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
        
    print bot.getPosition()
    print bot.getGoals()
    """
    
    goals = bot.getGoals()
    
    if len(goals) != 0:
        goal = goals[len(goals)-1]
        pos = bot.getPosition()
        
        dx = goal[0] - pos[0] # difference in x
        dz = goal[1] - pos[1] # difference in y
        
        da = math.degrees(math.atan2(dz, dx)) # difference in angle
        
        ra = pos[2] - da # relative angle between robot orientation and the goal
        
        if ra > 180:
            ra -= 360
        if ra < -180:
            ra += 360
        """
        turn the face towards the goal; about 10 degrees of precision is sufficient. Then march!
        """
        if ra > 10:
            bot.setMotors(10, -10)
        elif ra < -10:
            bot.setMotors(-10, 10)
        else:
            bot.setMotors(10,10)
    else:
        bot.setMotors(0,0) # stop when all the goals are hit!

print("Closing...")
