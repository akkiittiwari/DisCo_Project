import numpy as np
import os
from PIL import Image
from PIL import ImageOps

floc = '/Users/shsu/Downloads/dump/' #wher you want to save it

def read_files_from_path(path): #function to read files and add date components
    list_ = []
    my_dir = os.listdir(path)
    for i in range(len(my_dir)):
    	my_sub_dir = os.listdir(path+ '/' + str(my_dir[i]))
    	for j in my_sub_dir:
            if j[-4:] == '.jpg':
        		img = Image.open(path+ '/' + str(my_dir[i]) + '/' + str(j))
        		mirror_img = ImageOps.mirror(img)

        		filename_path = floc +"1" + str(my_dir[i]) + '/'

        		try:
        			os.mkdir(filename_path)
        		except Exception:
        			pass 
            try:
                mirror_img.save(filename_path + str(j))
            except Exception:
                pass

read_files_from_path('/Users/shsu/Desktop/msan697/Project/wiki_crop')