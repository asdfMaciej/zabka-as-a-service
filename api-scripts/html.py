import csv

header = """
<html>
<head>
<meta charset="utf-8">
<title>Maciej Kaszkowiak uwielbia żabkę</title>
<style>
	.promka {
	display: flex;
	flex-direction: row;
	flex-wrap: nowrap;
	}
	.promka > div {
	flex: 1 1 auto;
	}
	img {
	width: 60px;
	height: 60px;
	}
</style>
</head>
<body>
"""

footer = """
</body>
</html>
"""

template = """

<div class="promka">
	<img src="{}">
	<div>{}</div>
	<div>{}</div>
	<div>{}</div>
	<div>{}</div>
</div>
"""
main = ""
with open('promocje.csv', newline='', encoding='utf-8') as csvfile:
    promki = list(csv.reader(csvfile))
    del promki[0]

promki = sorted(promki, key=lambda x: x[3])
for p in promki:
	main += template.format(
		p[7], # p7?
		p[2], p[3], p[4], p[0]
	)

with open('index.html','w', encoding='utf-8') as fff:
	fff.write(header)
	fff.write(main)
	fff.write(footer)
