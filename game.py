import pygame as pg
import math

pg.init()

#Define colours.
white=(255,255,255)
green=(0,255,0)
black=(0,0,0)


#Load game icon, display game icon.
icon=pg.image.load('tic-tac-toe.png')
pg.display.set_icon(icon)
pg.display.set_caption('TicTactoe')

#Win and input music:
winMusic=pg.mixer.Sound("audio/level-win.mp3")
inputMusic=pg.mixer.Sound('audio/turn.mp3')
tieMusic=pg.mixer.Sound('audio/tie-game.mp3')


#Define class for individual blocks of board
class block:
    state=False
    contains='*'

    x1,x2=0,0
    y1,y2=0,0
    center=(0,0)
    def findCenter(self):
        self.center= ((self.x1+(self.x2-self.x1)/2),(self.y1+(self.y2-self.y1)/2))

    def inBlock(self,x,y):
        if x<self.x2 and x>self.x1:
            if y<self.y2 and y>self.y1:
                return True
            else: return False
        else: return False


def game(talkObj):

    end=False
    turn=1
    empty=9
    running=True
    scrW,scrH=pg.display.get_surface().get_size()
    headFontSize=int(scrH/8)
    #load font
    headFont=pg.font.Font('fonts/PartyConfettiRegular-eZOn3.ttf',headFontSize)

    #Make list of 9 block objects i.e, board, define the block boundaries and find center of each block.
    ls=[]

    #Define constants for making block boundaries

    def makeBoundary():
        mX1=scrW/5
        mX2=2*scrW/5
        mY1=scrH/5
        mY2=2*scrH/5

        for i in range (0,9):
            b=block()
            ls.append(b)


        for i in range (0,9):
            ls[i].x1=mX1
            ls[i].x2=mX2
            if i!=0 and (i+1)%3==0:
                mX1=mX1+scrW/5
                mX2=mX2+scrW/5

        for i in range (0,9):
            ls[i].y1=mY1
            ls[i].y2=mY2
            mY1=mY1+scrH/5
            mY2=mY2+scrH/5
            if i!=0 and (i+1)%3==0:
                mY1=scrH/5
                mY2=2*scrH/5

        for i in range (0,9):
            ls[i].findCenter()


#Function to draw Board.
    def drawBoard():
        pg.draw.line(talkObj.screen,green,((2*scrW/5),scrH/5),((2*scrW/5),(4*scrH/5)),5)
        pg.draw.line(talkObj.screen,green,((3*scrW/5),scrH/5),((3*scrW/5),(4*scrH/5)),5)
        pg.draw.line(talkObj.screen,green,((scrW/5),(2*scrH/5)),((4*scrW/5),(2*scrH/5)),5)
        pg.draw.line(talkObj.screen,green,((scrW/5),(3*scrH/5)),((4*scrW/5),(3*scrH/5)),5)


#Function to draw X and O.
    def drawChar(str,mid):
        if str=='X':
            r=scrW/25
            a=float(mid[0])
            b=float(mid[1])
            point1=(a+r*math.cos(math.radians(45)),b+r*math.sin(math.radians(45)))
            point2=(a+r*math.cos(math.radians(225)),b+r*math.sin(math.radians(225)))
            point3=(a+r*math.cos(math.radians(135)),b+r*math.sin(math.radians(135)))
            point4=(a+r*math.cos(math.radians(315)),b+r*math.sin(math.radians(315)))
            pg.draw.line(talkObj.screen,black,point1,point2,5)
            pg.draw.line(talkObj.screen,black,point3,point4,5)
        
        if str=='O':
            pg.draw.circle(talkObj.screen,black,mid,scrW/25,5)


#Funtion to detect win.
    def win(a,b,c): 
        nonlocal end
        if(a.contains==b.contains==c.contains=='X') and end==False:
            pg.draw.line(talkObj.screen,green,a.center,c.center,5)
            winText='X WINS.'
            winMusic.play()
            end=True
            textW=headFont.size(winText)[0]
            textx=(scrW-textW)/2
            talkObj.screen.blit(headFont.render(winText,True,green),(textx,10))

        if(a.contains==b.contains==c.contains=='O') and end==False:
            pg.draw.line(talkObj.screen,green,a.center,c.center,5)
            winText='O WINS.'
            winMusic.play()
            end=True
            textW=headFont.size(winText)[0]
            textx=(scrW-textW)/2
            talkObj.screen.blit(headFont.render(winText,True,green),(textx,10))

    def tie():
        nonlocal end
        if empty==0 and end==False:
            winText='GAME TIED.'
            tieMusic.play()
            end=True
            textW=headFont.size(winText)[0]
            textx=(scrW-textW)/2
            talkObj.screen.blit(headFont.render(winText,True,green),(textx,10))

        


    makeBoundary()
    talkObj.screen.fill(white)

    while running:
        mouseX,mouseY=pg.mouse.get_pos()
        drawBoard()
        win(ls[0],ls[1],ls[2])   
        win(ls[3],ls[4],ls[5])   
        win(ls[6],ls[7],ls[8])   
        win(ls[0],ls[4],ls[8])   
        win(ls[2],ls[4],ls[6])   
        win(ls[0],ls[3],ls[6])   
        win(ls[1],ls[4],ls[7])   
        win(ls[2],ls[5],ls[8])        
        tie()  

        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                talkObj.screen.fill(white)
                return False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    talkObj.screen.fill(white)
                    return True
            if event.type==pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    for i in range(0,9):
                        if ls[i].inBlock(mouseX,mouseY) and ls[i].state==False and end==False:
                            if(turn%2==0):
                                drawChar('O',ls[i].center)
                                ls[i].state=True
                                ls[i].contains='O'
                                inputMusic.play()
                                turn=turn+1
                                empty=empty-1
                            else:
                                drawChar('X',ls[i].center)
                                ls[i].state=True
                                ls[i].contains='X'
                                inputMusic.play()
                                turn=turn+1
                                empty=empty-1
                    
                    
        pg.display.update()


