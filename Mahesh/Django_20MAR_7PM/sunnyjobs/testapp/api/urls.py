from django.urls import path,include
from rest_framework import routers
from testapp.api.views import HydJobsCRUDCBV
router = routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV)
urlpatterns = [
    path('',include(router.urls))
]
