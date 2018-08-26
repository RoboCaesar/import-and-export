#!/usr/bin/env python
import json
from pprint import pprint # A prettier way to display data (https://docs.python.org/3/library/pprint.html)


# Reference: https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
with open('small.city.list.json') as f:
    data = json.load(f)

print("This script will import data from a file.")
#pprint(data)

outdata = {}

print(len(data))
print(type(data))

for index in range(len(data)): 
    # print(data[index]["id"])
    # print(data[index]["coord"])
    # outdata[index]["id"] = data[index]["id"]
    # outdata[index]["coord"] = data[index]["coord"]
    # outdata[index]["name"] = data[index]["name"]
    # outdata[index]["country"] = data[index]["country"]
    outdata[index] = []
    outdata[index].append({
        'id': data[index]["id"],
        'coord': data[index]["coord"],
        'name': data[index]["name"],
        'country': data[index]["country"]
    })


pprint(outdata)

with open('output.json', 'w') as outf:
    json.dump(outdata, outf, indent=4)