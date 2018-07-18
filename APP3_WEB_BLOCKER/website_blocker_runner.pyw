from APP3_WEB_BLOCKER.website_blocker import block_websites

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect_target = "127.0.0.1"
websites_black_list = ["www.facebook.com", "facebook.com", "www.gazeta.pl", "gazeta.pl"]

block_websites(hosts_path, redirect_target, websites_black_list)