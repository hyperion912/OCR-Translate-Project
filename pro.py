from PIL import Image, ImageDraw, ImageFont
import pytesseract
import numpy as np
from googletrans import Translator
import googletrans
pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'
filename = "ph4.jpg"
img1 = np.array(Image.open(filename))
tex = pytesseract.image_to_string(img1)
print(tex)
print()
print()
translator = Translator()
tran = translator.translate(tex, dest = "fr")
a = tran.text
print(a)
# print(googletrans.LANGUAGES)
