import time
from datetime import datetime as dt
from working_hours import working_hours

def block_websites(hosts_path, redirect_target, websites_black_list):
    while True:
        if working_hours(dt.now()):
            print("Nie ma fejsa!!")
            with open(hosts_path, "r+") as hosts:
                content = hosts.read()
                for web in websites_black_list:
                    if web in content:
                        pass
                    else:
                        hosts.write(redirect_target + " " + web + "\n")
        else:
            print("Fruruu")
            with open(hosts_path, "r+") as hosts:
                content = hosts.readlines()
                hosts.seek(0)
                for line in content:
                    if not any(web in line for web in websites_black_list):
                        hosts.write(line)
                hosts.truncate()

        time.sleep(7)



