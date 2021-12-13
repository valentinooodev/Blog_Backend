from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.blog.models import PostModel, CategoryModel
from apps.users.models import UserModel
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('blog_api:post_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = CategoryModel.objects.create(name='django')

        self.testuser1 = UserModel.objects.create_user(
            username='test_user1', password='123456789')

        data = {"title": "new", "author": 1,
                "description": "new", "content": "new"}
        url = reverse('blog_api:post_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 6)
        root = reverse(('blog_api:post_detail'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client = APIClient()

        self.test_category = CategoryModel.objects.create(name='django')
        self.testuser1 = UserModel.objects.create_user(
            email='test_user1@gmail.com', full_name='user1',
            user_name='test_user1', password='123456789')
        self.testuser2 = UserModel.objects.create_user(
            email='test_user2@gmail.com',  full_name='user2',
            user_name='test_user2', password='123456789')
        test_post = PostModel.objects.create(
            category_id=1, title='Post Title', description='Post Description', content='Post Content',
            slug='post-title',
            author_id=1, status='published')

        client.login(username=self.testuser1.user_name,
                     password='123456789')

        url = reverse(('blog_api:post_detail'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "description": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
