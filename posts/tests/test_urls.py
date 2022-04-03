# from django.test import TestCase
# from django.urls import reverse, resolve
# from posts.views import (
#     edit_post, 
#     delete_post, 
#     add_post,
#     post_detail, 
#     like, 
#     delete_comment
# )
# from users.views import (
#     profile,
#     edit_profile
# )


# class TestUrls(TestCase):
#     # add_post
#     def test_post_urls_resolved(self):
#         url = reverse('add_post')
#         print('Add post URL -- PASSED')
#         self.assertEquals(resolve(url).func, add_post)

#     # edit_post
#     def test_post_urls_resolved2(self):
#         url = reverse('edit_post', args=['slug'])
#         print('Edit post URL -- PASSED')
#         self.assertEquals(resolve(url).func, edit_post)

#     # delete_post
#     def test_post_urls_resolved3(self):
#         url = reverse('delete', args=['slug'])
#         print("Delete post URL -- PASSED")
#         self.assertEquals(resolve(url).func, delete_post)

#     # post_detail
#     def test_post_urls_resolved4(self):
#         url = reverse('post_detail', args=['slug'])
#         print('post_detail URL -- PASSED')
#         self.assertEquals(resolve(url).func, post_detail)
 

#     # like
#     def test_post_urls_resolved5(self):
#         url = reverse('like', args=['slug'])
#         print('Like post URL -- PASSED')
#         self.assertEquals(resolve(url).func, like)

#     # Profile
#     def test_post_urls_resolved(self):
#         url = reverse('profile')
#         print('Profile URL -- PASSED')
#         self.assertEquals(resolve(url).func, profile)

#     # Edit Profile
#     def test_post_urls_resolved2(self):
#         url = reverse('edit')
#         print('Edit profile URL -- PASSED')
#         self.assertEquals(resolve(url).func, edit_profile)

