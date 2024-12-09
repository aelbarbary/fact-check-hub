
from django.urls import path
from factcheck.views import FactCheckAPI
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
     path('v1/fact-check', FactCheckAPI.as_view(),name="fact-check"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
