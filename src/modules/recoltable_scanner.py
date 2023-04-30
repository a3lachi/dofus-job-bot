import numpy as np
from monitor import Monitor
from ocr import OCR

class RecoltableScanner:
    
    def __init__(self):
        pass
    
    def init_grid_search(self, monitor: Monitor):
        screenshot = monitor.get_clickable_game_zone()
        shape = np.array(screenshot).shape
        # Define the x and y ranges
        x = range(30, shape[1], 40)
        y = range(30, shape[0], 40)
        # Create the grid using meshgrid
        self.X, self.Y = np.meshgrid(x, y)
        
    
    def scan_grid(grid: list, monitor: Monitor, ocr: OCR, recolt: bool) -> list:
        coords = []
        for i in range(len(X)):
            for j in range(len(X[0])):
                a = i 
                b = (j if i%2==0 else len(X[0])- j - 1) 
                x, y = X[a, b]+ init[0], Y[a, b]+init[1]
                pyautogui.moveTo((x, y))
                time.sleep(0.3)
              
                black_box = get_crop_box()
                text = get_text_box(black_box).lower()
                if type(black_box)!= np.ndarray:
                    black_box.close()
                if 'ble' in text or 'bie' in text:
                    coords.append([x, y])
                    if 'fauch' in text or 'puis' not in text:
                        pyautogui.click(button='left')
                        time.sleep(4)
