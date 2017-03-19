#!/bin/bash

cd /home/mateusz_kuzmik/Projects/tesco-full

# update database
python tesco_to_db_downloader.py

# make backup
cp my_app.db backups/`date +%d_%m_%Y`.db