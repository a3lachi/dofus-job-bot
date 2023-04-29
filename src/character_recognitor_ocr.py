from PIL import Image

class OCR:
    """
    A class that applies character recognition on an image and gets information. examples: [player position, wheat availability, ...]
    
    """
    def __init__(self):
        self.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        pass
    
    def recognize_text(self):
        pass
    
    def extract_position_coordinates(self, screenshot: Image):
        pass
    
    def extract_text_box(self, screenshot: Image):
        pass
    
    
     
        
'''
def get_text_box(img):
    if img.shape[0]  < 50 or img.shape[1] < 50:
        return ''
    else:
        # Read the image and convert it to grayscale
        custom_config = f'--psm 6 -c tessedit_char_whitelist={self.ascii_lowercase}{self.ascii_uppercase}'
        # Perform OCR on the image
        text = pytesseract.image_to_string(img, config=custom_config)
        return text

def get_current_coordinates():
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'  
    time.sleep(2)
    url = 'images/img.png'
    screenshot = get_mapshot()
    # Convert the PIL image to a numpy array
    pil_image = np.array(screenshot)
    # Convert the numpy array to a cv2 image
    img = cv2.cvtColor(pil_image, cv2.COLOR_RGB2BGR)
    custom_config = '--psm 6 -c tessedit_char_whitelist=-,0123456789'
    # Perform OCR on the image
    text = pytesseract.image_to_string(img, config=custom_config)
    ntext = ''
    for i, t in enumerate(text):
        if i!=0 and t=='-':
            if text[i-1] != ',':
                ntext += ','
        ntext += t
    text = ntext
    if len(text.split(','))>2:
        text = ','.join(text.split(',')[:2])
    # Print the text
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.strip(', \n'+ascii_lowercase+ascii_uppercase)
    x, y = text.split(',')
    start = [int(x), int(y)]
    return start
'''