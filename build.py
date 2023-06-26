import os
import random
import shutil
import sys

import PyInstaller.__main__


def build(name, version, console, onefile, uac_admin, icon, files, folders):
	work_path = "build"
	while os.path.isdir(work_path):
		work_path = f"build_{random.randint(1, 1_000_000_000)}"
	work_path = os.path.join(os.path.abspath("."), work_path)

	result_path = os.path.abspath(".")

	run_list = ['main.py',
	            '--noconfirm',
	            '--clean',
	            '--name', f"{name}-v{version}",
	            '--workpath', work_path,
	            '--specpath', work_path,
	            '--distpath', result_path]

	if console:
		run_list.append("--console")
	else:
		run_list.append("--noconsole")

	if onefile:
		run_list.append("--onefile")
	else:
		run_list.append("--onedir")

	if uac_admin:
		run_list.append("--uac-admin")

	if icon != "":
		icon_path = os.path.join(os.path.abspath("."), icon)
		if not os.path.isfile(icon_path):
			raise Exception("Invalid icon!")
		else:
			run_list.extend(('--icon', icon_path))

	for file in files:
		if os.path.isfile(os.path.join(os.path.abspath("."), file)):
			run_list.extend(('--add-data', f'{os.path.join(os.path.abspath("."), file)};{os.path.dirname(file)}'))
		else:
			raise Exception("Invalid file!")

	for folder in folders:
		if os.path.isdir(folder):
			for walk in os.walk(folder, followlinks=False):
				for file in walk[2]:
					if os.path.isfile(os.path.join(walk[0], file)):
						run_list.extend(('--add-data', f'{os.path.join(os.path.abspath("."), os.path.join(walk[0], file))};{os.path.dirname(os.path.join(walk[0], file))}'))
					else:
						raise Exception("Invalid folder!")
		else:
			raise Exception("Invalid folder!")

	PyInstaller.__main__.run(run_list)
	shutil.rmtree(path=work_path, ignore_errors=True)

def main():
	name = "Full-Tilt!-Pinball"
	version = "4.0.1"

	console = False
	onefile = True
	uac_admin = False
	icon = "full-tilt-icon.ico"

	files = []
	folders = ["boards"]

	if len(sys.argv) > 1 and sys.argv[1] == "--version":
		print(version)
	elif len(sys.argv) > 1 and sys.argv[1] == "--name":
		print(name)
	else:
		build(name, version, console, onefile, uac_admin, icon, files, folders)


if __name__ == '__main__':
	main()
