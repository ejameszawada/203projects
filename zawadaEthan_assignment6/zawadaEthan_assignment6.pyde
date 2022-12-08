'''
Ethan Zawada
CSCI 203 Section 1
Assignment 6: Classes and Objects
10/13/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''
position = 800
generateHamster = False

def setup():
    size(600, 450)
    background("#56D1E0")
    
class Z:
    
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        
    def drawZ(self):
        noStroke()
        fill("#F5C474")
        #body and head
        ellipse(self.x-5, self.y+15, 60, 40)
        ellipse(self.x+20, self.y+5, 35, 30)
        #feet
        strokeWeight(4)
        stroke("#F5C474")
        line(self.x-15, self.y+20, random(self.x-25, self.x-15), self.y+40)
        line(self.x+15, self.y+20, random(self.x+10, self.x+20), self.y+40)
        fill("#F0B152")
        #ear
        noStroke()
        ellipse(self.x+15, self.y-10, 10, 15)
        #tail
        ellipse(self.x-30, self.y+5, 15, 10)
        strokeWeight(5)
        stroke(0)
        point(self.x+27, self.y+2)
        fill(255, 70)
        strokeWeight(1)
        stroke(255)
        #ball
        ellipse(self.x, self.y, 100, 100)
        
def draw():
    global generateHamster, position
    mouseHamster = Z(mouseX, mouseY)
    scatterHamster = Z(position, random(height))
    if(position <= 850):
        position -= 6
    if(position <= -50):
        position = 700
    
    if generateHamster:
        scatterHamster.drawZ()
    else:
        background("#56D1E0")
        mouseHamster.drawZ()
    
def mousePressed():
    global generateHamster
    
    generateHamster = not generateHamster
    
    
