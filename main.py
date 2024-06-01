#Creator: t.me/Dev_Scorpian
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from PIL import Image, ImageFont, ImageDraw
from random import choice
from datetime import datetime
import time
import pytz

timee = pytz.timezone("Asia/Tehran") # A set TimeZone

#-------------------Account information------------

api_id =   # - Api id
api_hash = ""  # -Api hash
bio = "Desires do not die before God | Time:"  # Please replace this line with the text you would like to include in your biography.

#--------------------------------------------------

def number(number_str):  # It is related to changing the normal number to the one with font
    number_str = number_str.replace('0', '０')
    number_str = number_str.replace('1', '１')
    number_str = number_str.replace('2', '２')
    number_str = number_str.replace('3', '３')
    number_str = number_str.replace('4', '４')
    number_str = number_str.replace('5', '５')
    number_str = number_str.replace('6', '６')
    number_str = number_str.replace('7', '７')
    number_str = number_str.replace('8', '８')
    number_str = number_str.replace('9', '９')
    number_str = number_str.replace(':', ':')
    return number_str

def gettime():
    return datetime.now(timee).strftime('%H:%M')

def generateimage(text):
    photos = choice(["photos/iran.jpg","photos/1.jpg","photos/2.jpg","photos/3.jpg","photos/4.jpg"])
    image = Image.open(photos)
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='data/3.ttf', size=110)
    _, _, wt, ht = draw.textbbox((0, 0), text, font=font)
    x = (W - wt) / 2
    y = (H - ht) / 2 - 180
    draw.text((x, y), text, font=font, fill=choice(
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
                
                client(UpdateProfileRequest(last_name=number(current_time), about=f"{bio} {number(current_time)} 🪐"))
                image = client.upload_file('data/Time.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(file=image))  # Updated line
                
                time.sleep(60)

if __name__ == '__main__':
    main()
