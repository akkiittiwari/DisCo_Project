from PIL import Image
import numpy as np 
import os 
from PIL import Image 
from PIL import ImageOps 

'''[[135 137 138 ..., 148 131  92]
 [136 137 138 ..., 149 134  96]
 [137 138 138 ..., 149 135  96]
 ...,   
 [ 20  21  24 ...,  71  71  70]
 [ 21  22  26 ...,  68  70  73]
 [ 23  24  28 ...,  67  69  75]]'''

# create 1 pandas dataframe with 128 * 128 = 16384 columns with 1 pixel per column 

data = pd.DataFrame([])


def img_to_pixels(path): #function to read files and add date components 
 	list_ = [] 
 	my_dir = os.listdir(path) 
 	for i in range(len(my_dir)): 
 		my_sub_dir = os.listdir(path+ '/' + str(my_dir[i])) 
 		for j in my_sub_dir: 
 			img = Image.open(path+ '/' + str(my_dir[i]) + '/' + str(j)) 
			the_pixels =  (np.array(img))
			y = the_pixels.shape[0]
			x = the_pixels.shape[1]
			for i in range(0,y):
   				for j in range(0,x):
        			# add into a column ...


def turnToNumpy(files):
    """
    turn stored images on disk to numpy
    turnToNumpy('/home/username/XYZFolder/
    """  
    temp = []
    y = []
    print "Total Count of Files",len(files)
    responseArray = []
    for fileName in files:
                try:
                    if fileName.endswith(".jpg" or ".jpeg" or ".png"):
                        matchObj = re.search( r'nm*\d+_rm\d+_(\d+)-\d+-\d+_(\d+).jpg', fileName, re.M|re.I)
                        # yob - year of birth
                        # dopt - date of photo taken
                        yob =  matchObj.group(1) 
                        dopt =  matchObj.group(2)
						# print yob,dopt, int(dopt)-int(yob)
                        diff  = int(dopt)-int(yob)
                        if int(diff) > 0 and int(diff) <100:
						# print type(int(dopt)-int(yob)),diff,diff > 0
                            individualResponse = [0]*100
                            individualResponse[diff] =1 
                            responseArray.append(individualResponse)
							# responseArray.append(diff/100)
                            temp.append(load_image(fileName))
							# y.append(abs(int(dopt)-int(yob)))
                except:
                    ""
    return np.asarray(temp, dtype='float32'),np.asarray(responseArray, dtype='bool')

			
