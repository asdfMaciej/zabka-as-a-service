#!/bin/bash
cd /root/
python3 promki.py
python3 html.py
python3 phper.py
mv index.html /www/zabka-static/
mv promotions.php /www/api/
cp promocje.csv /root/backups/`date +%s`
