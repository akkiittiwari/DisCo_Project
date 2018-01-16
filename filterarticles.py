import os
import glob

path = '/Users/davidkes/classes/697/Project/wiki_crop/'
# b = os.path.getsize("/path/isa_005.mp3")

for i in os.listdir(path):
    if len(i) < 5:
        for j in os.listdir(path + str(i)):
            if os.path.getsize(path + str(i) + '/' + str(j)) < 2000:
                # print(path + str(i) + '/' + str(j))
                os.remove(path + str(i) + '/' + str(j))
