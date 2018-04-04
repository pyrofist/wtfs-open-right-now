import requests
import os

GOOGLE_API = os.environ["GOOGLE_API"]

def process_address(address):
	data = {}
	r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" +
						address + "&key=" + GOOGLE_API)
	if r.status_code == 200:
		json = r.json()
		data["lat"] = str(json["results"][0]["geometry"]["location"]["lat"])
		data["lng"] = str(json["results"][0]["geometry"]["location"]["lng"])
		data["formatted"] = json["results"][0]["formatted_address"]
		find_restaurants(data)
	return data

def process_coords(lat, lng):
	data = {}
	r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
						lat + "," + lng + "&key=" + GOOGLE_API)
	if r.status_code == 200:
		json = r.json()
		data["lat"] = lat
		data["lng"] = lng
		data["formatted"] = json["results"][0]["formatted_address"]
		find_restaurants(data)
	return data

def filter_relevant(item):
	restaurant = {}
	restaurant["name"] = item["name"]
	restaurant["address"] = item["vicinity"]
	restaurant["lat"] = str(item["geometry"]["location"]["lat"])
	restaurant["lng"] = str(item["geometry"]["location"]["lng"])
	return restaurant

def find_restaurants(data):
	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + 
						data["lat"] + "," + data["lng"] + 
						"&rankby=distance&opennow=true&type=restaurant&key=" + GOOGLE_API)
	if r.status_code == 200:
		json = r.json()
		data["restaurants"] = list(map(filter_relevant,json["results"]))
	return
