from tkinter import *
from PIL import Image, ImageTk

class pharmacymanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg="white", fg="darkblue", font=("times new roman", 24), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("C:\\Users\\Ohm Gaud\\OneDrive\\Desktop\\pharmacy project\\pharma1.jpeg")
        img1 = img1.resize((50, 50))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Use Label instead of BufferError for displaying the image
        b1 = Label(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=30, y=10)

if __name__ == "__main__":
    root = Tk()
    obj = pharmacymanagementSystem(root)
    root.mainloop()
    #******************************************dataframe*********************************
Dataframe=Frame(self.root, bd=15, relief=RIDGE , padx=20)
Dataframe.place(x=0,y=120,width=1230,height=400)
