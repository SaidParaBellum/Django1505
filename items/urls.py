from django.urls import path

from items.views import get_item
from items.views import get_all
from items.views import delete_first

urlpatterns = [
    path('get/<int:pk>', get_item, name='get_item'),
    path('get/<int:pk>', get_all, name='get_all'),
    path('get/<int:pk>', delete_first, name='delete_first')
]