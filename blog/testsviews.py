from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.user = User.objects.create_user('user', 'user@example.com', 'password')
        self.post = Post.objects.create(title='Test Post', slug='test-post', content='Test content', author=self.superuser, status=1)
        self.comment = Comment.objects.create(post=self.post, author=self.user, body='Test comment', approved=True)

    def testpost_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def testpost_detail_view(self):
        response = self.client.get(reverse('blogpost', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost.html')

    def testcomment_edit_view(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('comment_edit', args=[self.post.slug, self.comment.id]), {'body': 'Updated comment'})
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Updated comment')
        self.assertFalse(self.comment.approved)  # Should be unapproved after editing

    def testcomment_delete_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def testuser_admin_access(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('admin'))
        #print(response.status_code)
        #print(response.content)
        self.assertEqual(response.status_code, 200)

    def testuser_admin_access_denied(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('admin'))
        print('response for admin denied', response.status_code)
        if response.status_code == 302:
            print('Redirect URL:', response.url)  # Print the redirect URL
        self.assertEqual(response.status_code, 302)

    def testuser_admin_access_not_logged_in_denied(self):
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 302)  # Expecting redirect to login

    def testcreate_or_update_post_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post', 
            'slug': 'new-post', 
            'excerpt': 'new excerpt', 
            'content': 'New content', 
            'status': '1', 
            'tags': 'tag1'})
        print(response.status_code)  # check if the response is a redirect or not
        print(response.content)  # print the full content to debug the issue
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(slug='new-post').exists())

    def testspost_delete_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())