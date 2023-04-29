
import screeninfo

class ScreenshotHandler:
    """
    A class that serves to take a screenshot of a defined box or through globally defined boxes (such as recoltable text box)
    
    """
    def __init__(self, screen_id: int):
        screen = screeninfo.get_monitors()[screen_id]
        self.width, self.height = screen.width, screen.height
    
    def get_box(self):
        pass
    
    def get_box_near_mouse_position(self):
        pass
    
    def get_game_screen(self):
        pass


'''
def get_mapshot(l_off=0.00368,t_off=0.07,w=0.05,h=0.038):
    # Get the current screen resolution
    screen = screeninfo.get_monitors()[0]
    width, height = screen.width, screen.height
    # Define the region of the screen to capture as a percentage of the screen size
    left = int(width * l_off) # 10% from the left
    top = int(height * t_off) # 10% from the top
    width = int(width * w) # 80% of the screen width
    height = int(height * h) # 80% of the screen height
    if top+height < top:     
        bbox = (left, top+height, left+width, top)
    else:
        bbox = (left, top, left+width, top+height)

    # Take a screenshot of the defined region
    img = ImageGrab.grab(bbox)

    # Save the screenshot to a file
    img.save("map_coords.png")
    return img

def get_crop_box():
    def scan_crop_box():
        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        pos = pyautogui.position()
        img = get_mapshot(l_off=pos[0]/width-0.012, t_off=pos[1]/height+0.04, w=0.15, h=-0.21)
        return img
    image = scan_crop_box()
    #image = Image.open(url)
    # Convert the PIL image to a numpy array
    image = np.array(image)
    #plt.imshow(image)
    # Convert the numpy array to a cv2 image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Define the lower and upper boundaries of the black color
    lower = np.array([0, 0, 0], dtype=np.uint8)
    upper = np.array([30, 30, 30], dtype=np.uint8)
    # Create a mask of the black pixels
    mask = cv2.inRange(image, lower, upper)
    # Find the contours of the black box
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    try:
        # Find the bounding box of the black box
        x, y, w, h = cv2.boundingRect(contours[0])
        # Extract the black box from the original image using the bounding box
        black_box = image[y:y+h, x:x+w]
    except:
        black_box=np.array([[]])
    #fig = plt.figure()
    #plt.imshow(black_box)
    return black_box

def screen_map():
    return get_mapshot(l_off=0.15,t_off=0.04,w=0.64 ,h=0.82)

'''