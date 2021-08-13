#!/bin/bash
sudo apt-get update -qy
sudo apt-get install -y python3-dev python3-pip
pip install -r requirements.txt
python3 manage.py test
