#! /usr/bin/env python3
# cahnging_names
# import os, sys
# from PIL import Image

# user = os.getenv('USER')
# image_directory = f"/home/{user}/supplier-data/images/"

# for image_names in os.listdir(image_directory):
#     if not image_names.startswith('.') and 'tiff' in image_names:
#         image_path = image_directory + image_names
#         path = os.path.splitext(image_path) [0]
#         im = Image.open(image_path)
#         new_path = f"{path}.jpeg"
#         im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")




#--------------------------supplier_image_upload.py---------------------------------
#! /usr/bin/env python3

import requests, os

url = "http://localhost/upload/"

USER = os.getenv('USER')

image_directory = '/home/{}/supplier-data/images/'.format(USER)

files = os.listdir(image_directory)

for image_names in files:
    if not image_names.startswith('.') and 'jpeg' in image_names:
        image_path = image_directory + image_names
        with open(image_path, 'rb') as opening:
            read = requests.post(url, files={'file': opened})



#--------------------------run.py---------------------------------

#! /usr/bin/env python3

import os, requests, json


def catalog(url, description_directory):
    fruit = {}
    for item in os.listdir(description_directory):
        fruit.clear()
        filename = os.path.join(description_directory,item)
        with open(filename) as food:
            line = food.readlines()
            description = ""
            for i in range(2,len(line)):
                description=description+line[i].strip('\n').replace(u'\xaO',u'')
            fruit["description"]=description
            fruit["weight"]=int(line[1].strip('\n').strip('lbs'))
            fruit["name"]=line[0].strip('\n')
            fruit["image_name"]=(item.strip('.txt'))+'.jpeg'
            print(fruit)
            if url != "":
                response = requests.post(url, json=fruit)
                print(response.request.url)
                print(response.status_code)
    return 0

if __name__ == "__main__":
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    catalog(url, description_directory)


#--------------------------reports.py---------------------------------

#!/usr/bin/env python3

# from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
# from reportlab.lib.styles import getSampleStyleSheet

# def  generate_report(file, title, add_info):
#     styles = getSampleStyleSheet()
#     report = SimpleDocTemplate(file)
#     report_title = Paragraph(title, styles['h1'])
#     report_info = Paragraph(add_info, styles['BodyText'])
#     empty_lines = Spacer(1, 20)

#     report.build([report_title, empty_lines, report_info, empty_lines])


#--------------------------report_email.py---------------------------------

#! /usr/bin/env python3

import datetime, os

from run import catalog
from reports import generate_report
from emails import generate_email, send_email

def pdf_body(input_for, description_directory):
    res = []
    wt = []
    for item in os.listdir(description_directory):
        filename=os.path.join(description_directory, item)
        with open(filename) as found:
            line=found.readlines()
            weight=line[1].strip('\n')
            name=line[0].strip('\n')
            print(name,weight)
            res.append('name: ' + name)
            wt.append('weight: ' + weight)
            print(res)
            print(wt)
    new_object = ""
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_object += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_object

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on ' + str(current_date)
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf', description_directory))
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached'
    msg = generate_email("automation@example.com", "student-01-244f6b63944f@example.com".format(user),email_subject, email_body, "/tmp/processed.pdf")

    send_email(msg)

#--------------------------emails.py---------------------------------

# #!/usr/bin/env python3


# import email
# import mimetypes
# import smtplib
# import os

# def generate_email(sender, recipient, subject, body, attachment_path):
#     message = email.message.EmailMessage()
#     message["From"] = sender
#     message["To"] = recipient
#     message["Subject"] = subject
#     message.set_content(body)
    
#     if not attachment_path == "":
#         attachment_filename = os.path.basename(attachment_path)
#         mime_type, _ = mimetypes.guess_type(attachment_path)
#         mime_type, mime_subtype = mime_type.split('/', 1)

#         with open(attachment_path, 'rb') as ap:
#             message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)
    
#     return message     

# def send_email(message):
#     mail_server = smtplib.SMTP('localhost')
#     mail_server.send_message(message)
#     mail_server.quit()


#
#--------------------------health_check.py---------------------------------

#!/usr/bin/env python3
import socket
import shutil
import psutil
import emails

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20 

def check_memory_usage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def send_email(subject):
    email = emails.generate_email("automation@example.com", "<>@example.com",subject,"Please check your system and resolve the issuse as soon as possible")
    emails.send_email(email)


if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    print(subject)
    send_email(subject)

if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
if not check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    send_email(subject)
if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    send_email(subject)    

