#20CS023 Jayraj Karelia
def addkey(dict,keyname,keyvalue):
    dict[keyname] = keyvalue
    return dict

dict = {0: 10, 1: 20}
keyname = 2
keyvalue = 30

dict = addkey(dict,keyname,keyvalue)

print(dict)