size(300,300)
background('#FFFFFF')
noStroke()


r = int( random(-40,40) )
stroke(3)
fill('#f4d3a6')
ellipse(156, 146, 160+r, 180+r);

abstractt = [
  'abstract1.png',
  'abstract2.png',
  'abstract5.png', 
  'abstract7.png',
  'abstract6.png',
]

hair = [
  'hair1.png',
  'hair2.png',
  'hair3.png',
  'hair4.png',
  'hair5.png',
  
]
eyesl = [
  'eye1.png',
  'eye2.png',
  'eye3.png',
  'eye4.png',
  'eye5.png',
  'eye6.png',  
]

eyesr = [
  'eye1.png',
  'eye2.png',
  'eye3.png',
  'eye4.png', 
  'eye5.png',
  'eye6.png',
]

nose = [
        'nose1.png',
        'nose2.png',  
        'nose3.png',
]

lips = [ 
    'lips1.png',
    'lips2.png',
    'lips3.png',
]

earsl = [ 
    'ear1.png',
    'ear2.png',
]
earsr = [ 
    'ear1.png',
    'ear2.png',
]

abstractb = [
     'abstract3.png',
     'abstract4.png', 
     'abstract5.png',
     'abstract6.png',
]

r = int( random(4) )
abstractt = loadImage(abstractt[r])
image(abstractt,  40,40,250,60)

r = int( random(5) )
hair = loadImage(hair[r])
image(hair,  0,0,280,280)

r = int( random(6) )
eyesl = loadImage(eyesl[r])
image(eyesl,  90,90,60,50)

r = int( random(6) )
eyesr = loadImage(eyesr[r])
image(eyesr,  170,90,60,50)

r = int( random(3) )
nose = loadImage(nose[r])
image(nose,  140,120, 40,90)

r = int( random(3) )
lips = loadImage(lips[r])
image(lips,  120,170, 100,65)

r = int( random(2) )
earsl = loadImage(earsl[r])
image(earsl,  200,130, 70,50)

r = int( random(2) )
earsr = loadImage(earsr[r])
image(earsr,  40,130, 70,50)

r = int( random(4) )
abstractb = loadImage(abstractb[r])
image(abstractb,  60,220,200,70)
