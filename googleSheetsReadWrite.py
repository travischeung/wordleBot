import pygsheets
from googleapiclient.discovery import build 
import pandas as pd

# Google API set up
from google.oauth2 import service_account
SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
authFile = 'C:\\Users\\Travi\\Documents\\Code\\wordleBot\\assets\\googleAuthWordleBot.json'
credentials = service_account.Credentials.from_service_account_file(authFile, scopes=SCOPES)
spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)

# authFile = 'C:\\Users\\Travi\\Documents\\Code\\wordleBot\\assets\\clientSecretsWordleBot.json'
gc = pygsheets.authorize(authFile)

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('wordle bot test env')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))



###### current todo: download secret from OAuth 2.0 Client ID table when it becomes available (?)
