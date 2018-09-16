# MapMyIndia-API
Python version of MapMyIndia API to store result in CSV format
Note: Please Don't forget to add your API key in URL

## Getting Started

This small python script uses the API MapMyIndia.com to retrieve details for the given Latitude & Longitude and store it in CSV format

## What is Retrieved

```
houseNumber
houseName
poi
poi_dist
street
street_dist
subSubLocality
subLocality
locality
village
district
subDistrict
city
state
pincode
lat
lng
area
formatted_address
```

## Install

```
git clone https://github.com/aravazhimdr/MapMyIndia-API.git
python mapmyindia.py -h

usage: mapmyindia.py [-h] -lat LATITUDE -lng LONGITUDE [-f FILE]

Python version of MapMyIndia API to store result in CSV format

optional arguments:
  -h, --help            show this help message and exit
  -lat LATITUDE, --latitude LATITUDE
                        Pass the Latitude value.Ex: 28.6129602407977
  -lng LONGITUDE, --longitude LONGITUDE
                        Pass the Longitude value.Ex: 77.2294557094574
  -f FILE, --file FILE  The file name to store result Default: result.csv

```

## Screenshots

![alt text](https://s33.postimg.cc/4q9hx7auz/Screenshot_from_2018-09-16_19-48-15_copy_----.png | width=640)

![](https://s33.postimg.cc/40qpkuxgr/Screenshot_from_2018-09-16_20-39-53-----.png =640x480)

