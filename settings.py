__author__ = 'bmbayad'

import json


mainArray = []
unions = []
size = 0


def setup():
    global mainArray, unions, size
    with open("data.json") as inputJson:
        data = json.load(inputJson)
        size = data["size"]
        unions = data["union"]
        mainArray = [ i for i in range(size)]


