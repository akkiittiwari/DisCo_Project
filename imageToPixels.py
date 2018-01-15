from PIL import Image
from PIL import ImageOps 
import numpy as np 
import os 

import glob
import re


def load_image2(infilename) :
    '''  
    convert image file to pixels
    load_image2('fileName')
    '''
    img = Image.open(infilename)
    data = np.array(img)
    return data


def ageAtPhoto(fileName):
    '''
    get age at time of photo 
    ageAtPhoto('full_path_to_file')
    10049200_1891-09-16_1958.jpg
    yob is 1891
    dtpt is 1958 
    '''
    tailPath = os.path.basename(fileName)
    matchObj = re.search(r'^[^_]+_([^_]+)_[^_]+$', tailPath)
    yob = int(matchObj.group(1)[:4])
    nojpg = matchObj.group(0)[:-4]
    dtpt = int(nojpg[-4:])
    currAge = abs(dtpt - yob)
    return currAge


def convertToNumpy(folder):
    '''
    get pixels and age for each image in a folder
    x_values, y_values = convertToNumpy(fileNames)    
    '''
    pixels = []
    ages = []
    for fileName in folder:
        if fileName.endswith(".jpg" or ".jpeg" or ".png"):
            pixels.append(load_image2(fileName))
            ages.append(ageAtPhoto(fileName))
    return pixels, ages


# Running This:    

folderName = '/Users/mbk/desktop/wiki_crop/' 
fileNames = glob.glob(folderName +'*_resized/*.jpg')
# only test 20 files for now
NumberOfFileToBetested = 20

# x_values, y_values = convertToNumpy(fileNames[:NumberOfFileToBetested])

# print x_values
# print y_values 
