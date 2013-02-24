from django.db import models

class Distribuidor(models.Model):
	nombre = models.CharField(max_length = 40)
	direccion = models.CharField(max_length = 80, blank = True)
	telefono = models.CharField(max_length = 15)
	persona_contacto = models.CharField(max_length = 60)
	email = models.EmailField()

	def __unicode__(self):
		return self.nombre

class Item(models.Model):
	titulo = models.CharField(max_length=50)
	#tipo_item = {cd, dvd, disco laser}
	distribuidor = models.ForeignKey(Distribuidor)
	precio = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0)
	fecha_lanzamiento = models.DateField()
	#genero = {accion, suspenso, terror}
	cantidad_en_stock = models.IntegerField()

	def __unicode__(self):
		return self.titulo

class Cliente(models.Model):
	nombre = models.CharField(max_length = 40)
	apellido = models.CharField(max_length = 40)
	direccion = models.CharField(max_length = 80, blank = True)
	distrito = models.CharField(max_length = 25)
	provincia = models.CharField(max_length = 20)
	telefono = models.CharField(max_length = 15)	
	email = models.EmailField()

	def __unicode__(self):
		return self.email

class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha_pedido = models.DateField()
	numero_tarjeta_credito = models.CharField(max_length = 19)
	fecha_exp_tarj_credito = models.CharField(max_length = 5)
	#pedido_completo = models.BooleanField()
	#recojo_o_envio = 
	
	def __unicode__(self):
		return self.cliente

class ItemPedido(models.Model):
	pedido = models.ForeignKey(Pedido)
	item = models.ForeignKey(Item)
	cantidad = models.IntegerField()
	#descuento = models.Decimal()
	precio_venta = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0)
	enviado = models.BooleanField()
	fecha_envio = models.DateField()
	
	def __unicode__(self):
		return self.pedido


