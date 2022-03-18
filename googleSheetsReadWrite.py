from fileinput import filename
import discord
from wordleBoyScript import client
import gspread
import discord

# NOTE: session kept alive using tmux

### sign into g-account and access the sheets   
sa = gspread.service_account(filename="C:\\Users\\Travi\\Documents\\Code\\wordleBot\\assets\\wordle_write_credentials.json")
sh = sa.open("Wordle")
wk = sh.worksheet("Populated Sheet")
# 
players = wk.row_values(2)
wordles = wk.col_values(3)
abc = "0abcdefghijklmnopqrstuvwxyz".upper()
memberDict = {}

for guild in client.guilds:
    for member in guild.members:
        memberDict.update(member = ["INPUT RANKING","INPUT MONTH AVG"])
        
## this allows the bot to refresh the wksheet with every input (keeps it fresh ya dig)
def updateWK():
    players = wk.row_values(2)
    wordles = wk.col_values(3)

### ugly as fuck but whatever, inputs the silly number and does it fine
def wordleDetected(targetPlayer, points, wordleNum):
    updateWK()
    # gets the row # of the current wordle
    currWordle = 0
    if str(wordleNum) in wordles:
        for wordle in range(len(wordles)):
            if wordles[currWordle] == wordleNum:
                currWordle=currWordle+1
                print(currWordle)
                break
            else:
                currWordle=currWordle+1
    ### adds the day's wordle if not already added
    else:
        currWordle = len(wordles)+2
        wk.update('C'+str(currWordle), wordleNum)
    ### updates the player now
    try:
        playerIndex = 1
        for index in range(len(players)):
            if players[index] == targetPlayer:
                playerColumn = abc[playerIndex]
                break
            else:
                playerIndex=playerIndex+1
        matrix =  playerColumn+str(currWordle)
        wk.update(matrix, int(points))
        return "sheets page epically updated"
    except:
        print(targetPlayer)
        print(players)
        return "travis did not consider this edge case. update failed."
def leaderboard(ctx):
    msg = discord.Embed(title="Current Wordle Leaderboard", url="https://docs.google.com/spreadsheets/d/1HCbvbXUtEs9EQUn-KPtfW_2ZyvllE7XCL09st8ITAXo/edit?usp=sharing", description="Rankings:", color=0xe11414)
    msg.set_author(name=" Wordle Bot", icon_url="https://www.cnet.com/a/img/resize/8906525406e54cace918e0a3f22edf58c46536ab/2022/01/10/db42e78a-77bb-45f1-ac02-5ee68e34d182/boombox.jpg?auto=webp&fit=crop&height=675&width=1200")
    # TODO: set up the names to output the scores of actual people
    for rankedMember in sorted(memberDict.keys()):
        msg.add_field(name=rankedMember, value="Current Avg: {}".format(rankedMember[0]), inline=False)
    ctx.send(embed=msg)
    return