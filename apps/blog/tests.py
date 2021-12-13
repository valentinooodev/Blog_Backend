from django.test import TestCase
from django.contrib.auth.models import User
from apps.blog.models import PostModel, CategoryModel


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = CategoryModel.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = PostModel.objects.create(
            category_id=1, title='Post Title', description='Post Description', content='Post Content', slug='post-title',
            author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = PostModel.postobjects.get(id=1)
        cat = CategoryModel.objects.get(id=1)
        author = f'{post.author}'
        description = f'{post.description}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")
        self.assertEqual(description, "Post Description")
