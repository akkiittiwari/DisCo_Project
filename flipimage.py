import numpy as np
import os
from PIL import Image
from PIL import ImageOps
import glob

# path of file
path = '/Users/davidkes/classes/697/Project/wikitemp/'
# where to put the dump the mirror images
floc = '/Users/davidkes/classes/697/Project/dump/'


def read_files_from_path(path, floc):  # function to read files and add date components
    try:
        os.mkdir(floc)
    except:
        pass
    my_sub_dir = glob.glob(path + '*/*.jpg')
    for j in my_sub_dir:
        img = Image.open(j)
        mirror_img = ImageOps.mirror(img)
        inx = j.split('/')
        try:
            os.mkdir(floc + '1' + inx[-2])
        except:
            pass
        mirror_img.save(floc + '1' + '/'.join(inx[-2:]))


read_files_from_path(path, floc)
