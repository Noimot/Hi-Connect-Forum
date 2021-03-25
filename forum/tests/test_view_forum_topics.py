from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Category
from ..views import TopicListView


class ForumTopicsTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Education', description='education discussion')

    def test_forum_topics_view_success_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forum_topics_view_not_found_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_forum_topics_url_resolves_forum_topics_view(self):
        view = resolve('/forum/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_forum_topics_view_contains_navigation_links(self):
        forum_topics_url = reverse('forum_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(forum_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))