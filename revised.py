from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacymanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # Establish connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            port="3306",
            database="pharma1"
        )

        # Add medicine variables
        self.addref_var = StringVar()
        self.addmed_var = StringVar()

        #-------------------------------------------------HEADING------------------------------------------------------------------------------------------
        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=FLAT, bg="LIGHTGREY", fg="green", font=("times new roman", 24,"bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("pharmapic2.jpg")
        img1 = img1.resize((100, 60))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        b1 = Label(self.root, image=self.photoimg1, borderwidth=5, background="green")
        b1.place(x=30, y=0)
        
        # Frame for medicine info
        self.infodataframe = LabelFrame(self.root, bd=15, relief=RIDGE, padx=20, text="Medicine Information", fg="NAVYBLUE", font=("times new roman", 24, "bold", "underline"))
        self.infodataframe.place(x=0, y=100, width=850, height=300)

        # Reference number
        refinfo1 = Label(self.infodataframe, text="Reference No.:", fg="black", font=("times new roman", 15), padx=25)
        refinfo1.grid(row=0, column=0)
        ref_combo = ttk.Combobox(self.infodataframe, width=19, font=("times new roman", 10), state="readonly")
        ref_combo["values"] = ("Ref", "Medname", "Lot")
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        # Company name
        companyname = Label(self.infodataframe, text="Company Name:", fg="black", font=("times new roman", 15), padx=25)
        companyname.grid(row=1, column=0)
        cname_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        cname_combo.grid(row=1, column=1, sticky=W)

        # Type of medicine
        typeofmedicine = Label(self.infodataframe, text="Type of Medicine:", fg="black", font=("times new roman", 15), padx=25)
        typeofmedicine.grid(row=2, column=0)
        type_combo = ttk.Combobox(self.infodataframe, width=19, font=("times new roman", 10), state="readonly")
        type_combo["values"] = ("tablet", "syrup", "capsules", "Topical medicines", "Drops", "Inhails", "Injection")
        type_combo.grid(row=2, column=1)
        type_combo.current(0)

        # Medicine Name
        medicinename = Label(self.infodataframe, text="Medicine Name:", fg="black", font=("times new roman", 15), padx=25)
        medicinename.grid(row=3, column=0)
        medname_combo = ttk.Combobox(self.infodataframe, width=19, font=("times new roman", 10), state="readonly")
        medname_combo["values"] = ("nice")
        medname_combo.grid(row=3, column=1)
        medname_combo.current(0)

        # Lot No
        lotno = Label(self.infodataframe, text="Lot No.:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        lotno.grid(row=4, column=0)
        lotno_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        lotno_combo.grid(row=4, column=1, sticky=W)

        # Issue Date
        issuedate = Label(self.infodataframe, text="Issue Date:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        issuedate.grid(row=5, column=0)
        issuedate_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        issuedate_combo.grid(row=5, column=1, sticky=W)

        # Exp Date
        expdate = Label(self.infodataframe, text="Exp Date:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        expdate.grid(row=6, column=0)
        expdate_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        expdate_combo.grid(row=6, column=1, sticky=W)

        # Uses
        uses = Label(self.infodataframe, text="Uses:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        uses.grid(row=7, column=0)
        uses_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        uses_combo.grid(row=7, column=1, sticky=W)

        # Side Effects
        sideEffect = Label(self.infodataframe, text="Side Effect:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        sideEffect.grid(row=8, column=0)
        sideEffect_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        sideEffect_combo.grid(row=8, column=1, sticky=W)

        # Precautions & Warning
        warning = Label(self.infodataframe, text="Prec & Warning:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        warning.grid(row=0, column=2)
        warning_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        warning_combo.grid(row=0, column=3, sticky=W)

        # Dosage
        Dosage = Label(self.infodataframe, text="Dosage:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        Dosage.grid(row=1, column=2)
        Dosage_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        Dosage_combo.grid(row=1, column=3, sticky=W)

        # Tablet Price
        price = Label(self.infodataframe, text="Tablet Price:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        price.grid(row=2, column=2)
        price_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        price_combo.grid(row=2, column=3, sticky=W)

        # Product Quantity
        Qt = Label(self.infodataframe, text="Product Qt:", justify="left", fg="black", font=("times new roman", 15), padx=25)
        Qt.grid(row=3, column=2)
        Qt_combo = Entry(self.infodataframe, width=23, font=("times new roman", 10), relief=RIDGE)
        Qt_combo.grid(row=3, column=3, sticky=W)

       
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

        #==================================================================================================================================
         #new add medicine column
        self.adddataframe = LabelFrame(self.root,bd=15,relief=RIDGE,padx=20,text="New Medicine Add Department",fg="NAVYBLUE",font=("times new roman", 24,"bold","underline"))
        self.adddataframe.place(x=800,y=100 , width=800, height=300)

         #---adding image inside the new medicine box--
        img4 = Image.open("pHARMA 5.jpeg")
        img4 = img4.resize((180, 100))
        self.photoimg4= ImageTk.PhotoImage(img4)
        b3 = Label(self.root, image=self.photoimg4,bd=2)
        b3.place(x=1150, y=140)

        img5 = Image.open("pharma6.jpeg")
        img5 = img5.resize((180, 100))
        self.photoimg5= ImageTk.PhotoImage(img5)
        b3 = Label(self.root, image=self.photoimg5,bd=2)
        b3.place(x=1350 ,y=140)
        #----adding reference number in new medicine box---
        refaddmedicine=Label(self.adddataframe,text="Reference No.:",fg="black",font=("times new roman", 15))
        refaddmedicine.place(x=0,y=5)
        refaddmedicine_combo=Entry(self.adddataframe,textvariable=self.addref_var,width=28,font=("times new roman", 10),relief=RIDGE,bd=2)
        refaddmedicine_combo.place(x=135,y=5)

        #-----adding medicine name in new medicine box---

        Addmedicinename=Label(self.adddataframe,text="Medicine name:",fg="black",font=("times new roman", 15))
        Addmedicinename.place(x=0,y=35)
        Addmedicinename_combo=Entry(self.adddataframe,textvariable=self.addmed_var,width=28,font=("times new roman", 10),relief=RIDGE,bd=2)
        Addmedicinename_combo.place(x=135,y=35)

       #========side frame box=====================
        self.sideframe = Frame(self.adddataframe,bd=15,relief=FLAT,padx=10,bg="white")
        self.sideframe.place(x=0,y=70,width=250,height=160)
        
        scroll_x=ttk.Scrollbar(self.sideframe,orient=HORIZONTAL)
        scroll_x.pack(fill=X,side=BOTTOM)
        scroll_y=ttk.Scrollbar(self.sideframe,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        self.medicine_table=ttk.Treeview(self.sideframe,column=("ref no.","medicine name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.medicine_table.xview)
        scroll_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref no.", text="Reference no.")
        self.medicine_table.heading("medicine name",text="Medicine Name")
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table["show"]="headings"
        self.medicine_table.column("ref no.",width=100)
        self.medicine_table.column("medicine name",width=100)
        #------------------------------------------------
         #============addition button frames=================
        self.rightframe=Frame(self.adddataframe,relief=RIDGE,bd=2,bg="green")
        self.rightframe.place(x=530,y=110,width=110,height=145)

  
        btr1 = Button(self.rightframe, text="ADD", bd=2, bg="yellow", padx=37, fg="black", pady=6,command=self.addmedicine)
        btr1.grid(row=0, column=0)

        btr2=Button(self.rightframe,text="UPDATE",bd=2,bg="red",padx=30,fg="black",pady=6)
        btr2.grid(row=1,column=0)

        btr3=Button(self.rightframe,text="DELETE",bd=2,bg="yellow",padx=32,fg="black",pady=6)
        btr3.grid(row=2,column=0)

        btr4=Button(self.rightframe,text="CLEAR",bd=2,bg="RED",padx=34,fg="black",pady=6)
        btr4.grid(row=3,column=0)

        Quat=Label(self.adddataframe,text="Health is the greatest of",fg="darkgreen",font=("times new roman", 15,"bold"))
        Quat.place(x=300,y=110)
        Quat=Label(self.adddataframe,text="      Human blessings",fg="darkgreen",font=("times new roman", 15,"bold"))
        Quat.place(x=300,y=140)

#============================================================================================================================================
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
#==================================================================================================================================================

        #database column
        self.dataframe = Frame(self.root,bd=15,relief=RIDGE,padx=10)
        self.dataframe.place(x=0,y=500 , width=1530, height=250)

        #---scrollbar---
        Databasescroll_x=ttk.Scrollbar(self.dataframe,orient=HORIZONTAL)
        Databasescroll_x.pack(fill=X,side=BOTTOM)
        Databasescroll_y=ttk.Scrollbar(self.dataframe,orient=VERTICAL)
        Databasescroll_y.pack(fill=Y,side=RIGHT)

        self.datbase_table=ttk.Treeview(self.dataframe,column=("ref no.","companyname","type","medicine name","lot no.","issue date","exp date","uses","side effect","warning","dosage","price","Qt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        Databasescroll_x.config(command=self.datbase_table.xview)
        Databasescroll_y.config(command=self.datbase_table.yview)
        self.datbase_table["show"]="headings"

        self.datbase_table.heading("ref no.", text="Reference no.")
        self.datbase_table.heading("companyname",text="Company Name")
        self.datbase_table.heading("type",text="Medicine type")
        self.datbase_table.heading("medicine name",text="Medicine Name")
        self.datbase_table.heading("lot no.",text="Lot No.")
        self.datbase_table.heading("issue date",text="Issue Date")
        self.datbase_table.heading("exp date",text="Exp Date")
        self.datbase_table.heading("uses",text="Medicine Usage")
        self.datbase_table.heading("side effect",text="Side Effect")
        self.datbase_table.heading("warning",text="warning")
        self.datbase_table.heading("dosage",text="Dosage")
        self.datbase_table.heading("price",text="Medicine Price")
        self.datbase_table.heading("Qt",text="Medicine Qt")
        self.datbase_table.pack(fill=BOTH,expand=1)



        self.datbase_table.column("ref no.",width=100)
        self.datbase_table.column("companyname",width=100)
        self.datbase_table.column("type",width=100)
        self.datbase_table.column("medicine name",width=100)
        self.datbase_table.column("lot no.",width=100)
        self.datbase_table.column("issue date",width=100)
        self.datbase_table.column("exp date",width=100)
        self.datbase_table.column("uses",width=100)
        self.datbase_table.column("side effect",width=100)
        self.datbase_table.column("warning",width=100)
        self.datbase_table.column("dosage",width=100)
        self.datbase_table.column("price",width=100)
        self.datbase_table.column("Qt",width=100)






    def addmedicine(self):
        ref = self.addref_var.get()
        medname = self.addmed_var.get()

        # Database operation
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO new_pharmacy (ref, medname) VALUES (%s, %s)", (ref, medname))
            self.connection.commit()
            messagebox.showinfo("Success", "Medicine added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()

     
       
if __name__ == "__main__":
    root = Tk()
    obj = PharmacymanagementSystem(root)
    root.mainloop()
