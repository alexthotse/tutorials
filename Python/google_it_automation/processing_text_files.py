1. sudo apt-get update
2. sudo apt install python-django-common
3. sudo ssystemctl start google-startup-scripts.service


#! /usr/bin/env python3

import os
import requests

path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    reponse = requests.post("http://<IP Address>/feedback/",json=fb)

print(response.request.body)
print(response.status_code)


