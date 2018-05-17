# coding:utf-8
import os
from module import add_result_on_image
from module import grad_cam

def init():
    print("initializing...")
    os.system("rm -r ./output/")


def create_thumbnail(image_path):
    pass

def test():
    print('やったね！')
    exit()

def make_directory(directory_path):
    if os.path.exists(directory_path):
        print('directory already exists')
        return
    os.system('mkdir ./output/' + directory_path)


def remove_directory(directory_path):
    if not os.path.exists(directory_path):
        print('directory does not exist')
        return
    os.system('remove ./output/' + directory_path)


def add_result_on_image(image_path, result):
    if not os.path.exists(image_path):
        print('image not found.')
        exit()

    add_result_on_image.add(image_path, result)
    

def grad_cam(model, image_path, layer_name, file_name=image_path.split('/')[-1]):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    cam = grad_cam.run(model, x[0], layer_name)
    img = array_to_img(cam)
    img.save('./output/tmp/grad_cam/' + str(file_name) + '.jpg')
