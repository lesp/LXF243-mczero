"""
Minecraft for kids aka Minecraft Zero
Les Pounder
"""

def connect():
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    chat("Connected")

def chat(msg):
    mc.postToChat(str(msg))

def get_position():
    x, y, z = mc.player.getPos()
    print(x,y,z)

def teleport(x,y,z):
    mc.player.setPos(x, y, z)

def drop(height):
    get_position()
    mc.player.setPos(x, height, z)
    
def setblock(blocktype):
    from mcpi import block
    get_position()
    mc.setBlock(x, y, z, blocktype)

def cube(size,blocktype)
    from mcpi import block
    get_position()
    mc.setBlock(x+1, y+1, z+1, x+size, y+size, z+size, blocktype)
    
def tnt_trail():
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, 46,1)
    sleep(0.1)

def tnt_cube(size)
    from mcpi import block
    get_position()
    mc.setBlock(x+1, y+1, z+1, x+size, y+size, z+size, 46,1)
