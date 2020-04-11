from tkinter import *
from tkinter.filedialog import askopenfile,askopenfilename,asksaveasfilename,asksaveasfile,askopenfilenames
from tkinter import messagebox as mb
from PIL import Image
import pytesseract
window=Tk(className="Image Manipulator")
window.configure(background='#ffbf00')
window.geometry("500x300")
window.resizable(False,False)

def km_to_miles():
    print(e1_value.get())
    print("Sucess!")
    t1.insert(END, e1_value.get())
def open_file():
    path=askopenfilename(filetype=[('Image Files',['*.jpg','*png'])])
    print(path)
    if len(path)>0:
        global img
        img=Image.open(path)
        print(img)
    else:
        mb.showerror(title="Error", message='Choose correct file location')
        #file=askopenfile(mode='r',filetype=[('Image Files','*jpg')])
        #if file is not None:
         #   photo=PhotoImage(file)
         #  print(cv2.imshow('shivam', photo))
         #   img = cv2.imread(photo)
         #   print(img)
def save_file_location():
    HP=e1.get()
    VP=e2.get()
    try:
        if (HP.isdigit()) and (VP.isdigit()) and (HP is not None) and (VP is not None):
            resized_img = img.resize((int(HP),int(VP)))
            window.filename = asksaveasfilename(title="select file",
                                                filetypes=[("JPEG file", "*.jpg"), ("PNG file", "*.png")],
                                                defaultextension=[("JPEG file", "*.jpg"), ("PNG file", "*.png")])
            print(window.filename)
            print(type(resized_img))
            if len(window.filename) > 0:
                resized_img.save(window.filename)
        else:
            mb.showerror(title="Error",message='Please enter numerical Values')

    except NameError:
        mb.showerror(title="Error", message='Select image file first')
def open_image_file():
    files=askopenfilenames(filetype=[('Image Files',['*.jpg','*png'])])
    print(files)
    global imagelist
    imagelist=[]
    count=1
    for file in files:
        if count==1:
            print(file)
            im = Image.open(file)
            global image1
            image1=im.convert('RGB')
            count=count+1
        else:
            print(file)
            image = Image.open(file)
            imagelist.append(image.convert('RGB'))
    print(imagelist)

def save_pdf_file():
    window.filename = asksaveasfilename(title="select file",
                                        filetypes=[("PDF", "*.pdf")],
                                        defaultextension=[("PDF file", "*.pdf")])
    image1.save(window.filename, append_images=imagelist, save_all=True)

def open_image_to_text():
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    path = askopenfilename(filetype=[('Image Files', ['*.jpg', '*png'])])
    print(path)
    if len(path) > 0:
        img = Image.open(path)
        global image_text
        image_text = pytesseract.image_to_string(img)
def save_image_to_text():
    try:
        if image_text is not None:
            window.filename = asksaveasfilename(title="select file",
                                                filetypes=[("TEXT ", "*.txt")],
                                                defaultextension=[("TEXT", "*.txt")])
            f = open(window.filename, 'w')
            f.write(image_text)
    except NameError:
        mb.showerror(title="Error", message='Select image file first')
b1=Button(window,text="Upload file to Resize",command=open_file)
b2=Button(window,text="Save Resized file",command=save_file_location)

#b1.pack() grid provide row and column to manage the button position .
b1.grid(row=3,column=2)
b2.grid(row=7,column=2)
l4=Label(text="Welcome",font='TimeRoman')
l4.grid(row=0,column=2)


l1=Label(text="Horizontal Pixel")
l1.grid(row=10,column=1)
l2=Label(text="Vertical Pixel")
l2.grid(row=12,column=1)
e1=Entry(window)
e1.grid(row=10,column=2)
e2=Entry(window)
e2.grid(row=12,column=2)
l3=Label(text="Convert Image to PDF",font='Bold')
l3.grid(row=19,column=2)
b3=Button(window,text="Upload Image file",command=open_image_file)
b3.grid(row=22,column=2)
b3=Button(window,text="Select Location to save Pdf",command=save_pdf_file)
b3.grid(row=28,column=2)
l4=Label(text="Extract text from image",font='Bold')
l4.grid(row=34,column=2)
b4=Button(window,text="Upload image to extract text",command=open_image_to_text)
b4.grid(row=37,column=2)
b5=Button(window,text="Select Location to save text",command=save_image_to_text)
b5.grid(row=43,column=2)
l5=Label(text="Made by Shivam",underline=True)
l5.grid(row=60,column=0)

window.mainloop()