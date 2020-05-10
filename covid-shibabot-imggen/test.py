from PIL import Image
from PIL import ImageDraw

"""
play_path = '/home/hitoiki103/covid-shibabot-imggen/CloseDoor.png'
Door = Image.open(play_path).copy().rotate(90)
#Door.show()
NewImg = '/home/hitoiki103/covid-shibabot-imggen/savefolder/Door.png'
Door.save(NewImg)
"""

Canbas = Image.new('RGBA', (300, 300), '#EE6351')
Pen = ImageDraw.Draw(Canbas)
Pen.text((25, 160), 'Test Message\nExample', fill='black', spacing=10, align='right')
Canbas.show()