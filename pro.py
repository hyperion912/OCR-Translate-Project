from PIL import Image, ImageDraw, ImageFont
import pytesseract
import numpy as np
from googletrans import Translator
import googletrans
import cv2
pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'
def select_img():
    filename = "ph4.jpg"
    img1 = np.array(Image.open(filename))
    tex = pytesseract.image_to_string(img1)
    print(tex)
    print()
    print()
    translator = Translator()
    tran = translator.translate(tex, dest = "hi")
    a = tran.text
    print(a)
    # print(googletrans.LANGUAGES)
def take_pic():
    vid = cv2.VideoCapture(0)
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord("c"):
            cv2.imwrite("frame.png", frame)
            img2 = Image.open("frame.png")
            # img2.show()
            break
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    filename = "frame.png"
    img3 = np.array(Image.open(filename))
    tex = pytesseract.image_to_string(img3)
    print(tex)
    print()
    print()
    translator = Translator()
    tran = translator.translate(tex, dest = "fr")
    a = tran.text
    print(a)

take_pic()
