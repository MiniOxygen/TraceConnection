from flask import Flask, render_template, request
import os
import json
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tracert', methods=['POST'])
def tracert():
    url = request.form['url']
    tracert_output = os.popen(f"tracert {url}").read()
    ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", tracert_output)
    result = []

    for ip in ip_list:
        ip_data = {}
        ip_data['ip'] = ip
        url = f"http://ip-api.com/json/{ip}?fields=city"
        response = requests.get(url)
        data = json.loads(response.text)
        if 'city' in data:
            ip_data['city'] = data['city']
        else:
            ip_data['city'] = 'INDIRIZZO PRIVATO'
        result.append(ip_data)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
