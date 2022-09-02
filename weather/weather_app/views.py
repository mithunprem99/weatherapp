from django.shortcuts import render,redirect
import json
import urllib.request
from django.contrib import messages

# Create your views here.

def index(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a4016369286dbf7520e1a93d734dbaee').read()
		json_data = json.loads(res)
		data = {
		'Country_code': str(json_data['sys']['country']),
		'temperature': str(json_data['main']['temp']),
		'Pressure': str(json_data['main']['pressure']),
		'Humidity': str(json_data['main']['humidity']),
		}
	

		print(city.upper())
		print(data)
		# return (data)
		# return render(request, 'index.html',data)

	else:
		data={}
	# 	messages.info(request,'no city')
	# 	# return redirect('index')
		city=''
	
	return render(request, 'index.html',{'city':city.upper(), 'data':data})
