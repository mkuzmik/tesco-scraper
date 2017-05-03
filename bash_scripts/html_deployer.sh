#!/bin/bash

# Script that update index.html in github.io repo and push it

cd /home/mateusz_kuzmik/Projects/tesco-full/

python html_file_saver.py

cp -f index.html /home/mateusz_kuzmik/Projects/mkuzmik.github.io/index.html

# Commit and push repo

cd /home/mateusz_kuzmik/Projects/mkuzmik.github.io/

git add .

pwd

git commit -m "update"

git push origin master