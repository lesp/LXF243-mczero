"""
Minecraft for kids aka Minecraft Zero
Les Pounder
"""
try:
    from mcpi import minecraft
    from mcpi import block
    from time import sleep
    mc = minecraft.Minecraft.create()
    print("Connected to world")
except:
    print("Connection Error, is Minecraft running?")

def chat(msg):
    mc.postToChat(str(msg))

def teleport(x,y,z):
    mc.player.setPos(x, y, z)

def drop(height):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y+height, z)
    
def setblock(blocktype):
    x, y, z = mc.player.getPos()
    print(x,y,z)
    mc.setBlock(x, y, z, blocktype)

def cube(size,blocktype):
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+size, y+size, z+size, blocktype)
    
def tnt_trail():
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, 46,1)
    sleep(0.1)

def tnt_cube(size):
    x, y, z = mc.player.getPos()
    tnt = 46
    mc.setBlocks(x+1, y+1, z+1, x+size, y+size, z+size, tnt ,1)

def pyramid(size):
    x, y, z = mc.player.getPos()
    for i in range(size):
        mc.setBlocks(x+1, y+1, z+1, x+i, y+size, z+i, 41, 1)

def slab(size):
    x, y, z = mc.player.getPos()
    for i in range(size,0,-1):
        mc.setBlocks(x+1, y+1, z+1, x+i, y+1, z+i, 41, 1)   
