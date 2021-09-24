#!/usr/bin/env python3

import os
import sys
from time import sleep
from progress.bar import Bar

print(
    """                 __     _       _     
                / _|   | |     | |    
  _______ _ __ | |_ ___| |_ ___| |__  
 |_  / _ \ '_ \|  _/ _ \ __/ __| '_ \ 
  / /  __/ | | | ||  __/ || (__| | | |
 /___\___|_| |_|_| \___|\__\___|_| |_|
                                      
                                      """
)
x = input("install, uninstall, or exit? ")

if x == "install":
    os.system("pip install wmctrl-python3")
    print("\nInstructions")
    print("Please run 'sudo ln -s '/path/to/zenfetch/main.py /usr/bin/zenfetch' in your terminal.")    
    sys.exit()

if x == "uninstall":
    print("\nUninstalling")
    sleep(2)
    print("\nMake sure you're running with root permissions.")
    sleep(2)
    with Bar('Processing...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
    os.system("sudo rm /usr/bin/zenfetch")
    print("Done")
    sys.exit()

if x == "exit":
    print("\nBye")
    sys.exit()
