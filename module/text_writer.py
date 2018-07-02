# coding: utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def write(image, text, fill):
    '''
    画像に引数で指定されたテキストを記述する
    Args:
        image: 画像データ
        text: 画像に記述するテキスト
        fill: テキストの色情報
    Returns:
        画像をタイル状に並べたサムネイルデータ
    '''
    font_size = 20
    draw_x = 20
    draw_y = 30
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    image = image.convert('RGB')
    draw = ImageDraw.Draw(image)
    draw.text((draw_x, draw_y), text, font=font, fill=fill)
    return image
