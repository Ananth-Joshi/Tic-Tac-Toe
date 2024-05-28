import pygame as pg

pg.init()
red=(255,0,0)
white=(255,255,255)


#load font
headFont=pg.font.Font('PartyConfettiRegular-eZOn3.ttf',50)
textFont=pg.font.SysFont('Times New Roman',20)

#pointer object
pointer=pg.image.load('pointer.png')



def options(obj):
    pointerY=50
    running=True
    print('abc')
    while running:
        for event in pg.event.get():

                if event.type==pg.QUIT:
                    return False

                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_ESCAPE:
                        running=False

                    if event.key==pg.K_RETURN:
                        if pointerY==50:
                            if obj.musicRunning:
                                obj.musicRunning=False
                                obj.mus.pause()
                            else:
                                obj.mus.unpause()
                                obj.musicRunning=True



        obj.screen.fill(white)
        heading=headFont.render('OPTIONS:',True,red)
        obj.screen.blit(heading,(0,0))
        obj.screen.blit(pointer,(30,60))

        musicState= 'ON' if obj.musicRunning else 'OFF'
        obj.screen.blit(textFont.render('MUSIC:'+musicState,True,red),(pointerY,60))
        pg.display.update()
    return True
        
