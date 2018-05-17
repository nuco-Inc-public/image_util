# coding:utf-8
import glob
import os
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from util import grad_cam
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img, img_to_array, load_img

def run(output_image ,predict_result, model, layer_name):
    __init()

    index_ = 0
    for small_category_path, small_category_result in zip(output_image, predict_result):
        write_text(small_category_path, small_category_result, type_='normal')
        grad_cam_path = add_heat_map(small_category_path, model, layer_name)
        # write_text(grad_cam_path, small_category_result, type_='grad_cam')
        
        create_thumbnail(index_, type_='grad_cam')
        create_thumbnail(index_, type_='normal')
        index_ += 1
    print('Thumbnail creation finished')

def __init():
    print("initializing...")
    os.system("rm -r ../output/images/*")
    os.system("rm -r ../output/thumbnail/*")
    os.system("mkdir ../output/images/normal")
    os.system("mkdir ../output/images/grad_cam")
    os.system("mkdir ../output/thumbnail/normal")
    os.system("mkdir ../output/thumbnail/grad_cam")

def create_concat_tile(img_list2D):
    im_list_v = [get_concat_h(im_list_h) for im_list_h in img_list2D]
    return get_concat_v(im_list_v)
    
def get_concat_h(im_list1D):
    total_height = min(im.height for im in im_list1D)
    total_width = sum(im.width for im in im_list1D)
    dst = Image.new('RGB', (total_width, total_height))
    pos_x = 0
    for im in im_list1D:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst

def get_concat_v(im_list1D):
    total_height = sum(im.height for im in im_list1D)
    total_width = min(im.width for im in im_list1D)
    dst = Image.new('RGB', (total_width, total_height))
    pos_y = 0
    for im in im_list1D:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst
    
def write_text(small_category_path, small_category_result, type_):
    font_size = 40
    draw_x = 30
    draw_y = 30
    output_file_name = 0
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    for image_path, acc in zip(small_category_path, small_category_result):
        file_name = image_path.split('/')[-1]
        text = 'OK' if acc else 'NG'
        fill = ('#0000ff') if acc else ('#ff0000')
        image = Image.open(image_path).resize((224, 224))
        draw = ImageDraw.Draw(image)
        draw.text((draw_x, draw_y), text, font=font, fill=fill)
        image.save("../output/images/" + type_ + "/" + str(output_file_name) + ".jpg")
        output_file_name += 1
    
def add_heat_map(small_category_path, model, layer_name):
    file_name = 0
    for image_path in small_category_path:
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        cam = grad_cam.run(model, x[0], layer_name)
        img = array_to_img(cam)
        img.save('../output/images/grad_cam/' + str(file_name) + '.jpg')
        file_name += 1
    grad_cam_path = glob.glob('../output/images/grad_cam/*')
    grad_cam_path.sort()

    return grad_cam_path

def create_thumbnail(index_,type_):
    count = 0
    row_list = []
    img_list2D = []
    print(len(glob.glob("../output/images/" + type_ + "/*.jpg")))
    image_path_list = glob.glob("../output/images/" + type_ + "/*.jpg")
    image_path_list.sort()
    for image_path in image_path_list:
        row_list.append(Image.open(image_path).resize((224, 224)))
        count += 1
        if count == 5:
            count = 0
            img_list2D.append(row_list)
            row_list = []
            continue
    create_concat_tile(img_list2D).save("../output/thumbnail/" + type_ + "/" + str(index_) + ".jpg")

    
