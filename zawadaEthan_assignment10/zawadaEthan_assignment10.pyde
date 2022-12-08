add_library("sound")

def setup():
    global mic, vol
    size(400, 400)
    
    mic = AudioIn(this, 0)
    vol = Amplitude(this)
    
    mic.start()
    vol.input(mic)
    
def draw():
    global soundLevel
    
    background("#4A6DE5")
    soundLevel = map(vol.analyze(), 0, 1, 60, 400)
     
    Face(200, 200)
    
def Face(x, y):
    #face
    fill("#F2CE89")
    noStroke()
    ellipse(200, 175, 225, 250)
    ellipse(200, 250, 175, 150)
    #hair
    fill("#583E0E")
    stroke("#583E0E")
    strokeWeight(2)
    for x in range(90, 315, 3):
        for y in range(25, 50, 4):
            line(x, y, x, y+100)
    noStroke()
    fill("#F2CE89")
    ellipse(200, 150, 200, 50)
    
    #eyes
    stroke(0)
    strokeWeight(2)
    fill(255)
    ellipse(140, 190, soundLevel, soundLevel)
    ellipse(260, 190, soundLevel, soundLevel)
    fill(0, 255, 0)
    ellipse(140, 190, 30, 30)
    ellipse(260, 190, 30, 30)
    
    
    #mouth
    fill(0)
    ellipse(200, 275, 75, 50)
            
    
    
    
    
    
    
    
