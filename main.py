#Creator: t.me/Dev_Scorpian
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest,UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import JoinChannelRequest
from PIL import Image, ImageFont, ImageDraw
from random import choice
from datetime import datetime
import time, base64
import pytz 
timee = pytz.timezone("Asia/Tehran")# A set TimeZone

#-------------------Account information------------

api_id = 1234#- Api id
api_hash = "" #-Api hash
bio = "Desires do not die before God | Time:" #Please replace this line with the text you would like to include in your biography.

#--------------------------------------------------

def number(number:"It is related to changing the normal number to the one with font")-> str:
    number = number.replace('0', '０')
    number = number.replace('1', '１')
    number = number.replace('2', '２')
    number = number.replace('3', '３')
    number = number.replace('4', '４')
    number = number.replace('5', '５')
    number = number.replace('6', '６')
    number = number.replace('7', '７')
    number = number.replace('8', '８')
    number = number.replace('9', '９')
    number = number.replace(':', ':')
    return number


def gettime():
    return datetime.now(timee).strftime('%H:%M')


def generateimage(text):
    image = Image.open("data/pic.jpg")
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='data/font.ttf', size=110)
    _, _, wt, ht = draw.textbbox((0, 0), text, font=font)
    draw.text(((W - wt) + -200, (H - ht) / 1.5), text, font=font, fill=choice(
        ["#00c7a4", "#0071c7", "#c7a200", "#728593", "#943633", "#6495ed", "#43f70a", "#e1b2ae", "#527130", "#629f5d", "#3d4e90", "#9a9ec4"]))
    image.save('data/Time.jpg')

def main():
    set_time = ''
    with TelegramClient('Time&Bio', api_id, api_hash) as client:
        print('Run Time & Bio ...')
        while True:
            if not set_time == gettime():
                current_time = gettime()
                set_time = current_time
                generateimage(current_time)
                
                client(UpdateProfileRequest(last_name=number(current_time),about=f"{bio} {number(current_time)}"))
                image = client.upload_file('data/Time.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(True,image))
                
                time.sleep(60)



if __name__ == '__main__':
    main()
