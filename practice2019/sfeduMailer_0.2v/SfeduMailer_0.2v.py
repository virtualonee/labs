from tkinter import Tk, Label, Button, Text, Entry
import os
from tkinter import *
from tkinter import filedialog

import smtplib

import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("SfeduMailer")

        self.addr_from = "addr@sfedu.ru"
        self.addr_to = "addr@sfedu.ru"
        self.password = "password"
        self.titleMesg = "Приемная комиссия ЮФУ"
        self.textMesg = ""

        self.label = Label(master, text="Путь к файлу:")
        self.label.place(x=50, y=20)

        self.fileWay = Text(master, height=1, width=25)
        self.fileWay.place(x=50, y=50)
        self.path = ""

        self.label = Label(master, text="Почта получателя:")
        self.label.place(x=50, y=80)

        self.mail = Text(master, height=1, width=30)
        self.mail.place(x=50, y=110)

        self.greet_button = Button(master, text="Отправить", width=7, height=1, command=self.SendMail)
        self.greet_button.place(x=50, y=200-50)

        self.close_button = Button(master, text="Закрыть", width=7, height=1, command=master.destroy)
        self.close_button.place(x=150, y=200-50)

        self.greet_button = Button(master, text="...", width=1, height=1, command=self.SavePath)
        self.greet_button.place(x=235, y=50)

    def SavePath(self):
        self.path = filedialog.askopenfilename( filetypes = ( ("howCode files", ".txt"),("All files", "*.*")))
        self.fileWay.delete(1.0, END)
        self.fileWay.insert(INSERT, self.path)

    def attach_file(self, msg, filepath):  # Функция по добавлению конкретного файла к сообщению
        filename = os.path.basename(filepath)  # Получаем только имя файла
        ctype, encoding = mimetypes.guess_type(filepath)  # Определяем тип файла на основе его расширения
        if ctype is None or encoding is not None:  # Если тип файла не определяется
            ctype = 'application/octet-stream'  # Будем использовать общий тип
        maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
        if maintype == 'text':  # Если текстовый файл
            with open(filepath) as fp:  # Открываем файл для чтения
                file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
                fp.close()  # После использования файл обязательно нужно закрыть
        elif maintype == 'image':  # Если изображение
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':  # Если аудио
            with open(filepath, 'rb') as fp:
                file = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
        else:  # Неизвестный тип файла
            with open(filepath, 'rb') as fp:
                file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
                fp.close()
                encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
        file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
        msg.attach(file)

    def SendMail(self):
        msg = MIMEMultipart()
        self.addr_to = self.mail.get(1.0, END)
        msg['From'] = self.addr_from
        msg['To'] = self.addr_to
        msg['Subject'] = self.titleMesg
        body = self.textMesg  # Текст сообщения
        msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
        pathFile = self.path
        self.attach_file(msg, pathFile)

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.set_debuglevel(True)
        server.login(self.addr_from, self.password)
        server.send_message(msg)
        print("Отправленно")
        server.quit()

class Authorization:
    def __init__(self, master):
        self.master = master
        master.title("Вход")

        self.labelLogin = Label(master, text="Почта")
        self.labelLogin.place(x=130, y=20)

        self.addr_fromText = Text(master, height=1, width=23)
        self.addr_fromText.place(x=50, y=50)
        self.path = ""
        self.addr_fromText.insert(INSERT, "publish2018@mail.ru")

        self.labelPass = Label(master, text="Пароль")
        self.labelPass.place(x=130, y=80)

        #self.passwordText = Text(master, height=1, width=30)
        passwordText1=""
        self.passEntry = Entry(master, textvariable=passwordText1, show='*', )
        self.passwordText = passwordText1
        self.passEntry.place(x=50, y=110)

        self.greet_button = Button(master, text="Войти", width=15, height=2, command=self.EnterInMainWindow)
        self.greet_button.place(x=80, y=200 - 50)

    def EnterInMainWindow(self):
        addr_from = self.addr_fromText.get(1.0, END)
        password = self.passwordText
        print(password)
        self.master.destroy()
        root = Tk()
        root.geometry('300x200+200+100')
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.resizable(width=False, height=False)
        my_gui = MainWindow(root)
        my_gui.addr_from = addr_from
        my_gui.password = password
        root.mainloop()







root = Tk()
root.geometry('300x200+200+100')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.resizable(width=False, height=False)
my_gui = Authorization(root)
root.mainloop()