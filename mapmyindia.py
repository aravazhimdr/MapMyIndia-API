#!/usr/bin/env python
import os
import sys
import requests
import json
import csv
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#A monkey-patched script :P
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
parser = argparse.ArgumentParser(description='Python version of MapMyIndia API to store result in CSV format')
parser.add_argument('-lat', '--latitude', help='Pass the Latitude value.Ex: 28.6129602407977', required=True)
parser.add_argument('-lng', '--longitude', help='Pass the Longitude value.Ex: 77.2294557094574', required=True)
parser.add_argument('-f', '--file', help='The file name to store result Default: result.csv',default='result.csv', required=False)
args = parser.parse_args()

#Please Put Your REST-API Key in the below URL
url="https://apis.mapmyindia.com/advancedmaps/v1/your_rest_key_here/rev_geocode?&lng=" +args.longitude+ "&lat=" +args.latitude+"&region=ind"

#For Debugging Connection
http_proxy  = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"
ftp_proxy   = "ftp://127.0.0.1:8080"
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

resp = requests.get(url,  verify=False)
response = json.loads(resp.text.encode("ascii"), encoding="ascii")
print "HTTP Code: " + str(response["responseCode"])
x = response["results"][0]
print "Address: " + str(x["formatted_address"])
fp = open(args.file, "a+")
f = csv.writer(fp)

header = ["houseNumber",
    "houseName",
    "poi",
    "poi_dist",
    "street",
    "street_dist",
    "subSubLocality",
    "subLocality",
    "locality",
    "village",
    "district",
    "subDistrict",
    "city",
    "state",
    "pincode",
    "lat",
    "lng",
    "area",
    "formatted_address"
    ]
if os.path.getsize(args.file) == 0:
  print "Appending Header To " + args.file
  f.writerow(header)
print "Writing to " + args.file
f.writerow([x["houseNumber"],
    x["houseName"],
    x["poi"],
    x["poi_dist"],
    x["street"],
    x["street_dist"],
    x["subSubLocality"],
    x["subLocality"],
    x["locality"],
    x["village"],
    x["district"],
    x["subDistrict"],
    x["city"],
    x["state"],
    x["pincode"],
    x["lat"],
    x["lng"],
    x["area"],
    x["formatted_address"]
    ])

