import json

def initJson():
    with open("resources/affairs.json","r") as fp:
        if fp != None:
            affairs_json = fp.read()
            affairs = json.loads(affairs_json)
            return affairs

def new_affairs_json(affairs, name, text, data, priority):
    item = json.dumps({"name": name, "text": text, "data": data, "priority": priority})
    item = json.loads(str(item))
    affairs["affairs"].append(item)
    affairs = json.dumps(affairs)
    affairs = json.loads(str(affairs))
    with open("resources/affairs.json","w", encoding='utf-8') as fp:
        json.dump(affairs, fp, indent=2)
    return affairs
