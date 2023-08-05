from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('myforms/', my_form_view, name='myforms'),
    path('list/',manufacturer_list, name='manufacturer_list'),
    path('manufacturer/<int:pk>/pdf/', GeneratePDF.as_view(), name="manufacturer_pdf"),
    path('delete/<int:pk>', delete_manufacturer, name="delete"),
    path('manufacturer/<int:pk>/', manufacturer_detail, name='manufacturer_detail'),
    path('feedback/',feedback,name="feedback"),
    path('submitted/', success_page, name="success_page"),

    path('edit_manufacturer/<int:pk>/', manufacturer_edit,name="edit" )]
# =======
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from .views import *

# urlpatterns = [
#     path('', index, name='home'),
#     path('myforms/', my_form_view, name='myforms'),
#     path('list/',manufacturer_list, name='manufacturer_list'),
#     path('submitted_report/', submitted_reports, name="submitted_report"),
#     path('manufacturer/<int:pk>/pdf/', GeneratePDF.as_view(), name="manufacturer_pdf"),
#     path('delete/<int:pk>', delete_manufacturer, name="delete"),
#     path('order_detail/<int:pk>/', report_detail, name="report_detail"),
#     path('manufacturer/<int:pk>/', manufacturer_detail, name='manufacturer_detail'),
#     path('edit_manufacturer/<int:pk>/', manufacturer_edit,name="edit" )
