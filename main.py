import os
from dotenv import load_dotenv

import discord
import copy
import sudoku

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("connected")
    
@client.event
async def on_message(message):
    
    if message.content == "!sudoku":
        # ランダムな数独の問題を作成します。
        board = sudoku.generate_puzzle(num_blanks)


        # 問題を解決します。
        board_copy = copy.deepcopy(board)
        sudoku.solve(board_copy)
        
        # 解答を整形して、Discordチャンネルに送信します。
        response = "Problem:\n"
        for i in range(len(board)):
            for j in range(len(board[0])):
                response += f"{board[i][j]} "
                if j == 2 or j == 5:
                    response += "| "
            response += "\n"
            if i == 2 or i == 5:
                response += "------+-------+------\n"
       
        await message.channel.send(response)
        


load_dotenv()

num_blanks = 40  # Number of blank cells in the puzzle
    
client.run(os.environ['TOKEN'])