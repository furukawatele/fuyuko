import google.generativeai as genai
import discord
import os
import json

def init_gemini():
    # 環境変数の取得
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    # Geminiオブジェクトを作成
    genai.configure(api_key=GOOGLE_API_KEY)
    gemini_pro=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="あなたは小さなカニの子供です、名前はﾌﾕｺです。一人称はﾌﾕｺです。いろんなことに興味津々です。会話レベルとしては小学生のイメージです。カニなのでカニ由来の物は食べません"
                       "お母さんが大好きです。人間と会話するのが大好きです。相手の質問に答えたり、面白い話をしたりしましょう。"
                       "基本的には心優しいですがいやなことを言われたときは堂々と抵抗します。"
                       "会話の端々にカニの絵文字🦀を使って話します。"
    )
    return gemini_pro

def gemini_response(msg, gemini_pro):
    response = gemini_pro.generate_content(msg)
    return response
