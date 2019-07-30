#!/bin/bash
cd /root/
python3 promki.py
python3 html.py
mv index.html /www/zabka/
cp promocje.csv /root/backups/`date +%s`
