from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.conf import settings
from .forms import *
from .mapa import *
import sys
import math

sys.setrecursionlimit(500000)

g, inverted_dict_total, dic_total = initializeGraph()

nombres_linea2 = ["Heroiv Dnipra", "Minska", "Obolon", "Petrivka", "Tarasa Shevchenka",
                      "Kontraktova ploshcha", "Poshtova ploshcha", "Maidan Nezalezhnosti",
                      "Ploshcha Lva Tolstoho", "Olimpiiska", "Palats Ukraina", "Lybidska", "Demiivska",
                      "Holosiivska", "Vasylkivska", "Vystavkovyi tsentr", "Ipodrom", "Teremky"]
nombres_linea1 = ["Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
                      "Shuliavska", "Politekhnichnyi instytut", "Vokzalna", "Universytet", "Teatralna",
                      "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", "Livoberezhna", "Darnytsia",
                      "Chernihivska", "Lisova"]
nombres_linea3 = ["Syrets", "Dorohozhychi", "Lukianivska", "Zoloti vorota", "Palats sportu",
                      "Klovska", "Pecherska", "Druzhby narodiv", "Vydubychi", "Slavutych", "Osokorky",
                      "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervonyi khutir"]


"""
time1 = time.time()
ejecucion_a_star(g, inverted_dict_total["Heroiv Dnipra"], inverted_dict_total["Druzhby narodiv"], dic_total)
time2 = time.time()
print(f'{round(time2 - time1, 2)} segundos ha tardado la búsqueda')
"""

# Create your views here.

def homepage(request):
	context = {}
	#print(dic_total)
	#ejecucion_a_star(g, inverted_dict_total["Heroiv Dnipra"], inverted_dict_total["Druzhby narodiv"], dic_total)
	if request.method == 'POST':
		form = GetPath(request.POST)
		
		if form.is_valid():
			origin = form.cleaned_data.get('origin')
			to = form.cleaned_data.get('to')
			
			camino, coste = ejecucion_a_star(g, inverted_dict_total[origin], inverted_dict_total[to], dic_total)        
			time.sleep(3)
			
			str_path = ''
			for stop in camino:
				str_path += '-' + stop
			
			return redirect('path/' + str_path[1:] + '/' + str(coste))
	
	names = sorted(nombres_linea1 + nombres_linea2 + nombres_linea3)
	context['names'] = names
	template = loader.get_template('main/homepage.html')
	return HttpResponse(template.render(context, request))

def showPath(request, strPath: str, cost: str):

	list_path = strPath.split('-')
	colors = {}
	for stop in list_path:
		if stop in nombres_linea1:
			colors[stop] = 'red'
		elif stop in nombres_linea2:
			colors[stop] = 'blue'
		else:
			colors[stop] = 'green'		

	average_speed_of_subway = 600
	time_ = int(cost / average_speed_of_subway)
	if (time_ >= 60):
		time_ = str(math.floor(time_/60)) + 'h ' + str(time_%60) + 'min'
	else:
		time_ = str(time_) + 'min'	


	context = {'distance': cost, 'time': time_, 'colors': colors}
	template = loader.get_template('main/path.html')
	return HttpResponse(template.render(context, request))
	


	