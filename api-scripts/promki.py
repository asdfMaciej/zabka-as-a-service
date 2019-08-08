import requests
import json
import sys
import csv

url = "https://api.synerise.com/v4/auth/login/client"
api = "<provide an api key>"
uuid = "<provide an uuid - randomly generate one, it'll work>"

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Api-Version": "4.4"
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

		url_get = "https://api.synerise.com/v4/promotions/promotion/get-for-client?status=ASSIGNED&page="
		headers["Authorization"] = "Bearer "+token

		pages = [1]
		for currentPage in pages:
			r = requests.get(url_get+str(currentPage), headers=headers)
			promki = r.json()['data']

			if len(promki) == 100:
				pages.append(currentPage+1)

			towar = []
			print("[*] "+email+", page: "+str(currentPage))

			for promka in promki:
				if promka['params']:
					if "countdown" in promka['params']:
						towar.append(promka)

			for hotdog in towar:
				#hajs = str(int(float(hotdog['discountValue'])*100))
				hajs = str(hotdog['price'])

				img_big = ""
				img_thumbnail = ""

				for img in hotdog['images']:
					if img['type'] == 'image':
						img_big = img['url']

					if img['type'] == 'thumbnail':
						img_thumbnail = img['url']

				if img_big and not img_thumbnail:
					img_thumbnail = img_big

				if img_thumbnail and not img_big:
					img_big = img_thumbnail


				dzieciateczko_z_nazaretu = [
					email, barcode, hotdog['params']['countdown'],
					hotdog['name'], hajs, 
					hotdog['description'].replace('\n', ' '),
					img_big, img_thumbnail
				]

				hotdogi_boze.append(dzieciateczko_z_nazaretu)

		print("\n")

with open('promocje.csv', 'w', encoding="utf-8", newline='') as result:
	writer = csv.writer(result, delimiter=",")
	writer.writerows(hotdogi_boze)
	