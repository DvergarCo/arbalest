"""coin handler."""

from controller import Supervisor
import math

supervisor = Supervisor()

timestep = int(supervisor.getBasicTimeStep())

player = supervisor.getFromDef("kedi")

ACCEPT_DISTANCE = 0.5

coinRoot = supervisor.getFromDef("COINS").getField("children")


def make_coin(pos):
    coinRoot.importMFNode(0, "../../protos/coin.wbo")
    coin = coinRoot.getMFNode(0)
    translation = coin.getField("translation")
    translation.setSFVec3f(pos)
    

def update():
    coinRoot = supervisor.getFromDef("COINS").getField("children")
    
    
    count = coinRoot.getCount()
  
    
    if count == 0:
        supervisor.setLabel(1, "VICTORY", 0.35, 0.35, 0.2, 0xffffff, 0)
    
    
    supervisor.setLabel(0, "COINS LEFT: %d" %(count), 0.02, 0.02, 0.1, 0xffffff, 0)
    
 
    for idx in reversed(range(count)):
        coin = coinRoot.getMFNode(idx)
        
        pos = coin.getPosition()
        player_pos = player.getPosition()
        
        dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(pos, player_pos)]))
                
        if dist < ACCEPT_DISTANCE: 
           print("touch", idx)
           coinRoot.removeMF(idx)
           return
                
        # turn coinw
        rotationField = coin.getField("rotation")
        angle = rotationField.getSFRotation()
        angle[3] = angle[3] + 0.1 # TODO: Related to fps?
        rotationField.setSFRotation(angle)
        

make_coin([1.5,0,1.5])
make_coin([1.5,0,-1.5]) 
make_coin([-1.5,0,-1.5]) 

make_coin([0.5,0,0]) 
make_coin([-0.5,0,0]) 
make_coin([0,0,0.5])
make_coin([0,0,-0.5]) 
 




# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    update()

# Enter here exit cleanup code.
