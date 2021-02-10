import gspread 
import sys
import json
from oauth2client.service_account import ServiceAccountCredentials

with open('/usr/src/app/config/config.json','r') as json_file:
    dados = json.load(json_file)['env']
of = dados['OUTPUT_FILE']
gac = dados['GOOGLE_APPLICATION_CREDENTIALS']

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(gac, scope)
client = gspread.authorize(creds)
worksheet = client.open('VendeTudo').sheet1
loja = worksheet.get_all_records()

with open(of, 'w') as json_file:
    json.dump(loja, json_file, indent=4)

print("docker funcionando!")