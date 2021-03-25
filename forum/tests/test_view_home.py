from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Category
from ..views import CategoryListView


class HomeTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Education', description='Education discussion.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, CategoryListView)

    def test_home_view_contains_link_to_topics_page(self):
        forum_topics_url = reverse('forum_topics', kwargs={'pk': self.category.pk})
        self.assertContains(self.response, 'href="{0}"'.format(forum_topics_url))