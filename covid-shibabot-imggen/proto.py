# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import datetime
import locale
import math

#怒涛の定数定義
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

def Gradation (code1,code2,degree):
    if degree == 0:
        return code1
    elif degree == 1:
        return code2
    else:
        c1 = (int(code1[1:3],16),int(code1[3:5],16),int(code1[5:7],16))
        c2 = (int(code2[1:3],16),int(code2[3:5],16),int(code2[5:7],16)) 
        newcolor = '#%02X%02X%02X' % ( int((c2[0]-c1[0])*degree + c1[0]) , int((c2[1]-c1[1])*degree + c1[1] ), int ((c2[2]-c1[2])*degree + c1[2]) )
        return newcolor

#Grids = [Image.new('RGBA', (65, 65), '#CCCCCC'),Image.new('RGBA', (65, 65), '#F8CFCA'),Image.new('RGBA', (65, 65), '#F3AAA1'),Image.new('RGBA', (65, 65), '#EE6351')]
Grids =  [SoftSquare((65, 65),40, '#CCCCCC'),SoftSquare((65, 65),40, '#F8CFCA'),SoftSquare((65, 65),40, '#F3AAA1'),SoftSquare((65, 65),40, '#EE6351')]
GridPalette = ['#CCCCCC', '#F8CFCA' , '#F3AAA1', '#EE6351']
Yobifont = ImageFont.truetype("./FontRoboto/Roboto-Bold.ttf", 20)
Nihonfont = ImageFont.truetype("./meiryo.ttc", 24)
Streakfont = ImageFont.truetype("./FontRoboto/Roboto-Bold.ttf", 120)
STARTX = 131
STARTY = 266
DISTANCE = 83
HIKIKOMO_POS = (205,105)
DAY_POS = (410,140)
YOBI1_POS = (144,242)
YOBI2_POS = (394,242)
YOBI3_POS = (648,242)
STREAK_POS = (380,55)
NAME_POS = (64,20)

def Calendar(Activity,streak,name,day,AvarageMode):
    Canbas = Image.new('RGBA', (829, 512), '#F2F2F2')

    #ここからリストの長さが21であるのが前提
    Xtarget = STARTX
    Ytarget = STARTY
    for i in range(0,21):
        if Activity[i] == -1:
            pass
        else:
            #Canbas.paste(Grids[Activity[i]],(Xtarget,Ytarget),Grids[Activity[i]])
            TargetsGrid = SoftSquare( (65, 65), 40, Gradation( GridPalette[int(Activity[i])] , GridPalette[int(min((Activity[i])+1,3))] , Activity[i]-int(Activity[i]) ) )
            Canbas.paste(TargetsGrid, (Xtarget,Ytarget) ,TargetsGrid)
        if i%7 == 6:
            Xtarget = STARTX
            Ytarget +=  DISTANCE
        else:
            Xtarget += DISTANCE     
    else:
        pass
    #日時の処理
    dt = datetime.datetime.strptime(day, '%Y%m%d') 
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    #文字を書く処理
    dc = ImageDraw.Draw(Canbas)
    #Yobifont = ImageFont.truetype("./FontRoboto/Roboto-Bold.ttf", 20)
    #カレンダーが満タンなら曜日をずらす
    if Activity[20] == -1:
        dc.text(YOBI1_POS, 'San', fill='#737373', spacing=10, align='right',font=Yobifont)
        dc.text(YOBI2_POS, 'Wed', fill='#737373', spacing=10, align='right',font=Yobifont)
        dc.text(YOBI3_POS, 'Sat', fill='#737373', spacing=10, align='right',font=Yobifont)
    else:
        dc.text(YOBI1_POS, (dt - datetime.timedelta(days=6)).strftime('%a'), fill='#737373', spacing=10, align='right',font=Yobifont)
        dc.text(YOBI2_POS, (dt - datetime.timedelta(days=3)).strftime('%a'), fill='#737373', spacing=10, align='right',font=Yobifont)
        dc.text(YOBI3_POS, dt.strftime('%a'), fill='#737373', spacing=10, align='right',font=Yobifont)
    #Nihonfont = ImageFont.truetype("./meiryo.ttc", 24)
    if AvarageMode:
        dc.text(NAME_POS,'%s' %(name), fill='#737373', spacing=10, align='right',font = ImageFont.truetype("./meiryob.ttc", 17))
    else:
        dc.text(NAME_POS,'%s さんの自宅警備勤怠記録' %(name), fill='#737373', spacing=10, align='right',font = ImageFont.truetype("./meiryob.ttc", 17))
    dc.text((NAME_POS[0],NAME_POS[1]+27),dt.strftime('%Y年%m月%d日現在'), fill='#737373', spacing=10, align='right',font = ImageFont.truetype("./meiryo.ttc", 13))
    dc.text(HIKIKOMO_POS, '引きこもり\nストリーク', fill='#737373', spacing=10, align='right',font = ImageFont.truetype("./meiryob.ttc", 24))
    textwidth = dc.textsize(format(streak, '.1f'),font=Streakfont)[0]
    dc.text((DAY_POS[0] + textwidth,DAY_POS[1]),'日', fill = '#737373', spacing=10,align = 'right', font = ImageFont.truetype("./meiryob.ttc", 40))
    #Streakfont = ImageFont.truetype("./FontRoboto/Roboto-Bold.ttf", 120)

    dc.text((STREAK_POS[0] , STREAK_POS[1]),format(streak, '.1f'), fill='#EE7361',font=Streakfont)
    #終わったので表示
    return Canbas
    

Calendar([0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,2,0,1,2,-1,-1],1234.547,"xxx","20190510",False).show()