# GSD
Scrape phone number complaint data from 800notes.com and provide the parsed data via a RESTful API
Originally ported from https://github.com/fgao22/GSD, with changes for python 3.5.

Requirement: python 3.x, pip

Install Dependencies:

$ pip install -r requirements.txt

Run server:

$ python app.py

API queries:

$ curl http://127.0.0.1:5000/api/v1.0/entries/all
$ curl http://127.0.0.1:5000/api/v1.0/entries?area=[an_existing_area_code]

(please substitute [an_existing_area_code] with an area code)


I've tested this out using Python 3.5.
