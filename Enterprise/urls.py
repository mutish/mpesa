from django.contrib import admin
from django.urls import path, include
from shoe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', views.new),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('',include('shoe.urls')),
    path('', views.show)
]
