from django.urls import path
from . import views

urlpatterns = [
		path('', views.homepage, name = "homepage"),
		path('path/<str:strPath>/<int:cost>', views.showPath, name = "path")
]	