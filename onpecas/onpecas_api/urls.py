#from django.urls import include, path
#from rest_framework import routers
#from . import views

#router = routers.DefaultRouter()
#router.register(r'heroes', vies.PartsViewSet)

#urlpatterns = [
#	path('', include(router.urls)),
#	path('api-auth/', include('rest_framework.urls', 
#namespace='rest_framrwork'))
#]

from rest_framework import routers
#from .views import PartsViewSet
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'parts', views.PartsViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', 
namespace='rest_framrwork'))
]
