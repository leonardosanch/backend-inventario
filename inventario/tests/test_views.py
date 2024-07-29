import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from inventario.models import Product, Warehouse, CustomUser, Inventory

@pytest.mark.django_db
def test_create_warehouse_api():
    client = APIClient()
    user = CustomUser.objects.create_user(email="admin@example.com", password="password123", is_staff=True)
    client.force_authenticate(user=user)
    
    url = reverse('warehouse-list')
    data = {
        "name": "Test Warehouse",
        "location": "Test Location"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_create_inventory_api():
    client = APIClient()
    user = CustomUser.objects.create_user(email="admin@example.com", password="password123", is_staff=True)
    client.force_authenticate(user=user)
    
    product = Product.objects.create(name="Test Product", description="Test Description", price="10.00")
    warehouse = Warehouse.objects.create(name="Test Warehouse", location="Test Location")
    
    url = reverse('inventory-list')
    data = {
        "product": product.id,
        "warehouse": warehouse.id,
        "quantity": 100
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201

