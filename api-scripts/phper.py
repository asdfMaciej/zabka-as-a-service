import csv
from datetime import datetime

header = """
<?php
$promotions = [];
"""

header += '$datetime = "'+str(datetime.now())+'";\n';

template = """
$p = [];
$p["barcode"] = "{}";
$p["timeout"] = "{}";
$p["name"] = "{}";
$p["price"] = "{}";
$p["thumbnail"] = "{}";
$p["image"] = "{}";
$p["email"] = "{}";
$promotions[] = $p;
"""
main = ""
footer = "?>";
with open('promocje.csv', newline='', encoding='utf-8') as csvfile:
    promki = list(csv.reader(csvfile))
    del promki[0]

promki = sorted(promki, key=lambda x: x[3])
for p in promki:
	main += template.format(
		p[1], p[2], p[3],p[4], p[7], p[6], p[0]
	)

with open('promotions.php','w', encoding='utf-8') as fff:
	fff.write(header)
	fff.write(main)
	fff.write(footer)
