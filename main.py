from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("300x300")
def msg():
    messagebox.showwarning("ALERT","stop! virus found")
btn=Button(window,text="scan for virus",command=msg)
btn.pack()
window.mainloop()
