from django.urls import path
from .views import IndexView

urlpatterns = [
    # path('endereço/', minhaView.as_view(, nome='noma-da-url'))
    path('', IndexView.as_view(), name='inicio'),
]