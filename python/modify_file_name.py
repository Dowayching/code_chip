import glob
import os

for f in glob.glob('IMG_8*.jpg'):
	new_filename = '_' + f
	os.rename(f, new_filename)
