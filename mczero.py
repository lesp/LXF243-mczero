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
    print("For help with the block numbers, type blocks() into the Python shell")
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

def slab(l,w,blocktype):
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+w, y+1, z+l, blocktype)

def blocks():
    print("Here are all the blocks that can be used in Minecraft Pi, remember to use the numbers!")
    block_dictionary = {
        "AIR":0,
        "STONE":1,
        "GRASS":2,
        "DIRT":3,
        "COBBLESTONE":4,
        "WOOD_PLANKS":5,
        "SAPLING":6,
        "BEDROCK":7,
        "WATER_FLOWING":8,
        "WATER":8,
        "WATER_STATIONARY":9,
        "LAVA_FLOWING":10,
        "LAVA":10,
        "LAVA_STATIONARY":11,
        "SAND":12,
        "GRAVEL":13,
        "GOLD_ORE":14,
        "IRON_ORE":15,
        "COAL_ORE":16,
        "WOOD":17,
        "LEAVES":18,
        "GLASS":20,
        "LAPIS_LAZULI_ORE":21,
        "LAPIS_LAZULI_BLOCK":22,
        "SANDSTONE":24,
        "BED":26,
        "COBWEB":30,
        "GRASS_TALL":31,
        "WOOL":35,
        "FLOWER_YELLOW":37,
        "FLOWER_CYAN":38,
        "MUSHROOM_BROWN":39,
        "MUSHROOM_RED":40,
        "GOLD_BLOCK":41,
        "IRON_BLOCK":42,
        "STONE_SLAB_DOUBLE":43,
        "STONE_SLAB":44,
        "BRICK_BLOCK":45,
        "TNT":46,
        "BOOKSHELF":47,
        "MOSS_STONE":48,
        "OBSIDIAN":49,
        "TORCH":50,
        "FIRE":51,
        "STAIRS_WOOD":53,
        "CHEST":54,
        "DIAMOND_ORE":56,
        "DIAMOND_BLOCK":57,
        "CRAFTING_TABLE":58,
        "FARMLAND":60,
        "FURNACE_INACTIVE":61,
        "FURNACE_ACTIVE":62,
        "DOOR_WOOD":64,
        "LADDER":65,
        "STAIRS_COBBLESTONE":67,
        "DOOR_IRON":71,
        "REDSTONE_ORE":73,
        "SNOW":78,
        "ICE":79,
        "SNOW_BLOCK":80,
        "CACTUS":81,
        "CLAY":82,
        "SUGAR_CANE":83,
        "FENCE":85,
        "GLOWSTONE_BLOCK":89,
        "BEDROCK_INVISIBLE":95,
        "STONE_BRICK":98,
        "GLASS_PANE":102,
        "MELON":103,
        "FENCE_GATE":107,
        "GLOWING_OBSIDIAN":246,
        "NETHER_REACTOR_CORE":247
        }
    for key,val in block_dictionary.items():
        print(key,val)
        sleep(0.1)
