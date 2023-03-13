from django.contrib import admin
from django.urls import path, include
from shoe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shoe.urls')),
    path('new', views.new),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('delete/<int:id>', views.destroy),
    path('', views.show)
]



