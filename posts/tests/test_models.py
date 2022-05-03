# from django.test import TestCase, Client
# from django.urls import reverse
# from posts.models import Post
# from users.models import BlogUser

# from django.contrib.auth.models import User

# import datetime


# class TestModels(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.add_post = reverse('profile')
#         self.like_post = reverse('like', args=['some-title'])
#         self.user = User.objects.create_user(
#             username='testuser', password='12345')
#         self.user2 = User.objects.create_user(
#             username='undefined', password='undefined')
#         self.client.login(username='testuser', password='12345')
#         self.blog_user = BlogUser.objects.get(user=self.user)
#         self.post1 = Post.objects.create(
#             author=self.blog_user,
#             post_image=None,
#             post_title="Some Random Title",
#             post_body='some random content',
#             posted=datetime.datetime,
#             status=1,
#         )

#     def test_post_slug_is_slug_on_creation(self):
#         self.assertEquals(self.post1.slug, 'some-random-title')
#         print(
#             f"""Test assertEquals Test-Case:
#             '{self.post1.slug}' === 'some-random-title'"""
#         )

#     def test_user_is_blog_user_on_signup(self):
#         self.assertEquals(self.user.username, self.blog_user.user.username)
#         print(
#             f"""Test Assert Equals Test-Case:
#             user == blog_user
#             user-'{self.user.username}'
#             blog_user-'{self.blog_user.user.username}'
#             """
#         )
