import requests

url = "https://maps.googleapis.com/maps/api/geocode/json?address=千葉県%2野田市%2山崎&key=AIzaSyCcbFT5eHDI9O_6qV4yXIjWBvp7rM2s2d0,


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)