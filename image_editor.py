
import pyttsx3
import pyperclip
import numpy as np
import cv2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
from rembg import remove
from PIL import Image
from PIL import Image, ImageOps
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
root = Tk()
root.title("Photo Editor")
root.geometry("950x640")
photo = PhotoImage(file="edit-image.png")
root.iconphoto(False, photo)


deg = 45
img_path = 'ganpati.jpg'
img = Image.open(img_path)
img.thumbnail((350, 350))
img5 = ImageTk.PhotoImage(img)
height = 300
width = 210
border_w = 25


def select():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1


def blur(event):
    global img_path, img1, imgg, img, img5
    for m in range(0, v1.get()+1):

        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1
    img = imgg


def brightness(event):
    global img_path, img2, img3, img, img5
    for m in range(0, v2.get()+1):
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 210, image=img3)
        canvas2.image = img3
    img = img2


def removebg():
    global img_path, img1, imgg, img, img5

    imgg = remove(img)
    img1 = ImageTk.PhotoImage(imgg)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1
    img = imgg


def imgtotxt():
    txt = image_to_string(Image.open(img_path))
    pyperclip.copy(txt)
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()


def imgtospeech():
    txt = image_to_string(Image.open(img_path))
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()


def flip_up():
    global img_path, img1, imgg, img, img5

    converted_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img5 = ImageTk.PhotoImage(converted_img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = converted_img


def rotate():
    global img_path, img1, imgg, deg, img, img5
    rotated_img = img.rotate(deg+45)
    img5 = ImageTk.PhotoImage(rotated_img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    deg = deg+45
    img = rotated_img


def sharpen():
    global img_path, img1, imgg, deg, img, img5
    sharp_img = img.filter(ImageFilter.SHARPEN)
    img5 = ImageTk.PhotoImage(sharp_img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = sharp_img


def resize_big():
    global img_path, img1, imgg, deg, img, img5, height, width
    im = img.resize((height, width))
    img = im
    canvas2.delete('all')
    img5 = ImageTk.PhotoImage(image=im)
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    height = height+50
    width = width+50


def resize_small():
    global img_path, img1, imgg, deg, img, img5, height, width
    im = img.resize((height, width))
    img = im
    canvas2.delete('all')
    img5 = ImageTk.PhotoImage(image=im)
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    height = height-50
    width = width-50


def edge():
    global img_path, img1, imgg, deg, img, img5
    img_gray_smooth = img.filter(ImageFilter.SMOOTH)
    edges_smooth = img.filter(ImageFilter.FIND_EDGES)
    img5 = ImageTk.PhotoImage(edges_smooth)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = edges_smooth


def frame():
    global img_path, img1, imgg, deg, img, img5, border_w
    img = ImageOps.expand(img, border=border_w, fill="#f00")
    img5 = ImageTk.PhotoImage(img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = img
    border_w = border_w+25
    # ImageOps.expand(img, border=border_w,fill="#f00")


def gray():
    global img_path, img1, imgg, deg, img, img5
    gray_img = img.convert("L")
    img5 = ImageTk.PhotoImage(gray_img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = gray_img


def cartoonify():
    global img_path, img1, imgg, deg, img, img5
    img = np.array(img.convert('RGB'))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    im = Image.fromarray(cartoon)
    img = im
    img5 = ImageTk.PhotoImage(image=im)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5


def smooth():
    global img_path, img1, imgg, deg, img, img5
    smooth_img = img.filter(ImageFilter.SMOOTH)
    img5 = ImageTk.PhotoImage(smooth_img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5
    img = smooth_img


def contrast(event):
    global img_path, img4, img5, img
    for m in range(0, v3.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 210, image=img5)
        canvas2.image = img5
        img = img4


def reset():
    global img
    img = Image.open(img_path)
    img1 = img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.delete('all')
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1


def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[(
        "All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        img.save(file)


blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1,
                   orient=HORIZONTAL, command=blur)
scale1.place(x=150, y=10)
bright = Label(root, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2,
                   orient=HORIZONTAL, command=brightness)
scale2.place(x=150, y=55)
contrast = Label(root, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=92)
v3 = IntVar()
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3,
                   orient=HORIZONTAL, command=contrast)
scale3.place(x=150, y=100)
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)
btn1 = Button(root, text="Select Image", bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=select)
btn1.place(x=100, y=595)
btn2 = Button(root, text="Save", width=12, bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)
btn3 = Button(root, text="Exit", width=12, bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=460, y=595)
btn4 = Button(root, text="Remove Background", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=removebg)
btn4.place(x=280, y=50)
btn5 = Button(root, text="copy text from image", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=imgtotxt)
btn5.place(x=650, y=428)
btn6 = Button(root, text="Flip Upside", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=flip_up)
btn6.place(x=650, y=476)
btn7 = Button(root, text="Rotate 45 degrees", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=rotate)
btn7.place(x=650, y=92)
btn8 = Button(root, text="Sharpen Image", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=sharpen)
btn8.place(x=650, y=50)
btn9 = Button(root, text="Smooth Image", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=smooth)
btn9.place(x=650, y=8)
btn9 = Button(root, text="edge of Image", width=19, bg='#E5E5CB', fg='black',
              font=('ariel 17 bold'), relief=GROOVE, command=edge)
btn9.place(x=650, y=140)
btn10 = Button(root, text="B&W image", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=gray)
btn10.place(x=650, y=188)
btn11 = Button(root, text="Cartoonify", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=cartoonify)
btn11.place(x=650, y=236)
btn12 = Button(root, text="Read text of the image", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=imgtospeech)
btn12.place(x=650, y=284)
btn13 = Button(root, text="Increase size", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=resize_big)
btn13.place(x=650, y=332)
btn14 = Button(root, text="Decrease size", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=resize_small)
btn14.place(x=650, y=380)
btn15 = Button(root, text="Add frame", width=19, bg='#E5E5CB', fg='black',
               font=('ariel 17 bold'), relief=GROOVE, command=frame)
btn15.place(x=650, y=524)
btn3 = Button(root, text="Reset", width=12, bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=reset)
btn3.place(x=650, y=595)
root.mainloop()
