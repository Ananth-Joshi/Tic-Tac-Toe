import pygame as pg
import instructions as ins
import options as op
import game as g

#initializing game.
pg.init()


#define variables and colors.
red=(255,0,0)
white=(255,255,255)


#Load game icon, display game icon.
icon=pg.image.load('tic-tac-toe.png')
pg.display.set_icon(icon)
pg.display.set_caption('TicTactoe')

#load music.
pg.mixer.music.load('audio/game music.mp3')

#create music object.
p=pg.mixer.Sound('audio/select.mp3')

class imp:
    musicRunning=True
    mus=pg.mixer.music
    screen=pg.display.set_mode((600,400),pg.FULLSCREEN)
    

talkObj=imp()

talkObj.mus.play()

scrW,scrH=talkObj.screen.get_size()

#load font
headFont=pg.font.Font('PartyConfettiRegular-eZOn3.ttf',int(scrH/4))
textFont=pg.font.Font('PartyConfettiRegular-eZOn3.ttf',int(scrH/12))

choicePointer=['>','','','']
choices=['PLAY','INSTRUCTIONS','OPTIONS','EXIT']
pointerPos=0


running=True

def swap(list,x,y):
    list[x],list[y]=list[y],list[x]

while running:

    talkObj.screen.fill(white)

    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_DOWN and pointerPos<3:
                p.play()
                swap(choicePointer,pointerPos,pointerPos+1)
                pointerPos=pointerPos+1
            if event.key==pg.K_UP and pointerPos>0:
                p.play()
                swap(choicePointer,pointerPos,pointerPos-1)
                pointerPos=pointerPos-1
            if event.key==pg.K_RETURN:
                if pointerPos==0:
                    running=g.game(talkObj)
                if pointerPos==1:
                    running=ins.ins(talkObj)
                if pointerPos==2:
                    running=op.options(talkObj)
                if pointerPos==3:
                    running=False


            

    
    headW=headFont.size('TIC-TAC-TOE')[0]
    talkObj.screen.blit(headFont.render('TIC-TAC-TOE',True,red),((scrW-headW)/2,10))


    textW=textFont.size(choicePointer[0]+choices[0])[0]
    talkObj.screen.blit(textFont.render((choicePointer[0]+choices[0]),True,red),((scrW-textW)/2,scrH/2))
    textW=textFont.size(choicePointer[1]+choices[1])[0]
    talkObj.screen.blit(textFont.render((choicePointer[1]+choices[1]),True,red),((scrW-textW)/2,scrH/2+scrH/15))
    textW=textFont.size(choicePointer[2]+choices[2])[0]
    talkObj.screen.blit(textFont.render((choicePointer[2]+choices[2]),True,red),((scrW-textW)/2,scrH/2+(2*scrH/15)))
    textW=textFont.size(choicePointer[3]+choices[3])[0]
    talkObj.screen.blit(textFont.render((choicePointer[3]+choices[3]),True,red),((scrW-textW)/2,scrH/2+3*scrH/15))
    print(pointerPos)
    
    pg.display.update()


