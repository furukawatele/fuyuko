import os
import random


# パスを解決する処理を外に出しとくとごちゃるので
def pic_init():
    picname = './resource/kane.jpg'
    qrpath = os.path.abspath(picname)
    return qrpath

def get_random_map():
    maplist = ['アイスボックス', 'アセント', 'バインド', 'スプリット', 'パール', 'フラクチャー', 'ロータス', 'サンセット', 'ブリーズ', 'アビス']
    map = random.choice(maplist)
    return map


