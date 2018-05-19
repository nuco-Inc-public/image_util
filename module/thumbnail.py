# coding:utf-8
import os
import glob
from PIL import Image

def create_concat_tile(img_list2D):
    '''
    2次元のリストに並べた画像をrow単位→column単位の順に結合する処理を呼びだす
    Args:
       img_list2D (2Dのlist): 画像データを格納したの2次元リスト
    Returns:
        画像をタイル状に並べたサムネイルデータ
    '''
    im_list_v = [get_concat_h(im_list_h) for im_list_h in img_list2D]
    return get_concat_v(im_list_v)
    

def get_concat_h(im_list1D):
    '''
    1次元の配列の画像をrow方向に結合する
    Args:
       img_list1D (1Dのlist): 画像データを格納したの1次元リスト
    Returns:
        画像をrow方向に結合した画像データ
    '''
    total_height = min(im.height for im in im_list1D)
    total_width = sum(im.width for im in im_list1D)
    dst = Image.new('RGB', (total_width, total_height))
    pos_x = 0
    for im in im_list1D:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst


def get_concat_v(im_list1D):
    '''
    1次元の配列の画像をcolumn方向に結合する
    Args:
       img_list1D (1Dのlist): 画像データを格納したの1次元リスト
    Returns:
        画像をcolumn方向に結合した画像データ
    '''
    total_height = sum(im.height for im in im_list1D)
    total_width = min(im.width for im in im_list1D)
    dst = Image.new('RGB', (total_width, total_height))
    pos_y = 0
    for im in im_list1D:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst
    

def create_thumbnail(type_, file_name):
    '''
    output/tmp/type_/内の画像を1枚のサムネイルに並べる
    TODO: 20枚未満の場合への対応
    Args:
       type_ (string): サムネイルにする画像の種別
       file_name (string): ファイル名
    Returns:
       なし
    '''
    count = 0
    row_list = []
    img_list2D = []
    image_path_list = glob.glob("./util/image_util/output/tmp/" + type_ + "/*.jpg")
    image_path_list.sort()
    for image_path in image_path_list:
        row_list.append(Image.open(image_path).resize((224, 224)))
        count += 1
        if count == 5:
            count = 0
            img_list2D.append(row_list)
            row_list = []
            continue
    create_concat_tile(img_list2D).save("./util/image_util/output/thumbnail/" + type_ + "/" + file_name + ".jpg")
    print('Craeted thumnail type: %s, file_name: %s' %(type_, file_name))

    
