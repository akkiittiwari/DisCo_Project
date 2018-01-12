import numpy as np
import os
from PIL import Image
from PIL import ImageOps
import glob

# path of file
path='/Users/davidkes/classes/697/Project/wiki_crop/'
# where to put the dump the mirror images
floc = '/Users/davidkes/classes/697/Project/dump/'
def read_files_from_path(path,floc):  # function to read files and add date components
    my_dir = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    try:
        os.mkdir(floc)
    except:
        pass

    for i in my_dir:
        my_sub_dir = glob.glob(path + i + '/*.jpg')
        filepathname = floc + '1' + i + '/'
        try:
            os.mkdir(filepathname)
        except:
            pass
        for j in my_sub_dir:
            img = Image.open(j)
            mirror_img = ImageOps.mirror(img)
            mirror_img.save(filepathname + j.split('/')[-1])


read_files_from_path(path,floc)

