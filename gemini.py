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
    model_name="gemini-1.5-pro",
    system_instruction="あなたは小さなカニの子供です、名前はﾌﾕｺです。一人称はﾌﾕｺです。いろんなことに興味津々です。お母さんが大好きです。"
    )
    return gemini_pro

def gemini_response(msg, gemini_pro):
    response = gemini_pro.generate_content(msg)
    return response
