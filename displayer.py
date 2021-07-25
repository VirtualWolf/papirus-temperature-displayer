#!/usr/bin/env python3

import os
import json
import requests
from papirus import PapirusTextPos

def read_configuration():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/config.json') as file:
        config = json.load(file)
        return config['url']

def get_data():
    r = requests.get(read_configuration())
    json = r.json()

    return json

def update_display():
    font = os.path.dirname(os.path.abspath(__file__)) + '/fonts/pixellium.ttf'
    data = get_data()

    # Don't update the screen immediately
    text = PapirusTextPos(False)

    outdoor_temperature = data['outdoor']['temperature'] + '\u00B0'
    indoor_temperature = data['indoor']['temperature'] + '\u00B0'

    outdoor_humidity = data['outdoor']['humidity'] + '%'
    indoor_humidity = data['indoor']['humidity'] + '%'

    text.AddText(outdoor_temperature, 6, -12, size=112, fontPath=font)
    text.AddText(outdoor_humidity, 180, 26, size=64, fontPath=font)

    text.AddText(indoor_temperature, 6, 82, size=112, fontPath=font)
    text.AddText(indoor_humidity, 180, 118, size=64, fontPath=font)

    # Once we've got everything in place, _then_ update the entire screen at once
    text.WriteAll()

if __name__ == '__main__':
    update_display()
