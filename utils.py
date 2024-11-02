import os
import random
from operator import truediv


# パスを解決する処理を外に出しとくとごちゃるので
def pic_init():
    picname = './resource/kane.jpg'
    qrpath = os.path.abspath(picname)
    return qrpath

def get_random_map():
    maplist = ['アイスボックス', 'アセント', 'バインド', 'スプリット', 'パール', 'フラクチャー', 'ロータス', 'サンセット', 'ブリーズ', 'ヘイブン']
    map = random.choice(maplist)
    return map
# そらまめ対策
def sex_check(message):
    checklist = ['sex', 's3x', '𝑺𝑬𝑿', 'SEX', 'せっくす', 'セックス', 'Sex', 'sEx', 'seX', 'SEx', 'SeX', 'sEX']
    if message in checklist:
        return 1
    return 0
