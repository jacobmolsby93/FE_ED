# from django.test import TestCase, Client
# from django.urls import reverse
# from posts.models import Post, Comment
# from users.models import BlogUser
# from django.contrib.auth.models import User

# import datetime


# class TestViews(TestCase):
#     """
#     Test all the views of the post app
#     """

#     def setUp(self):
#         """
#         Setting up the client by creating a user
#         to test the views that require a user to use.
#         """ 
#         self.client = Client()
#         self.add_post = reverse('profile')
#         self.edit_profile = reverse('edit')
#         self.like_post = reverse('like', args=['some-title'])
#         self.user = User.objects.create_user(
#             username='testuser', password='12345')
#         self.user2 = User.objects.create_user(
#             username='undefined', password='undefined')
#         self.client.login(username='testuser', password='12345')
#         self.blog_user = BlogUser.objects.get(user=self.user)
#         self.post = Post.objects.create(
#             author=self.blog_user,
#             post_title='Some title',
#             post_body='Some Body',
#             posted=datetime.datetime,
#             status=1,
#         )

#         self.post2 = Post.objects.create(
#             author=self.blog_user,
#             post_title='some other title',
#             post_body='Some Body',
#             posted=datetime.datetime,
#             status=1,
#         )
#         self.post_detail = reverse('post_detail', args=[self.post.slug])
#         self.add_comment = reverse('post_detail', args=[self.post.slug])
#         self.edit_post = reverse('edit_post', args=['some-title'])
#         self.posts = Post.objects.all()

#     def test_post_detail_GET(self):
#         response = self.client.get(self.post_detail)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'posts/post_detail.html')
#         print("Post detail view GET -- PASSED")

#     def test_post_detail_POST(self):
#         response = self.client.post(self.post_detail, {
#             'author': self.blog_user,
#             'post_title': 'Some title',
#             'post_body': 'Some Body',
#             'posted': datetime.datetime,
#             'status': 1,
#         })
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(self.post.author.user.username, 'testuser')
#         print("Post detail view POST -- PASSED")

#     def test_add_post_view(self):
#         """
#         Testing the add post view.
#         """

#         response = self.client.get(self.add_post)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/profile.html')
#         print("Add post view -- PASSED")

#     def test_edit_post_view(self):
#         """
#         Test edit post view
#         """
#         response = self.client.post(self.edit_post)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'posts/edit_post.html')
#         print("Edit post view -- PASSED")

#     def test_delete_post_view(self):
#         """
#         Test delete post view
#         """
#         self.delete_post = reverse('delete', args=['some-other-title'])
#         response = self.client.delete(self.delete_post)
#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(self.posts.count(), 1)
#         print("Delete post view -- PASSED")

#     def test_like_post_view(self):
#         """
#         Testing the like functionality
#         """
#         self.post.likes.set([self.user.id])
#         self.assertEquals(self.post.likes.count(), 1)
#         print("Like post view -- PASSED")

#     def test_post_detail_comment_POST(self):
#         response = self.client.post(self.add_comment, {
#             'comment_author': self.user,
#             'comment_content': "some content",
#             'posted': datetime.datetime,
#         })
#         # Add Comment
#         comments = Comment.objects.all().count()
#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(comments, 1)
#         print("Comment Added -- PASSED")

#     def test_userprofile_view(self):
#         """
#         Test for userprofile
#         """
#         response = self.client.get(self.add_post)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/profile.html')
#         print("Profile view -- PASSED")

#     def test_edit_userprofile_view(self):
#         """
#         Test for edit profile view
#         """
#         response = self.client.post(self.edit_profile)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/edit_profile.html')
#         print("Edit Profile view -- PASSED")
