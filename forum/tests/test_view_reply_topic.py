from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Category, Post, Topic
from ..views import reply_topic
from http import HTTPStatus

class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        self.category = Category.objects.create(name='Education', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', category=self.category, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.category.pk, 'topic_pk': self.topic.pk})

# class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
#     # ...

# class ReplyTopicTests(ReplyTopicTestCase):
#     # ...

class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    # ...

    def test_redirection(self):
        url = reverse('topic_posts', kwargs={'pk': self.category.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)

# class InvalidReplyTopicTests(ReplyTopicTestCase):
#     # ...