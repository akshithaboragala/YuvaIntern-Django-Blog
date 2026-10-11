from django.test import TestCase
from .models import Post, Comment


class BlogModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Blog Post",
            content="Testing Django Blog Application",
            author="Akhi"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Blog Post")
        self.assertEqual(self.post.author, "Akhi")


class CommentModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author="Akhi"
        )

        self.comment = Comment.objects.create(
            post=self.post,
            name="Akhi",
            comment="Great blog!"
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.name, "Akhi")
        self.assertEqual(self.comment.comment, "Great blog!")
        self.assertEqual(self.comment.post.title, "Test Post")


class BlogViewTest(TestCase):

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
