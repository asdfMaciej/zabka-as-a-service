import requests
import json
import sys
import csv

url = "https://api.synerise.com/v4/auth/login/client"
api = "<provide an api key>"
uuid = "<provide an uuid>"

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Api-Version": "4.3"
}

hotdogi_boze = [
	["email", "barcode", "timeout", "name", "price", "description", "image", "thumbnail"]
]

with open("tokens", "r") as tf:
	for line in tf.readlines():
		data = line.split('<<<<>>>>')
		barcode = data[2].strip()
		email = data[1].strip()
		token = data[0].strip()

		url_get = "https://api.synerise.com/v4/promotions/promotion/get-for-client"
		headers["Authorization"] = "Bearer "+token

		r = requests.get(url_get, headers=headers)
		promki = r.json()['data']

		towar = []
		print("[*] "+email)
		with open("test/"+email, "w", encoding="utf-8") as ffff:
			ffff.write(str(promki))

		for promka in promki:
			if promka['params']:
				if "countdown" in promka['params']:
					towar.append(promka)

		for hotdog in towar:
			hajs = str(int(float(hotdog['discountValue'])*100))
			dzieciateczko_z_nazaretu = [
				email, barcode, hotdog['params']['countdown'],
				hotdog['name'], hajs, 
				hotdog['description'].replace('\n', ' '),
				hotdog['images'][0]['url'],
				hotdog['images'][1]['url']
			]

			hotdogi_boze.append(dzieciateczko_z_nazaretu)

		print("\n")

with open('promocje.csv', 'w', encoding="utf-8", newline='') as result:
	writer = csv.writer(result, delimiter=",")
	writer.writerows(hotdogi_boze)
	