from django.http import HttpResponse
from django.test import Client
from django.urls import reverse
import pytest

from webdev.tarefas.models import Tarefa


@pytest.fixture
def response(client: Client, db) -> HttpResponse:
    """ Retorna resposta da página Home após o POST

    Args:
        client (Client): Classe Client de testes do Django

    Returns:
        HttpResponse: Resposta de acesso à pagina.
    """
    # named url -> reverse(app:view)
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_task_exists_on_db(response: HttpResponse) -> None:
    """ Verifica se há dados no banco de dados.

    Args:
        response (HttpResponse): Resposta obtida pela página.
    """
    assert Tarefa.objects.exists()


def test_redirect_after_save_data(response: HttpResponse) -> None:
    """ Verifica se houve redirecionamento da página. Ou seja, os dados foram salvos.

    Args:
        response (HttpResponse): Resposta de acesso à pagina.
    """
    assert response.status_code == 302


@pytest.fixture
def response_invalid_data(client: Client, db) -> HttpResponse:
    """ Retorna resposta da página Home após o POST

    Args:
        client (Client): Classe Client de testes do Django

    Returns:
        HttpResponse: Resposta de acesso à pagina.
    """
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp


def test_task_doesnt_exists_on_db(response_invalid_data: HttpResponse) -> None:
    """ Verifica se não há dados no banco de dados.

    Args:
        response (HttpResponse): Resposta obtida pela página.
    """
    assert not Tarefa.objects.exists()


def test_invalid_data(response_invalid_data: HttpResponse) -> None:
    """ Verifica se não houve redirecionamento da página. Ou seja, os dados não foram salvos.

    Args:
        response (HttpResponse): Resposta de acesso à pagina.
    """
    assert response_invalid_data.status_code == 400
