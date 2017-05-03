#!/bin/bash

# It is the script that you can add to anacron and add new products to database every day automatically

cd /home/mateusz_kuzmik/Projects/tesco-full

# update database
python tesco_to_db_downloader.py

# clear old backups
rm -rf backups/
mkdir -p backups

# make new backup
cp my_app.db backups/`date +%d_%m_%Y`.db