#! /usr/bin/env python3

import os
import json
import requests

text_files = os.listdir(r"/data/feedback")


for files in text_files:
    contentdict = {}
    with open ( r"/data/feedback/" + files ) as file:
        content = file.readlines()
        contentdict['title'] = content[0].strip('\n')
        contentdict['name'] = content[1].strip('\n')
        contentdict['date'] = content[2].strip('\n')
        contentdict['feedback'] = content[3].strip('\n')
        response = requests.post("http://http://35.226.98.227/feedback/", json=contentdict)
        print("Posted{} succesfully".format(str(files)))