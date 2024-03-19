from django.http import HttpResponse
from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains


@pytest.fixture
def response(client: Client) -> HttpResponse:
    """ Retorna resposta da página Home

    Args:
        client (Client): Classe Client de testes do Django

    Returns:
        HttpResponse: Resposta de acesso à pagina.
    """
    # named url -> reverse(app:view)
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(response: HttpResponse) -> None:
    """ Verifica se o status code retornado é 200

    Args:
        response (HttpResponse): Resposta obtida pela página.
    """
    assert response.status_code == 200


def test_formulario_presente(response: HttpResponse) -> None:
    """ Verifica se há o formulário presente na página.

    Args:
        response (HttpResponse): Resposta obtida pela página.
    """
    assertContains(response, '<form>')


def test_botao_salvar_presente(response: HttpResponse) -> None:
    """ Verifica se há o botão de submit na página.

    Args:
        response (HttpResponse): Resposta obtida pela página.
    """
    assertContains(response, '<button type="submit"')
