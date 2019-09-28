from pygame import*
from random import*
from math import*
import os
from tkinter import*
root = Tk()
root.withdraw()
from tkinter.colorchooser import*
os.environ['SDL_VIDEO_WINDOW_POS']='10,30'

pygame.display.set_caption("League of Painting", 'Spine Runtime')

tool=1
colour=(0,0,0)
size=1
pensize=3
cilsize=1
erasize=3
linesize=1
spraysize=20
stampsize=140
rectsize=1
elsize=1
sx=1
sy=1
fill=0
name="Pencil"
result="untitled.png"
font.init()
undoimages=[]
icons=[1,2,3,4,5,6,7,8,9,10,11,12,13]
counter=-1
iconFlip=False
stampclick=False
comicFont = font.SysFont("Comic Sans MS", 20)
sizerect=Rect(1160,250,40,30)
pencilRect = Rect(30,210,60,60)
markerRect = Rect(100,210,60,60)
eraserRect = Rect(30,280,60,60)
elRect = Rect(100,280,60,60)
rectRect = Rect(30,350,60,60)
sprayRect = Rect(100,350,60,60)
lineRect = Rect(30,420,60,60)
fillRect = Rect(100,420,60,60)
canvas = Rect(200,30,900,600)
pal = Rect(1105,330, 150, 350)
openRect = Rect(65,20,40,40)
saveRect = Rect(15,20,40,40)
undoRect = Rect(100,20,40,40)
redoRect = Rect(165,20,40,40)
clearRect = Rect(1040,3,60,25)
arrowRect = Rect(1040,640,60,140)
fillrect = Rect(1120,250,60,30)
unfillrect = Rect(1180,250,60,30)
iconRects=[1,2,3,4,5,6]
for i in range(6):
    iconRects[i]=Rect(200+140*i,640,140,140)
screen = display.set_mode((1260,800))#size of screen
running=True
drawing=False
background = image.load("images/background.png")
screen.blit(background,(0,0))
plus=image.load("images/plus.png")
minus=image.load("images/minus.png")
#canvas
draw.rect(screen,(255,255,255),(200,30,900,600))
#stamps boxes
draw.rect(screen,(159,159,159),(200,640,900,140))
for i in range(6):
    draw.rect(screen,(100,100,100),(200+140*i,640,140,140),4)
#layout rects
def layout():
    draw.rect(screen,(159,159,159),(1105,3,150,300))
    draw.rect(screen,(100,100,100),(1105,3,150,300),3)
    screen.blit(plus,(1125,250))
    screen.blit(minus,(1205,250))
    sizetxt = comicFont.render(str(size), True, (0,0,0))
    cleartxt = comicFont.render("clear", True, (0,0,0))
    draw.rect(screen,(255,255,255),sizerect)
    screen.blit(sizetxt,(1167,250))
    draw.rect(screen,colour,(1165,210,30,30))
    nametxt = comicFont.render(str(name), True, (0,0,0))
    screen.blit(nametxt,(1140,10))
layout()
#images
pencil=image.load("images/pencil.png")
pencil = transform.smoothscale(pencil,(60,60))
screen.blit(pencil,(30,210))
marker=image.load("images/marker.png")
marker = transform.smoothscale(marker,(60,60))
screen.blit(marker,(100,210))
eraser=image.load("images/eraser.png")
eraser = transform.smoothscale(eraser,(60,60))
screen.blit(eraser,(30,280))

el=image.load("images/elipse.png")
el = transform.smoothscale(el,(60,60))
screen.blit(el,(100,280))
rect=image.load("images/rect.png")
rect = transform.smoothscale(rect,(60,60))
screen.blit(rect,(30,350))
spray=image.load("images/spray.png")
spray = transform.smoothscale(spray,(60,60))
screen.blit(spray,(100,350))
line=image.load("images/line.png")
line = transform.smoothscale(line,(60,60))
screen.blit(line,(30,420))
bucket=image.load("images/fill.png")
bucket = transform.smoothscale(bucket,(60,60))
screen.blit(bucket,(100,420))

