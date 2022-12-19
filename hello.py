import customtkinter as ct
from tkinter import filedialog 
from tkinter import dnd 
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import numpy as np
from googletrans import Translator
import googletrans
import cv2
from tkinter import Tk, Toplevel
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'
def get_key(val):
    for key, value in lang.items():
        if val == value:
            return key
    else:
        print("key doesn't exist")
lang = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 
'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 
'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
avallang = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 
            'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']
out = list(map(lambda x:x.title(), avallang))
# def select_pic():
#     filename = "ph4.jpg"
#     img1 = np.array(Image.open(filename))
#     tex = pytesseract.image_to_string(img1)
#     print(tex)
    # tr = input("Do you want to translate(YES/NO): ").lower()
    # if tr == "yes":
    #     print()
    #     print()
    #     z = input("Input the desired language to translate: ").lower()
    #     a = get_key(z)
    #     translator = Translator()
    #     tran = translator.translate(tex, dest = z)
    #     a = tran.text
    #     print()
    #     print(a)
    #     # print(googletrans.LANGUAGES)
    # else:
    #     pass
def take_pic():
    vid = cv2.VideoCapture(0)
    while(True):
        
        # Capture the video frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # To capture image with key "c"
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

 
win = ct.CTk() 
win.geometry("900x600") 
win.title("Project OCR") 
win.maxsize(width=900,height=600) 
 
ct.set_appearance_mode("dark") 
ct.set_default_color_theme("blue") 
 
def browse(): 
        win.filename = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes = (("jpg file", "*.jpg"), ("jpeg file", "*.jpeg"), ("png file", "*.png"))) 
        if win.filename == "": 
                pass 
        else: 
    
            filename = win.filename
            img1 = np.array(Image.open(filename))
            tex = pytesseract.image_to_string(img1)
            global ext
            ext = tex
            top = ct.CTkToplevel(win) 
            top.geometry("1000x800") 
            top.config(pady=25, padx=25) 
            top.title("Extracted Text")
            top2 = ct.CTkLabel(master = top, text = ext).pack()

            def optionmenu_callback(choice):
                print("optionmenu dropdown clicked:", choice)
                z = choice.lower()
                a = get_key(z)
                translator = Translator()
                tran = translator.translate(tex, dest = a)
                final = tran.text
                
                top2 = ct.CTkLabel(master = top, text = final).pack()
                top2.configure(text="")
            combobox = ct.CTkOptionMenu(master=top,
                                        values= out,
                                       
                                       command=optionmenu_callback)
            combobox.pack(padx=20, pady=10)
            combobox.set("Translate")  # set initial
 
browse_btn = ct.CTkButton(master=win,text="🔍 Browse",command=browse,font=('Calibri',24)).place(x=485,y=315) 

 
drop_files_here_btn = ct.CTkLabel(master=win,text="Drop Your Files Here",font=('Calibri',42,"bold")).place(x=285,y=185) 


def capture_img():
    top3 = Toplevel()
    top3.title("Second window")
    top3.geometry("1200x1000")
    top3.config(bg="black")
    #top3.maxsize(width=400,height=500)    # By default, it is kept as the geometry of the main window, but you can change it.
    canva = Canvas(top3,width=800,height=400,bg='white',highlightthickness=0).pack()
    img_1 = PhotoImage(file="ph4.jpg")
    canva.create_image(200,400,image=img_1)


capture_btn = ct.CTkButton(master=win,text="Capture 📷",command=capture_img,font=('Calirbri',24,"bold")).place(x=292,y=315)
    

 
 
 
 
 
 
 
win.mainloop()
 
 
 
 
 
 
 
