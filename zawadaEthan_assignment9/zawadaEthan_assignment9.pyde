'''
Ethan Zawada
CSCI 203 Section 1
Assignment 9: Images
10/25/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''

imageList = []

imageIndex = 0

def setup():
    global imageList
    size(400, 300)
    
    frameRate(1)
    
    #Concatenation
    for i in range(6):
        stringI = str(i)
        imageList.append(loadImage("pic" + stringI + ".jpg"))
        
def draw():
    global imageList, imageIndex
    imageMode(CENTER)
    image(imageList[imageIndex], width/2, height/2, 400, 300)
    imageIndex = (imageIndex + 1) % len(imageList)
