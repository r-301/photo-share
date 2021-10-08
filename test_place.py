import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=35.6987769,139.76471&radius=300&language=ja&keyword=公園OR広場OR駅&key=AIzaSyCcbFT5eHDI9O_6qV4yXIjWBvp7rM2s2d0"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)