#from search.models import Usuario, Publicacion
from django.contrib import admin
from search.models import Item, Cliente, Pedido
from search.models import ItemPedido, Distribuidor

admin.site.register(Item)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Distribuidor)
