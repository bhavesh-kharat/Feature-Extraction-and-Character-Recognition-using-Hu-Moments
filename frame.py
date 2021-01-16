from tkinter import *
import tkinter

# import filedialog module
from tkinter import filedialog
from PIL import Image, ImageTk
import time

#import Other Files :-  test.py and train.py
import train
import test



#Splash Screen
splash = tkinter.Tk()
splash.title("Welcome to Our GUI")
splash.geometry("1200x600")
# splash.configure(background='green')

fr1 = Frame(splash)

y = Image.open("Images\ocr.png")
render = ImageTk.PhotoImage(y)
img1 = Label(fr1, image = render)
# img1.pack()

w = Label(fr1, width = 60, height = 5, text="FEATURE EXTRACTION AND CHARACTER RECOGNITION \nUSING INVARIANT MOMENTS",font=("Helvetica", 22,"bold"),fg="black" ,bg="pale green")
img1.grid(row=1,column = 1)
w.grid(row = 1, column = 2)
fr1.pack(side = TOP)

fr2 = Frame(splash)
t = Label(fr2,width= 20, text="This is Welcome Window\n  Splash Screen\n",font=("Helvetica", 22,"bold"),fg="Black",bg="IndianRed1")
# t.pack(side = LEFT)
y1 = Image.open("Images\welcome.png")
render1 = ImageTk.PhotoImage(y1)
q = Label(fr2,image = render1)
# q.pack(side = RIGHT)
t.grid(row=2 , column =1,padx = 10, pady = 30)
q.grid(row =2, column = 2,padx= 10, pady = 30)
fr2.pack()

r=Label(splash,text= "( Add Your Text Here )",font=("Helvetica", 20, "bold"),fg="Black",bg="IndianRed1" )
r.pack()

splash.update()
time.sleep(2)
y = Label(splash,text= "Please Wait Loading.......",font=("Helvetica", 20),fg="Black",pady=40)
y.pack()

splash.update()
time.sleep(3)
splash.deiconify()
splash.destroy()





i = 0
num = 0
lst = []

def submit():
    global num
    num = int(number.get())
    label1.configure(text = "You have Enter  "+ str(num) +" ,press CONTINUE for moving to next frame", bg = "IndianRed1")
    global i
    i = 1

def next_page():
    global num
    if num== 0  :
        label1.configure(text = "Please select number of Images, before moving to next Frame\n( Input Image cannot be Zero)", bg = "IndianRed1")
    else :
        frame1.destroy()

frame1 = tkinter.Tk()
frame1.title("Optical Character Recognition")
frame1.geometry("1200x600")

f1 = Frame(frame1)
f2 = Frame(frame1)
f3 = Frame(frame1)

f1.pack(side = TOP, pady=20)
f2.pack(pady=40)
f3.pack(pady = 20)

label1 = Label(f1, text= "FEATURE EXTRACTION AND CHARACTER RECOGNITION \nUSING INVARIANT MOMENTS",width=80 , height=4,bg = "pale green", font=('calibre', 18, 'bold'), anchor = CENTER)
num=IntVar()
num = 0
# global i

number_label = Label(f2,text = 'Number of Images you want to Input',font=("Helvetica", 18, "bold"), anchor = CENTER)
number = Entry(f2,textvariable = num,font=('calibre',20,'normal'))


number_submit = Button(f3, text="Submit",height = 2, width = 15,bg="khaki1",font = ('calibre', 10, 'bold'),  command=submit, anchor = CENTER)

button1 = Button(f3, text="Move to the Next Page",height = 2, width = 25,bg="Steelblue1",font = ('calibre', 10, 'bold'),  command=next_page, anchor = CENTER)


label1.grid(row = 1, column = 1)
number_label.grid(row = 2 , column = 1, pady= 20)
number.grid(row = 2 , column = 2, pady = 20,padx=10)
number_submit.grid(row = 3, column = 1, pady = 20)

button1.grid(row = 4 , column = 1, pady = 20)

frame1.mainloop()





