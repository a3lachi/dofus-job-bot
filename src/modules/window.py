from PIL import Image
import config
import subprocess
import pyautogui

class Window :
    """ 
      A class for the window object
    
    """
    def __init__(self, _id: int, name: str, window) -> None:
      self.id = _id
      self.name = name
      self.window = window

    def focus(self) -> bool :
      pass
  
    def maximize(self) -> bool :
      pass

class WindowMac(Window) :
  
    def __init__(self, _id: int, name: str, window) -> None:
        super().__init__(id, name, window)

    def focus(self) -> bool :
        try :
            return (subprocess.run(['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is '+self.pid+') to true'], check=True).returncode != 0)    
        except : 
            return False
    
    def maximize(self) -> bool:
        pass
    
class WindowWindows(Window) :
  def __init__(self, _id: int, name: str, window: pyautogui.window):
    super().__init__(_id, name, window)
    self.width = window.width
    self.height = window.height

  def focus(self) -> bool :
    return self.window.activate()
  
  def maximize(self) -> bool :
    return self.window.maximize()
