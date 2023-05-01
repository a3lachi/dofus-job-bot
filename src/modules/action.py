from ui_handler import UIHandler
import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config


class Action :
    
    def __init__(self):
        pass

    def do(self, ui_hanlder: UIHandler)-> bool :
        pass

class ClickOnCoords(Action) : 

    def __init__(self, coord_x: int, coord_y: int)->None :
        super().__init__()
        self.coord_x = coord_x
        self.coord_y = coord_y

    def do(self, ui_handler: UIHandler) -> bool :
        return ui_handler.click_on_pixel(self.coord_x, self.coord_y)
    
class MoveTopMapPosition(Action):
    
    def __init__(self, start: list, destination: list):
        self.start = start
        self.destination = destination
    
    def _get_direction(self) -> list:
        dx, dy = self.destination[0] - self.start[0], self.destionation[1] - self.start[1]
        direction = [abs(dx), abs(dy)].index(max(abs(dx), abs(dy)))
        monitor = self.ui_handler.monitor
        if direction==0:
            if dx==0:
                return []
            elif dx > 0:
                return config.RIGHT * monitor.width + monitor.x_offset
            else:
                return config.LEFT * monitor.width + monitor.x_offset
        else:
            if dy==0:
                return []
            elif dy > 0:
                return config.DOWN * monitor.height + monitor.y_offset
            else:
                return config.UP * monitor.height + monitor.y_offset
    
    def do(self, ui_handler: UIHandler):
        direction = self._get_direction()
        self.ui_handler.click_on_pixel(direction[0], direction[1])