import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
temp_path = "hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "www.gazeta.pl", "gazeta.pl"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 17) < \
            dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Nie ma fejsa!!")
        with open(hosts_path, "r+") as hosts:
            content = hosts.read()
            for web in websites_list:
                if web in content:
                    pass
                else:
                    hosts.write(redirect + " " + web + "\n")
    else:
        print("Fruruu")
        with open(hosts_path, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(web in line for web in websites_list):
                    hosts.write(line)
            hosts.truncate()

    time.sleep(7)
