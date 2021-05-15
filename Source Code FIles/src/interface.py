from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

base = Tk()
base.title('detection of skin cancer')
title_label = Label(base,text="click upload button and upload your X-ray")
title_label.grid(row=0,column = 0,columnspan=3) 
def func():
    global img
    base.filename = filedialog.askopenfilename(initialdir="/",title="select",filetypes=[('image files', '.png'),('image files', '.jpg'),('image files', '.jpeg')])
    print(base.filename)
    x=Image.open(base.filename)
    resize = x.resize((400,400),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize)
    image_print = Label(image=img)
    image_print.grid(row=6,column = 0,columnspan=3) 

    a = base.filename
    global file
    file = a
    print(file)
    test()

butt = Button(base,text="upload image",command=func)
butt.grid(row=2,column = 0,columnspan=3) 
base.minsize(200,200)
base.mainloop()


def test():
    print("Testing...")
	# Test code here....

	dimension=(512, 512)
	images = []
	flat_data = []

	# print("file",file)
	# file = 'data/test/Uni/y.png'
	img = skimage.io.imread(file)
	# print(img)
	img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
	flat_data.append(img_resized.flatten()) 
	images.append(img_resized)
	flat_data = np.array(flat_data)
	# print(flat_data)

	result = clf.predict(flat_data)
	# print(result)
	if result[0] == 0:
	    print("Infected")
	    user = 'person has Skin Cancer!!!'
	    a = user
	    Label(win,text="                                                              ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    Label(win,text=user,fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    MsgBox = tk.messagebox.showwarning ('warning','person is infected',icon = 'warning')
	else:
	    print("Uninfected")
	    person = Fname.get()
	    user = person + ' does not have Skin Cancer!!!'
	    a = user
	    Label(win,text=". ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=12,y=460)
	    MsgBox = tk.messagebox.showinfo ('information','person is not infected')