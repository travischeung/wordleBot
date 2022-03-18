# WordleBot
It's a bit of a mess and needs to be combed through later, but for now gets the job done.

The bot currently is pretty hard coded cuz I just wanted to get a proof of concept out before the NYT put an epic paywall on it. As a result, right now it is pretty fragile and many
edge cases are not accounted for.

Right now, the bot works by taking in Discord.py events and responding to on_message() calls. The on_message() takes the message event and takes the following elements:
```message.content``` and ```message.author```

The content of the message is broken into a list where if ```[0]=="Wordle"``` and then is parsed in the ```googleSheetsReadWrite.py``` file.

NB: The ```googleSheetsReadWrite.py``` file is currently very spaghetti (this is the part that I mentioned needs work). Good lucking reading this lmao, its doable but just gross.


# Requirements:
run the following:

```pip3 install discord.py```

```pip3 install gspread``` 

```pip3 install dotenv``` 

```pip3 install schedule``` 

You also need to get a DISCORDTOKEN to run the bot, as well as a security JSON for the Sheets API to work.
