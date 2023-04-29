class MapCoordinator:
    """
    A class that handles actions for the player to move from map (x1, y1) to map (x2, y2)

    """
    def __init__(self):
        pass
    
    def go_to(self, destination_map_position: list) -> None:
        pass
    

'''


def go_to(coord1, coord2):
    direction = get_direction(coord1, coord2, [], None)
    screenshots = [get_mapshot()]
    pretty = {UP: 'UP', DOWN: 'DOWN', RIGHT:'RIGHT', LEFT: 'LEFT'}
    not_include = []
    while(direction!='FINAL'):  
        print('----------------------')
        move_to(direction)
        pyautogui.click()
        wait_human_like()  
        move_to((400, 400))
        screenshots.append(get_mapshot())
        hasMo = has_moved(screenshots)
        if not hasMo:
            # Retry
            wait_human_like()
            screenshots.append(get_mapshot())
            hasMo = has_moved(screenshots)
        if hasMo:
            not_include = [] 
            coord1 = where_am_I(coord1, direction)
        else:
            not_include.append(direction)
        direction  = get_direction(coord1, coord2, not_include, direction)
        print(coord1)
    
  
def orthogonal(res):
    return {LEFT: UP, UP: RIGHT, RIGHT: DOWN, DOWN: LEFT}[res]

def get_direction(coord1, coord2, not_include, old_direction):
    dx, dy = coord2[0] - coord1[0], coord2[1] - coord1[1]
    direction = [abs(dx), abs(dy)].index(max(abs(dx), abs(dy)))

    if len(not_include)==1:
        res = orthogonal(old_direction)
    elif len(not_include)!=0:
        res = random.choice(list(set([UP, DOWN, LEFT, RIGHT]).difference(not_include)))
    else:
        if direction==0:
            if dx==0:
                res =  'FINAL'
            elif dx > 0:
                res = RIGHT
            else:
                res = LEFT
        else:
            if dy==0:
                res = 'FINAL'
            elif dy > 0:
                res = DOWN
            else:
                res = UP
    inverse = {DOWN:UP, UP:DOWN, RIGHT:LEFT, LEFT:RIGHT}
    if old_direction != None and res == inverse[old_direction]:
        return random.choice(list(set([UP, DOWN, LEFT, RIGHT]).difference([res])))
    
    return res

'''