# FINANCIAL CONTROL APP 
check every incomes and spends to get personal financial report

base on cli

## Requirements
1. Python version 3.11.0
1. Docker and Docker Compose
1. ubuntu linux or another distro linux or mac os

## Database
1. run docker compose for postgres database `sudo dokcer compose up`

## how to install
1. clone from github `git clone https://github.com/rizkydarmadi/Financial-Control-App.git`
1. create virtual env `python -m venv env`
1. run with virtualenv `source env/bin/activate`
1. install third party library `pip install -r requirements.txt`
1. copy then rename `config copy.json` to `config.json`
1. copy then rename `alembic copy.ini` to `alembic.ini`
1. migrations database `alembic upgrade head`
1. run app `python main.py` 🚀🚀🚀
