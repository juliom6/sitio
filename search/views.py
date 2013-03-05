from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render_to_response
from  search.models import Funcion, Pelicula

class Buscador(TemplateView):
	template_name = "cartelera.html"
	#def resultados():
	#	template_name = "cartelera.html"

def resultados(request):
	error = False
	cine = request.GET['cine']
	pelicula = request.GET['pelicula']
	distrito = request.GET['distrito']
	horario = request.GET['horario']
	p = Pelicula.objects.get(titulo = pelicula)
	q = p.funcion_set.filter()
	if q:
		return render_to_response('resultados.html', {'funciones': q})
	else:
		error = True
		return render_to_response('cartelera.html', {'error': error})