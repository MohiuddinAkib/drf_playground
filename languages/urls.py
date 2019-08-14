from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'languages', views.LanguageViewSet)
router.register(r'paradigms', views.ParadigmViewSet)
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
