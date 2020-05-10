# coding:utf_8
from PIL import Image,ImageDraw,ImageFont

#怒涛の定数定義
Canbas = Image.new('RGBA', (829, 512), '#F2F2F2')
def SoftSquare (posision,roundness,color):
    #丸みのついた四角を生成する
    Img = Image.new('RGBA', (posision[0],posision[1]), 0)
    d = ImageDraw.Draw(Img)
    d.ellipse([(0,0), (roundness,roundness)], fill=color)
    d.ellipse([(posision[0]-roundness,0), (posision[0],roundness)], fill=color)
    d.ellipse([(0,posision[1]-roundness), (roundness,posision[1])], fill=color)
    d.ellipse([(posision[0]-roundness,posision[1]-roundness), (posision[0],posision[1])], fill=color)
    d.rectangle([(0, roundness/2), (posision[0], posision[1]-roundness/2)], fill=color)
    d.rectangle([(roundness/2,0), (posision[0]-roundness/2, posision[1])], fill=color)
    return Img
#Grids = [Image.new('RGBA', (65, 65), '#CCCCCC'),Image.new('RGBA', (65, 65), '#F8CFCA'),Image.new('RGBA', (65, 65), '#F3AAA1'),Image.new('RGBA', (65, 65), '#EE6351')]
Grids =  [SoftSquare((65, 65),40, '#CCCCCC'),SoftSquare((65, 65),40, '#F8CFCA'),SoftSquare((65, 65),40, '#F3AAA1'),SoftSquare((65, 65),40, '#EE6351')]
STARTX = 131
STARTY = 266
DISTANCE = 83
HIKIKOMO_POS = (172,175)
DAY_POS = (490,170)
YOBI1_POS = (144,242)
YOBI2_POS = (394,242)
YOBI3_POS = (648,242)
STREAK_POS = (390, 50)

def Calendar(Activity,streak,todaydate,name,day):
    #ここからリストの長さが21であるのが前提
    Xtarget = STARTX
    Ytarget = STARTY
    for i in range(0,21):
        if Activity[i] == -1:
            pass
        else:
            Canbas.paste(Grids[Activity[i]],(Xtarget,Ytarget),Grids[Activity[i]])
        if i%7 == 6:
            Xtarget = STARTX
            Ytarget +=  DISTANCE
        else:
            Xtarget += DISTANCE     
    else:
        pass
    #文字を書く処理
    dc = ImageDraw.Draw(Canbas)
    Yobifont = ImageFont.truetype("/home/hitoiki103/covid-shibabot-imggen/FontRoboto/Roboto-Bold.ttf", 20)
    dc.text(YOBI1_POS, 'Sun', fill='black', spacing=10, align='right',font=Yobifont)
    dc.text(YOBI2_POS, 'Wed', fill='black', spacing=10, align='right',font=Yobifont)
    dc.text(YOBI3_POS, 'Sat', fill='black', spacing=10, align='right',font=Yobifont)
    Hikifont = ImageFont.truetype("/home/hitoiki103/covid-shibabot-imggen/FontArial/Arial.ttf", 24)
    dc.text(HIKIKOMO_POS, '引きこもり\nストリーク', fill='black', spacing=10, align='right',font=Hikifont)
    dc.text(DAY_POS,'日', fill = 'black', spacing=10,align = 'right', font = Hikifont)
    Streakfont = ImageFont.truetype("/home/hitoiki103/covid-shibabot-imggen/FontRoboto/Roboto-Bold.ttf", 120)
    dc.text(STREAK_POS,"%d" %(streak), fill='#EE7361', spacing=10, align='right',font=Streakfont)
    #終わったので表示
    Canbas.show()
    

Calendar([0,-1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0],1,0,"xxx","YYYYMMDD")


