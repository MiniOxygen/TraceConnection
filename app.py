import os
import json
import requests
import re

tracert_output = os.popen("tracert google.com").read()

ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", tracert_output)

for ip in ip_list:
    url = f"http://ip-api.com/json/{ip}?fields=city"
    response = requests.get(url)
    data = json.loads(response.text)
    try:
        print(ip + ": " + data["city"])
    except:
        print(ip + ": INDIRIZZO PRIVATE")

x = input()
