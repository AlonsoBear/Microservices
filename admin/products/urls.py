from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',        
    }), name='products'),
    path('products/<str:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user/', UserAPIView.as_view(), name='users')
]
