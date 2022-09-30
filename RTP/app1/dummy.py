import requests
import json

url = "https://www.fast2sms.com/dev/bulkV2"
message='This Message Is A Normal Text Message'

querystring = {"authorization":"3jrwpnUzdAtoQ1fWGCXiSgamOPx8qT0IZs5Ju9bRFy2vLB4kEcHTwCe5WSN6iK3QYM7yR1BtE0c2zJoF",
               "sender_id":"TXTIND",
               "message":message,
               "route":"v3",
               "numbers":contact,
               }

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.status_code)
#print(response.text)
#convert from json_data into python
json_data = response.text
d1=json.loads(json_data)
if d1['return']:
    print('message sent')
else:
    print('message is not send')
