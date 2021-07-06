import os
import pathlib

def solve(namePic, nameFile, nameOut):
	if not pathlib.Path(namePic).is_file():
		print("wrong input picture name")
		return
	if not pathlib.Path(nameFile).is_file():
		print("wrong input file name")
		return
	if pathlib.Path(nameOut).is_file():
		print("output file name already exist")
		return
	os.system("copy /b " + namePic + "+" + nameFile + " " + nameOut)
	print("merge succeed")

if __name__ == "__main__":
	namePic = input("picture name : ")
	nameFile = input("file name : ")
	nameOut = input("output name : ")
	solve(namePic, nameFile, nameOut)