palette=image.load("images/palette.jpg")
screen.blit(palette,(1105,330))
plus=image.load("images/plus.png")
screen.blit(plus,(1125,250))
minus=image.load("images/minus.png")
screen.blit(minus,(1205,250))
save=image.load("images/save.png")
open=image.load("images/open.png")
undo=image.load("images/undo.png")
undo = transform.scale(undo,(40,40))
redo=image.load("images/redo.png")
redo = transform.scale(redo,(40,40))
arrow=image.load("images/next.png")
arrow = transform.scale(arrow,(60,120))
screen.blit(arrow,(1040,650))
logo=image.load("images/Logo.png")
logo = transform.smoothscale(logo,(200,80))
screen.blit(logo,(1,100))
resulttxt = comicFont.render(result, True, (0,0,0))
screen.blit(resulttxt,(200,1))
cleartxt = comicFont.render("clear", True, (0,0,0))
draw.rect(screen,(190,190,190),clearRect)
draw.rect(screen,(0,0,0),clearRect,1)
screen.blit(cleartxt,(1045,1))
draw.rect(screen,(255,255,255),sizerect)
draw.rect(screen,(190,190,190),(200,1,700,28))
draw.rect(screen,(0,0,0),(200,1,700,28),1)
resulttxt = comicFont.render(result, True, (0,0,0))
screen.blit(resulttxt,(205,1))
#icon images
for i in range(6):
    icons[i]=image.load("images/icons/icon%d.png" %i)
    icons[i] = transform.smoothscale(icons[i],(140,140))
    screen.blit(icons[i],(200+140*i,640))
#Option Rect
draw.rect(screen,(169,169,169),(5,3,190,80))
draw.rect(screen,(0,0,0),(5,3,190,80),3)
screen.blit(open,(55,20))
screen.blit(save,(10,20))
screen.blit(undo,(100,20))
screen.blit(redo,(150,20))
redolist = []
def toolrects():
    draw.rect(screen,(0,0,0),pencilRect,3)
    draw.rect(screen,(0,0,0),eraserRect,3)
    draw.rect(screen,(0,0,0),markerRect,3)
    draw.rect(screen,(0,0,0),elRect,3)
    draw.rect(screen,(0,0,0),rectRect,3)
    draw.rect(screen,(0,0,0),sprayRect,3)
    draw.rect(screen,(0,0,0),lineRect,3)
    draw.rect(screen,(0,0,0),fillRect,3)
toolrects()
    
undoimage=screen.subsurface(canvas).copy()
undoimages.append(undoimage)

while running:
    CLICK=False
    CLICKUP=False
    for evt in event.get():
        shift=False
        keys=key.get_pressed()
        if keys[K_RSHIFT] or keys[K_LSHIFT]:
           shift=True
        if keys[K_ESCAPE]:
           break
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            CLICK=True
            srtx=mx
            srty=my
            toolcopy=screen.copy()
        if evt.type==MOUSEBUTTONUP:
            CLICKUP=True
