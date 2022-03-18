###### pi@192.168.0.107
from email import message
import collections
import os
from xml.sax.handler import property_interning_dict
from googleapiclient import discovery
import discord
from discord.ext import commands
from dotenv import load_dotenv
import gspread
import schedule
import time

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# client = discord.Client()
bot = commands.Bot(command_prefix="!")
serverID = 936704754275483738


### sign into g-account and access the sheets
sa = gspread.service_account(filename="C:\\Users\\Travi\\Documents\\Code\\wordleBot\\assets\\wordle_write_credentials.json")
sh = sa.open("Wordle")
wk = sh.worksheet("Current Scores")
players = wk.get('D2:J2')
wordles = wk.get('C:C')
daysLeft = 31 -int(wk.get('B3')[0][0])
abc = "0abcdefghijklmnopqrstuvwxyz".upper()
memberDict = {}
@bot.event  # idk what this means but you have to do it
async def on_ready():  # when the bot is ready
    guild = discord.utils.get(bot.guilds, name=936704754275483738)
    print('{bot.user} has joined this cringe discord.')
    channel2 = bot.get_channel(936704754275483742)
    await channel2.send("I'm back, baby!")

def updateMembers(ctx):
    members = wk.get('L3:L9')
    rankings = wk.get('Q3:Q9')
    mean = wk.get('M3:M9')
    i = 0
    while i < len(members):
        ranked = rankings[i][0]
        memberDict[ranked] = [members[i][0],mean[i][0]]
        i+=1

### ugly as fuck but whatever, inputs the silly number and does it fine
def updateScores(targetPlayer, points, wordleNum):
    playerCell = wk.find(targetPlayer)
    if wk.find(wordleNum) is None:
        newWordleNum = int(wordleNum)-1
        try:
            newWordleCell = wk.find(str(newWordleNum))
            print(newWordleCell)
            # add the new wordle cell
            wk.update_cell(row=newWordleCell.row+1, col=newWordleCell.col, value=wordleNum)
            # update the score
            wk.update_cell(row=newWordleCell.row+1, col=playerCell.col, value=points)
        except:
            return "you arent valid stop stress testing me"
    else:
        wordleCell = wk.find(wordleNum)
        wk.update_cell(row=wordleCell.row, col=playerCell.col, value=points)
    return "sheets page epically updated"

@bot.command()
async def score(ctx):
    updateMembers(ctx)
    # design the response that will be sent
    msg = discord.Embed(title="Current Wordle Leaderboard",
    url="https://docs.google.com/spreadsheets/d/1HCbvbXUtEs9EQUn-KPtfW_2ZyvllE7XCL09st8ITAXo/edit?usp=sharing",
    description="Rankings:",
    color=0xe11414)
    msg.set_author(name="Days Left: %s" % (daysLeft),
    icon_url="https://www.cnet.com/a/img/resize/8906525406e54cace918e0a3f22edf58c46536ab/2022/01/10/db42e78a-77bb-45f1-ac02-5ee68e34d182/boombox.jpg?auto=webp&fit=crop&height=675&width=1200")

    for rank in collections.OrderedDict(sorted(memberDict.items())):
        msg.add_field(name=memberDict[rank][0], value="Current Avg: {}".format(memberDict[rank][1]), inline=False)
    await ctx.send(embed=msg)
    return

# responds to the bot message
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    messageList = message.content.split()
    # exit message parse if sender is a bot
    if message.author == bot.user:
        return
    if message.content.startswith("Wordle"):
        sender = message.author.display_name.strip('\#')
        points = messageList[2][0]
        if (int(points) not in range(1,7)):
            await message.channel.send("nice try cheater...")
            return
        wordleNum = messageList[1]
        updateStatus = updateScores(sender, points, wordleNum)
        await message.channel.send(updateStatus)
        return

# everyday at 11:59 will input 6 for all people who missed the day
def missedSubmission():
    currWordle = [i for i in wordles if i][-1]
    wk.find(currWordle)
    slackers = wk.findall(query='', in_row=currWordle.row)
    for slacker in slackers:
        updateScores(slacker, 6, currWordle)

# checks for end of playing month (31 days)
@bot.event
async def monthEnd(ctx):
    if daysLeft == 0:
        winner = collections.OrderedDict(sorted(memberDict.items()))[0]
        # Send congrats
        msg =discord.Embed(title="End of the current playing period!", description="Winner of this month is: ")
        msg.add_field(name="{}".format(winner[0]), value="Average of Avg: {}".format(memberDict[1]), inline=True)
        await ctx.send(embed=msg)

schedule.every().day.at("23:59").do(missedSubmission)
schedule.every().day.at("23:59").do(monthEnd)




bot.run(TOKEN)
