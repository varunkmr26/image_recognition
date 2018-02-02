#For testing use only images of 8 by 8 dimensions. 
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
from collections import Counter
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

def whatNumIsThis(filePath):
    
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    loadExamps = loadExamps[:-1];   
    i = Image.open(filePath)
    iar = np.array(i)
#The next 5 lines of code only if alpha channel is turned off
#    z = np.ones((8,1),dtype = np.uint8)
#    z = z * 255
#    niar = np.zeros((8,8,4),dtype = np.uint8)
#    for i in range(0,8):
#        niar[i] = np.append(iar[i], z,axis = 1)
    tiar = threshold(iar)#Use niar if alpha channel is turned off
    iarl = tiar.tolist()
    
    inQuestion = str(iarl)
    maxno = 0
    maxc = 0
    curc = 0
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            
            x = 0
            curc = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                    curc += 1
                if (curc > maxc):
                    maxc = curc
                    maxno = currentNum
                x+=1
            
        except Exception as e:
            print(str(e))

    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []
    
    ylimi = 0
    
    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    print("The number detected is: " + str(maxno))
    plt.show()

whatNumIsThis('images/test/test5.png')