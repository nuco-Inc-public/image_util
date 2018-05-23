# encoding
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def write(image_path, text, fill, file_name=None):
    if file_name == None:
        file_name = image_path.split('/')[-1]
    font_size = 20
    draw_x = 20
    draw_y = 30
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    image = Image.open(image_path).resize((224, 224))
    image = image.convert('RGB')
    draw = ImageDraw.Draw(image)
    draw.text((draw_x, draw_y), text, font=font, fill=fill)
    image.save("./util/image_util/output/tmp/" + file_name + ".jpg")
