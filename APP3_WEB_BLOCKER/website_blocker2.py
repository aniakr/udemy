import time
from datetime import datetime as dt
from working_hours import working_hours

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
temp_path = "hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "www.gazeta.pl", "gazeta.pl"]

while True:
    if working_hours(dt.now()):
        print("Nie ma fejsa!!")
        with open(temp_path, "r+") as hosts:
            content = hosts.read()
            for web in websites_list:
                if web in content:
                    pass
                else:
                    hosts.write(redirect + " " + web + "\n")
    else:
        print("Fruruu")
        with open(temp_path, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(web in line for web in websites_list):
                    hosts.write(line)
            hosts.truncate()

    time.sleep(7)