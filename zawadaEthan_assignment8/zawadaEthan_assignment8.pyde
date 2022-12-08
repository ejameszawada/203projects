'''
Ethan Zawada
CSCI 203 Section 1
Assignment 8: Arcs and Transformations
10/25/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''

spin = 0

def setup():
    size(800, 800)
    

def draw():
    global spin
    background(255, 100, 100)
    strokeWeight(2)
    
    fill(255, 0, 50)
    rectMode(CENTER)
    rect(650, 400, 80, 80)
    #base
    fill(70)
    triangle(400, 500, 200, 800, 600, 800)
    #back circle
    fill(125)
    ellipse(width/2, height/2, 550, 550)
    
    
    #keep it isolated
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(spin))
    wheel(0, 0)
    popMatrix()
    
    #stopper
    fill(255, 0, 0)
    triangle(615, 400, 690, 360, 690, 440)
    
    #center
    fill(255, 0, 0)
    ellipse(400, 400, 40, 40)
    
    #conditionals to make it spin and stop
    if(keyCode == DOWN):
        spin += 10
        
    if(keyCode == UP):
        spin == 0
    
    #text
    fill(0)
    textSize(25)
    text("Press DOWN to SPIN", 75, 75)
    text("Press UP to STOP", 525, 75)
    
    
    
#wheel function to create the pieces and color
def wheel(x, y):
    pushMatrix()
    translate(x, y)
    for r in range(0, 360, 45):
        for c in range(0, 255, 32):
            rotate(radians(r))
            fill(c, c+100, c+200)
            arc(0, 0, 500, 500, radians(0), radians(45), PIE)
    popMatrix()
    
