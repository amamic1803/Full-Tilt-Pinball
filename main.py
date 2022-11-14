import os
import sys
import time
from tkinter import *
from tkinter.messagebox import showerror

import pygetwindow
from PIL import Image, ImageTk


def resource_path(relative_path=""):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def ext(event):
	root.destroy()

def cadet(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Cadet\\CADET.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! - Space Cadet" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! - Space Cadet")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! - Space Cadet" in pygetwindow.getAllTitles():
		time.sleep(5)

def pirates(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Pirates\\PIRATES.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! - Skulduggery" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! - Skulduggery")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! - Skulduggery" in pygetwindow.getAllTitles():
		time.sleep(5)

def dragon(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Dragon\\DRAGON.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! - Dragon's Keep" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! - Dragon's Keep")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! - Dragon's Keep" in pygetwindow.getAllTitles():
		time.sleep(5)

def scientist(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Mad\\mad.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! 2 - Mad Scientist" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! 2 - Mad Scientist")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! 2 - Mad Scientist" in pygetwindow.getAllTitles():
		time.sleep(5)

def captain(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Hero\\hero.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! 2 - Captain Hero" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! 2 - Captain Hero")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! 2 - Captain Hero" in pygetwindow.getAllTitles():
		time.sleep(5)

def alien(event):
	global current_folder
	os.startfile(os.path.join(current_folder, "boards/Alien\\alien.EXE"))
	start = time.time()
	while time.time() - start <= 100:
		time.sleep(0.1)
		if "Full Tilt! 2 - Alien Daze" in pygetwindow.getAllTitles():
			window = pygetwindow.getWindowsWithTitle("Full Tilt! 2 - Alien Daze")[0]
			window.minimize()
			window.restore()
			window.moveTo((root.winfo_screenwidth() - window.width) // 2, (root.winfo_screenheight() - window.height) // 2)
			window.minimize()
			window.restore()
			window.activate()
			window.activate()
			break
	root.destroy()
	while "Full Tilt! 2 - Alien Daze" in pygetwindow.getAllTitles():
		time.sleep(5)

def ext_enter(event):
	global x_sign
	ext_cnv.configure(background="red")
	ext_cnv.itemconfigure(x_sign[0], fill="white")
	ext_cnv.itemconfigure(x_sign[1], fill="white")

def ext_leave(event):
	global x_sign
	ext_cnv.configure(background="#1C263B")
	ext_cnv.itemconfigure(x_sign[0], fill="grey")
	ext_cnv.itemconfigure(x_sign[1], fill="grey")

def cadet_enter(event):
	cnv_cadet.config(background="#263450")

def cadet_leave(event):
	cnv_cadet.config(background="#1C263B")

def pirates_enter(event):
	cnv_pirates.config(background="#263450")

def pirates_leave(event):
	cnv_pirates.config(background="#1C263B")

def dragon_enter(event):
	cnv_dragon.config(background="#263450")

def dragon_leave(event):
	cnv_dragon.config(background="#1C263B")

def scientist_enter(event):
	cnv_scientist.config(background="#263450")

def scientist_leave(event):
	cnv_scientist.config(background="#1C263B")

def captain_enter(event):
	cnv_captain.config(background="#263450")

def captain_leave(event):
	cnv_captain.config(background="#1C263B")

def alien_enter(event):
	cnv_alien.config(background="#263450")

def alien_leave(event):
	cnv_alien.config(background="#1C263B")


if __name__ == '__main__':

	current_folder = resource_path()
	running = False
	for i in ["Full Tilt! - Space Cadet", "Full Tilt! - Skulduggery", "Full Tilt! - Dragon's Keep", "Full Tilt! 2 - Mad Scientist", "Full Tilt! 2 - Captain Hero", "Full Tilt! 2 - Alien Daze"]:
		if i in pygetwindow.getAllTitles():
			running = True

	if not running:
		root = Tk()
		root.overrideredirect(True)
		root.geometry(f"510x400+{(root.winfo_screenwidth() - 510) // 2}+{(root.winfo_screenheight() - 400) // 2}")
		root.resizable(False, False)
		root.wm_attributes("-topmost", True)
		root.config(background="#1C263B")

		title_1 = Label(root, background="#1C263B", text="Full Tilt! Pinball", font=("Helvetica", 13, "italic"), foreground="light grey")
		title_1.place(x=46, y=0, width=418, height=30)
		title_2 = Label(root, background="#1C263B", text="Full Tilt! Pinball 2", font=("Helvetica", 13, "italic"), foreground="light grey")
		title_2.place(x=46, y=200, width=418, height=30)

		ext_cnv = Canvas(root, background="#1C263B", highlightthickness=0)
		ext_cnv.place(x=464, y=0, height=30, width=46)
		x_sign = (ext_cnv.create_line(18, 10, 29, 21, fill="grey"), ext_cnv.create_line(18, 20, 29, 9, fill="grey"))
		ext_cnv.bind("<ButtonRelease-1>", ext)
		ext_cnv.bind("<Enter>", ext_enter)
		ext_cnv.bind("<Leave>", ext_leave)

		img_cadet = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Cadet\\CADET.bmp")).crop((5, 5, 115, 115)))
		img_pirates = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Pirates\\PIRATES.bmp")).crop((5, 5, 115, 115)))
		img_dragon = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Dragon\\DRAGON.bmp")).crop((5, 5, 115, 115)))
		img_scientist = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Mad\\Mad.bmp")).crop((5, 5, 115, 115)))
		img_captain = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Hero\\Hero.bmp")).crop((5, 5, 115, 115)))
		img_alien = ImageTk.PhotoImage(Image.open(os.path.join(current_folder, "boards/Alien\\Alien.bmp")).crop((5, 5, 115, 115)))

		cnv_cadet = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_cadet.place(x=0, y=30, width=170, height=170)
		cnv_pirates = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_pirates.place(x=170, y=30, width=170, height=170)
		cnv_dragon = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_dragon.place(x=340, y=30, width=170, height=170)
		cnv_cadet.create_image(85, 85, image=img_cadet, anchor="center")
		cnv_pirates.create_image(85, 85, image=img_pirates, anchor="center")
		cnv_dragon.create_image(85, 85, image=img_dragon, anchor="center")
		cnv_cadet.bind("<ButtonRelease-1>", cadet)
		cnv_cadet.bind("<Enter>", cadet_enter)
		cnv_cadet.bind("<Leave>", cadet_leave)
		cnv_pirates.bind("<ButtonRelease-1>", pirates)
		cnv_pirates.bind("<Enter>", pirates_enter)
		cnv_pirates.bind("<Leave>", pirates_leave)
		cnv_dragon.bind("<ButtonRelease-1>", dragon)
		cnv_dragon.bind("<Enter>", dragon_enter)
		cnv_dragon.bind("<Leave>", dragon_leave)

		cnv_scientist = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_scientist.place(x=0, y=230, width=170, height=170)
		cnv_captain = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_captain.place(x=170, y=230, width=170, height=170)
		cnv_alien = Canvas(root, background="#1C263B", highlightthickness=0, cursor="tcross")
		cnv_alien.place(x=340, y=230, width=170, height=170)
		cnv_scientist.create_image(85, 85, image=img_scientist, anchor="center")
		cnv_captain.create_image(85, 85, image=img_captain, anchor="center")
		cnv_alien.create_image(85, 85, image=img_alien, anchor="center")
		cnv_scientist.bind("<ButtonRelease-1>", scientist)
		cnv_scientist.bind("<Enter>", scientist_enter)
		cnv_scientist.bind("<Leave>", scientist_leave)
		cnv_captain.bind("<ButtonRelease-1>", captain)
		cnv_captain.bind("<Enter>", captain_enter)
		cnv_captain.bind("<Leave>", captain_leave)
		cnv_alien.bind("<ButtonRelease-1>", alien)
		cnv_alien.bind("<Enter>", alien_enter)
		cnv_alien.bind("<Leave>", alien_leave)

		root.mainloop()
	else:
		showerror("ERROR!", "ALREADY RUNNING!")
