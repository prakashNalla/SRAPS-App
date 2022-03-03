

__version__ = "1.0.0"


from kivymd.app import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.label import *
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivymd.toast import *
from kivy.uix.scrollview import *
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.uix.carousel import Carousel
from kivymd.uix.expansionpanel import *
import requests
import webbrowser
import os
import os
import subprocess
import sys
import threading
from pathlib import Path
from kivy.clock import Clock
from functools import partial
from kivymd.icon_definitions import md_icons
from kivy.utils import platform
from kivy.core.window import Window
import time
import _thread


screen_manager = ScreenManager()
if platform != "android":
	Window.size =(360,640)

def check_intr():
	import requests
	try:
		requests.get("https://motherfuckingwebsite.com",timeout=0.2)
	except Exception as e:
		print(str(e))
		return False
	return True

	
def getDb():
	apiUrl = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/app.database"
	try:
		a = requests.get(apiUrl,timeout=1)
		open('dataDb.py', 'wb').write(a.content)
		import dataDb
		from dataDb import DataBase
	except Exception as e:
		return exit(str(e))
	return DataBase

class SRAPS_APP(MDApp):
	def colorHex(self, color):
		return get_color_from_hex(color)
	screen_manager = screen_manager
	if check_intr() == True:
		DataBase = getDb()
		SliderImages = DataBase["SilderImages"]
		News = DataBase["News"]
	else:
		SliderImages=["https://github.githubassets.com/images/mona-loading-default.gif","https://github.githubassets.com/images/mona-loading-default.gif","https://github.githubassets.com/images/mona-loading-default.gif","https://github.githubassets.com/images/mona-loading-default.gif","https://github.githubassets.com/images/mona-loading-default.gif"]
		News="No Internet"
	def build(self):

		screen_manager.add_widget(Builder.load_file('main.kv'))
		screen_manager.current = "Mscreen"
		return screen_manager
			
SRAPS_APP().run()