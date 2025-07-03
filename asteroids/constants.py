# TODO: Introduce game settings (global?) object that can be saved and loaded.

# 1280*720 resolution is recommended
SCREEN_WIDTH = 1280  # if 0: uses current monitor width
SCREEN_HEIGHT = 720  # if 0: uses current monitor height
FULLSCREEN = False

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.3  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3  # seconds

SHOT_RADIUS = 5
