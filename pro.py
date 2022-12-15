from PIL import Image, ImageDraw, ImageFont
import pytesseract
import numpy as np
from googletrans import Translator
import googletrans
import cv2
pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'
def get_key(val):
    for key, value in lang.items():
        if val == value:
            return key
 
    return "key doesn't exist"
lang = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 
'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 
'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
def select_img():
    filename = "ph4.jpg"
    img1 = np.array(Image.open(filename))
    tex = pytesseract.image_to_string(img1)
    print(tex)
    tr = input("Do you want to translate(YES/NO): ").lower()
    if tr == "yes":
        print()
        print()
        z = input("Input the desired language to translate: ").lower()
        a = get_key(z)
        translator = Translator()
        tran = translator.translate(tex, dest = z)
        a = tran.text
        print()
        print(a)
        # print(googletrans.LANGUAGES)
    else:
        pass
def take_pic():
    vid = cv2.VideoCapture(0)
    while(True):
        
        # Capture the video frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord("c"):
            cv2.imwrite("frame.png", frame)
            img2 = Image.open("frame.png")
            break
        # the 'x' button is set as the quitting button
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
    tr = input("Do you want to translate(YES/NO): ").lower()
    if tr == "yes":
        print()
        print()
        z = input("Input the desired language to translate: ").lower()
        a = get_key(z)
        translator = Translator()
        tran = translator.translate(tex, dest = z)
        a = tran.text
        print()
        print(a)
    else:
        pass

select_img()
