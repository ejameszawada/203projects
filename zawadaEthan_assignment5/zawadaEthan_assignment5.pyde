'''
Ethan Zawada
CSCI 203 Section 1
Assignment 5: User Defined Functions
9/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''

h1 = 15
h2 = 210
h3 = 95

fast = False

def setup():
    size(600, 450)
    
def draw():
    global h1, h2, h3, fast
    frameRate(25)
    background("#70B3F7")
    stroke(0)
    fill("#F5A6E6")
    triangle(150, 0, 0, 450, 300, 450)
    triangle(450, 0, 300, 450, 600, 450)
    
    if fast:
        hamster(random(600), 75)
        hamster(random(600), 190)
        hamster(random(600), 325)
    else:
        if h1 >= 680:
            h1 = -100
        if h2 >= 680:
            h2 = -100
        if h3 >= 680:
            h3 = -100
            
        hamster(h1, 75)
        hamster(h2, 190)
        hamster(h3, 325)
    
        h1 += 5
        h2 += 5
        h3 += 5
    
    
def hamster(x, y):
    
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
    ellipse(x, y, 100, 100)
    
def mousePressed():
    global fast
    
    fast = not fast
    
    
    
