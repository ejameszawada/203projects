'''
Ethan Zawada
CSCI 203 Section 1
Assignment 1: Pixels and Shapes
9/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''
press = False

r = random(255)
g = random(255)
b = random(255)

def setup():
    size(500,600)
    
    
def draw():
    global press, r, g, b
    background("#82F2C4")
    strokeWeight(2)
    
    #gumballs
    for x in range(85, 425, 55):
        for y in range(100, 400, 55):
            fill(x-25, y-50, 200)
            ellipse(x, y, 50, 50)
            fill(255)
            ellipse(x-13, y-12, 10, 10)  
            ellipse(x-9, y-7, 5, 5)
            
    #glass of gumball machine
    fill(255, 140)
    rect(250, 240, 425, 350, 50)
    
    #base of gumball machine
    fill(255,0,0)
    rectMode(CORNER)
    rect(50, 425, 400, 175)
    rectMode(CENTER)
    rect(250, 425, 425, 50, 150) 
    
    #top of gumball machine
    ellipse(250, 25, 55, 25)
    rect(250, 50, 375, 35, 100)
    
    #slot
    fill(140)
    rect(250, 470, 350, 30)
    fill(215)
    rect(390, 470, 40, 20)
    
    if press:
        fill(255, 0, 0)
        rect(250, 535, 100, 100)
        fill(0, 140)
        rect(250, 535, 100, 100)
        fill(215) 
        rect(250, 490, 100, 10)
        fill("#DE0D2D")
        triangle(250, 515, 200, 585, 300, 585)
        fill(r, g, b)
        ellipse(250, 535, 55, 55)
        fill(255)
        ellipse(235, 520, 10, 10)
        ellipse(240, 525, 5, 5)
        
        
    
    else:
        #flap
        fill(215)
        rect(250, 535, 100, 100)
    
        i = 220
        while i < 300:
            strokeWeight(5)
            line(i, 500, i, 570)
            i += 30
        
def keyPressed():
    global press
    press = not press
