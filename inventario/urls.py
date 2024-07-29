from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarehouseViewSet, InventoryViewSet, SaleViewSet, RecordSaleView,UserCreateView, UserListView, UserDetailView, ObtainTokenView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('record-sale/', RecordSaleView.as_view(), name='record_sale'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create-user/', UserCreateView.as_view(), name='user_create'),
    path('token/', ObtainTokenView.as_view(), name='token_obtain'),
] 

