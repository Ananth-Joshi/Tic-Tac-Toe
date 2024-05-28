import pygame as pg


pg.font.init()
red=(255,0,0)
white=(255,255,255)

#load font
headFont=pg.font.Font('PartyConfettiRegular-eZOn3.ttf',50)
textFont=pg.font.SysFont('Times New Roman',20)

#load and read lines of instruction file
file=open("Instructions.txt","r")
text=file.readlines()

def ins(obj):
    running=True
    while running:

        x=75

        for event in pg.event.get():
            if event.type==pg.QUIT:
                return False
            
            if  (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
                running=False

        heading=headFont.render('INSTRUCTIONS:',True,red)
        obj.screen.blit(heading,(0,0))

        for line in text:
            rendered=textFont.render(line.strip(),True,red)
            obj.screen.blit(rendered,(0,x))
            x=x+30

        
        pg.display.update()

    file.close()
    return True
        