# pharmacy
from tkinter import *

class pharmacymanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg="white", fg="darkblue", font=("times new roman", 24), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

if __name__ == "__main__":
    root = Tk()
    obj = pharmacymanagementSystem(root)
    root.mainloop()
    rtg55
