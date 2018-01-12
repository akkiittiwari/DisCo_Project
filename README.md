# DisCo_Project

Preprocessing:

1. First run the flip.py to get the mirrored images into a certain directory

2. Second, run the resize.py on BOTH the original photos as well as the mirrored images 


Useful Links:

Logistic Regression in Spark for images:
https://medium.com/linagora-engineering/making-image-classification-simple-with-spark-deep-learning-f654a8b876b8

Some of our project information
https://docs.google.com/document/d/12hIHMe3JidhVz9ysI4MKhEljzSekDJXpbVAcesHH8Tk/edit

Image resizing / similar project to this 
https://www.machinelearningpython.org/single-post/face-to-Age-Prediction


More Brainstorming:

- what size should you resize the images to be ?
- need to take in an image file and then convert it into pixels (this can be done using np.array(image) ) 
- Each image is 1 row
- First n-1 columns are 1 pixel from the image
- the last column is the actual age of the person 
- fit a model to the data to predict the age column
- new input image: convert to pixels then use the model .transform() to get the predicted age value
