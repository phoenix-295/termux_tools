import requests as r
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ['key']

resp = r.post(f"https://api.simple-mmo.com/v1/worldboss/all?api_key={key}")

y = json.loads(resp.text)

god_list = []
print("Gods list")
for each in y:
    if each["god"] == 1:
        if each["enable_time"] > int(time.time()):
            god_list.append(each["enable_time"])
god_list.sort()
for each in god_list:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(each)))

normal_list = []
print("Normal List")
for each in y:
    if each["god"] == 0:
        if each["enable_time"] > int(time.time()):
            normal_list.append(each["enable_time"])

normal_list.sort()

for each in normal_list:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(each)))