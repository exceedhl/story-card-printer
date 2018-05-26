import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('API Project-f0091087a4aa.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Test Script").sheet1
print(len(wks.get_all_values()))
