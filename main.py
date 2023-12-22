import os
import sys
import time
from tkinter import Canvas, Label, Tk
from tkinter.messagebox import showerror

import pygetwindow
from PIL import Image, ImageTk


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)


class App:
	def __init__(self):
		for board in ["Full Tilt! - Space Cadet", "Full Tilt! - Skulduggery", "Full Tilt! - Dragon's Keep",
		              "Full Tilt! 2 - Mad Scientist", "Full Tilt! 2 - Captain Hero", "Full Tilt! 2 - Alien Daze"]:
			if board in pygetwindow.getAllTitles():
				showerror("ERROR!", "ALREADY RUNNING!")
				return

		self.root = Tk()
		self.root.overrideredirect(True)
		self.root.wm_attributes("-topmost", True)
		self.root.geometry(f"510x400"
		                   f"+{(self.root.winfo_screenwidth() - 510) // 2}"
		                   f"+{(self.root.winfo_screenheight() - 400) // 2}")
		self.root.resizable(False, False)
		self.root.config(background="#1C263B")

		self.title_1 = Label(self.root, text="Full Tilt! Pinball", font=("Helvetica", 13, "italic"),
		                     background="#1C263B", foreground="light grey")
		self.title_1.place(x=46, y=0, width=418, height=30)

		self.title_2 = Label(self.root, text="Full Tilt! Pinball 2", font=("Helvetica", 13, "italic"),
		                     background="#1C263B", foreground="light grey")
		self.title_2.place(x=46, y=200, width=418, height=30)

		self.ext_cnv = Canvas(self.root, background="#1C263B", highlightthickness=0)
		self.ext_cnv.place(x=464, y=0, height=30, width=46)
		self.x_sign = (
			self.ext_cnv.create_line(18, 10, 29, 21, fill="grey"),
			self.ext_cnv.create_line(18, 20, 29, 9, fill="grey"),
		)
		self.ext_cnv.bind("<ButtonRelease-1>", lambda event: self.root.destroy())
		self.ext_cnv.bind("<Enter>", lambda event: self.ext_enter())
		self.ext_cnv.bind("<Leave>", lambda event: self.ext_leave())

		self.img_cadet = ImageTk.PhotoImage(Image.open(resource_path("boards/Cadet/CADET.bmp")).crop((5, 5, 115, 115)))
		self.img_pirates = ImageTk.PhotoImage(Image.open(resource_path("boards/Pirates/PIRATES.bmp")).crop((5, 5, 115, 115)))
		self.img_dragon = ImageTk.PhotoImage(Image.open(resource_path("boards/Dragon/DRAGON.bmp")).crop((5, 5, 115, 115)))
		self.img_scientist = ImageTk.PhotoImage(Image.open(resource_path("boards/Mad/Mad.bmp")).crop((5, 5, 115, 115)))
		self.img_captain = ImageTk.PhotoImage(Image.open(resource_path("boards/Hero/Hero.bmp")).crop((5, 5, 115, 115)))
		self.img_alien = ImageTk.PhotoImage(Image.open(resource_path("boards/Alien/Alien.bmp")).crop((5, 5, 115, 115)))

		self.cnv_cadet = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_cadet.place(x=0, y=30, width=170, height=170)
		self.cnv_cadet.create_image(85, 85, image=self.img_cadet, anchor="center")
		self.cnv_cadet.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! - Space Cadet", "boards/Cadet/CADET.EXE"))
		self.cnv_cadet.bind("<Enter>", lambda event: self.cnv_cadet.config(background="#263450"))
		self.cnv_cadet.bind("<Leave>", lambda event: self.cnv_cadet.config(background="#1C263B"))

		self.cnv_pirates = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_pirates.place(x=170, y=30, width=170, height=170)
		self.cnv_pirates.create_image(85, 85, image=self.img_pirates, anchor="center")
		self.cnv_pirates.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! - Skulduggery", "boards/Pirates/PIRATES.EXE"))
		self.cnv_pirates.bind("<Enter>", lambda event: self.cnv_pirates.config(background="#263450"))
		self.cnv_pirates.bind("<Leave>", lambda event: self.cnv_pirates.config(background="#1C263B"))

		self.cnv_dragon = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_dragon.place(x=340, y=30, width=170, height=170)
		self.cnv_dragon.create_image(85, 85, image=self.img_dragon, anchor="center")
		self.cnv_dragon.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! - Dragon's Keep", "boards/Dragon/DRAGON.EXE"))
		self.cnv_dragon.bind("<Enter>", lambda event: self.cnv_dragon.config(background="#263450"))
		self.cnv_dragon.bind("<Leave>", lambda event: self.cnv_dragon.config(background="#1C263B"))

		self.cnv_scientist = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_scientist.place(x=0, y=230, width=170, height=170)
		self.cnv_scientist.create_image(85, 85, image=self.img_scientist, anchor="center")
		self.cnv_scientist.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! 2 - Mad Scientist", "boards/Mad/mad.EXE"))
		self.cnv_scientist.bind("<Enter>", lambda event: self.cnv_scientist.config(background="#263450"))
		self.cnv_scientist.bind("<Leave>", lambda event: self.cnv_scientist.config(background="#1C263B"))

		self.cnv_captain = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_captain.place(x=170, y=230, width=170, height=170)
		self.cnv_captain.create_image(85, 85, image=self.img_captain, anchor="center")
		self.cnv_captain.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! 2 - Captain Hero", "boards/Hero/hero.EXE"))
		self.cnv_captain.bind("<Enter>", lambda event: self.cnv_captain.config(background="#263450"))
		self.cnv_captain.bind("<Leave>", lambda event: self.cnv_captain.config(background="#1C263B"))

		self.cnv_alien = Canvas(self.root, background="#1C263B", highlightthickness=0, cursor="hand2")
		self.cnv_alien.place(x=340, y=230, width=170, height=170)
		self.cnv_alien.create_image(85, 85, image=self.img_alien, anchor="center")
		self.cnv_alien.bind("<ButtonRelease-1>", lambda event: self.run_board("Full Tilt! 2 - Alien Daze", "boards/Alien/alien.EXE"))
		self.cnv_alien.bind("<Enter>", lambda event: self.cnv_alien.config(background="#263450"))
		self.cnv_alien.bind("<Leave>", lambda event: self.cnv_alien.config(background="#1C263B"))

		self.root.mainloop()

	def ext_enter(self):
		self.ext_cnv.configure(background="red")
		self.ext_cnv.itemconfigure(self.x_sign[0], fill="white")
		self.ext_cnv.itemconfigure(self.x_sign[1], fill="white")

	def ext_leave(self):
		self.ext_cnv.configure(background="#1C263B")
		self.ext_cnv.itemconfigure(self.x_sign[0], fill="grey")
		self.ext_cnv.itemconfigure(self.x_sign[1], fill="grey")

	def run_board(self, board, path):
		os.startfile(resource_path(path))
		start = time.time()
		while time.time() - start <= 100:
			time.sleep(0.1)
			if board in pygetwindow.getAllTitles():
				window = pygetwindow.getWindowsWithTitle(board)[0]
				window.minimize()
				window.restore()
				window.moveTo((self.root.winfo_screenwidth() - window.width) // 2,
				              (self.root.winfo_screenheight() - window.height) // 2)
				window.minimize()
				window.restore()
				window.activate()
				window.activate()
				break
		self.root.destroy()
		while board in pygetwindow.getAllTitles():
			time.sleep(5)


def main():
	App()


if __name__ == '__main__':
	main()
