'''
Ethan Zawada
CSCI 203 Section 1
Assignment 1: Pixels and Shapes
9/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''
def setup():
    # size and background color
    size(400,400)
    background(165)
    
def draw():
    #lines for the vines and connected to the leaves made by ellipses as well as
    # color and weight
    strokeWeight(6)
    stroke("#05F51E")
    line(90,0,90,400)
    line(210,0,210,400)
    line(330,0,330,400)
    line(60,115,90,115)
    line(210,240,250,240)
    line(285,340,330,340)
    
    # flowers
    stroke("#D8096A")
    fill("#F50575")
    rect(95, 225, 25, 95)
    rect(57 ,265, 100, 20)
    stroke("#C4CB0A")
    fill("#EAF20C")
    rect(95,265,25,20)
    
    stroke("#D8096A")
    fill("#F50575")
    rect(300, 110, 25, 95)
    rect(260 ,147, 100, 20)
    stroke("#C4CB0A")
    fill("#EAF20C")
    rect(300,147,25,20)
    
    
    # ellipses created for the leaves
    stroke("#13A507")
    fill("#1FDB0F")

    ellipse(60,90,15,45)
    ellipse(60,135,15,45)
    ellipse(40,115,45,15)

            
    ellipse(250, 215, 15, 45)
    ellipse(250, 260, 15, 45)
    ellipse(270, 240, 45,15)

    
    ellipse(285, 315, 15,45)
    ellipse(285, 360, 15,45)
    ellipse(265,340,45,15)
    
    #triangle for the thorn / extra credit
    stroke("#D8096A")
    fill("#F50575")
    triangle(205, 115, 190, 125, 205, 135)
    
    # key pressed and mouse pressed
def mousePressed():
    background("#1F241E")
        
def keyPressed():
    background(165)
    
