import pytest

from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='Olá Django com Fabrica', content='Conteúdo do post')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Olá Django com Fabrica'
    assert post_published.content == 'Conteúdo do post'



