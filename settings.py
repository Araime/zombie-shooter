import pygame as pg

vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Radar settings
RADAR_WIDTH = 150
RADAR_HEIGHT = 90
PLAYER_BLIP_RADIUS = 3
MOB_BLIP_RADIUS = 2
RADAR_COLOR = LIGHTGREY

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 700,
                     'bullet_lifetime': 900,
                     'rate': 300,
                     'kickback': 0,
                     'spread': 3,
                     'damage': 16,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 600,
                      'bullet_lifetime': 500,
                      'rate': 1000,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 7,
                      'bullet_size': 'sm',
                      'bullet_count': 15}

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [170, 160, 150, 135]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 30
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png']
SPLAT = 'splat green.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 30
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
TITLE_MUSIC = 'Dark_Intro.ogg'
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
