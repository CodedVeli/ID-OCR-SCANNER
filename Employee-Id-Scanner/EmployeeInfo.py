#---CFT[0]
# -*- coding: utf-8 -*-
import tkinter
from tkinter import*
import tkinter as tk
from tkinter.ttk import*
from tkinter.filedialog import askopenfilename
from PIL import*
from PIL import Image, ImageTk
import time
import pygame
import mysql.connector
from mysql.connector import Error
from matplotlib import pyplot as plt
#---

#---CFT[1]
#Initializing pygame.mixer to beep a sound when it detects ID's
pygame.mixer.init()
def play():
    pygame.mixer.music.load('detect-music.wav')
    pygame.mixer.music.play(loops=0)
play()

def sendData(empid, fname, gender, dob, depmt, degn, doj, addr, empPhoto):
    pygame.mixer.init()
    def play():
        pygame.mixer.music.load('detect-music.wav')
        pygame.mixer.music.play(loops=0)
    play()

    #---CFT[1.2]
    print("\nStarting Panel....\n")
    time.sleep(1)
    #Staring with basic app
    root = tk.Tk()
    root.geometry("680x680")
    root.title("EI-System")
    root.configure(bg="#4863A0") #AzureBlue
    root.resizable(0,0)
    #---

    #---CFT[2]
    #Inserting title for app
    canvas1 = Canvas(root,width=660,height=100, bg="black", bd=0, highlightthickness=0)
    label  = tk.Label(canvas1, text="EMPLOYEE  INFORMATION  SYSTEM", width="400", height=2, 
                    bg="#4863A0",fg="white",font=("Ariel",18,'bold'))
    label.pack(side=LEFT, anchor='nw')
    canvas1.pack(side=TOP,anchor="nw", padx=0, pady=0)

    #Employee Information Section
    canvas2 = Canvas(root,width=660, bg="orange",highlightthickness=0) #bg="#CCCCFF"
    canvas2.pack(side=TOP,anchor="nw", padx=0)

    #App control section
    canvas3 = Canvas(root,width=660,height=400, bg="#4863A0",highlightthickness=0) #bg="#CCCCFF"
    canvas3.pack(side=TOP,anchor="sw", padx=5,pady=0,expand=False)

    #InfoSection******************************
    label3left = Canvas(canvas2,width=460, height=540,highlightthickness=0)
    label3left.config(background="#CCCCFF") #bg="#CCCCFF"
    label3left.pack(side='left',anchor='nw')

    #ID Section********************************
    label3right = Canvas(canvas2,width=250, height=540,highlightthickness=0)
    label3right.config(background="#CCCCFF") #bg="#CCCCFF"
    label3right.pack(side='left', anchor='w',padx=0)
    #---

    #---CFT[3]
    #Required Informations for An Employee 
    empid = "SWTNYC-22E01PP-CF"
    fname = "Peter Parker"
    gender = "Male"
    dob = "19/02/1888"
    depmt = "Research & Development"
    degn = "Tech. Training Coordinator"
    doj = "01/01/2023"
    addr = "Wilson Street, Escondido, California, US, 92025"
    empPhoto = r"img7.jpg"

    # Displaying result in console
    print(empid)
    print(fname)
    print(gender)
    print(dob)
    print(depmt)
    print(degn)
    print(doj)
    print(addr)
    print(empPhoto)
    img = plt.imread(empPhoto)
    plt.imshow(img)
    #---

    #---CFT[4]
    #Drawing columns and rows to show Employees' Information
    #Row ONE--------------------------
    empLabel1 = Label(label3left,width=460)
    empfrm1 = tk.Frame(empLabel1,width=100,height=40,background="#CCCCFF")
    empBoxEntry1 = tk.Label(empfrm1,width=15,height=1,background="#CCCCFF")
    empBoxEntry1.configure(text="Employee ID : ",font=("Ariel",12,'bold'))
    empBoxEntry1.pack(padx=5,pady=5)
    empfrm1.pack(side=LEFT)

    empfrm1o = tk.Frame(empLabel1,width=100,height=40,background="gray")
    empBoxEntry1o = tk.Label(empfrm1o,width=20,height=1,background="#CCCCFF")
    empBoxEntry1o.configure(text=str(empid),font=("Ariel",12,'bold'))
    empBoxEntry1o.pack(padx=5,pady=5)
    empfrm1o.pack(side=LEFT)
    empLabel1.place(anchor="nw",x=8,y=15)
    #---

    #---CFT[5]
    #Row TWO----------------------------------
    empLabel2 = Label(label3left,width=460)
    empfrm2 = tk.Frame(empLabel2,width=100,height=40,background="#CCCCFF")
    empBoxEntry2 = tk.Label(empfrm2,width=15,height=1,background="#CCCCFF")
    empBoxEntry2.configure(text="Full Name : ",font=("Ariel",12,'bold'))
    empBoxEntry2.pack(padx=5,pady=5)
    empfrm2.pack(side=LEFT)

    empfrm2o = tk.Frame(empLabel2,width=100,height=40,background="gray")
    empBoxEntry2o = tk.Label(empfrm2o,width=20,height=1,background="#CCCCFF")
    empBoxEntry2o.configure(text=str(fname),font=("Ariel",12,'bold'))
    empBoxEntry2o.pack(padx=5,pady=5)
    empfrm2o.pack(side=LEFT)
    empLabel2.place(anchor="nw",x=8,y=70)
    #---

    #---CFT[6]
    #Row THREE----------------------------------
    empLabel3 = Label(label3left,width=460)
    empfrm3 = tk.Frame(empLabel3,width=100,height=40,background="#CCCCFF")
    empBoxEntry3 = tk.Label(empfrm3,width=15,height=1,background="#CCCCFF")
    empBoxEntry3.configure(text="Gender : ",font=("Ariel",12,'bold'))
    empBoxEntry3.pack(padx=5,pady=5)
    empfrm3.pack(side=LEFT)

    empfrm3o = tk.Frame(empLabel3,width=100,height=40,background="gray")
    empBoxEntry3o = tk.Label(empfrm3o,width=20,height=1,background="#CCCCFF")
    empBoxEntry3o.configure(text=str(gender),font=("Ariel",12,'bold'))
    empBoxEntry3o.pack(padx=5,pady=5)
    empfrm3o.pack(side=LEFT)
    empLabel3.place(anchor="nw",x=8,y=130)
    #---

    #---CFT[7]
    #Row FOUR----------------------------------
    empLabel4 = Label(label3left,width=460)
    empfrm4 = tk.Frame(empLabel4,width=100,height=40,background="#CCCCFF")
    empBoxEntry4 = tk.Label(empfrm4,width=15,height=1,background="#CCCCFF")
    empBoxEntry4.configure(text="DOB : ",font=("Ariel",12,'bold'))
    empBoxEntry4.pack(padx=5,pady=5)
    empfrm4.pack(side=LEFT)

    empfrm4o = tk.Frame(empLabel4,width=100,height=40,background="gray")
    empBoxEntry4o = tk.Label(empfrm4o,width=20,height=1,background="#CCCCFF")
    empBoxEntry4o.configure(text=str(dob),font=("Ariel",12,'bold'))
    empBoxEntry4o.pack(padx=5,pady=5)
    empfrm4o.pack(side=LEFT)
    empLabel4.place(anchor="nw",x=8,y=190)
    #---

    #---CFT[8]
    #Row FIVE ----------------------------------
    empLabel5 = Label(label3left,width=460)
    empfrm5 = tk.Frame(empLabel5,width=100,height=40,background="#CCCCFF")
    empBoxEntry5 = tk.Label(empfrm5,width=15,height=1,background="#CCCCFF")
    empBoxEntry5.configure(text="Department : ",font=("Ariel",12,'bold'))
    empBoxEntry5.pack(padx=5,pady=5)
    empfrm5.pack(side=LEFT)

    empfrm5o = tk.Frame(empLabel5,width=100,height=40,background="gray")
    empBoxEntry5o = tk.Label(empfrm5o,width=20,height=1,background="#CCCCFF")
    empBoxEntry5o.configure(text=str(depmt),font=("Ariel",12,'bold'))
    empBoxEntry5o.pack(padx=5,pady=5)
    empfrm5o.pack(side=LEFT)
    empLabel5.place(anchor="nw",x=8,y=250)
    #---

    #---CFT[9]
    #Row SIX ----------------------------------
    empLabel6 = Label(label3left,width=460)
    empfrm6 = tk.Frame(empLabel6,width=100,height=40,background="#CCCCFF")
    empBoxEntry6 = tk.Label(empfrm6,width=15,height=1,background="#CCCCFF")
    empBoxEntry6.configure(text="Designation : ",font=("Ariel",12,'bold'))
    empBoxEntry6.pack(padx=5,pady=5)
    empfrm6.pack(side=LEFT)

    empfrm6o = tk.Frame(empLabel6,width=100,height=40,background="gray")
    empBoxEntry6o = tk.Label(empfrm6o,width=20,height=1,background="#CCCCFF")
    empBoxEntry6o.configure(text=str(degn),font=("Ariel",12,'bold'))
    empBoxEntry6o.pack(padx=5,pady=5)
    empfrm6o.pack(side=LEFT)
    empLabel6.place(anchor="nw",x=8,y=310)
    #---

    #---CFT[10]
    #Row SEVEN ----------------------------------
    empLabel7 = Label(label3left,width=460)
    empfrm7 = tk.Frame(empLabel7,width=100,height=40,background="#CCCCFF")
    empBoxEntry7 = tk.Label(empfrm7,width=15,height=1,background="#CCCCFF")
    empBoxEntry7.configure(text="Date of Joining : ",font=("Ariel",12,'bold'))
    empBoxEntry7.pack(padx=5,pady=5)
    empfrm7.pack(side=LEFT)

    empfrm7o = tk.Frame(empLabel7,width=100,height=40,background="gray")
    empBoxEntry7o = tk.Label(empfrm7o,width=20,height=1,background="#CCCCFF")
    empBoxEntry7o.configure(text=str(doj),font=("Ariel",12,'bold'))
    empBoxEntry7o.pack(padx=5,pady=5)
    empfrm7o.pack(side=LEFT)
    empLabel7.place(anchor="nw",x=8,y=370)
    #---

    #---CFT[11]
    #Row EIGHT----------------------------------
    empLabel8 = tk.Label(label3left,width=460,bg="#CCCCFF")
    empfrm8 = tk.Frame(empLabel8,width=100,height=40,background="#CCCCFF")
    empBoxEntry8 = tk.Label(empfrm8,width=15,height=1,background="#CCCCFF")
    empBoxEntry8.configure(text="Address : ",font=("Ariel",11,'bold'))
    empBoxEntry8.pack(side=RIGHT,padx=5,pady=5)
    empfrm8.pack(side=LEFT)

    empfrm8o = tk.Frame(empLabel8,width=100,height=40,background="gray")
    empBoxEntry8o = tk.Label(empfrm8o,width=20,height=2,background="#CCCCFF")
    empBoxEntry8o.configure(text=str(addr), font=("Ariel",12,'bold'), wraplength=210, justify="left")
    empBoxEntry8o.pack(padx=5,pady=5)
    empfrm8o.pack(side=LEFT)
    empLabel8.place(anchor="nw",x=20,y=430)
    #---

    #---CFT[12]
    #Column THIRD
    #IDSection******************************
    empLabelID = tk.Label(label3right,width=460,bd=5,bg="gray")
    empfrmId = tk.Frame(empLabelID,width=40,height=100,background="gray")
    empBoxEntry10 = tk.Label(empfrmId,width=12,height=6,background="skyblue")
    empBoxEntry10.configure(text="PHOTO",font=("Ariel",12,'bold'))
    empBoxEntry10.pack(padx=5,pady=5)
    empfrmId.pack(side=LEFT)
    empLabelID.place(anchor="n",x=110,y=30)
    #---

    #---[13]
    #Setting up employee photo
    global imgtk    
    #img = Image.open(imagePath).convert("1") #Changing colour
    img = Image.open(empPhoto)
    newimg = img.resize((180,180),resample=1)
    imgtk = ImageTk.PhotoImage(image = newimg)
    empBoxEntry10.configure(image=imgtk,bd=80)
    empBoxEntry10.grid(row=0,column=0)
    #---

    #---CFT[14]
    #******************Edit View***************************
    #Basic Actions
    def action():
        print("\nEditing mode activated!\n")
        
    def close():
        print("This application has been closed!")
        root.destroy()
        #import Data_Scan

    pygame.mixer.init()
    #---

    #---CFT[15]
    #Defining function to add new employees' data
    def editData():
        global imgtk
        #ID Section********************************
        #Row ONE: EmployeeID--------------------------
        empLabel1 = Label(canvas2, width=460)
        empfrm1 = tk.Frame(empLabel1,width=100,height=40,background="#CCCCFF")
        empBoxEntry1 = tk.Label(empfrm1,width=15,height=1,background="#CCCCFF")
        empBoxEntry1.configure(text="Employee ID : ",font=("Ariel",12,'bold'))
        empBoxEntry1.pack(padx=5,pady=5)
        empfrm1.pack(side=LEFT)

        empfrm1o = tk.Frame(empLabel1,width=100,height=40,background="gray")
        empBoxEntry1o = tk.Entry(empfrm1o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry1o.insert(0, "")
        empBoxEntry1o.pack(padx=5,pady=5)
        empfrm1o.pack(side=LEFT)
        empLabel1.place(anchor="nw",x=8,y=15)

        #Row TWO: Employee Name----------------------------------
        empLabel2 = Label(canvas2,width=460)
        empfrm2 = tk.Frame(empLabel2,width=100,height=40,background="#CCCCFF")
        empBoxEntry2 = tk.Label(empfrm2,width=15,height=1,background="#CCCCFF")
        empBoxEntry2.configure(text="Full Name : ",font=("Ariel",12,'bold'))
        empBoxEntry2.pack(padx=5,pady=5)
        empfrm2.pack(side=LEFT)

        empfrm2o = tk.Frame(empLabel2,width=100,height=40,background="gray")
        empBoxEntry2o = tk.Entry(empfrm2o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry2o.insert(0, "")
        empBoxEntry2o.pack(padx=5,pady=5)
        empfrm2o.pack(side=LEFT)
        empLabel2.place(anchor="nw",x=8,y=70)

        #Row THREE: Gender----------------------------------
        empLabel3 = Label(canvas2,width=460)
        empfrm3 = tk.Frame(empLabel3,width=100,height=40,background="#CCCCFF")
        empBoxEntry3 = tk.Label(empfrm3,width=15,height=1,background="#CCCCFF")
        empBoxEntry3.configure(text="Gender : ",font=("Ariel",12,'bold'))
        empBoxEntry3.pack(padx=5,pady=5)
        empfrm3.pack(side=LEFT)

        empfrm3o = tk.Frame(empLabel3,width=100,height=40,background="gray")
        empBoxEntry3o = tk.Entry(empfrm3o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry3o.insert(0,"")
        empBoxEntry3o.pack(padx=5,pady=5)
        empfrm3o.pack(side=LEFT)
        empLabel3.place(anchor="nw",x=8,y=130)

        #Row FOUR: Date of Birth----------------------------------
        empLabel4 = Label(canvas2,width=460)
        empfrm4 = tk.Frame(empLabel4,width=100,height=40,background="#CCCCFF")
        empBoxEntry4 = tk.Label(empfrm4,width=15,height=1,background="#CCCCFF")
        empBoxEntry4.configure(text="DOB : ",font=("Ariel",12,'bold'))
        empBoxEntry4.pack(padx=5,pady=5)
        empfrm4.pack(side=LEFT)

        empfrm4o = tk.Frame(empLabel4,width=100,height=40,background="gray")
        empBoxEntry4o = tk.Entry(empfrm4o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry4o.insert(0, "")
        empBoxEntry4o.pack(padx=5,pady=5)
        empfrm4o.pack(side=LEFT)
        empLabel4.place(anchor="nw",x=8,y=190)

        #Row FIVE: Department----------------------------------
        empLabel5 = Label(canvas2,width=460)
        empfrm5 = tk.Frame(empLabel5,width=100,height=40,background="#CCCCFF")
        empBoxEntry5 = tk.Label(empfrm5,width=15,height=1,background="#CCCCFF")
        empBoxEntry5.configure(text="Department : ",font=("Ariel",12,'bold'))
        empBoxEntry5.pack(padx=5,pady=5)
        empfrm5.pack(side=LEFT)

        empfrm5o = tk.Frame(empLabel5,width=100,height=40,background="gray")
        empBoxEntry5o = tk.Entry(empfrm5o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry5o.insert(0, "")
        empBoxEntry5o.pack(padx=5,pady=5)
        empfrm5o.pack(side=LEFT)
        empLabel5.place(anchor="nw",x=8,y=250)

        #Row SIX: Designation----------------------------------
        empLabel6 = Label(canvas2,width=460)
        empfrm6 = tk.Frame(empLabel6,width=100,height=40,background="#CCCCFF")
        empBoxEntry6 = tk.Label(empfrm6,width=15,height=1,background="#CCCCFF")
        empBoxEntry6.configure(text="Designation : ",font=("Ariel",12,'bold'))
        empBoxEntry6.pack(padx=5,pady=5)
        empfrm6.pack(side=LEFT)

        empfrm6o = tk.Frame(empLabel6,width=100,height=40,background="gray")
        empBoxEntry6o = tk.Entry(empfrm6o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry6o.insert(0, "")
        empBoxEntry6o.pack(padx=5,pady=5)
        empfrm6o.pack(side=LEFT)
        empLabel6.place(anchor="nw",x=8,y=310)

        #Row SEVEN: Date of Joining----------------------------------
        empLabel7 = Label(canvas2,width=460)
        empfrm7 = tk.Frame(empLabel7,width=100,height=40,background="#CCCCFF")
        empBoxEntry7 = tk.Label(empfrm7,width=15,height=1,background="#CCCCFF")
        empBoxEntry7.configure(text="Date of Joining : ",font=("Ariel",12,'bold'))
        empBoxEntry7.pack(padx=5,pady=5)
        empfrm7.pack(side=LEFT)

        empfrm7o = tk.Frame(empLabel7,width=100,height=40,background="gray")
        empBoxEntry7o = tk.Entry(empfrm7o,width=22,background="white",font=("Ariel",12,'bold'))
        empBoxEntry7o.insert(0, "")
        empBoxEntry7o.pack(padx=5,pady=5)
        empfrm7o.pack(side=LEFT)
        empLabel7.place(anchor="nw",x=8,y=370)

        #Row EIGHT: Address----------------------------------
        empLabel8 = tk.Label(canvas2,width=460,bg="#CCCCFF")
        empfrm8 = tk.Frame(empLabel8,width=100,height=40,background="#CCCCFF")
        empBoxEntry8 = tk.Label(empfrm8,width=15,height=1,background="#CCCCFF")
        empBoxEntry8.configure(text="Address : ",font=("Ariel",11,'bold'))
        empBoxEntry8.pack(side=RIGHT,padx=5,pady=5)
        empfrm8.pack(side=LEFT)

        empfrm8o = tk.Frame(empLabel8,width=100,height=40,background="gray",bd=2)
        elephant = tk.Text(empfrm8o,width=22,height=2,background="white",font=("Ariel",12,'bold'))
        elephant.insert("1.0","")
        elephant.pack(padx=5,pady=5)
        empfrm8o.pack(side=LEFT)
        empLabel8.place(anchor="nw",x=20,y=430)

        #PhotoID Section
        #Draw photo frame******************************
        empLabelID = tk.Label(canvas2,width=460,bd=5,bg="gray")
        empfrmId = tk.Frame(empLabelID,width=40,height=100,background="gray")
        empBoxEntry10 = tk.Label(empfrmId,width=12,height=6,background="skyblue")
        empBoxEntry10.configure(text="PHOTO",font=("Ariel",12,'bold'))
        empBoxEntry10.pack(padx=5,pady=5)
        empfrmId.pack(side=RIGHT)
        empLabelID.place(anchor="nw",x=468,y=30)

        #DefaultValue
        imagePath = r"empform.png"
        #img = Image.open(imagePath).convert("1") #Changing colour
        img = Image.open(imagePath)
        newimg = img.resize((180,180),resample=1)
        imgtk = ImageTk.PhotoImage(image = newimg)
        empBoxEntry10.configure(image=imgtk,bd=80)

        #---CFT[16]
        ###############Data Mining, Data Validation and MessageBox, MySQL Database****************
        #Specifying image path
        filePathEntry = Label(canvas2,width=460)
        filePathFrm= tk.Frame(filePathEntry,width=100,height=40,background="gray")
        fPath = tk.Entry(filePathFrm,width=22,background="#CCCCFF")
        fPath.insert(0,"")
        fPath.configure(fg="blue", bg="lightgray",font=("Ariel",9,'bold'))
        fPath.pack(padx=5,pady=5)
        filePathFrm.pack(side=LEFT)
        filePathEntry.place(anchor="ne",x=658,y=220)

        #Open file locations and saving address
        def browseFile():
            print("Find your file location!")
            filename = askopenfilename()
            fPath.delete(0,END)
            fPath.insert(0,str(filename))
            print(filename)
            fileUploaded(filename)
            return filename

        #Uploading image
        def fileUploaded(filelocation):
            global imgtk
            empLabelID = tk.Label(canvas2,width=460,bd=5,bg="gray")
            empfrmId = tk.Frame(empLabelID,width=40,height=100,background="gray")
            empBoxEntry10 = tk.Label(empfrmId,width=12,height=6,background="skyblue")
            empBoxEntry10.configure(text="PHOTO",font=("Ariel",12,'bold'))
            empBoxEntry10.pack(padx=5,pady=5)
            empfrmId.pack(side=RIGHT)
            empLabelID.place(anchor="nw",x=468,y=30)
            #File Uploaded message
            print("\nFile has been uploaded!\n")
            print("r"+filelocation)
            imagePath = filelocation
            img = Image.open(filelocation)
            newimg = img.resize((180,180),resample=1)
            imgtk = ImageTk.PhotoImage(image = newimg)
            empBoxEntry10.configure(image=imgtk,bd=80)

        #choose path
        pth = tk.Button(canvas2,text="Path:",width=5, command=lambda:[fileUploaded(browseFile())])
        pth.configure(fg="white",bg="#6667AB")
        pth.place(anchor="ne",x=488,y=222)
        
        #--------

        #---CFT[17]
        #Alert Message, for Empty Data, if tried to submit empty data
        def emptyBoxCheck():
            empid = empBoxEntry1o.get()
            name = empBoxEntry2o.get()
            gender = empBoxEntry3o.get()
            dob = empBoxEntry4o.get()
            depmt = empBoxEntry5o.get()
            degn = empBoxEntry6o.get()
            doj = empBoxEntry7o.get()
            addrs = elephant.get(1.0,END)
            p_path = fPath.get()

            flag = None

            if ((empid == "") or (name == "") or (gender == "") or (dob == "") or (depmt == "") or (degn == "") or (doj == "") or ((addrs == "") or ((len(addrs)-1) == 0)) or (p_path == "")):

                flag = True #If data is equal is null

                if empid == "":
                    errorMsg = tk.Label(canvas2,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=60)

                if name == "":
                    errorMsg = tk.Label(canvas2,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=115)

                if gender == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=240)

                if dob == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=300)

                if depmt == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=360)

                if degn == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=420)

                if doj == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=480)

                if (addrs == "") or (len(addrs)-1 == 0):
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=230,y=562)

                if p_path == "":
                    errorMsg = tk.Label(root,text="*This field is required!")
                    errorMsg.configure(fg="red",bg="#CCCCFF", font=('Ariel',8,''))
                    errorMsg.place(anchor="center",x=540,y=330)

            else:
                flag = False

            return flag
        
        #emptyBoxCheck()
        #------

        #---CFT[18]
        #User Already Exists Message***********
        #This function will be called when user already exists
        def userExistsAlert():
            msgbx = tk.Tk()
            msgbx.title("Alert Message")
            msgbx.geometry("240x180")
            msgbx.configure(bg="black")
            msgbx.wm_attributes("-toolwindow","True")
            msgbx.resizable(0,0)

            def play():
                pygame.mixer.music.load('dataSaved.mp3')
                pygame.mixer.music.play(loops=0)
            play()

            canvas_up = tk.Canvas(msgbx, height=70, bg="#992233",  bd=0, highlightthickness=0)
            textid = canvas_up.create_text(170,40, anchor="n", angle=270, fill="white", font=("Ariel",54,"bold"))
            canvas_up.itemconfig(textid, text=":(")
            canvas_up.pack(anchor="nw", side=TOP)
            
            def destroymsb():
                msgbx.destroy()

            canvas_down = tk.Canvas(msgbx, height=110, bg="white", bd=0, highlightthickness=0)
            
            tk.Label(canvas_down, fg="#225599",bg="white",font=("Ariel",10,"bold"),
            text="D A T A  A L R E A D Y  E X I S T S !").place(anchor="center",x=120,y=20)
            tk.Label(canvas_down, fg="#225599",bg="white",font=("Ariel",10),
            text="Please Check User ID.\n").place(anchor="center",x=120,y=50)

            okbtn = tk.Button(canvas_down,text="CLOSE",bg="red", fg="white", font=("Ariel",10,"bold"), command=destroymsb)
            okbtn.place(anchor="center",x=120,y=80)
            canvas_down.pack(anchor="sw", side=BOTTOM)

            msgbx.mainloop() 
        #----

        #---CFT[19]
        #Data Saved Message************
        #This fucntion will be called while you're saving data
        def messageBox():
            msgbx = tk.Tk()
            msgbx.title("Alert Message")
            msgbx.geometry("240x180")
            msgbx.configure(bg="black")
            msgbx.wm_attributes("-toolwindow","True")
            msgbx.resizable(0,0)

            def play():
                pygame.mixer.music.load('dataSaved.mp3')
                pygame.mixer.music.play(loops=0)
            play()

            canvas_up = tk.Canvas(msgbx, height=70, bg="#119944",  bd=0, highlightthickness=0)
            textid = canvas_up.create_text(120,10, anchor="n", angle=0, fill="white", font=("Ariel",28,"bold"))
            canvas_up.itemconfig(textid, text="✅")
            canvas_up.pack(anchor="nw", side=TOP)
            
            def destroymsb():
                msgbx.destroy()

            canvas_down = tk.Canvas(msgbx, height=110, bg="white", bd=0, highlightthickness=0)
            
            tk.Label(canvas_down, fg="#225599",bg="white",font=("Ariel",12,"bold"),
            text="D A T A  S A V E D !").place(anchor="center",x=120,y=35)

            okbtn = tk.Button(canvas_down, width=8,text="OK",bg="#119944", fg="white",font=("Ariel",10,"bold"), command=destroymsb)
            okbtn.place(anchor="center",x=120,y=80)

            canvas_down.pack(anchor="sw", side=BOTTOM)

            msgbx.mainloop()
        #------

        #---CFT[20]
        #MySQL Database and Data Validation*****************
        #Writing database file to add new infomations
        def insert(sample):
            a,b,c,e,f,g,h,i,j = sample[0],sample[1],sample[2],sample[3],sample[4],sample[5],sample[6],sample[7],sample[8]

            def insertNewData(Empid,Name,Gender,Dob,Depmt,Degn,Doj,Addrs,EmPhoto):
                #Accessing database************************
                import mysql.connector
                from mysql.connector import Error

                try:    
                    mydatabase = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password = 'root',
                        database = 'employeeinfosystem'
                    )

                    if mydatabase.is_connected():

                        mydb = mydatabase.cursor()
                        #Accessing database************************

                        insert_cmd = "INSERT INTO employeeinfo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
                        val =  (f'{Empid}', f'{Name}', f'{Gender}', f'{Dob}', f'{Depmt}', f'{Degn}', f'{Doj}', f'{Addrs}', f'{EmPhoto}')

                        mydb.execute(insert_cmd,val)
                        mydatabase.commit()
                        print("Data Inserted..")
                        messageBox() #show pop 'data saved'

                except Error as e:
                    print("Error while connecting to database..", e)

            insertNewData(a,b,c,e,f,g,h,i,j)
        #-----

        #---CFT[21]
        #Defining function for data validation and export data    
        def dataInserted():
            chk = emptyBoxCheck()
            if chk == False:
                def chkdata(uinput):
                    #Calling DataBase*****************************************
                    import mysql.connector
                    from mysql.connector import Error

                    try:

                        mydatabase = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password = 'root',
                            database = 'employeeinfosystem'
                        )

                        if mydatabase.is_connected():
                            mydb = mydatabase.cursor()
                            #mydb.execute("USE employeeinfosystem")
                            mydb.execute("SELECT * FROM EmployeeInfo")
                            #Calling DataBase end*****************************************

                            flag = 0
                            for i in mydb:
                                for j in i:
                                    if uinput == j:
                                        flag = 1
                            if flag == 1:
                                print("Data already exists! Please check user id.")
                                userExistsAlert()

                            else:                    
                                empid = empBoxEntry1o.get()
                                name = empBoxEntry2o.get()
                                gender = empBoxEntry3o.get()
                                dob = empBoxEntry4o.get()
                                depmt = empBoxEntry5o.get()
                                degn = empBoxEntry6o.get()
                                doj = empBoxEntry7o.get()
                                addrs = elephant.get("1.0", END)
                                p_path = fPath.get()

                                data = (empid,name,gender,dob,depmt,degn,doj,addrs,p_path)
                                insert(data)
                    except Error as e:
                        print("Error while connecting to database: ",e)

                empid = empBoxEntry1o.get() #access id from entry
                chkdata(empid)
        #-----

        #---CFT[22]
        #Control Panel-II
        #Draw button to add new employee's data
        btnLabel = Label(canvas3,width=460)
        btnfrm = tk.Frame(btnLabel,width=100,height=40,background="gray")
        btnBoxEntry = tk.Button(btnfrm,width=10,height=1,background="#CCCCFF",
                                command=lambda:[action(),editData()])
        btnBoxEntry.configure(text="ADD NEW : ",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'))
        btnBoxEntry.pack(padx=5,pady=5)
        btnfrm.pack(side=LEFT)
        btnLabel.place(anchor="nw",x=20,y=10)

        #This control button will help you to save employee's data
        btnLabel2 = Label(canvas3,width=460)
        btnfrm1_1 = tk.Frame(btnLabel2,width=100,height=40,background="gray")
        btnBoxEntry = tk.Button(btnfrm1_1,width=10,height=1,background="#CCCCFF",
                                command=lambda: [dataInserted()])
        btnBoxEntry.configure(text="SAVE",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'))
        btnBoxEntry.pack(padx=5,pady=5)
        btnfrm1_1.pack(side=LEFT)
        btnLabel2.place(anchor="nw",x=260,y=10)

        #Function and control button to close application after saving data
        def closeme():
            root.destroy()

        btnLabel3 = Label(canvas3,width=460)
        btnfrm1_2 = tk.Frame(btnLabel3,width=100,height=40,background="gray")
        btnBoxEntry = tk.Button(btnfrm1_2,width=10,height=1,background="#CCCCFF",
                                command=lambda:[closeme()])
        btnBoxEntry.configure(text="CLOSE",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'))
        btnBoxEntry.pack(padx=5,pady=5)
        btnfrm1_2.pack(side=LEFT)
        btnLabel3.place(anchor="nw",x=500,y=10)
    #Edit View Closed**********
    #-----

    #---CFTE[23]
    #Control Panel Section
    #Draw add button to add new employee's data
    btnLabel = Label(canvas3,width=460)
    btnfrm = tk.Frame(btnLabel,width=100,height=40,background="gray")
    #btnBoxEntry = tk.Button(btnfrm,width=10,height=1,background="#CCCCFF")
    btnBoxEntry = tk.Button(btnfrm,width=10,height=1,background="#CCCCFF",
                            command=lambda:[action(),editData()])
    btnBoxEntry.configure(text="ADD NEW : ",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'))
    btnBoxEntry.pack(padx=5,pady=5)
    btnfrm.pack(side=LEFT)
    btnLabel.place(anchor="nw",x=20,y=10)

    #This control button will help you to save employee's data
    btnLabel2 = Label(canvas3,width=460)
    btnfrm1_1 = tk.Frame(btnLabel2,width=100,height=40,background="gray")
    #btnBoxEntry = tk.Button(btnfrm1_1,width=10,height=1,background="#CCCCFF")
    btnBoxEntry = tk.Button(btnfrm1_1,width=10,height=1,background="#CCCCFF",
                            command=lambda: [saveme()])
    btnBoxEntry.configure(text="SAVE",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'),state='disabled')
    btnBoxEntry.pack(padx=5,pady=5)
    btnfrm1_1.pack(side=LEFT)
    btnLabel2.place(anchor="nw",x=260,y=10)

    #Function and control button to close application
    def close():
        root.destroy();
        
    btnLabel3 = Label(canvas3,width=460)
    btnfrm1_2 = tk.Frame(btnLabel3,width=100,height=40,background="gray")
    btnBoxEntry = tk.Button(btnfrm1_2,width=10,height=1,background="#CCCCFF")
    btnBoxEntry = tk.Button(btnfrm1_2,width=10,height=1,background="#CCCCFF",
                            command=lambda:[close()])
    btnBoxEntry.configure(text="CLOSE",fg="maroon", bg="lightgray",font=("Ariel",12,'bold'))
    btnBoxEntry.pack(padx=5,pady=5)
    btnfrm1_2.pack(side=LEFT)
    btnLabel3.place(anchor="nw",x=500,y=10)

    mainloop()
    #---

# empid = "SWTNYC-22E01PP-CF"
# fname = "Peter Parker"
# gender = "Male"
# dob = "19/02/1888"
# depmt = "Research & Development"
# degn = "Tech. Training Coordinator"
# doj = "01/01/2023"
# addr = "Wilson Street, Escondido, California, US, 92025"
# empPhoto = r"img7.jpg"

# sendData(empid, fname, gender, dob, depmt, degn, doj, addr, empPhoto)