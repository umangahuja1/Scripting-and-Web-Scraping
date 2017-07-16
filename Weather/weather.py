import requests

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

def print_temp(result):
	print("{}'s temperature : {}°C ".format(result['name'],result['main']['temp']))

def current_temperature():
	lat,lon,city=location();
	query='lat='+lat+'&lon='+lon;
	data=weather_data(query);
	print_temp(data);

def temp_by_city():
	city=input('Enter the city:')
	print()
	query='q='+city;
	data=weather_data(query);
	print_temp(data)
	
def menu():
	print()
	print('1. Location coordinates')
	print('2. Current Temperature')
	print('3. Temperature by city')
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
