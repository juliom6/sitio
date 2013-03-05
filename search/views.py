from django.views. generic import TemplateView
from django.http import HttpResponse

class Buscador(TemplateView):
	template_name = "cartelera.html"
	#def resultados():
	#	template_name = "cartelera.html"

#def display_meta(request):
#    values = request.META.items()
#    values.sort()
#    html = []
#    for k, v in values:
#        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#
#    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def resultados(request):
	cine = request.GET['cine']
	pelicula = request.GET['pelicula']
	distrito = request.GET['distrito']
	horario = request.GET['horario']
	mensaje = "%r %r %r %r" % (cine, pelicula, distrito, horario)
	return HttpResponse(mensaje)