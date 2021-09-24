#!/usr/bin/env python3

import platform  
import os     
import distro   
import wmctrl

escape = "\033[1;"  
colors = [
    "30m",
    "32m",
    "36m",
    "33m",
    "37m"
]  

art = ("""
       .-.
 __   /   \   __
(  `'.\   /.'`  )
 '-._.(;;;)._.-'
 .-'  ,`"`,  '-.
(__.-'/   \'-.__)/)_
      \   /\    / / )
       '-'  |   \/.-')
       ,    | .'/\'..)
       |\   |/  | \_)
       \ |  |   \_/
        | \ /
         \|/   
""")

titles = [" ",
          " ",
          " ",
          " ",
          " "]

entry =  [distro.name(),                  
          platform.node(),                               
          f"Linux {platform.release()}",
          os.getenv('SHELL'),
          wmctrl.os.environ.get('DESKTOP_SESSION'),
]               

color = colors[1]  
reset = colors[4]  

print(art)

for title, entry in zip(titles, entry):
    print(f"{escape}{color}{title}  {escape}{reset}{entry}") 

print("\n"+" ".join([escape+color+" "*1 for color in colors])) 

print(escape+reset)  