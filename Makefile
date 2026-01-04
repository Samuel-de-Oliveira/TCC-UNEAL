FILE = Main.py

all:
	pyinstaller -F $(FILE)

run:
	python $(FILE)
