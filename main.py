from tkinter import*
root= Tk()

root.title("Trini Ride Taxi Service")
root.geometry("400x400")
root.configure(background="white")

adminlogin_label = Label(root, text="Administrator Main Screen")
adminlogin_label.grid(row=1, column=3, padx=10, pady=10)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "New Booking Request")

#Create Button Booked

button1 = Button(root, text="New Bookings", command=onClick, height=1, width=10, padx=10, pady=10, bg="yellow")
button1.grid(row=2, column=3, columnspan=3)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "Confirm Booking")

#Create Button Confrim Booking

button2 = Button(root, text="Confirm Booking", command=onClick, height=1, width=10, padx=10, pady=10, bg="gold")
button2.grid(row=3, column=3, columnspan=3)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "Deny Booking")

#Create Button Deny Booking

button2 = Button(root, text="Deny Booking", command=onClick, height=1, width=10, padx=10, pady=10, bg="orange")
button2.grid(row=4, column=3, columnspan=3)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "Log Out")

#Create Button Log Out

button2 = Button(root, text="Log Out", command=onClick, height=1, width=10, padx=10, pady=10, bg="red")
button2.grid(row=5, column=3, columnspan=3)

root.mainloop()