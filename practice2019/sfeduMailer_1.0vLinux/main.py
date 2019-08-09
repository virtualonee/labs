from windows.Auth import Authorization
from tkinter import *
from db.data import Data


data = Data()
dataDef = data.Get()



root = Tk()
root.geometry('300x200+200+100')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.resizable(width=False, height=False)
my_gui = Authorization(root, dataDef)
root.mainloop()
