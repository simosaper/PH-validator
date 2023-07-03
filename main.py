#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 


#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from requests import get
from pyfiglet import Figlet
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor
from rich import print
from datetime import datetime
import json
import ctypes
import sys
import tkinter as tk
from tkinter import filedialog


try:
    os.mkdir('Results')
except:
    pass

#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
class Bot():
    def __init__(self):
        self.valid_numbers = 0
        self.invalid_numbers = 0
        self.checked_numbers = 0

    def Checker(self, i):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://telnyx.com/",
            "origin": "https://telnyx.com",
        }
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        try:
            response = get(url=f"https://api.telnyx.com/anonymous/v2/number_lookup/{i}", headers=headers, allow_redirects=False)
            data = response.json()['data']
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
            if data['valid_number']:
                carrier_name = data['carrier']['name']
                self.valid_numbers += 1
                print(f"[green][{datetime.now().strftime('%H:%M:%S')}] Valid Number: {i} | Carrier: {carrier_name}[/green]")
                with open(f"Results/{carrier_name}.txt", "a") as save_file:
                    save_file.write(f"\n{i}")
            else:
                self.invalid_numbers += 1
                print(f"[red][{datetime.now().strftime('%H:%M:%S')}] Die Number: {i}[/red]")
                with open("Results/die.txt", "a") as save_invalid:
                    save_invalid.write(f"\n{i}")
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
            self.checked_numbers += 1
            self.update_title()
        except Exception as e:
            self.update_title()
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
    def update_title(self):
        title = f"Valid Numbers: {self.valid_numbers} | Invalid Numbers: {self.invalid_numbers} | Checked Numbers: {self.checked_numbers} | WeedyDev"
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            sys.stdout.write(f'\x1b]2;{title}\x07')

    def choose_file(self):
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
     
        root = tk.Tk()
        root.withdraw()
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
         
        file_path = filedialog.askopenfilename(title="Choose the file to check")
        return file_path

if __name__ == '__main__':
    bot = Bot()
    console = Console()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font="standard")
        console.print(f.renderText("Blackhat Egypt"), style="green")
        
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        console.print("[bold magenta]CODED BY  | @simosaper11 | Channel:- https://t.me/simosaper [/bold magenta]")
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        console.print('')

        try:
            inpFile = bot.choose_file()
            threads = []
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
             
            with open(inpFile) as NumList:
                argFile = NumList.read().splitlines()
                total_numbers = len(argFile)
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
            with ThreadPoolExecutor(max_workers=50) as executor:  # prefer 50 if use rdp can keep upto 100-200 :)
                for data in argFile:
                    threads.append(executor.submit(bot.Checker, data))

           
            for thread in threads:
                thread.result()
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
            bot.update_title()
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        except Exception as e:
            console.print(e)
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 
        input("Press Enter to exit...")
        break
        
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
 