# DisCo_Project

Preprocessing:

1. First run the flip.py to get the mirrored images into a certain directory

2. Second, run the resize.py on BOTH the original photos as well as the mirrored images so that they are all same size

3. Lastly, load the images and run logistic regression on the pixels to classify age.

Check out final.ipynb to see what we actually did.



Steps not included in the code :

1. Pulling raw data from S3 into our AWS instance 

2. Unzipping and arranging the data in the instance for easy access

- These steps can be avoided by directly pulling the data from S3 on runtime but in our case as the dataset is of fixed limited size, this way works better.



Useful Links used by us:

Logistic Regression in Spark for images:
https://medium.com/linagora-engineering/making-image-classification-simple-with-spark-deep-learning-f654a8b876b8

Running Spark, Python and Jupyter Notebook on AWS :
https://medium.com/@josemarcialportilla/getting-spark-python-and-jupyter-notebook-running-on-amazon-ec2-dec599e1c297

Image resizing / similar project to this 
https://www.machinelearningpython.org/single-post/face-to-Age-Prediction


