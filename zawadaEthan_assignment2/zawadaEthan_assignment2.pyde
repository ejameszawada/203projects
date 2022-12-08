'''
Ethan Zawada
CSCI 203 Section 1
Assignment 1: Pixels and Shapes
9/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate the University of Mississippi academic policies set forth in the M book.
'''
#create global variables
bite = 10
head = 20

def setup():
    size(400,400)
    noCursor()
    frameRate(10)
    
def draw():
    #call variables
    global bite, head
    #make everthing move with the mouse
    translate(mouseX, mouseY)
    
    background("#2AE832")
    
    #create the leaf
    strokeWeight(4)
    stroke("#BEFA0F")
    line(-400,50,400,50)
    strokeWeight(2)
    line(-90,50,400,-75)
    line(-50,50,400,350)
    
    #made the caterpillar look like its eating
    head = random(20,40)
  
    #the caterpillar eating the leaf
    fill(0)
    ellipse(5,0,constrain(bite,10, 70),constrain(bite,10,70))
    
    fill("#FA0F23")
    stroke("#890B16")
    #mouth
    ellipse(0,-5,25,10)
    ellipse(0,5,25,10)
    #body and head
    ellipse(-45,0,20,35)
    ellipse(-35,0,20,35)
    ellipse(-25,0,20,35)
    ellipse(-15,0,20,35)
    ellipse(-5,0,20,head)
    #makes the hole largen
    bite+=1
    
    
