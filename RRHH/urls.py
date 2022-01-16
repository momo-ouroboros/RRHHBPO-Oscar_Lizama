from django.urls import path,include

from RRHH import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('',views.Inicio,name="Inicio"),
    path('Area',views.Area,name="Area"),
    path('Sub_Area',views.Sub_Area,name="Sub_Area"),
    path('TipoDoc',views.TipoDoc,name="TipoDoc"),
    path('Empleado',views.Empleado,name="Empleado"),
    path('Mantenimiento_Areas>',views.Areas_c,name="Areas_c"),
    path('Mantenimiento_Areas/<str:pk>/',views.Areas_u,name="Areas_u"),
    path('Eliminar_Area/<str:pk>/',views.Areas_d,name="Areas_d"),
    path('Mantenimiento_Sub-Areas',views.Sareas_c,name="Sareas_c"),
    path('Mantenimiento_Sub-Areas/<str:pk>/',views.Sareas_u,name="Sareas_u"),
    path('Eliminar_Sub-Area/<str:pk>/',views.Sareas_d,name="Sareas_d"),
	path('Mantenimiento_Documentos',views.Documentos_c,name="Documentos_c"),
    path('Mantenimiento_Documentos/<str:pk>/',views.Documentos_u,name="Documentos_u"),
    path('Eliminar_Documentos/<str:pk>/',views.Documentos_d,name="Documentos_d"),
    path('Mantenimiento_Empleados',views.Empleados_c,name="Empleados_c"),
    path('Mantenimiento_Empleados/<str:pk>/',views.Empleados_u,name="Empleados_u"),
    path('Eliminar_Empleados/<str:pk>/',views.Empleados_d,name="Empleados_d"),
    ]

