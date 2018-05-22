# encoding
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# TODO 全く同じコードが存在する
def add(image_path, result, file_name=None):
    if file_name == None:
        file_name = image_path.split('/')[-1]
    font_size = 40
    draw_x = 30
    draw_y = 30
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    text = 'OK' if result else 'NG'
    fill = '#0000ff' if result else '#ff0000'
    image = Image.open(image_path).resize((224, 224))
    image = image.convert('RGB')
    draw = ImageDraw.Draw(image)
    draw.text((draw_x, draw_y), text, font=font, fill=fill)
    image.save("./util/image_util/output/tmp/" + file_name + ".jpg")
