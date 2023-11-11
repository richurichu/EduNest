from django.urls import path
from .views import *

urlpatterns = [
    
    path('get-quiz/<int:testseries_id>/', TestseriesDetailAPI.as_view(), name='testseries'),
    path('get-marks/', CalculateMarksAPIView.as_view(), name='testseries-marks'),
]