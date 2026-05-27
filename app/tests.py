from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

class PostAPITests(APITestCase):

    def setUp(self):
        self.test_post = Post.objects.create(
            title="Initial Test Post",
            content="This is content stored within the testing setup database."
        )
        self.list_create_url = reverse('post-list')
        self.detail_url = reverse('post-detail', kwargs={'pk': self.test_post.id})

    def test_list_all_posts(self):
        """GET /api/posts/ -> Evaluates output list payloads"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_post(self):
        """POST /api/posts/ -> Validates parsing and initialization loops"""
        payload = {'title': 'Fresh API Entry', 'content': 'Populating entry elements.'}
        response = self.client.post(self.list_create_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_single_post(self):
        """GET /api/posts/{id}/ -> Evaluates detail object parsing structures"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.test_post.title)

    def test_update_post(self):
        """PUT /api/posts/{id}/ -> Assures full write-back operations update rows"""
        modified_payload = {'title': 'Altered Heading', 'content': 'Adjusted description details.'}
        response = self.client.put(self.detail_url, modified_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_post.refresh_from_db()
        self.assertEqual(self.test_post.title, 'Altered Heading')

    def test_delete_post(self):
        """DELETE /api/posts/{id}/ -> Validates clean records removal sequences"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)