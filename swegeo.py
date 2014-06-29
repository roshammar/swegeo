# -*- coding: utf-8 -*-

import json

TOWNS = json.load(open('tatort-kommun.json')) # tätort -> kommun
REGIONS = json.load(open('komm-lan.json')) # kommun -> län

def get_region(town):
    return REGIONS[TOWNS[town]]