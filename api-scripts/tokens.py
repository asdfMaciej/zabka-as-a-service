import requests
import json
import sys
import csv

url = "https://api.synerise.com/v4/auth/login/client"
api = "<provide an api key>"
uuid = "<provide an uuid - randomly generate one, it'll work>"

emails = [
"email1@list.com",
"email2@list.com"
# and so on...
]

password = "<accounts password>"

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Api-Version": "4.3"
}

with open("tokens", "w") as tokenfile:
	for email in emails:
		body = {
			"apiKey": api,
			"email": email,
			"password": password,
			"uuid": uuid
		}
		r = requests.post(url, json=body, headers=headers)
		print(email)
		token = r.json()['token']

		headers["Authorization"] = "Bearer "+token
		r = requests.get("https://api.synerise.com/v4/my-account/personal-information", headers=headers)
		custom = r.json()['customId']
		print(custom)
		line = token+"<<<<>>>>"+email+"<<<<>>>>"+custom
		print(line, file=tokenfile)

sys.exit()