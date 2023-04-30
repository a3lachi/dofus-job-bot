import numpy as np
import pyautogui
from monitor import Monitor
from ocr import OCR
import config
import time
import pandas as pd

class RecoltableScanner:
    
    def __init__(self):
        pass
    
    def init_grid_search(self, monitor: Monitor):
        
        # Define the x and y ranges
        x = range(config.P_GROUND_LEFT * monitor.width + monitor.x_offset, 
                  config.P_GROUND_RIGHT * monitor.width + monitor.x_offset, 
                  config.P_SCAN_X_SKIP)
        
        y = range(config.P_GROUND_TOP * monitor.height + monitor.y_offset, 
                  config.P_GROUND_BOTTOM * monitor.height + monitor.y_offset, 
                  config.P_SCAN_Y_SKIP)
        
        # Create the grid using meshgrid
        self.X, self.Y = np.meshgrid(x, y)
        
    
    def scan_grid(self, grid: list, monitor: Monitor, ocr: OCR, recolt: bool) -> pd.DataFrame:
        x_coords = []
        y_coords = []
        recoltable_names = []
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                a = i 
                b = (j if i%2==0 else len(self.X[0])- j - 1) 
                x, y = self.X[a, b], self.Y[a, b]
                monitor.move_cursor(x, y)
                time.sleep(0.3)
                black_box = monitor.get_box_near_cursor_position()
                text = ocr.recognize_text(black_box, config.ALPHABET_CHARS)
                if type(black_box) != np.ndarray:
                    black_box.close()
                for name in config.RECOLTABLE_NAMES:
                    if name in text:
                        x_coords.append(x)
                        y_coords.append(y)
                        recoltable_names.append(name)
                    if config.STR_RECOLTABLE_AVAILABLE in text or config.STR_RECOLTABLE_UNAVAILABLE not in text:
                        if recolt:
                            monitor.click_on_mouse()
                            time.sleep(3)
        df = pd.DataFrame({'name': recoltable_names, 'x': x_coords, 'y': y_coords})
        return df
        
