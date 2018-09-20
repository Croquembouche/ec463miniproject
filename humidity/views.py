from django.http import HttpResponse
from django.template import loader
from .models import Humidity, Temperature
from django.shortcuts import render

from .fusioncharts import FusionCharts



def humidity_details(request):
	latest_humidity_recorded = Humidity.objects.order_by('datetime_recorded')[:5]

	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource_humidity = {}
	dataSource_humidity['chart'] = { 
	    "caption": "Humdity",
	        "subCaption": "Harry's Home",
	        "xAxisName": "Time",
	        "yAxisName": "Humdity",
	        "theme": "zune"
	    }

	# The data for the chart should be in an array where each element of the array is a JSON object
	# having the `label` and `value` as key value pair.

	dataSource_humidity['data'] = []
	# Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
	for humidity in latest_humidity_recorded:
	  data = {}
	  data['label'] = str(humidity.datetime_recorded)
	  data['value'] = str(humidity)
	  dataSource_humidity['data'].append(data)

	# Create an object for the Column 2D chart using the FusionCharts class constructor                      
	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource_humidity)

	return render(request, 'humidity/index.html', {'output': column2D.render()}) 

def temperature_details(request):
	latest_temperature_recorded = Temperature.objects.order_by('datetime_recorded')[:5]

    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource_temp = {}
	dataSource_temp['chart'] = { 
	    "caption": "Temperature",
	        "subCaption": "Harry's Home",
	        "xAxisName": "Time",
	        "yAxisName": "Temperature Celsius",
	        "theme": "zune"
	    }

	# The data for the chart should be in an array where each element of the array is a JSON object
	# having the `label` and `value` as key value pair.

	dataSource_temp['data'] = []
	# Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
	for temp in latest_temperature_recorded:
	  data = {}
	  data['label'] = str(temp.datetime_recorded)
	  data['value'] = str(temp)
	  dataSource_temp['data'].append(data)

	# Create an object for the Column 2D chart using the FusionCharts class constructor                      
	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource_temp)

	return render(request, 'temperature/index.html', {'output': column2D.render()}) 

def frontpage(request):
	latest_humidity_recorded = Humidity.objects.order_by('datetime_recorded')[:5]
	latest_temperature_recorded = Temperature.objects.order_by('datetime_recorded')[:5]
	template = loader.get_template('frontpage/index.html')
	context = {
		'latest_humidity_recorded' : latest_humidity_recorded,
		'latest_temperature_recorded' : latest_temperature_recorded,
	}

	return HttpResponse(template.render(context, request))


    