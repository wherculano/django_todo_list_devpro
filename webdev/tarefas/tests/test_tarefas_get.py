from django.test import Client
from django.urls import reverse


def test_status_code(client: Client):
    # named url -> reverse(app:view)
    response = client.get(reverse('tarefas:home'))
    assert response.status_code == 200
