from django.shortcuts import render,HttpResponse,redirect
from django.db.models import ProtectedError,RestrictedError
from django.http import JsonResponse
import json
from django.http import HttpResponse

from RRHH.models import Areas,SubAr,TipoDoce,Empleados
from RRHH.forms import Areas_Form,SubAr_Form,Documentos_Form,Empleados_Form

# Create your views here.

def login(request):
	return render(request,"RRHH/Login.html")

def Inicio(request):
	return render(request,"RRHH/home.html")

def Area(request):
	Areasl = Areas.objects.all()
	return render(request,"RRHH/Areas.html",{"Areas":Areasl})

def Sub_Area(request):
	Subarsl = SubAr.objects.all()
	return render(request,"RRHH/Sub_Areas.html",{"Subars":Subarsl})

def TipoDoc(request):
	TipoDocesl = TipoDoce.objects.all()
	return render(request,"RRHH/TipoDoce.html",{"TipoDoces":TipoDocesl})

def Empleado(request):
	Empleadosl = Empleados.objects.all()
	return render(request,"RRHH/Empleados.html",{"Empleados":Empleadosl})

def Areas_c(request):
	Area=Areas.objects.latest('id')
	initial_dict = {
    	"Areaid" :int(Area.id)+1 ,
    }
	form =Areas_Form()	
	form =Areas_Form(request.POST or None,initial = initial_dict)
	if request.method =='POST':
		if form.is_valid():
			form.save()
			return redirect('/Area')

	context = {'form':form}
	return render(request,"RRHH/Areas_cu.html",context)

def Areas_u(request,pk):
	Area = Areas.objects.get(id=pk)
	form =Areas_Form(instance=Area)
	if request.method =='POST':
		form =Areas_Form(request.POST,instance=Area)
		if form.is_valid():
			form.save()
			return redirect('/Area')

	context = {'form':form}
	return render(request,"RRHH/Areas_cu.html",context)

def Areas_d(request,pk):
	Area = Areas.objects.get(id=pk)
	if request.method=="POST":
		try:
			Area.delete()
			return redirect('/Area')
		except RestrictedError:
			context={'Areade':Area}
			return render(request,"RRHH/Deletes.html",context)

	context={'Aread':Area}
	return render(request,"RRHH/Deletes.html",context)

def Sareas_c(request):
	SubAr1=SubAr.objects.latest('id')
	initial_dict = {
    	"SubArid" :int(SubAr1.id)+1 ,
    }
	form =SubAr_Form()	
	form =SubAr_Form(request.POST or None,initial = initial_dict)
	if request.method =='POST':
		if form.is_valid():
			form.save()
			return redirect('/Sub_Area')

	context = {'form':form}
	return render(request,"RRHH/Sub_Areas_cu.html",context)

def Sareas_u(request,pk):
	Sar = SubAr.objects.get(id=pk)
	form =SubAr_Form(instance=Sar)
	if request.method =='POST':
		form =SubAr_Form(request.POST,instance=Sar)
		if form.is_valid():
			form.save()
			return redirect('/Sub_Area')

	context = {'form':form}
	return render(request,"RRHH/Sub_Areas_cu.html",context)

def Sareas_d(request,pk):
	Sar = SubAr.objects.get(id=pk)
	if request.method=="POST":
		try:
			Sar.delete()
			return redirect('/Sub_Area')
		except RestrictedError:
			context={'SubAre':Sar,}
			return render(request,"RRHH/Deletes.html",context) 


	context={'SubAr':Sar,}
	return render(request,"RRHH/Deletes.html",context)  

def Documentos_c(request):
	Doc=TipoDoce.objects.latest('id')
	initial_dict = {
    	"TipoDoceid" :int(Doc.id)+1 ,
    }
	form =Documentos_Form()	
	form =Documentos_Form(request.POST or None,initial = initial_dict)
	if request.method =='POST':
		if form.is_valid():
			form.save()
			return redirect('/TipoDoc')

	context = {'form':form}
	return render(request,"RRHH/Tipodoce_cu.html",context)

def Documentos_u(request,pk):
	Doc = TipoDoce.objects.get(id=pk)
	form =Documentos_Form(instance=Doc)
	if request.method =='POST':
		form =Documentos_Form(request.POST,instance=Doc)
		if form.is_valid():
			form.save()
			return redirect('/TipoDoc')

	context = {'form':form}
	return render(request,"RRHH/Tipodoce_cu.html",context)

def Documentos_d(request,pk):
	Doc = TipoDoce.objects.get(id=pk)
	if request.method=="POST":
		try:
			Doc.delete()
			return redirect('/TipoDoc')
		except RestrictedError:
			context={'Doce':Doc,}
			return render(request,"RRHH/Deletes.html",context) 


	context={'Doc':Doc,}
	return render(request,"RRHH/Deletes.html",context)

def Empleados_c(request):
	Empleado=Empleados.objects.latest('id')
	initial_dict = {
    	"Empleadoid" :int(Empleado.id)+1 ,
    }
	form =Empleados_Form()	
	form =Empleados_Form(request.POST or None,initial = initial_dict)
	if request.method =='POST':
		if form.is_valid():
			form.save()
			return redirect('/Empleado')

	context = {'form':form}
	return render(request,"RRHH/Empleados_cu.html",context) 

def Empleados_u(request,pk):
	Empleado = Empleados.objects.get(id=pk)
	form =Empleados_Form(instance=Empleado)
	if request.method =='POST':
		form =Empleados_Form(request.POST,instance=Empleado)
	if form.is_valid():
		form.save()
		return redirect('/Empleado')

	context = {'form':form}
	return render(request,"RRHH/Empleados_cu.html",context) 

def Empleados_d(request,pk):
	Empleado = Empleados.objects.get(id=pk)
	if request.method=="POST":
		try:
			Empleado.delete()
			return redirect('/Empleado')
		except RestrictedError:
			context={'Empleadoe':Empleado,}
			return render(request,"RRHH/Deletes.html",context)

	context={'Empleado':Empleado,}
	return render(request,"RRHH/Deletes.html",context)