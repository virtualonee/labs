from tkinter import *

class Success:
    def __init__(self, master):
        self.master = master
        master.title("SfeduMailer")

        self.labelLogin = Label(master, text="Письмо успешно отправлено ")
        self.labelLogin.place(x=70, y=20)

        self.greet_button = Button(master, text="Закрыть", width=5, height=1, command=master.destroy)
        self.greet_button.place(x=120, y=40)
