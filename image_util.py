# coding:utf-8
import os
import io
import numpy as np
from PIL import Image
from keras.preprocessing import image
from util.image_util.module import grad_cam
from util.image_util.module import thumbnail 
from util.image_util.module import text_writer
from keras.preprocessing.image import array_to_img, img_to_array, load_img

def init():
    '''
    前回生成されたoutputデータをすべて削除する
    Args:
        なし
    Returns:
        なし
    '''
    print("initializing...")
    os.system("rm -r ./util/image_util/output/*")


def create_thumbnail(images):
    '''
    tmpディレクトリ内にある画像からサムネイルを生成する
    Args:
        20枚の画像データ
    Returns:
        生成されたサムネイルデータ

    '''
    return thumbnail.create_thumbnail(images)


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


def add_result_on_image(image, text, fill):
    '''
    画像に評価結果を記述する
    Args:
        image_path(string): 評価記述の対象画像のパス
        result(bool): 評価結果
        file_name(string): 結果出力時のファイル名
    Returns:
        なし
    '''

    return text_writer.write(image, text, fill)
    

def create_grad_cam(model, layer_name):
    '''
    画像にgrad_camを適用する
    Args:
        model:(model): 画像の評価モデル
        layer_name(string): grad_camを適用するモデルのレイヤー名
    Returns:
       function (PIL Image Object) -> PIL Image Object
    '''
    def f(img):
        cam = grad_cam.run(model, img, layer_name)
        img = array_to_img(cam)
        return img
    return f


def img2bytes(img):
    '''
    画像データをバイナリデータに変換する
    Args:
        画像データ
    Returns:
       バイナリデータ
    '''
    f = io.BytesIO()
    img.save(f, format='JPEG')
    return f.getvalue()


def bytes2img(bs):
    '''
    バイナリデータを画像データに変換する
    Args:
        バイナリデータ
    Returns:
        画像データ
    '''
    img_bin = io.BytesIO(bs)
    return Image.open(img_bin)
