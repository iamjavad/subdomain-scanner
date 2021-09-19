#!/usr/bin/python3

import requests

domain = input(str("Domain: "))

file = open("subdomain.txt")

content = file.read()

subdomains = content.splitlines()

discovered_subdomains = []

for subdomain in subdomains:
	url = f"http://{subdomain}.{domain}"
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass
	else:
		print("[+] Discoverd subdomain", url)
		discovered_subdomains.append(url)
with open("discovered_subdomains.txt", "w") as f:
	for subdomain in discovered_subdomains:
		print(subdomain, file=f)
