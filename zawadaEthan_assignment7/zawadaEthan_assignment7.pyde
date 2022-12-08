'''
Ethan Zawada
CSCI 203 Section 1
Assignment 7: List and Append
10/25/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''

generateHamster = False
xPos = 650

def setup():
    size(600, 450)
    background(255)
    frameRate(10)
    
def draw():
    global generateHamster, xPos
    hamsterList = []
    
    #append the list to create hamsters
    if generateHamster:
        background(255)
        for i in range(50):
            hamsterList.append(hamster(xPos, random(450), random(255)))
            
            xPos += 10
            if(xPos >= 650):
                xPos = -50
    
    else:
        xPos = xPos
        


#create hamsters                          
def hamster(x, y, t):
    fill(255, t)
    noStroke()
    fill("#F5C474")
    #body and head
    ellipse(x-5, y+15, 60, 40)
    ellipse(x+20, y+5, 35, 30)
    #feet
    strokeWeight(4)
    stroke("#F5C474")
    line(x-15, y+20, random(x-25, x-15), y+40)
    line(x+15, y+20, random(x+10, x+20), y+40)
    fill("#F0B152")
    #ear
    noStroke()
    ellipse(x+15, y-10, 10, 15)
    #tail
    ellipse(x-30, y+5, 15, 10)
    strokeWeight(5)
    stroke(0)
    point(x+27, y+2)
    fill(255, 70)
    strokeWeight(1)
    stroke(255)
    #ball
    fill(random(255), random(255), random(255), 100)
    ellipse(x, y, 100, 100)
    #streaks
    stroke(200, 90)
    line(x-90, y-25, x-50, y-25)
    line(x-120, y-5, x-40, y-5)
    line(x-80, y +10, x-50, y+10)

    
#mouse pressed to generate hamsters
def mousePressed():
    global generateHamster
    generateHamster = not generateHamster
