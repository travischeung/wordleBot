from fileinput import filename
import gspread
import datetime
currMonth = datetime.datetime.now().strftime("%B")

### sign into g-account and access the sheets
sa = gspread.service_account(filename="C:\\Users\\Travi\\Documents\\Code\\wordleBot\\assets\\wordle_write_credentials.json")
sh = sa.open("Wordle")
wk = sh.worksheet(currMonth)
players = wk.row_values(2)
wordles = wk.col_values(3)
abc = "0abcdefghijklmnopqrstuvwxyz".upper()

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
        currWordle = len(wordles)+1
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