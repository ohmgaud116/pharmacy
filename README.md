from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class PharmacymanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=FLAT, bg="LIGHTGREY", fg="green", font=("times new roman", 24,"bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("pharmapic2.jpg")
        img1 = img1.resize((100, 60))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Use Label instead of BufferError for displaying the image
        b1 = Label(self.root, image=self.photoimg1, borderwidth=5,background="green")
        b1.place(x=30, y=0)
        
        # frame medicine info
        self.infodataframe = LabelFrame(self.root, bd=15, relief=RIDGE, padx=20,text="Medicine Inforamtion",fg="NAVYBLUE",font=("times new roman", 24,"bold","underline"))
        self.infodataframe.place(x=0, y=100, width=850, height=300)
        
        #---------------reference number------------------
        refinfo1=Label(self.infodataframe,text="Reference No.:",fg="black",font=("times new roman", 15),padx=25)
        refinfo1.grid(row=0,column=0)
        ref_combo=ttk.Combobox(self.infodataframe,width=19,font=("times new roman", 10),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        #---------------company name---------------------
        companyname=Label(self.infodataframe,text="Company Name:",fg="black",font=("times new roman", 15),padx=25)
        companyname.grid(row=1,column=0)
        cname_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        cname_combo.grid(row=1,column=1,sticky=W)

        #---------------type of medicine----------------
        typeofmedicine=Label(self.infodataframe,text="Type of Medicine:",fg="black",font=("times new roman",15),padx=25)
        typeofmedicine.grid(row=2,column=0)
        type_combo=ttk.Combobox(self.infodataframe,width=19,font=("times new roman",10),state="readonly")
        type_combo["values"]=("tablet","syrup","capsules","Topical medicines","Drops","Inhails","Injection")
        type_combo.grid(row=2,column=1)
        type_combo.current(0)
        #---------------Medicine Name------------------------

        medicinename=Label(self.infodataframe,text="Medicine Name:",fg="black",font=("times new roman",15),padx=25)
        medicinename.grid(row=3,column=0)
        medname_combo=ttk.Combobox(self.infodataframe,width=19,font=("times new roman",10),state="readonly")
        medname_combo["values"]=("nice")
        medname_combo.grid(row=3,column=1)
        medname_combo.current(0)


        #---------------Lot No..............................

        lotno=Label(self.infodataframe,text="Lot No.:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        lotno.grid(row=4,column=0)
        lotno_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        lotno_combo.grid(row=4,column=1,sticky=W)

        #---------------issue date-------------------------
        issuedate=Label(self.infodataframe,text="Issue Date:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        issuedate.grid(row=5,column=0)
        issuedate_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        issuedate_combo.grid(row=5,column=1,sticky=W)
        #---------------exp date---------------------------

        expdate=Label(self.infodataframe,text="Exp Date:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        expdate.grid(row=5,column=0)
        expdate_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        expdate_combo.grid(row=5,column=1,sticky=W)
        #---------------uses-------------------------------

        uses=Label(self.infodataframe,text="Uses:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        uses.grid(row=6,column=0)
        uses_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        uses_combo.grid(row=6,column=1,sticky=W)
        #---------------side effects-----------------------
        sideEffect=Label(self.infodataframe,text="Side Effect:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        sideEffect.grid(row=7,column=0)
        sideEffect_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        sideEffect_combo.grid(row=7,column=1,sticky=W)

        #---------------prec&warning-----------------------
        warning=Label(self.infodataframe,text="Prec&Warning:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        warning.grid(row=0,column=2)
        warning_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        warning_combo.grid(row=0,column=3,sticky=W)

        #---------------dosage-----------------------------
        Dosage=Label(self.infodataframe,text="Dosage:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        Dosage.grid(row=1,column=2)
        Dosage_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        Dosage_combo.grid(row=1,column=3,sticky=W)
        #---------------tablet price-----------------------
        price=Label(self.infodataframe,text="Tablet Price:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        price.grid(row=2,column=2)
        price_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        price_combo.grid(row=2,column=3,sticky=W)
        #---------------product qt-------------------------
        Qt=Label(self.infodataframe,text="Product Qt:",justify="left",fg="black",font=("times new roman", 15),padx=25)
        Qt.grid(row=3,column=2)
        Qt_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        Qt_combo.grid(row=3,column=3,sticky=W)

        #--Addding imaging inside the informatuon box--
        img2 = Image.open("pharama 4.jpeg")
        img2 = img2.resize((200, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Label(self.root, image=self.photoimg2)
        b2.place(x=400, y=250)

        img3 = Image.open("pharma3.webp")
        img3 = img3.resize((200, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b2 = Label(self.root, image=self.photoimg3)
        b2.place(x=600, y=250)

        Quat=Label(self.infodataframe,text="Health is the greatest of human blessings",justify="left",fg="black",font=("times new roman", 15),padx=25)
        Quat.place(x=450,y=350)


        #new add medicine column
        self.adddataframe = LabelFrame(self.root,bd=15,relief=RIDGE,padx=20,text="New Medicine Add Department",fg="NAVYBLUE",font=("times new roman", 24,"bold","underline"))
        self.adddataframe.place(x=800,y=100 , width=800, height=300)

         #---adding image inside the new medicine box--
        img4 = Image.open("pHARMA 5.jpeg")
        img4 = img4.resize((250, 100))
        self.photoimg4= ImageTk.PhotoImage(img4)
        b3 = Label(self.root, image=self.photoimg4)
        b3.place(x=830, y=140)



        # buttons frame
        self.buttonframe = Frame(self.root,bd=15,relief=FLAT,padx=10)
        self.buttonframe.place(x=75,y=400 , width=1530, height=55)
        #button1(Medicine add)
        btnAddData=Button(self.buttonframe,text="Add medicine", fg="black",font=("times new roman", 15),bg="green",bd=5)
        btnAddData.grid(row=0, column=0)
        #button2(update)
        btn2=Button(self.buttonframe,text="Update", fg="black",font=("times new roman", 15),bg="green",padx=25,bd=5)
        btn2.grid(row=0, column=1)

        #button3(delete)
        btn3=Button(self.buttonframe,text="Delete", fg="black",font=("times new roman", 15),bg="red",padx=25,bd=5)
        btn3.grid(row=0, column=2)

        #button4(reset)
        btn4=Button(self.buttonframe,text="Reset", fg="black",font=("times new roman", 15),bg="green",padx=25,bd=5)
        btn4.grid(row=0, column=3)

        #button5(exit)
        btn5=Button(self.buttonframe,text="Exit",fg="black",font=("times new roman", 15),bg="green",padx=25,bd=5)
        btn5.grid(row=0,column=4)

        #button6( searchby)
        btn6=Button(self.buttonframe,text="Searchby",fg="black",font=("times new roman", 15),bg="RED",padx=25,bd=5)
        btn6.grid(row=0,column=5)

        search_combo=ttk.Combobox(self.buttonframe,width=12,font=("times new roman", 15),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        #search area 

        textsearch=Entry(self.buttonframe,bd=3,relief=RIDGE,width=15,font=("times new roman", 15))
        textsearch.grid(row=0,column=7)

        #button7( search)
        btn7=Button(self.buttonframe,text="Search",fg="black",font=("times new roman", 15),bg="green",padx=25,bd=5)
        btn7.grid(row=0,column=8)

        #button8(showall)
        btn7=Button(self.buttonframe,text="Show All",fg="black",font=("times new roman", 15),bg="green",padx=25,bd=5)
        btn7.grid(row=0,column=9)
        #database column
        self.dataframe = Frame(self.root,bd=15,relief=RIDGE,padx=10)
        self.dataframe.place(x=0,y=500 , width=1530, height=250)

if __name__ == "__main__":
    root = Tk()
    obj = PharmacymanagementSystem(root)
    root.mainloop()
