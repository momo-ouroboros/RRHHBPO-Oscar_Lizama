from django.forms import ModelForm
from RRHH.models import Areas,SubAr,TipoDoce,Empleados

class Areas_Form(ModelForm):
	class Meta:
		model=Areas
		fields ='__all__'

class SubAr_Form(ModelForm):
	class Meta:
		model=SubAr
		fields ='__all__'

class Documentos_Form(ModelForm):
	class Meta:
		model=TipoDoce
		fields ='__all__'

class Empleados_Form(ModelForm):
	class Meta:
		model=Empleados
		fields ='__all__'

def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)
	self.fields['Areaid'].queryset = SubAr.objects.none()
