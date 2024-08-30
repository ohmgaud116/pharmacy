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
        img1 = img1.resize((100, 80))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Use Label instead of BufferError for displaying the image
        b1 = Label(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=30, y=0)
        
        # frame medicine info
        self.infodataframe = LabelFrame(self.root, bd=15, relief=RIDGE, padx=20,text="Medicine Inforamtion",fg="NAVYBLUE",font=("times new roman", 24,"bold","underline"))
        self.infodataframe.place(x=0, y=100, width=1530, height=400)
        
        #---------------reference number------------------
        refinfo1=Label(self.infodataframe,text="Reference No.",fg="black",font=("times new roman", 15),padx=25)
        refinfo1.grid(row=0,column=0)
        ref_combo=ttk.Combobox(self.infodataframe,width=19,font=("times new roman", 10),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        #---------------company name---------------------
        companyname=Label(self.infodataframe,text="Company Name",fg="black",font=("times new roman", 15),padx=25)
        companyname.grid(row=1,column=0)
        cname_combo=Entry(self.infodataframe,width=23,font=("times new roman", 10),relief=RIDGE)
        cname_combo.grid(row=1,column=1,sticky=W)

        #---------------type of medicine----------------
        typeofmedicine=Label(self.infodataframe,text="Type of Medicine",fg="black",font=("times new roman",15),padx=25)
        typeofmedicine.grid(row=2,column=0)
        type_combo=ttk.Combobox(self.infodataframe,width=19,font=("times new roman",10),state="readonly")
        type_combo["values"]=("tablet","syrup","capsules")
        type_combo.grid(row=2,column=1)
        type_combo.current(0)
        #---------------



        #new add medicine column
        self.adddataframe = LabelFrame(self.root,bd=15,relief=RIDGE,padx=20,text="New Medicine Add Department",fg="NAVYBLUE",font=("times new roman", 24,"bold","underline"))
        self.adddataframe.place(x=1010,y=100 , width=520, height=400)

        # buttons frame
        self.buttonframe = Frame(self.root,bd=15,relief=FLAT,padx=10)
        self.buttonframe.place(x=75,y=500 , width=1530, height=50)
        #button1(Medicine add)
        btnAddData=Button(self.buttonframe,text="Add medicine", fg="green",font=("times new roman", 15),bg="lightgrey")
        btnAddData.grid(row=0, column=0)
        #button2(update)
        btn2=Button(self.buttonframe,text="Update", fg="green",font=("times new roman", 15),bg="lightgrey",padx=25)
        btn2.grid(row=0, column=1)

        #button3(delete)
        btn3=Button(self.buttonframe,text="Delete", fg="green",font=("times new roman", 15),bg="red",padx=25)
        btn3.grid(row=0, column=2)

        #button4(reset)
        btn4=Button(self.buttonframe,text="Reset", fg="green",font=("times new roman", 15),bg="lightgrey",padx=25)
        btn4.grid(row=0, column=3)

        #button5(exit)
        btn5=Button(self.buttonframe,text="Exit",fg="green",font=("times new roman", 15),bg="lightgrey",padx=25)
        btn5.grid(row=0,column=4)

        #button6( searchby)
        btn6=Button(self.buttonframe,text="Searchby",fg="green",font=("times new roman", 15),bg="RED",padx=25)
        btn6.grid(row=0,column=5)

        search_combo=ttk.Combobox(self.buttonframe,width=12,font=("times new roman", 15),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        #search area 

        textsearch=Entry(self.buttonframe,bd=3,relief=RIDGE,width=15,font=("times new roman", 15))
        textsearch.grid(row=0,column=7)

        #button7( search)
        btn7=Button(self.buttonframe,text="Search",fg="green",font=("times new roman", 15),bg="lightgrey",padx=25)
        btn7.grid(row=0,column=8)

        #button8(showall)
        btn7=Button(self.buttonframe,text="Show All",fg="green",font=("times new roman", 15),bg="lightgrey",padx=25)
        btn7.grid(row=0,column=9)
        #database column
        self.dataframe = Frame(self.root,bd=15,relief=RIDGE,padx=10)
        self.dataframe.place(x=0,y=565 , width=1530, height=250)

if __name__ == "__main__":
    root = Tk()
    obj = PharmacymanagementSystem(root)
    root.mainloop()
