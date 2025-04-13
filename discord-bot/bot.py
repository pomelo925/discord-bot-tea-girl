import discord  
from discord.ext import commands 

# 創建機器人對象，指定前綴為 "!"，即用戶發送消息時需要以 "!" 開頭
intents = discord.Intents.default()
intents.message_content = True  # 啟用 message_content intent 來接收伺服器訊息

bot = commands.Bot(command_prefix="!", intents=intents)

import os
token = os.getenv("DISCORD_TOKEN")

# 當機器人成功登入並準備好接收消息時，會執行此函數
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}') 

# 當收到 "ping" 訊息時，機器人會回應 "pong"
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

# 啟動機器人
if token:
    bot.run(token)
else:
    print("錯誤：未找到 Discord Bot Token，請檢查環境變數設定。")