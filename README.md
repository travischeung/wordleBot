# WordleBot
Rebuilt from the bottom up, using more of the actual Discord.py API. Much easier to read and add onto. 
NB:
The on_message and the actual commands (prefix: !) are handled independently. The command_prefix utilization makes it a lot more modular and able to be expanded.

# Requirements:
run the following:

```pip3 install discord.py```

```pip3 install gspread``` 

```pip3 install dotenv``` 

```pip3 install schedule``` 

```pip3 install google-api-python-client``` 

You also need to get a DISCORDTOKEN to run the bot, as well as a security JSON for the Sheets API to work.
