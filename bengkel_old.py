import json
import requests
import time
import datetime
import os, sys, inspect
import csv

def write_to_excel_and_upload (extracted_data, file_name):
	now = datetime.datetime.now()
	destination_path = "extracted_data/"+now.strftime("%Y_%m_%d")
	if not os.path.exists(destination_path):
		os.makedirs(destination_path)

	with open(destination_path+"/"+file_name, 'w') as f:
		wr = csv.writer(f, delimiter=',', dialect='excel')
		wr.writerows(extracted_data)

site = 'https://maps.googleapis.com/maps/api/'
service = 'place/textsearch/json?'
inputs = 'query=repaint&location=-5.9036076,106.5296896&radius=100000'
api_key = '&key=AIzaSyCOuXK2TAe7zqmaLCo5PRsfWNP5601aNFk'
url = site + service + inputs + api_key

# print(response)

if __name__ == '__main__':

	file_name 	= "repaint"
	file_name 	= file_name+".csv"
	header 	= ["name","lat","long","formatted_address","types"]
	result 	= list()
	result.append(header)
	response = requests.get(url=url).json()
	counter = 0
	for obj in response['results']:
		name = obj['name']
		lat = obj['geometry']['location']['lat']
		lng = obj['geometry']['location']['lng']
		addr = obj['formatted_address']
		types = obj['types']
		temp = [name, lat, lng, addr, types]
		result.append(temp)

	while 'next_page_token' in response:
		URL = url + '&pagetoken=' + response['next_page_token']
		time.sleep(5)
		response = requests.get(url=URL).json()
		for obj in response['results']:
			name = obj['name']
			lat = obj['geometry']['location']['lat']
			lng = obj['geometry']['location']['lng']
			addr = obj['formatted_address']
			types = obj['types']
			temp = [name, lat, lng, addr, types]
			result.append(temp)

write_to_excel_and_upload(result, file_name)