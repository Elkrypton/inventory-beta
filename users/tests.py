import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john','john@gmail.com','johnpassword')
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code ==  200

