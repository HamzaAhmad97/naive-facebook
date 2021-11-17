from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
from accounts.admin import CustomUser
class PostTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username = 'John',
            email='test@gmail.com',
            password='something123'
        )
        self.post = Post.objects.create(
            content = 'test post',
            added_by = self.user,
            created = None
        )
        

    def test_string_representation(self):
        post = Post(content = 'test post')
        self.assertEqual(str(post), post.content)

    def test_post_fields(self):
        self.assertEqual(f'{self.post.content}', 'test post')
        self.assertEqual(f'{self.post.added_by}', 'John')


    def test_post_create_view(self): 
        response = self.client.post(reverse('posts_create'), {
            'content': 'test post',
            'added_by': self.user.email,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().content, 'test post')
        self.assertEqual(Post.objects.last().added_by, 'test@gmail.com')

    def test_post_delete_view(self): 
        response = self.client.post(
            reverse('posts_delete', args='1'))
        self.assertEqual(response.status_code, 302)

