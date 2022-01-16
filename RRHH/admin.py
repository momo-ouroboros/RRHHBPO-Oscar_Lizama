from django.contrib import admin
from RRHH.models import Areas,SubAr,TipoDoce,Empleados

# Register your models here.

class AreasAdmin(admin.ModelAdmin):
	list_display=("Areaid","Areanombre")
	search_fields=("Areanombre",)

class SubArAdmin(admin.ModelAdmin):
	list_display=("Areaid","SubArid","SubArnom",)
	list_filter=("Areaid",)
	search_fields=("SubArnom",)

class TipodoceAdmin(admin.ModelAdmin):
	list_display=("TipoDoceid","TipoDocenom",)
	search_fields=("TipoDocenom",)

class EmpleadosAdmin(admin.ModelAdmin):
	list_display=("Empleadonom","Empleadoape",
		"Areaid","SubArid",
		)



admin.site.site_header ="Administración de RRHH"
admin.site.index_title= "Administración de RRHH"
admin.site.site_title ="Administración de RRHH"
admin.site.register(Areas,AreasAdmin)
admin.site.register(SubAr,SubArAdmin)
admin.site.register(TipoDoce,TipodoceAdmin)
admin.site.register(Empleados,EmpleadosAdmin)