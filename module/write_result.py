# encoding



def write_result_per_image(image_path, result):
    file_name = image_path.split('/')[-1]
    text = 'OK' if acc else 'NG'
    fill = ('#0000ff') if acc else ('#ff0000')
    image = Image.open(image_path).resize((224, 224))
    draw = ImageDraw.Draw(image)
    draw.text((draw_x, draw_y), text, font=font, fill=fill)
    # TODO インデックスでリネーム
    image.save("../output/images/" + type_ + "/" + file_name)
