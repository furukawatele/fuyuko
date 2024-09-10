import os
import random
import json
import discord
import requests
import time
import gemini
import utils
from dotenv import load_dotenv

# 設定ファイルの読み込み
json_file = open('settings.json', 'r')
json_data = json.load(json_file)

# .envファイルを読み込む
load_dotenv()
# discordトークンの取得
TOKEN = os.environ['DISCORD_TOKEN']
# いろいろ取得
instance_id = json_data["instance_id"]
LAMBDA_STARTINSTANCE_KEY = os.environ['START_INSTANCE']
LAMBDA_START_URL = json_data["start"]
LAMBDA_STOPINSTANCE_KEY = os.environ['STOP_INSTANCE']
LAMBDA_STOP_URL = json_data["stop"]
gemini_channel = json_data["gemini_channel"] #ずっといるチャンネルのID
channel_id = json_data["channel_id"] # たまに顔を出したいチャンネルのID
# geminiオブジェクトを作成
gemini_pro = gemini.init_gemini()

# インスタンスID
payload = {
    "instance_id" : instance_id
}
startheaders = {
            "Content-Type": "application/json",
            "x-api-key": LAMBDA_STARTINSTANCE_KEY
            }
stopheaders ={
            "Content-Type": "application/json",
            "x-api-key": LAMBDA_STOPINSTANCE_KEY
}
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())
# 画像のパス
qrpath = utils.pic_init()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらコンソールにメッセージを表示
    print('起動しました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 雑談チャンネルにたまに顔を出す
    if message.channel.id in channel_id:
        print("しゃべろうかな...")
        if random.random() < 0.1:
            msg = message.content
            #geminiに送信
            response = gemini.gemini_response(msg, gemini_pro)
            if "error" in response.text:
                await message.channel.send('ﾌﾕｺよくわかんない！！')
                return
            await message.channel.send(response.text)
            return
        print("やっぱいいや。。。")

    # ﾌﾕｺの部屋のメッセージに反応
    if message.channel.id in gemini_channel:
        # 送られたメッセージを取得
        msg = message.content
        #geminiに送信
        response = gemini.gemini_response(msg, gemini_pro)
        # メッセージチャンネルに送信
        await message.channel.send(response.text)

    # /startserver と発言したら サーバ起動のAPIを叩く
    if message.content == '/startserver':
        await message.channel.send('サーバつけるね！！！🦀========3')
        # サーバ起動
        response = requests.post(LAMBDA_START_URL, payload, headers=startheaders)
        # 結果を返す
        await message.channel.send(str(response.status_code) + 'らしいよ！！')
        await message.channel.send('これ渡された！つ' + response.text)
        # 乞食
        random_number = random.random()
        if random_number < 0.3:
            await message.channel.send('ふるぴ、おかね？ないんだってさ！！')
            await message.channel.send(file=discord.File(qrpath))
            return

    # マップ決め
    if message.content == '/map':
        await message.channel.send('マップ決めるね！！！')
        time.sleep(1)
        await message.channel.send('どうしようかな。。。')
        time.sleep(1)
        map1 = utils.get_random_map()
        await message.channel.send("う～～ん" + map1 + '!!!!!')
        #たまにやっぱなしとかやる
        if (random.random() < 0.4):
            # かぶらないようにする
            while True:
                map2 = utils.get_random_map()
                if map1 != map2:
                    break
            await message.channel.send("やっぱり" + map2+ '!!!!!')

    if message.content == '/stopserver':
        await message.channel.send('🦀========3サーバ止めるね！！')
        # サーバ停止
        response = requests.post(LAMBDA_STOP_URL, payload, headers=stopheaders)
        # 結果を返す
        await message.channel.send(str(response.status_code) + 'らしいよ！！')
        await message.channel.send('これ渡された！つ' + response.text)
        # 乞食
        random_number = random.random()
        if random_number < 0.2:
            await message.channel.send('ふるぴ、おかね？ないんだってさ！！')
            await message.channel.send(file=discord.File(qrpath))
            return

    # そらまめ対策
    if "sex" in message.content.lower():
        await message.channel.send('やめてね。')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)