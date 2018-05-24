# encoding
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def write(image, text, fill):
    font_size = 20
    draw_x = 20
    draw_y = 30
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    image = image.convert('RGB')
    draw = ImageDraw.Draw(image)
    draw.text((draw_x, draw_y), text, font=font, fill=fill)
    return image
