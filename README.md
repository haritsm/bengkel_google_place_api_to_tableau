# google-place-python

1. Import libraries needed

		import json
		import requests
		import time
		import datetime
		import os, sys, inspect
		import csv
		from urllib.request import urlopen
		from requests.adapters import HTTPAdapter
		from urllib3.util.retry import Retry
		from urllib3.exceptions import MaxRetryError
		import logging

2. Create functions for write to Excel and call google place API
		
		def write_to_excel_and_upload (extracted_data, file_name):
			now = datetime.datetime.now()
			destination_path = "extracted_data/"+now.strftime("%Y_%m_%d")
			if not os.path.exists(destination_path):
				os.makedirs(destination_path)

			with open(destination_path+"/"+file_name, 'w') as f:
				wr = csv.writer(f, delimiter=',', dialect='excel')
				wr.writerows(extracted_data)

		def call_google_place(query):
			site = 'https://maps.googleapis.com/maps/api/'
			service = 'place/textsearch/json?'
			inputs = 'query='+ query + '&location=-5.9036076,106.5296896&radius=100000'
			api_key = '&key=AIzaSyCOuXK2TAe7zqmaLCo5PRsfWNP5601aNFk'
			url = site + service + inputs + api_key
			return url

3. List of the queries
	  
		  list_query = [
			"audi",
			"bmw",
			"chevrolet",
			"classic",
			"daihatsu",
			"datsun",
			"ferrari",
			"ford",
			"honda",
			"hyundai",
			"kia",
			"isuzu",
			"lamborghini",
			"mercedes",
			"morris",
			"maxindo",
			"mistubishi",
			"nissan",
			"peugeot",
			"porsche",
			"proton",
			"renault",
			"toyota",
			"volvo",
			"volkswagen",
			"wuling",
			"mazda",
			"bengkel",
			"mobil",
			"car",
			"repair",
			"jeep",
			"hummer",
			"opel",
			"suspensi",
			"shockbreaker",
			"indomobil",
			"kampakan",
			"servis",
			"service"
		]

4. Execute
	
		if __name__ == '__main__':

			file_name 	= "all_list_query_3"
			file_name 	= file_name+".csv"
			header 	= ["name","lat","long","region","formatted_address","types"]
			result 	= list()
			result.append(header)
			counter = 0

			for item in list_query:
				url = call_google_place(item)
				time.sleep(30)
				response = requests.get(url=url).json()
				# response = request_data_from_url(url)
				print(counter)
				for obj in response['results']:
					name = obj['name']
					lat = obj['geometry']['location']['lat']
					lng = obj['geometry']['location']['lng']
					addr = obj['formatted_address']
					types = obj['types']
					# place_id = obj['place_id']
					temp = [name, lat, lng, addr, types]
					result.append(temp)
					print(temp)
			while 'next_page_token' in response:
				URL = url + '&pagetoken=' + response['next_page_token']
				time.sleep(30)
				response = requests.get(url=URL).json()
				# response = request_data_from_url(URL)
				for obj in response['results']:
					name = obj['name']
					lat = obj['geometry']['location']['lat']
					lng = obj['geometry']['location']['lng']
					addr = obj['formatted_address']
					types = obj['types']
					# place_id = obj['place_id']
					temp = [name, lat, lng, addr, types]
					result.append(temp)
					print(temp)
			counter += 1

		write_to_excel_and_upload(result, file_name)
