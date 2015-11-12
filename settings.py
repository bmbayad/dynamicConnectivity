__author__ = 'bmbayad'

import json

mainArray = []
levelsArray = []

unions = []
size = 0


def setup():
    global mainArray, unions, size, levelsArray
    with open("data.json") as inputJson:
        data = json.load(inputJson)
        size = data["size"]
        unions = data["union"]
        mainArray = [i for i in range(size)]

    levelsArray = [1 for i in range(size)]
