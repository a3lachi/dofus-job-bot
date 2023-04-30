import platform
from modules.logs.logs import Logs

# Get os type 
OS = platform.system()
OS_MAC = 'Darwin'
OS_WINDOWS = 'Windows'

# Wheat map positions file path-------------------------------------------------------------------
RECOLTABLE_MAP_POSITIONS_FILE_PATH = lambda recoltable: f"../data/{recoltable}_map_positions.csv"

# "Dofosdb" api url for web scraping recoltable map positions.
DOFUSDB_API_URL =  "https://api.dofusdb.fr/recoltable"
RECOLTABLE_NAME = 'wheat'
WHEAT_API_ID = 289
NMAX_RESPONSES = 91

# Move from map position to another : You can only move RIGHT, LEFT, UP, DOWN.--------------------
RIGHT = (1103, 389)
LEFT = (194, 358)
DOWN = (650,680)
UP = (650, 30)

# Map position (width or height) percentage for box edges ----------------------------------------
P_MAP_LEFT = 0
P_MAP_TOP = 0
P_MAP_RIGHT = 0
P_MAP_BOTTOM = 0

# Near current pixel coordiantes -----------------------------------------------------------------
# Offset from current pixel coordinates
P_OFFSET_HEIGHT = 0
P_OFFSET_WIDTH = 0
OFFSET_WIDTH = lambda width: width * P_OFFSET_WIDTH
OFFSET_HEIGHT = lambda height: height * P_OFFSET_HEIGHT
# Percentage for box edges
P_MOUSE_LEFT = 0
P_MOUSE_TOP = 0
P_MOUSE_RIGHT = 0
P_MOUSE_BOTTOM = 0
# Box minimal (width, height) 
P_MOUSE_MIN_HEIGHT = 50
P_MOUSE_MAX_HEIGHT = 50 

# Game Usable ground box cooridnates -------------------------------------------------------------
# Percentage for box edges
P_GROUND_LEFT = 0
P_GROUND_TOP = 0
P_GROUND_RIGHT = 0
P_GROUND_BOTTOM =0

# Logs object instance
LOGS = Logs()
