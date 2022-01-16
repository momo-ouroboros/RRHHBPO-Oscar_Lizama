from django.db import models

# Create your models here.
class Areas(models.Model):
	Areaid = models.IntegerField(verbose_name="Cod.Area")
	Areanombre=models.CharField(max_length=50,verbose_name="Area")
	class Meta:
		verbose_name='Area'
		verbose_name_plural='Areas'

	def __str__(self):
		return self.Areanombre

class SubAr(models.Model):
	SubArid = models.IntegerField(verbose_name="Cod.Sub-Area")
	SubArnom = models.CharField(max_length=50,verbose_name="Sub-Area")
	Areaid = models.ForeignKey(Areas, on_delete=models.RESTRICT,verbose_name="Area")
	class Meta:
		verbose_name='Sub-Area'
		verbose_name_plural='Sub-Areas'

	def __str__(self):
		return self.SubArnom

class TipoDoce(models.Model):
	TipoDoceid = models.IntegerField(verbose_name="Cod.Tipo de Documento")
	TipoDocenom = models.CharField(max_length=50,verbose_name="Tipo de Documento")

	class Meta:
		verbose_name='Tipo de Documento'
		verbose_name_plural='Tipos de Documentos'
	
	def __str__(self):
		return self.TipoDocenom

class Empleados(models.Model):
	Empleadoid = models.IntegerField(verbose_name="Cod.Empleado")
	Empleadonom = models.CharField(max_length=50,verbose_name="Nombre")
	Empleadoape = models.CharField(max_length=50,verbose_name="Apellido")
	Areaid = models.ForeignKey(Areas, on_delete=models.RESTRICT,verbose_name="Area")
	SubArid = models.ForeignKey(SubAr, on_delete=models.RESTRICT,verbose_name="Sub-Area")
	TipoDoceid = models.ForeignKey(TipoDoce, on_delete=models.RESTRICT,verbose_name="Tipo de Documento")
	Empleadodoc = models.CharField(max_length =50,verbose_name="N°Documento")

	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'

	def __str__(self):
		return self.Empleadonom

