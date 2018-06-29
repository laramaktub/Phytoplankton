import os
import sys


try:
	os.remove("synsets.txt")
	os.remove("train.txt")
except OSError:
	pass

j=0
for base, dirs, files in os.walk('.'):
		
	if ".git" in dirs:
		dirs.remove(".git")	
	for d in dirs[:]:
		
		d_sin_barras=d.replace("_"," ")
		with open("synsets.txt", "a") as myfile:
    			myfile.write(d_sin_barras+'\n')
		for i in os.listdir(d):
			with open("train.txt", "a") as afile:
				afile.write(d + "/" + os.path.relpath(i) + " " + str(j) + '\n')
		j=j+1