# Function for opening the
# file explorer window
def browseFiles():
    global num
    global lst
    for j in range(0,int(num)):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("BMP File", "*.bmp*"), ("all files","*.*")))

    # Change label contents
    #     label_file_explorer.configure(text="File Opened: " + filename)
        print(filename)
        lst.append(filename)
    s = ""
    for j in range(0,int(num)):
        s = s +str(j+1)+". "+ lst[j]+"\n"
    print(lst)
    label_file_explorer.configure(text="Path of the File to be Opened for Testing:\n" + s)





#Funtion for Run
def run() :
    window.destroy()

    train_images = ["a.bmp", "b.bmp", "c.bmp", "d.bmp", "e.bmp", "f.bmp", "g.bmp",
                    "h.bmp", "i.bmp", "j.bmp", "k.bmp", "l.bmp", "m.bmp",
                    "n.bmp", "o.bmp", "p.bmp", "q.bmp", "r.bmp", "s.bmp",
                    "t.bmp", "u.bmp", "v.bmp", "w.bmp", "x.bmp", "y.bmp", "z.bmp"];
    train_features, train_labels, train_mean, train_std = train.train(train_images)

    for i in lst:
        bbox_list, labels = test.test(i, train_features, train_labels, train_mean, train_std)


# Create the root window
# Set window title
# Set window size
window = Tk()
window.title('Optical Character Recognisation')
window.geometry("1200x600")


# Set window background color
bg = Image.open("Images\gui.jpeg")
render = ImageTk.PhotoImage(bg)
img = Label(window, image = render)
img.place(x=0,y=0)
# window.config(background = bg)


# Create a File Explorer label
l= Label(window, text= "FEATURE EXTRACTION AND CHARACTER RECOGNITION \nUSING INVARIANT MOMENTS",width=60 , height=4,bg = "pale green", font=('calibre', 18, 'bold'), anchor = CENTER)


label_file_explorer = Label(window, text="Choose the Image File Path ",
                            width=110 , height=4,bg ="SteelBlue1",  fg="brown", font=('calibre', 14 ), anchor = CENTER)

button_explore = Button(window, text="Browse Files",font=('calibre', 16, 'bold'), bg = "SteelBlue", command=browseFiles, width = 10, pady = 20)

run_button = Button(window, text= "GO", font = ("calibre", 16,"bold"),command = run,bg="tan1",height = 2, width = 15 )
button_exit = Button(window, text="Exit",height = 2, width = 10,font=('calibre', 16, 'bold'),bg= "IndianRed1", command = exit)

# Grid method is chosen for placing the widgets at respective positions
# in a table like structure by specifying rows and columns

l.grid(column=1, row=1, pady = 10)
label_file_explorer.grid(column=1, row=2, pady = 10)
button_explore.grid(column=1, row=3, pady = 10 )
run_button.grid(column = 1,row = 4, pady = 10)
button_exit.grid(column=1, row=5)

# Let the window wait for any events
window.mainloop()







for k in range(0,num) :
    last = Tk()
    last.title("Optical Character Recognisation")
    last.geometry("1400x750")

    last1 = Frame(last)
    last2 = Frame(last)


    last1.pack(side = LEFT)
    last2.pack(side = RIGHT)

    img2 = Image.open(lst[k])
    img2 = img2.resize((300,400),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(img2)
    output_img = Label(last1, image=render,padx=40)

    last_label = Label(last2,text="Output  "+" :\n"+test.label_list[k],font=('calibre', 12),bg= "SteelBlue1")
    last_component = Label(last2,width = 50, text="Components  " +" :\t" + str(test.component_list[k]),font=('calibre', 18, 'bold'),bg= "pale green")

    next_exit = Button(last2, text = "Next / Exit",bg = "IndianRed1" ,height = 2, width = 10, command = last.destroy)

    output_img.grid(column = 1, row =1)
    last_component.grid(column = 1, row=1,pady = 10,padx = 50)
    last_label.grid(column = 1, row =2,pady = 10,padx = 50)
    next_exit.grid(column = 1 , row= 3,pady = 10,padx = 50)
    last.mainloop()

