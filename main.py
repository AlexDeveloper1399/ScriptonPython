import shutil

from PIL import Image, ImageDraw,ImageFont
import os



nameFile = "jeremy-bishop.jpg"
# nameFile = "erik-kaha.jpg"
# nameFile = "casey-horner.jpg"


def ModifiteImage(imgname):
    img = Image.open(imgname)
    imagedraw = ImageDraw.Draw(img)
    text = os.path.basename(imgname)
    name = "©"+os.path.splitext(text)[0]
    imagedraw.text((800, 600), name, (255, 255, 0))
    if not os.path.exists("source-images"):
        os.mkdir("source-images")

    # img.show()
    img.save(imgname,"JPEG")
    shutil.move(imgname,"source-images")
    img.close()

ModifiteImage(nameFile)