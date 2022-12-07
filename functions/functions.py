import json

def initJson():
    with open("resources/affairs.json","r") as fp:
        affairs_json = fp.read()
    affairs = json.loads(affairs_json)
    return affairs

# def new_affairs_json():

