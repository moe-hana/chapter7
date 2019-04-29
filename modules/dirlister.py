# This is code that returns all files name.

import os

def run(**arg):
	
	print("[*] In dirlister module.")
	files = os.listdir(".")

	return str(files)
