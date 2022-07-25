import re

file_in = open("intrare.txt", "r")
file_out = open("iesire.txt", "w")
file_content = file_in.read()

def take_mails(mail_file):
    return re.findall('[a-z0-9\.\-\_]+@[a-z0-9\.\-\_]+', mail_file)

mail_list = take_mails(file_content)

if mail_list:
    mail = set(mail_list)
    str_data = ""
    for item in mail:
        str_data = str_data + item + '\n'
    file_out.write(str_data)
else:
    print("no mails!")