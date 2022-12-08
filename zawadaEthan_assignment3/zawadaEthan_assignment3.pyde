'''
Ethan Zawada
CSCI 203 Section 1
Assignment 1: Pixels and Shapes
9/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''

leftEye = 140
rightEye = 260
r = 0
g = 0
b = 0 
x = 175
y = 35
w = 50
h = 90
pressed = False
rollOver = 135
rollOver2 = 75

def setup():
    size(400,600)
    noCursor()

def draw():
    global leftEye, rightEye, pressed, r, g, b, x, y, w, h, rollOver, rollOver2
    
    print(mouseX, mouseY)
    
    background(0)
    stroke(0)
    
    #stem
    rectMode(CORNER)
    fill("#1D6420")
    rect(175, 35, 50, 90, 10)
    
    
    rectMode(CENTER)
    #body
    fill("#D65E13")
    rect(200,300,350,450,80)
    rect(200,300,275,450,80)
    rect(200,300,175,450,80)
    rect(200,300,75,450,80)
    
    #eyes
    fill(r,g,b)
    rect(140,225,75,90)
    rect(260,225,75,90)
    
    stroke(0)
    strokeWeight(2)
    
    #mouth
    ellipse(200,425,rollOver,rollOver2)
    
    if (mouseX > 135 and mouseX < 265 and mouseY > 385 and mouseY < 460):
        rollOver = 180
        rollOver2 = 110
    else:
        rollOver = 135
        rollOver2 = 75
    
    #nose
    triangle(200,275,165,350,235,350)
    
    if pressed:
        r = 236
        g = 237
        b = 7
    else:
        r = 0
        g = 0
        b = 0
    
    #pupils
    fill("#D65E13")
    stroke(0)
    rect(leftEye,245,30,40)
    rect(rightEye,245,30,40)
    
    if mouseX > 140:
        leftEye += 1
    if mouseX < 140:
        leftEye -= 1
    
    if leftEye >= 160:
        leftEye = 160
    if leftEye <= 120:
        leftEye = 120
        
    if mouseX > 260:
        rightEye += 1
    if mouseX < 260:
        rightEye -= 1
    
    if rightEye >= 280:
        rightEye = 280
    if rightEye <= 240:
        rightEye = 240
        
    #fly
    stroke(110)
    fill(0)
    ellipse(mouseX, mouseY, 15, 30)
    stroke(210)
    fill(210, 70)
    ellipse(mouseX-5, mouseY+10, 10, 25)
    ellipse(mouseX+5, mouseY+10, 10, 25)
    
def mousePressed():
    global pressed, x, y, w, h

    if (mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h):
        pressed = not pressed
    
