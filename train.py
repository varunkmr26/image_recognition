from PIL import Image
import numpy as np

#The runs all the images from my training data and add the pixels details
#to the numArExx.txt filr
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    #numbersWeHave = range(1,10)
    for eachNum in range(0,10):
        for furtherNum in range(1,10):

            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)


createExamples()