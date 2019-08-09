import os
from tkinter import *
from tkinter import filedialog
from . Success import Success

import smtplib
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

class SendFile:
    def __init__(self, master, login, password, title, text):
        self.master = master
        master.title("SfeduMailer")

        self.addr_from = login
        self.addr_to = ""
        self.password = password
        self.titleMesg = title
        self.textMesg = text
        self.path = ""

        self.label = Label(master, text="Путь к файлу:")
        self.label.place(x=50, y=20)

        self.fileWay = Text(master, height=1, width=25)
        self.fileWay.place(x=50, y=50)

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

    def attach_file(self, msg, filepath):
        filename = os.path.basename(filepath)
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            with open(filepath) as fp:
                file = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'image':
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':
            with open(filepath, 'rb') as fp:
                file = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
        else:
            with open(filepath, 'rb') as fp:
                file = MIMEBase(maintype, subtype)
                file.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file)

    def SendMail(self):
        msg = MIMEMultipart()
        self.addr_to = self.mail.get(1.0, END)
        msg['From'] = self.addr_from
        msg['To'] = self.addr_to
        msg['Subject'] = self.titleMesg
        body = self.textMesg
        msg.attach(MIMEText(body, 'plain'))
        pathFile = self.path
        self.attach_file(msg, pathFile)

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.set_debuglevel(True)
        server.login(self.addr_from, self.password)
        server.send_message(msg)
        server.quit()

        root = Tk()
        root.geometry('300x70+200+100')
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 4
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4
        root.wm_geometry("+%d+%d" % (x*3+100, y*3+100))
        root.resizable(width=False, height=False)
        my_gui = Success(root)
        root.mainloop()


