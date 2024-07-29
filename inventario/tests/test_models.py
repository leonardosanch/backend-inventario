

import pytest
from django.utils import timezone
from inventario.models import Product, Warehouse, Inventory, Sale, CustomUser

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(name="Test Product", description="Test Description", price="10.00")
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == "10.00"

@pytest.mark.django_db
def test_create_warehouse():
    warehouse = Warehouse.objects.create(name="Test Warehouse", location="Test Location")
    assert warehouse.name == "Test Warehouse"
    assert warehouse.location == "Test Location"

@pytest.mark.django_db
def test_create_inventory():
    product = Product.objects.create(name="Test Product", description="Test Description", price="10.00")
    warehouse = Warehouse.objects.create(name="Test Warehouse", location="Test Location")
    inventory = Inventory.objects.create(product=product, warehouse=warehouse, quantity=100)
    assert inventory.product.name == "Test Product"
    assert inventory.warehouse.name == "Test Warehouse"
    assert inventory.quantity == 100

@pytest.mark.django_db
def test_create_sale():
    product = Product.objects.create(name="Test Product", description="Test Description", price="10.00")
    warehouse = Warehouse.objects.create(name="Test Warehouse", location="Test Location")
    sale = Sale.objects.create(product=product, warehouse=warehouse, quantity=10, sale_date=timezone.now())
    assert sale.product.name == "Test Product"
    assert sale.warehouse.name == "Test Warehouse"
    assert sale.quantity == 10

@pytest.mark.django_db
def test_create_custom_user():
    user = CustomUser.objects.create_user(email="testuser@example.com", password="password123", first_name="Test", last_name="User")
    assert user.email == "testuser@example.com"
    assert user.check_password("password123")
    assert user.first_name == "Test"
    assert user.last_name == "User"
