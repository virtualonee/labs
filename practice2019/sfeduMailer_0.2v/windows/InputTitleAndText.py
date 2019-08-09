from tkinter import *
from . SendFile import SendFile
from tkinter import Tk, Label, Button, Text

class InputTitleAndText:
    def __init__(self, master, login, password):
        self.master = master
        master.title("SfeduMailer")

        self.addr_from = login
        self.password = password
        self.titleMesg = "Приемная комиссия ЮФУ"
        self.textMesg = ""

        self.label = Label(master, text="Заголовок:")
        self.label.place(x=50, y=20)

        self.titleText = Text(master, height=2, width=30)
        self.titleText.place(x=50, y=50)

        self.label = Label(master, text="Текст письма:")
        self.label.place(x=50, y=87)

        self.TextField = Text(master, height=4, width=30)
        self.TextField.place(x=50, y=110)

        self.greet_button = Button(master, text="Далее", width=7, height=1, command=self.EnterInSendFileWindowWindow)
        self.greet_button.place(x=182, y=200 - 28)

    def EnterInSendFileWindowWindow(self):

        self.titleMesg = self.titleText.get(1.0, END)
        self.textMesg = self.TextField.get(1.0, END)
        self.master.destroy()

        root = Tk()
        root.geometry('300x200+200+100')
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.resizable(width=False, height=False)
        my_gui = SendFile(root, self.addr_from, self.password, self.titleMesg, self.textMesg)
        root.mainloop()