#---------------------------------------------------------
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #if mb[0]==1:
        #for i in range(1,10):
            #draw.circle(screen,(255,0,0),(mx,my),5*i,1)
    #size text
    sizetxt = comicFont.render(str(size), True, (0,0,0))
    #screen.blit(sizetxt,(1167,250))
    #resulttxt = comicFont.render(result, True, (0,0,0))
    #screen.blit(resulttxt,(200,1))
    
    #savingo
    if CLICKUP:
        if openRect.collidepoint(mx,my):
            result = filedialog.askopenfilename() # There are some options you can use to make these look nicer.
            print(result)                         # Do some Google searching to find them, if you care.
            #screen.blit(background, (200, 3), pygame.Rect(200, 3, 50, 50))
            #resulttxt = comicFont.render(result, True, (0,0,0))
            #screen.blit(resulttxt,(200,1))
            if result!="":
                screen.set_clip(canvas)
                image=image.load(result)
                screen.blit(image,(200,30))
                screen.set_clip(None)
        elif saveRect.collidepoint(mx,my):
            result = filedialog.asksaveasfilename()
            #screen.blit(background, (x, y), pygame.Rect(x, y, 62, 62))
            draw.rect(screen,(190,190,190),(200,1,700,28))
            draw.rect(screen,(0,0,0),(200,1,700,28),1)
            resulttxt = comicFont.render(result, True, (0,0,0))
            screen.blit(resulttxt,(205,1))
            if result!="":
                image.save(screen.subsurface(canvas),result)
            print(result)

    #clear
    if CLICK and clearRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),(200,30,900,600))
        copy=screen.copy()
        screen.blit(copy,(0,0))

    #stamps
    if CLICKUP and arrowRect.collidepoint(mx,my) and iconFlip==False:
        draw.rect(screen,(159,159,159),(200,640,900,140))
        for i in range(6):
            draw.rect(screen,(100,100,100),(200+140*i,640,140,140),4)
        for i in range(7,13):
            icons[i]=image.load("images/icons/icon%d.png" %i)
            icons[i] = transform.smoothscale(icons[i],(140,140))
            screen.blit(icons[i],(-780+140*i,640))
        iconFlip=True
        screen.blit(arrow,(1040,650))
        copy=screen.copy()
    elif CLICKUP and arrowRect.collidepoint(mx,my) and iconFlip==True:
        draw.rect(screen,(159,159,159),(200,640,900,140))
        for i in range(6):
            draw.rect(screen,(100,100,100),(200+140*i,640,140,140),4)
        for i in range(6):
            icons[i]=image.load("images/icons/icon%d.png" %i)
            icons[i] = transform.scale(icons[i],(140,140))
            screen.blit(icons[i],(200+140*i,640))
        iconFlip=False
        screen.blit(arrow,(1040,650))
        copy=screen.copy()

    for i in range(6):
        for k in range(6):
            if CLICK and iconRects[i].collidepoint(mx,my):
                size=stampsize
                tool=4
                toolrects()
                draw.rect(screen,(100,100,100),(200+140*k,640,140,140),4)
                draw.rect(screen,(0,255,255),iconRects[i],4)
                copy=screen.copy()
                if iconFlip==False:
                    stamp=icons[i]
                    iconRect=iconRects[i]
                    layout()
                    name="Stamp"
                    screen.blit(stamp,(1110,40))
                    copy=screen.copy()
                else:
                    stamp=icons[i+7]
                    layout()
                    name="Stamp"
                    screen.blit(stamp,(1110,40))
                copy=screen.copy()

    if tool==4 and canvas.collidepoint(mx,my):
        screen.blit(copy,(0,0))
        screen.set_clip(canvas)
        stamp2 = transform.smoothscale(stamp,(stampsize,stampsize))
        #print(stamp2.get_rect())
        screen.blit(stamp2,(mx-stampsize/2,my-stampsize/2))
        screen.set_clip(None)
        if CLICK and tool==4 and canvas.collidepoint(mx,my):
            copy=screen.copy()
            screen.blit(copy,(0,0))
            screen.set_clip(canvas)
            screen.blit(stamp2,(mx-70,my-70))
            screen.set_clip(None)
            
    elif tool==4:
        screen.blit(copy,(0,0))
        if CLICK and Rect(1125,250,30,30).collidepoint(mx,my):
            #draw.rect(screen,(255,255,255),sizerect)
            draw.rect(screen,(255,255,255),sizerect)
            stampsize+=5
            size=stampsize
            screen.blit(sizetxt,(1165,250))
        if CLICK and stampsize!=0 and Rect(1205,250,30,30).collidepoint(mx,my):
            draw.rect(screen,(255,255,255),sizerect)
            stampsize-=5
            size=stampsize
            screen.blit(sizetxt,(1165,250))
        copy=screen.copy()

    if tool!=4:
        for i in range(6):
            draw.rect(screen,(100,100,100),(200+140*i,640,140,140),4)

    #undo
    if CLICKUP and canvas.collidepoint(mx,my):
        undoimage=screen.subsurface(canvas).copy()
        undoimages.append(undoimage)
    
    if CLICK and undoRect.collidepoint(mx,my):
        if len(undoimages)>1:
            redolist.append(undoimages.pop())
        screen.blit(undoimages[-1],(200,30))
        copy=screen.copy()

    #redo
    if CLICK and redoRect.collidepoint(mx,my):
        if len(redolist)>1:
            undoimages.append(redolist.pop())
        screen.blit(redolist[-1],(200,30))
        copy=screen.copy()

    #getting colour
    if CLICK and pal.collidepoint(mx,my):
        colour=screen.get_at((mx,my))

    toolrects()
    
    #pencil tool
    if tool==1:
        layout()
        name="Pencil"
        size=cilsize
        screen.blit(pencil,(1150,80))
        draw.rect(screen,(0,0,255),pencilRect,3)
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),pencilRect,1)
        if CLICK:
            tool=1
            toolrects()
    if mb[0]==1 and tool==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            draw.line(screen,colour,(omx,omy),(mx,my),size)
            #drawing=True
            screen.set_clip(None)

    #eraser tool
    if tool==2:
        layout()
        name="Eraser"
        draw.rect(screen,(0,0,255),eraserRect,3)
        size=erasize
        screen.blit(eraser,(1150,80))
        if CLICK and tool==2 and erasize!=0 and Rect(1125,250,30,30).collidepoint(mx,my):
            erasize+=1
            draw.rect(screen,(255,255,255),sizerect)
        if CLICK and tool==2 and Rect(1205,250,30,30).collidepoint(mx,my):
            erasize-=1
            draw.rect(screen,(255,255,255),sizerect)
            size=erasize
        size=erasize
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),eraserRect,1)
        if CLICK:
            tool=2
            toolrects()
    if mb[0]==1 and tool==2 and canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        draw.line(screen,(255,255,255),(omx,omy),(mx,my),size)
        screen.set_clip(None)

    #marker
    if tool==3:
        layout()
        name="Marker"
        draw.rect(screen,(0,0,255),markerRect,3)
        size=pensize
        screen.blit(marker,(1150,80))
        if CLICK and tool==3 and pensize!=1 and Rect(1125,250,30,30).collidepoint(mx,my):
            pensize+=1
            draw.rect(screen,(255,255,255),sizerect)
            #time.delay(100)
        if CLICK and tool==3 and Rect(1205,250,30,30).collidepoint(mx,my):
            pensize-=1
            draw.rect(screen,(255,255,255),sizerect)
            size=pensize
            #time.delay(100)
    if markerRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),markerRect,1)
        if CLICK:
            tool=3
            toolrects()
    if mb[0]==1 and tool==3 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            draw.line(screen,colour,(omx,omy),(mx,my),size)
            if size>3:
                dist=hypot(omx-mx,omy-my)
                dist=max(size ,dist)
                numcircle=ceil(dist/size)
                sx=size*(omx-mx)/dist
                sy=size*(omy-my)/dist
                for i in range(int(numcircle)):
                    draw.circle(screen,(colour),(int(ceil(mx+sx)),int(ceil(my+sy))),int(size*0.45))
                    #draw.circle(screen,colour,(mx,my),int(size*0.4))
            screen.set_clip(None)

     #rect
    if tool==5:
        layout()
        name="Rectangle"
        draw.rect(screen,(0,0,255),rectRect,3)
        screen.blit(rect,(1150,80))
        draw.rect(screen,(110,110,110),fillrect,0)
        draw.rect(screen,(110,110,110),unfillrect,0)
        draw.rect(screen,(150,140,140),fillrect,3)
        draw.rect(screen,(140,140,140),unfillrect,3)
        if CLICK and fillrect.collidepoint(mx,my):
            fill=0
        elif CLICK and unfillrect.collidepoint(mx,my):
            fill=1
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            screen.blit(toolcopy,(0,0))
            draw.rect(screen,colour,(srtx,srty,mx-srtx+1,my-srty+1),fill)
            screen.set_clip(None)
            
    if rectRect.collidepoint(mx,my):
         draw.rect(screen,(0,0,255),rectRect,1)
         if CLICK:
            tool=5
            toolrects()

    #elipse
    if tool==6:
        layout()
        name="Elipse"
        draw.rect(screen,(0,0,255),elRect,3)
        screen.blit(el,(1150,80))
        draw.rect(screen,(110,110,110),fillrect,0)
        draw.rect(screen,(110,110,110),unfillrect,0)
        draw.rect(screen,(150,140,140),fillrect,3)
        draw.rect(screen,(140,140,140),unfillrect,3)
        if CLICK and fillrect.collidepoint(mx,my):
            fill=0
        elif CLICK and unfillrect.collidepoint(mx,my):
            fill=1
        
        if mb[0]==1 and shift==True and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            elipse=Rect(srtx,srty,mx-srtx,my-srty)
            elipse.normalize()
            screen.blit(toolcopy,(0,0))
            draw.circle(screen,colour,(mx,my),elipse.width,fill)

        elif mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            elipse=Rect(srtx,srty,mx-srtx,my-srty)
            elipse.normalize()
            screen.blit(toolcopy,(0,0))
            if elipse.width<elsize*2 or elipse.height<elsize*2:
                draw.ellipse(screen,colour,elipse,0)
            else:
                draw.ellipse(screen,colour,elipse,fill)
            screen.set_clip(None)

    if elRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),elRect,1)
        if CLICK:
            tool=6
            toolrects()

    #spray
    if tool==7:
        layout()
        name="Spray"
        draw.rect(screen,(0,0,255),sprayRect,3)
        screen.blit(spray,(1150,80))
        if CLICK and Rect(1125,250,30,30).collidepoint(mx,my):
            draw.rect(screen,(255,255,255),sizerect)
            spraysize+=2
            size=spraysize
            screen.blit(sizetxt,(1165,250))
        if CLICK and spraysize!=0 and Rect(1205,250,30,30).collidepoint(mx,my):
            draw.rect(screen,(255,255,255),sizerect)
            spraysize-=2
            size=spraysize

        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            sx=mx+randint(-spraysize,spraysize)
            sy=my+randint(-spraysize,spraysize)
            for i in range(25):
                if hypot(mx-sx,my-sy)<spraysize:
                    draw.circle(screen,colour,(sx,sy),1,0)
            screen.set_clip(None)
            
            screen.blit(sizetxt,(1165,250))
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),sprayRect,1)
        if CLICK:
            tool=7
            toolrects()
    

    #line
    if tool==8:
        layout()
        name="Line"
        draw.rect(screen,(0,0,255),lineRect,3)
        screen.blit(line,(1150,80))
        if CLICK and Rect(1125,250,30,30).collidepoint(mx,my):
            draw.rect(screen,(255,255,255),sizerect)
            linesize+=1
            size=linesize
            screen.blit(sizetxt,(1165,250))
        if CLICK and linesize!=0 and Rect(1205,250,30,30).collidepoint(mx,my):
            draw.rect(screen,(255,255,255),sizerect)
            linesize-=1
            size=linesize
            screen.blit(sizetxt,(1165,250))
            
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            screen.blit(toolcopy,(0,0))
            draw.line(screen,colour,(srtx,srty),(mx,my),size)
            screen.set_clip(None)
            
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),lineRect,1)
        if CLICK:
            tool=8
            toolrects()

    #fill
    if tool==9:
        layout()
        name="Fill"
        draw.rect(screen,(0,0,255),fillRect,3)
        screen.blit(bucket,(1150,80))
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),fillRect,1)
        if CLICK:
            tool=9
            toolrects()

    
#---------------------------------------------------------
    omx,omy=mx,my
    display.flip()
    print(len(undoimages))
    
font.quit()
del comicFont
quit()

#box=mx//20

