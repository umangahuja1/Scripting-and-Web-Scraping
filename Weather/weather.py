import requests
from pprint import pprint

def location():
	res=requests.get('http://ipinfo.io/')
	data=res.json() 
	loc=[];
	loc=data['loc'].split(',')
	lat=loc[0]
	lon=loc[1]
	return lat,lon,data['city']

def location_coordinates():
	lat,lon,city=location()
	print("Latitude: {}\nLongitude: {}\nCity: {}".format(lat,lon,city))

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=ac7c75b9937a495021393024d0a90c44&units=metric');	
	return res.json();

def print_temp(result,city):
	print("{}'s temperature : {}°C ".format(city,result['main']['temp']))
	print("Wind speed:{} m/s".format(result['wind']['speed']))
	print("Weather:{}".format(result['weather'][0]['main']))
	print("Description:{}".format(result['weather'][0]['description']))


def current_temperature():
	lat,lon,city=location();
	query='lat='+lat+'&lon='+lon;
	data=weather_data(query);
	print_temp(data,city);

def temp_by_city():
	city=input('Enter the city:')
	print()
	query='q='+city;
	data=weather_data(query);
	print_temp(data,city)
	
def menu():
	print()
	print('1. Location coordinates')
	print('2. Current Temperature')
	print('3. Temperature by city')
	choice=input('\nEnter your choice:')
	while (choice not in ['1','2','3']):
		print('Wrong choice')
		choice=input('\nEnter your choice:')
	print()

	return choice;

def call(ch):
	if ch=='1':
		location_coordinates()
	if ch=='2':
		current_temperature()
	if ch=='3':
		temp_by_city()

def main():
	choice=menu()
	call(choice)
	print()

if __name__=='__main__':
	main()
