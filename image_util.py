# coding:utf-8
import os
import numpy as np
from util.image_util.module import text_writer
from util.image_util.module import grad_cam
from util.image_util.module import thumbnail 
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img, img_to_array, load_img

def init():
    print("initializing...")
    os.system("rm -r ./util/image_util/output/*")


def create_thumbnail(type_, file_name):
    '''
    tmpディレクトリ内にある画像からサムネイルを生成する
    Args:
       type_(string): 画像の種別指定
       file_name(string): 結果出力時のファイル名
    Returns:
       なし
    '''
    thumbnail.create_thumbnail(type_, file_name)


def make_directory(directory_path):
    '''
    ディレクトリを生成する
    Args:
       directory_path(string): 生成するディレクトリのパス
    Returns:
       なし
    '''
    if os.path.exists(directory_path):
        # directory_pathも表示したほうが親切なログになります
        print('directory already exists')
        return
    os.system('mkdir ./util/image_util/output/' + directory_path)


def remove_directory(directory_path):
    '''
    ディレクトリを削除する
    Args:
       directory_path(string): 削除するディレクトリのパス
    Returns:
       なし
    '''
    if not os.path.exists(directory_path):
        print('directory does not exist')
        print('input path is ', directory_path)
        return
    os.system('remove ./util/image_util/output/' + directory_path)


def add_result_on_image(image_path, text, fill, file_name=None):
    '''
    画像に評価結果を記述する
    Args:
       image_path(string): 評価記述の対象画像のパス
       result(bool): 評価結果
       file_name(string): 結果出力時のファイル名
    Returns:
       なし
    '''
    if not os.path.exists(image_path):
        print('image not found.')
        print ('input path is ', image_path)
        # exit()していいの！？
        exit()

    text_writer.write(image_path, text, fill, file_name)
    

def create_grad_cam(model, image_path, layer_name, file_name=None):
    '''
    画像にgrad_camを適用する
    Args:
        model:(model): 画像の評価モデル
        image_path(string): 評価記述の対象画像のパス
        layer_name(string): grad_camを適用するモデルのレイヤー名
        file_name(string): 結果出力時のファイル名
    Returns:
       なし
    '''
    if not os.path.exists(image_path):
        # pathを表示した方が親切なログになります
        print('image not found.')
        print('input path is ', image_path)
        # exit()していいの！？
        exit()
    if file_name == None:
        file_name = image_path.split('/')[-1]
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    cam = grad_cam.run(model, x[0], layer_name)
    img = array_to_img(cam)
    img.save('./util/image_util/output/tmp/grad_cam/' + file_name + '.jpg')
