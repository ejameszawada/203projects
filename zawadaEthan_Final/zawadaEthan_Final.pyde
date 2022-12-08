'''
Ethan Zawada
CSCI 203 Section 1
Assignment Final
12/6/19

Sources Consutled: (Chapter slides, class notes, etc.)

By submitting this work, I attest that it is my original work and that I did not
violate thte University of Mississippi academic policies set forth in the M book.
'''
cPos = 245
cPos2 = 380
cPos3 = 475

sTheta = 0
mTheta = 0

coco = 225

drop = False

sPos = 250

dn = False

def setup():
    global seag
    size(500, 500)
    
    seag = loadImage("seagull.png")
       
    
def draw():
    global cPos, cPos2, cPos3, coco, seag, sPos, dn
    
    starList = []
    
    #night
    if dn:
        background("#2B5879")
        #stars
        pushMatrix()
        for i in range(2):
            starList.append(Star(550, random(350)))
        popMatrix()
        Moon(-75, -250)
        
    #day
    else:
        background("#61B0EA")
        noStroke()
        Sun(75, 250)
        
        
   
    
    Cloud(cPos, 110)
    Cloud(cPos2, 70)
    Cloud(cPos3, 90)
    
    cPos -= 2
    cPos2 -= 2
    cPos3 -= 2
    
    if cPos <= -50:
        cPos = 550
    if cPos2 <= -50:
        cPos2 = 550
    if cPos3 <= -50:
        cPos3 = 550
        
    #water
    fill("#1B4383")
    stroke(200)
    strokeWeight(2)
    rect(0, 325, 550, 175)
    
    #palm tree
    noFill()
    stroke("#643E19")
    strokeWeight(10)
    curve(300, 200, 235, 220, 250, 290, 0, 200)
    
    #island
    noStroke()
    fill("#E8BD60")
    ellipse(250, 335, 175, 125)
    fill(27, 67, 131)
    rect(0, 327, 550, 175)
    
    #coconut
    stroke(0)
    strokeWeight(1)
    fill("#764E19")
    ellipse(225, coco, 10, 10)
    fill(0)
    ellipse(227, coco+2, 1, 1)
    ellipse(224, coco+1, 1, 1)
    ellipse(228, coco, 1, 1)
    
    if drop:
        coco += 1
        
    if coco >= 275:
        coco = 275
    
    #leaves
    noStroke()
    fill("#30D83C")
    ellipse(242, 217, 40, 10)
    ellipse(228, 217, 43, 12)
    
    
    #cursor
    strokeWeight(3)
    noFill()
    noCursor()
    stroke(0)
    imageMode(CENTER)
    image(seag, mouseX, mouseY, 50, 50)
    
def Moon(x, y):
    global mTheta, sPos
    pushMatrix()
    noStroke()
    translate(250, sPos)
    rotate(radians(mTheta))
    fill(255, 70)
    ellipse(x, y, 80, 80)
    fill(160)
    ellipse(x, y , 75, 75)
    fill(125)
    ellipse(x+18, y-9, 14, 14)
    ellipse(x-7, y+15, 9, 9)
    ellipse(x+21, y+19, 12, 12)
    ellipse(x-12, y-14, 17, 17)
    mTheta += 1
    popMatrix()
    
def Sun(x, y):
    global sTheta
    pushMatrix()
    translate(250, 250)
    rotate(radians(sTheta))
    fill(250, 124, 66, 110)
    ellipse(x, y, 80, 80)
    fill("#F7FA62")
    ellipse(x, y, 75, 75)
    sTheta += 1
    popMatrix()
    
    
def Cloud(x, y):
    noStroke()
    fill(255, 70)
    ellipse(x, y, 45, 40)
    ellipse(x+10, y+6, 40, 30)
    ellipse(x-12, y+4, 45, 35)
    ellipse(x-10, y-3, 33, 27)
    
def Star(x, y):
    noStroke()
    fill(255)
    rect(random(x), random(y), 2, 2)

    
def mousePressed():
    global drop
    drop = not drop

def keyPressed():
    global dn
    dn = not dn
    
    
    
