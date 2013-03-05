from django.db import models

DISTRITOS = (
	('ANCON', 'Ancon'),
	('ATE', 'Ate'),
	('BARRANCO', 'Barranco'),
	('BRENA', 'Brena'),
	('CARABAYLLO', 'Carabayllo'),
	('CHACLACAYO', 'Chaclacayo'),
	('CHORRILLOS', 'Chorrillos'),
	('CIENEGUILLA', 'Cieneguilla'),
	('COMAS', 'Comas'),
	('SANTA ROSA', 'Santa Rosa'),
	('EL AGUSTINO', 'El Agustino'),
	('INDEPENDENCIA', 'Independencia'),
	('JESUS MARIA', 'Jesus Maria'),
	('LA MOLINA', 'La Molina'),
	('LA VICTORIA', 'La Victoria'),
	('LIMA', 'Lima'),
	('LINCE', 'Lince'),
	('LOS OLIVOS', 'Los Olivos'),
	('LURIGANCHO-CHOSICA', 'Lurigancho-Chosica'),
	('LURIN', 'Lurin'),
	('MAGDALENA DEL MAR', 'Magdalena del Mar'),
	('MIRAFLORES', 'Miraflores'),
	('PACHACAMAC', 'Pachacamac'),
	('PUCUSANA', 'Pucusana'),
	('PUEBLO LIBRE', 'Pueblo Libre'),
	('PUNTA HERMOSA', 'Punta Hermosa'),
	('PUNTA NEGRA', 'Punta Negra'),
	('RIMAC', 'Rimac'),
	('SAN BARTOLO', 'San Bartolo'),
	('SAN BORJA', 'San Borja'),
	('SAN ISIDRO', 'San Isidro'),
	('SAN JUAN DE LURIGANCHO', 'San Juan de Lurigancho'),
	('SAN JUAN DE MIRAFLORES', 'San Juan de Miraflores'),
	('SAN LUIS', 'San Luis'),
	('SAN MARTIN DE PORRES', 'San Martin de Porres'),
	('SAN MIGUEL', 'San Miguel'),
	('SANTA ANITA', 'Santa Anita'),
	('SANTA MARIA DEL MAR', 'Santa Maria del Mar'),
	('SANTIAGO DE SURCO', 'Santiago de Surco'),
	('SURQUILLO', 'Surquillo'),
	('VILLA EL SALVADOR', 'Villa el Salvador'),
	('VILLA MARIA DEL TRIUNFO', 'Villa Maria del Triunfo'),
)

class Director(models.Model):
	nombre = models.CharField(max_length = 20)
	apellido = models.CharField(max_length = 20)

	def __unicode__(self):
		return u"%s %s" % (self.nombre, self.apellido)
	class Meta:
		ordering = ['apellido']

class Actor(models.Model):
	nombre = models.CharField(max_length = 20)
	apellido = models.CharField(max_length = 20)

	def __unicode__(self):
		return u"%s %s" % (self.nombre, self.apellido)
	class Meta:
		ordering = ['apellido']

class Cine(models.Model):
	# Cines
	nombre = models.CharField(max_length = 50)
	distrito = models.CharField(max_length = 20,
								choices = DISTRITOS)
	direccion = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ['nombre']

class Pelicula(models.Model):
	titulo = models.CharField(max_length = 100)
	genero = models.CharField(max_length = 20)
	duracion = models.IntegerField()
	pais = models.CharField(max_length = 20)
	director = models.ForeignKey(Director)
	actores = models.ManyToManyField(Actor)
	censura = models.CharField(max_length = 30)
	sinopsis = models.TextField()
	sitio_web = models.URLField(blank = True)

	def __unicode__(self):
		return u"%s" % (self.titulo)
	class Meta:
		ordering = ['titulo']

class Sala(models.Model):
	NORMAL = 'N'
	TRESD = '3D'
	TIPO_DE_SALA_CHOICES = (
		(NORMAL, 'Normal'),
		(TRESD, '3D'),
	)
	numero = models.IntegerField(unique = True)
	capacidad = models.IntegerField()
	tipo_de_sala = models.CharField(max_length = 2,
									choices = TIPO_DE_SALA_CHOICES,
									default = NORMAL)
	def __unicode__(self):
		return u"Sala %s" % (self.numero)
	class Meta:
		ordering = ['numero']

class Funcion(models.Model):
	NORMAL = 'N'
	TRESD = '3D'
	TIPO_DE_FORMATO_CHOICES = (
		(NORMAL, 'Normal'),
		(TRESD, '3D'),
	)
	DOBLADA = 'DOB'
	SUBTITULADA = 'SUB'
	SUBTITULOS_CHOICES = (
		(DOBLADA, 'Doblada'),
		(SUBTITULADA, 'Subtitulada'),
	)
	pelicula = models.ForeignKey(Pelicula)
	sala = models.ForeignKey(Sala)
	hora_inicio = models.TimeField()
	tipo_de_formato = models.CharField(max_length = 2,
									choices = TIPO_DE_FORMATO_CHOICES,
									default = NORMAL)
	dob_sub = models.CharField(max_length = 3,
									choices = SUBTITULOS_CHOICES,
									default = DOBLADA)
	def __unicode__(self):
		return u"%s" % (self.pelicula)
	class Meta:
		ordering = ['pelicula']