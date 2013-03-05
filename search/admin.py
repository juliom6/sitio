from django.contrib import admin
from search.models import Director, Actor, Cine
from search.models import Pelicula, Sala, Funcion
#from search.models import Item, Cliente, Pedido
#from search.models import ItemPedido, Distribuidor

#admin.site.register(Item)
#admin.site.register(Cliente)
#admin.site.register(Pedido)
#admin.site.register(ItemPedido)
#admin.site.register(Distribuidor)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Cine)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Funcion)