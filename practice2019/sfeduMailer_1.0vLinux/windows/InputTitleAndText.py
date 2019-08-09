from tkinter import *
from . SendFile import SendFile
from tkinter import Tk, Label, Button, Text

class InputTitleAndText:
    def __init__(self, master, login, password, dataDef):
        self.master = master
        master.title("SfeduMailer")

        self.dataDef = dataDef
        self.addr_from = login
        self.password = password
        self.titleMesg = "Приемная комиссия ЮФУ"
        self.textMesg = ""

        self.label = Label(master, text="Заголовок:")
        self.label.place(x=50, y=15)

        self.titleText = Text(master, height=2, width=30)
        self.titleText.place(x=50, y=40)
        self.titleText.insert(INSERT,self.dataDef["title"])

        self.label = Label(master, text="Текст письма:")
        self.label.place(x=50, y=77)

        self.TextField = Text(master, height=3, width=30)
        self.TextField.place(x=50, y=100)
        self.TextField.insert(INSERT, self.dataDef["text"])

        self.greet_button = Button(master, text="Далее", width=7, height=1, command=self.EnterInSendFileWindowWindow)
        self.greet_button.place(x=182, y=200 - 40)

    def EnterInSendFileWindowWindow(self):

        title = self.titleText.get(1.0, END)
        text = self.TextField.get(1.0, END)
        self.master.destroy()

        self.dataDef["title"] = title
        self.dataDef["text"] = text

        root = Tk()
        root.geometry('300x200+200+100')
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.resizable(width=False, height=False)
        SendFile(root, self.addr_from, self.password, title, text, self.dataDef)
        root.mainloop()


